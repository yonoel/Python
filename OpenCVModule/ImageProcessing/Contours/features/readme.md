#GOAL
In this article, we will learn

+ To find the different features of contours, like area, perimeter, centroid, bounding box etc
+ You will see plenty of functions related to contours.
#1. Moments
图像矩，图像矩阵。。。
The function cv.moments() gives a dictionary of all moment values calculated. See below:

```
M = cv.moments(cnt)
```
#2. Contour Area
Contour area is given by the function cv.contourArea() or from moments, M['m00'].

```
area = cv.contourArea(cnt)
```
#3. Contour Perimeter
It is also called arc length. It can be found out using cv.arcLength() function. Second argument specify whether shape is a closed contour (if passed True), or just a curve.



