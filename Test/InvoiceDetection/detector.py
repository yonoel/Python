# coding:utf-8
import cv2 as cv
import pytesseract as tesseract
from utils import util
import os
import time


class Detector:
    temp_no = cv.imread("NO.jpeg", 0)
    temp_code = cv.imread("QR.jpg", 0)
    num_res, code_res = 0, 0

    def __init__(self, path):
        self.image = cv.imread(path, 0)
        self.pre_treat()

    def pre_treat(self):
        self.image = cv.adaptiveThreshold(self.image, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 7, 7)

    def find_roi(self):
        roi_list = []
        self.num_res = cv.matchTemplate(self.image, self.temp_no, cv.TM_CCOEFF)
        roi_num = self.get_invoice_num_roi()
        roi_list.append(roi_num)
        return roi_list

    def get_invoice_num_roi(self):
        src_width, src_height = self.image.shape
        tem_width, tem_height = self.temp_no.shape
        min_val, max_val, min_loc, max_lox = cv.minMaxLoc(self.num_res)
        top_left = max_lox
        rotate_flag = 0
        if top_left[1] < src_height / 2:
            top_left = (top_left[0] + tem_width, top_left[1])
            bottom_right = (top_left[0] + 7 * tem_width, top_left[1] + tem_height)
        else:
            bottom_right = (top_left[0], top_left[1] + tem_height)
            top_left = (top_left[0] - 7 * tem_width, top_left[1])
            rotate_flag = 1

        roi = self.image[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
        if rotate_flag == 1:
            roi = cv.rotate(roi, cv.ROTATE_180)
        return roi

    def get_invoice_num(self):
        roi_list = self.find_roi()
        ret = ""
        for roi in roi_list:
            roi = roi_pre_treat(roi)
            util.show_img_in_pl(roi)
            num = tesseract.image_to_string(roi, config="--psm 13")
            return num


def roi_pre_treat(roi):
    height_ = 28
    ratio_ = float(roi.shape[1]) / float(roi.shape[0])
    roi = cv.resize(roi, (int(ratio_ * height_), height_))
    roi = cv.equalizeHist(roi)
    x = cv.getStructuringElement(cv.MORPH_RECT, (3, 1))
    y = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    # roi = cv.dilate(roi, x, iterations=1)
    # roi = cv.erode(roi, y, iterations=1)
    # roi = cv.morphologyEx(roi, cv.MORPH_OPEN, y)
    return roi


if __name__ == '__main__':
    for root, dirs, files in os.walk("./resources"):
        for file in files:
            path = os.path.join(root, file)
            print(path + "  ", Detector(path).get_invoice_num())
