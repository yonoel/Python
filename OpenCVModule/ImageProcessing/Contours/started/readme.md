# GOAL
+ Understand what contours are.
+ Learn to find contours, draw contours etc
+ You will see these functions : cv.findContours(), cv.drawContours()
#What are contours?
轮廓
+ For better accuracy, use binary images. So before finding contours, apply threshold or canny edge detection.
+ Since OpenCV 3.2, findContours() no longer modifies the source image.
+ In OpenCV, finding contours is like finding white object from black background. So remember, object to be found should be white and background should be black.

```
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
```
See, there are three arguments in cv.findContours() function, first one is source image, second is contour retrieval mode, third is contour approximation method. And it outputs the contours and hierarchy. Contours is a Python list of all the contours in the image. Each individual contour is a Numpy array of (x,y) coordinates of boundary points of the object.
# How to draw the contours?
To draw the contours, cv.drawContours function is used. It can also be used to draw any shape provided you have its boundary points. Its first argument is source image, second argument is the contours which should be passed as a Python list, third argument is index of contours (useful when drawing individual contour. To draw all contours, pass -1) and remaining arguments are color, thickness etc.
+ To draw all the contours in an image:
    cv.drawContours(img, contours, -1, (0,255,0), 3)
+ To draw an individual contour, say 4th contour:
    cv.drawContours(img, contours, 3, (0,255,0), 3)
+ But most of the time, below method will be useful:
    cnt = contours[4]
    cv.drawContours(img, [cnt], 0, (0,255,0), 3)
# Contour Approximation Method
This is the third argument in cv.findContours function. What does it denote actually?

 cv.CHAIN_APPROX_NONE 会遍历保存所有的相似点，而CHAIN_APPROX_SIMPLE只保存相似点，比如一条直线，有2个点就够了，不用全部保存

