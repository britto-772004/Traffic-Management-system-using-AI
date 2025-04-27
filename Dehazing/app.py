import cv2
import numpy as np
import os

# Step 1: Dark Channel Calculation
def dark_channel(image, size=15):
    dark_channel_img = np.min(image, axis=2)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (size, size))
    return cv2.erode(dark_channel_img, kernel)

# Step 2: Estimate Atmospheric Light
def atmospheric_light(image, dark_channel_img):
    h, w = image.shape[:2]
    num_brightest = max(int(h * w / 1000), 1)  # top 0.1%
    dark_vec = dark_channel_img.ravel()
    image_vec = image.reshape(h * w, 3)
    indices = dark_vec.argsort()[::-1][:num_brightest]
    brightest = image_vec[indices]
    return np.mean(brightest, axis=0)

# Step 3: Estimate Transmission Map
def transmission_estimate(image, atmospheric_light, omega=0.95, size=15):
    norm_image = image / (atmospheric_light + 1e-6)  # avoid divide by zero
    return 1 - omega * dark_channel(norm_image, size)

# Step 4: Guided Filter
def guided_filter(I, p, r, eps):
    mean_I = cv2.boxFilter(I, cv2.CV_64F, (r, r))
    mean_p = cv2.boxFilter(p, cv2.CV_64F, (r, r))
    corr_I = cv2.boxFilter(I * I, cv2.CV_64F, (r, r))
    corr_Ip = cv2.boxFilter(I * p, cv2.CV_64F, (r, r))

    var_I = corr_I - mean_I * mean_I
    cov_Ip = corr_Ip - mean_I * mean_p

    a = cov_Ip / (var_I + eps)
    b = mean_p - a * mean_I

    mean_a = cv2.boxFilter(a, cv2.CV_64F, (r, r))
    mean_b = cv2.boxFilter(b, cv2.CV_64F, (r, r))

    return mean_a * I + mean_b

# Step 5: Recover Dehazed Image
def recover(image, transmission, atmospheric_light, t0=0.1):
    transmission = np.clip(transmission, t0, 1)
    result = np.empty_like(image, dtype=np.float32)
    for i in range(3):
        result[:, :, i] = (image[:, :, i] - atmospheric_light[i]) / transmission + atmospheric_light[i]
    return np.clip(result * 255, 0, 255).astype(np.uint8)

# Step 6: Dehazing Pipeline
def dehaze(image_path, return_gray=False):
    if not os.path.exists(image_path):
        print(f"Error: File {image_path} does not exist.")
        return None

    image = cv2.imread(image_path)
    if image is None:
        print("Error loading image")
        return None

    image = image.astype(np.float64) / 255.0
    dark = dark_channel(image)
    A = atmospheric_light(image, dark)
    transmission = transmission_estimate(image, A)

    gray_base = cv2.cvtColor((image * 255).astype(np.uint8), cv2.COLOR_BGR2GRAY).astype(np.float64) / 255
    transmission_refined = guided_filter(gray_base, transmission, r=10, eps=1e-1)
    dehazed = recover(image, transmission_refined, A)

    # Optional: Final grayscale polish
    if return_gray:
        gray = cv2.cvtColor(dehazed, cv2.COLOR_BGR2GRAY)

        # Step 1: Denoise to reduce blocks
        denoised = cv2.fastNlMeansDenoising(gray, h=10, templateWindowSize=7, searchWindowSize=21)

        # Step 2: CLAHE for local contrast boost
        clahe = cv2.createCLAHE(clipLimit=2.5, tileGridSize=(8, 8))
        contrast_enhanced = clahe.apply(denoised)

        # Step 3: Gamma correction
        gamma = 1.2
        gamma_corrected = np.array(255 * ((contrast_enhanced / 255) ** (1 / gamma)), dtype=np.uint8)

        return gamma_corrected

    # Optional: Bilateral Smoothing for Grayscale
    if return_gray:
        gray = cv2.cvtColor(dehazed, cv2.COLOR_BGR2GRAY)
        smooth_gray = cv2.bilateralFilter(gray, d=9, sigmaColor=75, sigmaSpace=75)
        return smooth_gray

    # Color Version Enhancements
    lab = cv2.cvtColor(dehazed, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    cl = clahe.apply(l)
    enhanced = cv2.merge((cl, a, b))
    final_color = cv2.cvtColor(enhanced, cv2.COLOR_LAB2BGR)

    sharpening_kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    sharpened_color = cv2.filter2D(final_color, -1, sharpening_kernel)

    return sharpened_color

# Step 7: Display
if __name__ == "__main__":
    image_path = "traffic_image.webp"
    result = dehaze(image_path, return_gray=True)  # Set to False for color version

    if result is not None:
        original = cv2.imread(image_path)
        cv2.imshow("Original Traffic Photo", original)
        if len(result.shape) == 2:
            cv2.imshow("Dehazed Grayscale Traffic Photo", result)
        else:
            cv2.imshow("Dehazed Color Traffic Photo", result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
