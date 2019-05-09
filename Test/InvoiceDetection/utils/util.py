# coding=utf-8
import cv2 as cv
from matplotlib import pyplot as plt


def template_match(template, src, method=cv.TM_CCOEFF):
    img = src.copy()
    return cv.matchTemplate(img, template, method)


def to_binary(src):
    img = src.copy()
    mask = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 7, 7)
    return mask


def show_img_in_pl(img):
    plt.subplot(121), plt.imshow(img, cmap="gray"), plt.title("result is")
    plt.show()


def show_img_in_cv(img):
    cv.imshow("原图", img)
    cv.waitKey(0)
    cv.destroyAllWindows()
