# Goal
+ Learn to apply different geometric transformation to images like translation, rotation, affine transformation etc.
+ You will see these functions: cv.getPerspectiveTransform
# Transformations
OpenCV provides two transformation functions, cv.warpAffine and cv.warpPerspective, with which you can have all kinds of transformations. cv.warpAffine takes a 2x3 transformation matrix while cv.warpPerspective takes a 3x3 transformation matrix as input.
# Scaling
Scaling is just resizing of the image. OpenCV comes with a function cv.resize() for this purpose. 

The size of the image can be specified manually, or you can specify the scaling factor. Different interpolation methods are used. Preferable interpolation methods are cv.INTER_AREA for shrinking and cv.INTER_CUBIC (slow) & cv.INTER_LINEAR for zooming.

 By default, interpolation method used is cv.INTER_LINEAR for all resizing purposes. You can resize an input image either of following methods:
 ```
import numpy as np
import cv2 as cv
img = cv.imread('messi5.jpg')
res = cv.resize(img,None,fx=2, fy=2, interpolation = cv.INTER_CUBIC)
#OR
height, width = img.shape[:2]
res = cv.resize(img,(2*width, 2*height), interpolation = cv.INTER_CUBIC)
 ```
 # Translation
 Translation is the shifting of object's location. 
 If you know the shift in (x,y) direction, let it be (tx,ty), you can create the transformation matrix M as follows:

x->x0
y->y0
M =[1,0,temp(x)],[0,1.temp(y)]


You can take make it into a Numpy array of type np.float32 and pass it into cv.warpAffine() function. See below example for a shift of (100,50):
```
import numpy as np
import cv2 as cv
img = cv.imread('messi5.jpg',0)
rows,cols = img.shape
M = np.float32([[1,0,100],[0,1,50]])
dst = cv.warpAffine(img,M,(cols,rows))
cv.imshow('img',dst)
cv.waitKey(0)
cv.destroyAllWindows()
```

#### warning
Third argument of the cv.warpAffine() function is 
+ the size of the output image, which should be in the form of **(width, height)**. Remember width = number of columns, and height = number of rows.
# Rotation(翻转)
Rotation of an image for an angle θ is achieved by the transformation matrix of the form

M = [cosθ,-sinθ],[sinθ,cosθ]

But OpenCV provides scaled rotation with adjustable center of rotation so that you can rotate at any location you prefer. Modified transformation matrix is given by

[αβ(1−α)⋅center.x−β⋅center.y],
[-βα⋅center.x+(1−α)⋅center.y]

and α=scale⋅cosθ,β=scale⋅sinθ

To find this transformation matrix, OpenCV provides a function, cv.getRotationMatrix2D.

below example which rotates the image by 90 degree with respect to center without any scaling.
```
img = cv.imread('messi5.jpg',0)
rows,cols = img.shape
# cols-1 and rows-1 are the coordinate limits. cv.getRotationMatrix2D(	center, angle, scale	)
M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
dst = cv.warpAffine(img,M,(cols,rows))
```
# Affine Transformation(仿射变换（映射）)
百度定义：仿射变换，又称仿射映射，是指在几何中，一个向量空间进行一次线性变换并接上一个平移，变换为另一个向量空间。
// todo 看不懂，先跳过,向量一脸懵
Check below example, and also look at the points I selected (which are marked in Green color):
```
img = cv.imread('drawing.png')
rows,cols,ch = img.shape
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
M = cv.getAffineTransform(pts1,pts2)
dst = cv.warpAffine(img,M,(cols,rows))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
```

# Perspective Transformation(透视)
百度定义:将图片投影到一个新的视平面(Viewing Plane),也称作投影映射(Projective Mapping)

For perspective transformation, you need a 3x3 transformation matrix.Straight lines will remain straight even after the transformation. 

o find this transformation matrix, you need 4 points on the input image and corresponding points on the output image.

Among these 4 points, 3 of them should not be collinear. Then transformation matrix can be found by the function cv.getPerspectiveTransform. Then apply cv.warpPerspective with this 3x3 transformation matrix.

```
img = cv.imread('sudoku.png')
rows,cols,ch = img.shape
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv.getPerspectiveTransform(pts1,pts2)
dst = cv.warpPerspective(img,M,(300,300))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
```

