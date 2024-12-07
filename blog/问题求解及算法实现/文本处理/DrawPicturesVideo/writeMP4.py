""" Write Mp4 Files
Example for capture the webcam video and show
"""
import cv2
import numpy as np
import os

# Video Path
videoPath = r"C:\Users\Lizhen\Videos"

# Init a VideoCapture object
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

# Check if camera opened successfully
if (cap.isOpened() == False):
    print("Unable to read camera feed")
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

out = cv2.VideoWriter(os.path.join(videoPath,'outWriter.avi'),cv2.VideoWriter_fourcc('M','J','P','G'),10,(frame_width,frame_height))

while(True):
    ret, frame = cap.read()

    if ret == True:
        out.write(frame)
        # v2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    else:
        break

cap.release()
out.release()

cv2.destroyAllWindows()
