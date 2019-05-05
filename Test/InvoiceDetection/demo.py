import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# All the 6 methods for comparison in a list
methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
           'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']


def imread(filename, flags=cv.IMREAD_COLOR):
    return cv.imread(filename, flags)


def toBinary(src):
    img = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    # ret,mask = cv.threshold(img,120,255,cv.THRESH_BINARY_INV)
    mask = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 7, 7)
    mask = cv.medianBlur(mask, 1)
    return mask


def drawContours(src):
    contours, hierarchy = cv.findContours(src, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(src, contours, -1, (0, 255, 0))


def templateMatch(template, src):
    height, width, un = template.shape[::]
    for meth in methods:
        img = src.copy()
        method = eval(meth)

        res = cv.matchTemplate(img, template, method)
        min_val, max_val, min_loc, max_lox = cv.minMaxLoc(res)

        if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_lox
        bottom_right = (top_left[0] + width, top_left[1] + height)

        cv.rectangle(img, top_left, bottom_right, (255, 0, 0), 5)

        plt.subplot(121), plt.imshow(res, cmap="gray")
        plt.title('matching result'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(img, cmap="gray")
        plt.title("detected point"), plt.xticks([]), plt.yticks([])
        plt.suptitle(meth)

        plt.show()


if __name__ == '__main__':
    src = imread("2019_04_18_155557555576697.jpg")
    template = imread("template.jpg")
    # img = toBinary(src)
    templateMatch(template, src)
    # cv.imshow("原图", img)
    # cv.waitKey(0)
    # cv.destroyAllWindows()
