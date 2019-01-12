import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frameqqqwqe
    cv.imshow('frame',gray)
    # waitKey(int delay)这个函数接收一个整型值，如果这个值是零，那么函数不会有返回值，如果delay大于0，那么超过delayms后，如果没有按键，那么会返回-1，如果按键那么会返回键盘值。
    #   在某些系统中，返回的键盘值可能不是ASCII编码的，所以通过与运算只取字符最后一个字节。
    if cv.waitKey(10) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()