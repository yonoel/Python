import numpy as np
import cv2 as cv
img = cv.imread('messi5.jpg')
# must be real number, not str
res = cv.resize(img,None,fx=0.5, fy=0.5, interpolation = cv.INTER_CUBIC)
cv.imshow("res",res)
cv.waitKey(0)
cv.destroyAllWindows()
#OR
# height, width = img.shape[:2]
# res = cv.resize(img,(2*width, 2*height), interpolation = cv.INTER_CUBIC)