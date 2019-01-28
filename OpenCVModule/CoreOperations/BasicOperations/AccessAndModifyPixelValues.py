import numpy as np
import cv2 as cv

img = cv.imread("roi.jpg", 0)
# You can access a pixel value by its row and column coordinates.
# For BGR image, it returns an array of Blue, Green, Red values.
# For grayscale image, just corresponding intensity is returned.
px = img[100, 100]
print("img's px---->", px)
# accessing only blue pixel
blue = img[100, 100, 0]
print("blue--->",blue)

img[100, 100] = [255, 255, 255]
print("modify px value---->",img[100, 100])
# The above method is normally used for selecting a region of an array, say the first 5 rows and last 3 columns.
# For individual pixel access, the Numpy array methods, array.item() and array.itemset() are considered better,
# however they always return a scalar.
# If you want to access all B,G,R values, you need to call array.item() separately for all.

# accessing red
print("red--->", img.item(10, 10, 2))

# modifying red value
img.itemset((10, 10, 2), 100)
print("change red---->", img.item(10, 10, 2))
