# coding=utf-8
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import os
import pytesseract


def image_read(filename, flags=cv.IMREAD_GRAYSCALE):
    return cv.imread(filename, flags)


def to_binary(src):
    img = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    mask = cv.adaptiveThreshold(
        img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 7, 7)
    return mask


def morphological(img):
    ele1 = cv.getStructuringElement(cv.MORPH_RECT, (9, 7))
    ele2 = cv.getStructuringElement(cv.MORPH_RECT, (9, 1))
    dilation = cv.dilate(img, ele1, iterations=1)
    erosion = cv.erode(dilation, ele1, iterations=1)
    dilation = cv.dilate(erosion, ele2, iterations=1)
    return dilation


def draw_contours(src):
    contours, hierarchy = cv.findContours(
        src, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(src, contours, -1, (0, 255, 0))


def template_match(template, src, method=cv.TM_CCOEFF):
    img = src.copy()
    return cv.matchTemplate(img, template, method)


def show_img_in_ply(img):
    plt.subplot(121), plt.imshow(img, cmap="gray"), plt.title("result is")
    plt.show()


def show_img_in_cv(img):
    cv.imshow("原图", img)
    cv.waitKey(0)
    cv.destroyAllWindows()


def get_invoice_num_roi(res, template, src):
    src_width, src_height, un_use = src.shape
    tem_width, tem_height, un_use = template.shape
    min_val, max_val, min_loc, max_lox = cv.minMaxLoc(res)
    top_left = max_lox
    if top_left[1] < src_height / 2:
        top_left = (top_left[0] + tem_width, top_left[1])
        bottom_right = (top_left[0] + 7 * tem_width, top_left[1] + tem_height)
    else:
        bottom_right = (top_left[0], top_left[1] + tem_height)
        top_left = (top_left[0] - 7 * tem_width, top_left[1])
    return (top_left[0], top_left[1], bottom_right[0], bottom_right[1])
    # cv.rectangle(output, top_left, bottom_right, 255, 2)
    # return output


def change(src):
    rows, cols, ch = src.shape
    pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
    pts2 = np.float32([[50, 50], [200, 50], [50, 200]])
    M = cv.getAffineTransform(pts1, pts2)
    dst = cv.warpAffine(src, M, (cols, rows))
    return dst


def find_code_roi(src):
    pass


img_path_suffix = "./resources/"
resize_path_suffix = "./resize/"

if __name__ == '__main__':
    filename = "110.jpg"
    temp_no = "NO2.jpg"
    path = resize_path_suffix + filename
    image = cv.imread(path, 0)
    temp_no = cv.imread(temp_no,0)
    res = cv.matchTemplate(image,temp_no,cv.TM_CCOEFF)
    min_val, max_val, min_loc, max_lox = cv.minMaxLoc(res)
    print(min_loc[0],min_loc[1])
    print(max_lox[0],max_lox[1])
    # cv.circle(image,max_lox,20,255,10)
    # show_img_in_cv(image)


