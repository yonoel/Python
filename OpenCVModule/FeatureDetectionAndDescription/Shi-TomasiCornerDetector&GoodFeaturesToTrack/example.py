# In below example, we will try to find 25 best corners:

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('blox.jpg')

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

conners = cv.goodFeaturesToTrack(gray,25,0.01,10)
corners = np.int0(conners)

for i in corners:
    x,y = i.ravel()
    cv.circle(img,(x,y),3,255,-1)
plt.imshow(img),plt.show()
