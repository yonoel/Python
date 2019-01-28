#OpenCV has the function cv.cornerHarris() for this purpose. Its arguments are :

#img - Input image, it should be grayscale and float32 type.
#blockSize - It is the size of neighbourhood considered for corner detection
#ksize - Aperture parameter of Sobel derivative used.
#k - Harris detector free parameter in the equation.
import numpy as np
import cv2 as cv
filename = 'chessboard.png'
img = cv.imread(filename)
# print ("img",type (img))
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv.cornerHarris(gray,2,3,0.04)
# print ("dst",dst)
#result is dilated for marking the corners, not important
dst = cv.dilate(dst,None) #扩大结果
# print ("dilate dst",dst)

# Threshold for an optimal value, it may vary depending on the image.
print (img[dst > 0.01 *dst.max()])
print (len(img[dst > 0.01 *dst.max()]))
print ("\n")
# print (img[dst == dst.max()])
# img[dst > 0.01*dst.max()]=[ 0,0,255] # img是个N维数组，然后img里找到这些特征点，并给他们赋值[ 0,0,255]
print (len(img[dst == dst.min()]))
img[dst == dst.min] = [ 0,0,255]
cv.imshow('dst',img)
if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()