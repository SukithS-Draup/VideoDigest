import os
import csv
import cv2
from tracker import EuclideanDistTracker
from create_video import create_video

import cv2

# Capture video from a camera or file
cap = cv2.VideoCapture('video.mp4')

object_positions = {}

# Create tracker object
tracker = EuclideanDistTracker()
cap = cv2.VideoCapture("./static/video/highway.mp4")

# Object detection from Stable camera
object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)

# Create a directory to save the images
output_dir = "output"
if not os.path.exists(output_dir):
    os.mkdir(output_dir)

# Create a CSV file to save the object positions and timestamps
output_file = 'object_positions.csv'
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['ID', 'X', 'Y', 'Width', 'Height', 'Appearance Time (ms)'])

while True:

    ret, frame = cap.read()
    if not ret:
        break
    height, width, _ = frame.shape

    # Extract Region of interest
    roi = frame[340: 720,500: 800]

    # 1. Object Detection
    mask = object_detector.apply(roi)
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    detections = []
    for cnt in contours:
        # Calculate area and remove small elements
        area = cv2.contourArea(cnt)
        if area > 100:
            x, y, w, h = cv2.boundingRect(cnt)
            detections.append([x, y, w, h])

    # 2. Object Tracking
    boxes_ids = tracker.update(detections)
    for box_id in boxes_ids:
        x, y, w, h, id = box_id
        cv2.putText(roi, str(id), (x, y - 15), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
        cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 3)

        # Store the object's position and appearance time in the object_positions dictionary
        object_positions[id] = [x, y, w, h, cap.get(cv2.CAP_PROP_POS_MSEC)]
        
        # Create a directory with the ID as its name
        id_dir = os.path.join(output_dir, str(id))
        if not os.path.exists(id_dir):
            os.mkdir(id_dir)
        
        # Save the corresponding image in the directory
        img_name = f"{id}_{len(os.listdir(id_dir))+1}.jpg"
        img_path = os.path.join(id_dir, img_name)
        cv2.imwrite(img_path, roi[y:y+h, x:x+w])
        
        # Save the object position and timestamp in the CSV file
        with open(output_file, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([id, x, y, w, h, cap.get(cv2.CAP_PROP_POS_MSEC)/1000])
        
    cv2.imshow("roi", roi)
    cv2.imwrite("frame.jpg", roi)
    create_video()
    key = cv2.waitKey(30)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
