import numpy as np
import cv2 as cv

img = cv.imread("roi.jpg", 0)
# If an image is grayscale, the tuple returned contains only the number of rows and columns,
# so it is a good method to check whether the loaded image is grayscale or color.
print("img's shape---->",img.shape)

print("total number of pixels---->",img.size)

print("img data type---->",img.dtype)




