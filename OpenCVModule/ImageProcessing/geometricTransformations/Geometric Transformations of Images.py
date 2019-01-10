import numpy as np
import cv2 as cv
img = cv.imread('messi5.jpg',0)
rows,cols = img.shape
print("rows's %d and cols's %d",rows,cols)
def translation():
    M = np.float32([[1,0,200],[0,1,50]])
    # cv.warpAffine(img, M, (cols, rows)) img=origin m=location Third argument of the cv.warpAffine() function is the size of the output image
    dst = cv.warpAffine(img,M,(cols,rows))
    cv.imshow('img',dst)
    cv.waitKey(0)
    cv.destroyAllWindows()

translation()