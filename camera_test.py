""" Take video footage from camera and show it on screen."""

import cv2

# 0 means the default video capture device in OS
cap = cv2.VideoCapture(0)

# Check if camera opened successfully
if not cap.isOpened():
    print("Error opening video stream or file")
    exit(1)

# Read until video is completed
while cap.isOpened():
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret:
        # Display the resulting frame
        cv2.imshow("Frame", frame)

        # Press Q on keyboard to exit
        if cv2.waitKey(25) & 0xFF == ord("q"):
            break
    # Break the loop
    else:
        break
