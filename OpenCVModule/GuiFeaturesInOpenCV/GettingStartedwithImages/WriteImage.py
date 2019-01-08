import numpy as np
import cv2 as cv

img = cv.imread("messi5.jpg",0)
cv.imwrite("messigray.png",img)