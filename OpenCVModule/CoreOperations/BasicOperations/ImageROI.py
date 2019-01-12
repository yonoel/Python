import numpy as np
import cv2 as cv

img = cv.imread("roi.jpg", 0)

ball = img[280:340,330:390]
img[273:333,100:160] = ball