import numpy as np
import cv2 as cv

img = cv.imread("roi.jpg", 0)
# Sometimes you will need to work separately on B,G,R channels of image.
# In this case, you need to split the BGR images to single channels.
# In other cases, you may need to join these individual channels to a BGR image.
# You can do it simply by:
# cv.split() is a costly operation (in terms of time). So do it only if you need it. Otherwise go for Numpy indexing.
b, g, r = cv.split(img)
img = cv.merge(b, g, r)

# or
b = img[:, :, 0]

# Suppose you want to set all the red pixels to zero, you do not need to split the channels first. Numpy indexing is faster:
img[:, :, 2] = 0
