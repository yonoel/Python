# coding:utf-8
import cv2 as cv
import pytesseract as tesseract
import os
from utils import util
import numpy


class Detector:
    width = 1200
    temp_no = cv.imread(
        "/Users/yonoel/Desktop/PythonWorkspace/Python/Test/InvoiceDetection/NO.jpeg", 0)

    def __init__(self, path):
        self.image = cv.imread(path, 0)
        if self.image is None:
            raise FileNotFoundError(path)
        self.rois = []
        self.pre_treat_image()
        self.set_rois()

    def pre_treat_image(self):
        self.resize()

    def resize(self):
        height, width = self.image.shape[:2]
        ratio = float(width / height)
        self.image = cv.resize(
            self.image, (int(self.width * ratio), self.width))

    def set_rois(self):
        match_point = self.get_match_point()
        temp_width, temp_height = self.temp_no.shape

        num_top_left = (match_point[0] + temp_width, match_point[1]-5)
        num_bottom_right = (
            num_top_left[0] + 7 * temp_width, num_top_left[1] + temp_height + 10)

        code_top_left = (match_point[0] - temp_width * 23, match_point[1]-20)
        code_bottom_right = (
            code_top_left[0] + 9 * temp_width, code_top_left[1] + temp_height + 30)

        roi_num = self.image[num_top_left[1]:num_bottom_right[1],
                             num_top_left[0]:num_bottom_right[0]]

        num_width = get_width_by_projection(roi_num, 250)
        roi_num = roi_num[0:roi_num.shape[0], num_width[0]:num_width[1]]

        roi_code = self.image[code_top_left[1]:code_bottom_right[1],
                              code_top_left[0]:code_bottom_right[0]]

        roi_code = cv.flip(roi_code,90)
        code_width = get_width_by_projection(roi_code, 300)
        roi_code = roi_code[0:roi_code.shape[0],code_width[0]:code_width[1]]
        roi_code = cv.flip(roi_code,90)

        self.rois.append(roi_code)
        self.rois.append(roi_num)

    def get_match_point(self):
        no_res = cv.matchTemplate(self.image, self.temp_no, cv.TM_CCOEFF)
        min_val, max_val, min_loc, max_lox = cv.minMaxLoc(no_res)

        if max_lox[1] > self.image.shape[1] / 2:
            self.image = cv.rotate(self.image, cv.ROTATE_180)
            no_res = cv.matchTemplate(self.image, self.temp_no, cv.TM_CCOEFF)
            min_val, max_val, min_loc, max_lox = cv.minMaxLoc(no_res)
        match_point = max_lox
        return match_point

    def get_invoice_code(self):
        code = self.rois[0]
        # code = self.pre_treat_roi(code)
        return do_ocr(code)

    def get_invoice_number(self):
        number = self.rois[1]
        # number = self.pre_treat_roi(number)
        return do_ocr(number)


def pre_treat_roi(img):
    ret, img = cv.threshold(img, 130, 255, cv.THRESH_BINARY)
    kernel = cv.getStructuringElement(
        cv.MORPH_RECT, (5, 5))  # 形态学处理:定义矩形结构
    closed = cv.erode(img, kernel, iterations=1)
    closed = cv.GaussianBlur(closed, (3, 3), 1)
    return closed


def split_invoice_code(img):
    height, width = img.shape[:2]
    closed = pre_treat_roi(img)
    z_list = []
    v_list = []
    acc = 0

    for y in range(height):
        for x in range(width):
            p_color = closed[y, x]
            if p_color == 0:
                acc += 1
            else:
                continue
        if acc != 0:
            v_list.append(x)
        acc = 0

    empty = numpy.zeros((height, width))
    for y in range(height):
        for x in range(width):
            empty[y, x] = 255
    util.show_img_in_pl(empty)


def get_width_by_projection(img, roi_width):
    height, width = img.shape[:2]
    closed = pre_treat_roi(img)
    z_list = []
    acc = 0
    for x in range(width):
        for y in range(height):
            p_color = closed[y, x]
            if p_color == 0:
                acc += 1
            else:
                continue
        if acc != 0:
            z_list.append(x)
        acc = 0
    return get_num_width(z_list, roi_width)


def get_num_width(z_list, width):
    length = len(z_list)
    num_width = (z_list[0], z_list[0]+width)
    for x in range(1, int(length/2)):
        p_pre = z_list[x-1]
        p = z_list[x]
        if p_pre + 1 != p and p - p_pre > 20:
            num_width = (p, p + width)
            break
    return num_width


def do_ocr(roi):
    config = "--psm 13 digits"
    return tesseract.image_to_string(roi, config=config)


if __name__ == '__main__':
    # name = "/Users/yonoel/Desktop/PythonWorkspace/Python/Test/InvoiceDetection/coderois/110.jpg"
    # # de = Detector(name)
    # img = cv.imread(name, 0)
    # flip_img = cv.flip(img,90)
    # pt = get_width_by_projection(flip_img, 300)
    # height, w = flip_img.shape[:2]
    # # flip_img = cv.flip(flip_img,90)
    # roi = flip_img[0:height, pt[0]:pt[1]]
    # roi = cv.flip(roi,90)
    # util.show_img_in_pl(roi)
    # Detector.do_split_char(number)

    # Detector.do_split_char(number)
    # de = Detector(name)
    # util.show_img_in_pl(de.rois[1])
    # show_img_in_pl(number)
    # n = de.do_ocr(number)
    # print(n)
    # show_img_in_pl(de.pre_treat_roi(number))
    # show_img_in_pl(code)
    # print(de.get_invoice_number()+"    "+ de.get_invoice_code())
    fileName = "/Users/yonoel/Desktop/PythonWorkspace/Python/Test/InvoiceDetection/resources"
    for root, dirs, files in os.walk(fileName):
        for f in files:
            if f.endswith(".jpg"):
                path = os.path.join(root, f)
                de = Detector(path)
                # code = de.get_invoice_code()
                # number = de.get_invoice_number()

                roi_code = de.rois[0]
                roi_number = de.rois[1]
    # cv.imwrite(
    # "/Users/yonoel/Desktop/PythonWorkspace/Python/Test/InvoiceDetection/coderois/"+f, roi_code)
                util.show_img_in_pl(roi_code)
    # util.show_img_in_pl(roi_number)
    # print("file is %s and code is %s and number is %s "%(f,code,number))
