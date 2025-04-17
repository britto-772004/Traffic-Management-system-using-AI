# from ultralytics import YOLO
# import cv2

# # Load trained YOLO model
# model = YOLO("best.pt")

# # Define class names (update based on your dataset)
# class_names = {1: "Fire Engine", 0: "Ambulance"}  # Modify according to your classes

# # Load test image
# image_path = "ambulance1.jpg"
# image = cv2.imread(image_path)

# # Run inference
# results = model(image)

# # Display results
# for r in results:
#     for box in r.boxes:
#         x1, y1, x2, y2 = map(int, box.xyxy[0])
#         class_id = int(box.cls[0])
#         confidence = box.conf[0]
        
#         # Get class name
#         class_name = class_names.get(class_id, "Unknown")  # Default to "Unknown" if not in dictionary
        
#         label = f"{class_name} ({confidence:.2f})"

#         # Reduce bounding box size
#         shrink_factor = 0.1
#         width = x2 - x1
#         height = y2 - y1
#         x1 += int(width * shrink_factor)
#         y1 += int(height * shrink_factor)
#         x2 -= int(width * shrink_factor)
#         y2 -= int(height * shrink_factor)

#         # Draw adjusted bounding box
#         cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
#         cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# cv2.imshow("Emergency Vehicle Detection", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

from ultralytics import YOLO
import cv2

# Load your trained model
model = YOLO("best.pt")

# Open video file or webcam stream
video_path = "videoplayback.mp4"  # or 0 for webcam
cap = cv2.VideoCapture(video_path)

# Define class names
class_names = {1: "Fire Engine", 0: "Ambulance"}

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run inference on each frame
    results = model(frame)

    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            class_id = int(box.cls[0])
            confidence = box.conf[0]
            class_name = class_names.get(class_id, "Unknown")

            label = f"{class_name} ({confidence:.2f})"
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow("Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
