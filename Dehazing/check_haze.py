import cv2
import numpy as np

def dark_channel(img, window_size=15):
    min_channel = np.min(img, axis=2)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (window_size, window_size))
    dark = cv2.erode(min_channel, kernel)
    return dark


def compute_contrast(img_gray):
    return img_gray.std()

def laplacian_variance(img_gray):
    return cv2.Laplacian(img_gray, cv2.CV_64F).var()

def haze_detector(image_path):
    # Read and resize image
    img = cv2.imread(image_path)
    img = cv2.resize(img, (500, 500))
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Feature 1: Dark Channel
    dark = dark_channel(img)
    dark_mean = np.mean(dark)
    
    # Feature 2: Contrast
    contrast = compute_contrast(img_gray)

    # Feature 3: Laplacian Variance
    lap_var = laplacian_variance(img_gray)

    print(f"Dark Channel Mean: {dark_mean}")
    print(f"Image Contrast: {contrast}")
    print(f"Laplacian Variance: {lap_var}")

    # Normalize scores
    dark_score = dark_mean / 255  # Normalize to [0,1]
    contrast_score = 1 - (contrast / 128)  # Invert because low contrast = haze
    laplacian_score = 1 - (lap_var / 1000)  # Invert because low sharpness = haze

    # Clip scores
    dark_score = np.clip(dark_score, 0, 1)
    contrast_score = np.clip(contrast_score, 0, 1)
    laplacian_score = np.clip(laplacian_score, 0, 1)

    # Final haze score
    haze_score = (0.5 * dark_score) + (0.25 * contrast_score) + (0.25 * laplacian_score)

    print(f"Haze Score: {haze_score:.3f}")

    # Decide
    if haze_score > 0.5:
        print("Prediction: Hazy Image 🌫️")
    else:
        print("Prediction: Clear Image 🌞")

# Example usage
haze_detector('traffic_image.webp')