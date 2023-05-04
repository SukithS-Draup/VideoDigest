import cv2
import time
from tracker import EuclideanDistTracker
from itertools import zip_longest

# Create tracker object
tracker = EuclideanDistTracker()

cap = cv2.VideoCapture("highway.mp4")

# Object detection from Stable camera
object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)

# Initialize dictionary to keep track of object IDs and corresponding video writers
object_writers = {}

# Get frame rate of the video
fps = int(cap.get(cv2.CAP_PROP_FPS))

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
        timestamp = int(cap.get(cv2.CAP_PROP_POS_FRAMES) / fps)
        cv2.putText(roi, str(timestamp)+str("sec"), (x, y - 15), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
        if id in object_writers:
            # If object ID is in dictionary, write current frame to the corresponding video writer
            object_writers[id].write(roi)
        # else:
        #     # If object ID is not in dictionary, create a new video writer and add it to the dictionary
        #     object_writers[id] = cv2.VideoWriter(f"object_{id}.mp4", cv2.VideoWriter_fourcc(*'mp4v'), fps, (roi.shape[1], roi.shape[0]))
        #     object_writers[id].write(roi)

    cv2.imshow("roi", roi)
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(30)
    if key == 27:
        break

# Release video writers and cleanup
for writer in object_writers.values():
    writer.release()
cap.release()
cv2.destroyAllWindows()