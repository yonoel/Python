#Goal
+ Learn to read video, display video and save video.
+ Learn to capture from Camera and display it.
+ You will learn these functions : cv.VideoCapture(), cv.VideoWriter()
# Capture Video from Camera
 Let's capture a video from the camera (I am using the in-built webcam of my laptop), convert it into grayscale video and display it. Just a simple task to get started.<br>
 To capture a video, you need to create a VideoCapture object.<br>
 Its argument can be either the device index or the name of a video file.<br>
Device index is just the number to specify which camera. Normally one camera will be connected (as in my case). So I simply pass 0 (or -1). You can select the second camera by passing 1 and so on. After that, you can capture frame-by-frame. But at the end, don't forget to release the capture.
```import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('frame',gray)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()```