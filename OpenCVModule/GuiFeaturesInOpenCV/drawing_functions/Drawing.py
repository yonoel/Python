import numpy as np
import cv2 as cv
# 四个参数
# img
# lineType
# color
# thickness

# Create a black image
img = np.zeros((512,512,3), np.uint8)
# Draw a diagonal blue line with thickness of 5 px 对角线
# cv.line(img,(0,0),(511,511),(255,0,0),5)
# cv.imshow('line-img',img)
# 矩形
# cv.rectangle(img,(384,0),(510,128),(255,0,0),5)
# cv.imshow('rectangle-img',img)
# cv.circle(img,(447,63), 63, (255,0,0), -1)
# cv.imshow("circle-img",img)
# cv.ellipse(img, (256, 256), (100, 50), 0, 0, 180, (0,0,255), -1)
# cv.imshow("ellipse",img)
# 多边形
# pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
# pts = pts.reshape((-1,1,2))
# cv.polylines(img,[pts],True,(0,255,255))
# cv.polylines(img,[pts],False,(0,255,255))
# cv.imshow("poly",img)
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)
cv.imshow("text",img)
if cv.waitKey(0) :
    cv.destroyAllWindows()
