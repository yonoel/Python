# coding=utf-8
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


def imread(filename, flags=cv.IMREAD_COLOR):
    return cv.imread(filename, flags)


def toBinary(src):
    img = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    mask = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 7, 7)
    return mask


def morphological(img):
    ele1 = cv.getStructuringElement(cv.MORPH_RECT, (9, 7))
    ele2 = cv.getStructuringElement(cv.MORPH_RECT, (9, 1))
    dilation = cv.dilate(img, ele1, iterations=1)
    erosion = cv.erode(dilation, ele1, iterations=1)
    dilation = cv.dilate(erosion, ele2, iterations=1)
    return dilation


def drawContours(src):
    contours, hierarchy = cv.findContours(src, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(src, contours, -1, (0, 255, 0))


def templateMatch(template, src, method=cv.TM_CCOEFF):
    img = src.copy()
    return cv.matchTemplate(img, template, method)


def showImgInPLY(img):
    plt.subplot(121), plt.imshow(img, cmap="gray"), plt.title("result is")
    plt.show()


def showImgInCV(img):
    cv.imshow("原图", img)
    cv.waitKey(0)
    cv.destroyAllWindows()


def getFpdmROI(res, template, src):
    src_width, src_height, un_use = src.shape
    tem_width, tem_height, un_use = template.shape
    output = src.copy()
    min_val, max_val, min_loc, max_lox = cv.minMaxLoc(res)
    top_left = max_lox
    top_left = (top_left[0] + tem_width, top_left[1])
    x = int(src_width - top_left[0] / 1.69)
    bottom_right = (top_left[0] + x, top_left[1] + tem_height)
    return (top_left[0], top_left[1], bottom_right[0], bottom_right[1])
    # cv.rectangle(output, top_left, bottom_right, 255, 2)
    # return output


def getFpdmRegion():
    region = []
    for i in range(len(contours)):
        contour = contours[i]
        rect = cv.boundingRect(contour)
        w = rect[2]
        h = rect[3]
        ratio = float(w) / float(h)
        if 6.5 > ratio > 6.2:
            region.append(rect)
    return region


if __name__ == '__main__':
    src = imread("2019_04_18_155557555576697.jpg")
    no = imread("NO.jpeg")
    res = templateMatch(no, src)
    fpdmROI = getFpdmROI(res, no, src)

    x = fpdmROI[0]
    y = fpdmROI[1]
    w = fpdmROI[2]
    h = fpdmROI[3]

    cv.imwrite("代码区域.jpg", src[y:h, x:w])
    # contours, hierarchy = cv.findContours(out, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    #     try:
    #         w = rect[2]
    #         h = rect[3]
    #         ratio = w / h
    #         if 5.5 < ratio < 6:
    #             print("1")
    #     except TypeError:
    #         print("发生异常")
    # showImgInCV(out)

    # print(len(region))
    # showImgInCV(out)
    # no = toBinary(no)
    # output = drawFpdmROI()
