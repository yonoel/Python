import numpy as np
import cv2 as cv

#load a image
img = cv.imread("messi5.jpg",0)
#print (img) # Even if the image path is wrong
# it won't throw any error, but print img will give you None

# cv.imshow('image',img)
# cv.waitKey(0) #is a keyboard binding function.
# cv.destroyAllWindows()
cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()
