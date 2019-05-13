# coding=utf-8
import cv2 as cv
from matplotlib import pyplot as plt


def get_u_d_l_r(rect_):
    # 获取rect的上下左右边界值
    upper_, down_ = rect_[1], rect_[1] + rect_[3]
    left_, right_ = rect_[0], rect_[0] + rect_[2]
    return upper_, down_, left_, right_


def get_top_left_bottom_right_(rect):
    return rect[1], rect[0], rect[3] + rect[1], rect[0] + rect[2]


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
