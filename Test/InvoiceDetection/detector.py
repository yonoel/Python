# coding:utf-8
import cv2 as cv
import pytesseract as tesseract
import os
from utils import util
import numpy


class Detector:
    width = 1200

    temp_no = cv.imread(
        "E:\\workspace\\python\Test\\InvoiceDetection\\NO.jpeg", 0)

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

        nums_width = get_width_by_projection(roi_num, 250, 20)

        roi_nums = [roi_num[0:roi_num.shape[0], width[0]:width[1]]
                    for width in nums_width]

        roi_code = self.image[code_top_left[1]:code_bottom_right[1],
                              code_top_left[0]:code_bottom_right[0]]

        roi_code = cv.flip(roi_code, 90)
        codes_width = get_width_by_projection(roi_code, 300, 10)
        roi_codes = [cv.flip(roi_code[0:roi_code.shape[0],
                                      width[0]:width[1]], 90) for width in codes_width]

        self.rois.append(roi_codes)
        self.rois.append(roi_nums)

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
        codes = self.rois[0]
        acc = ""
        for code in codes:
            code = self.pre_treat_code_roi_before_ocr(code)
            chars = do_ocr(code)
            for char in chars:
                if char.isdigit():
                    acc += char
        return acc[::-1]

    def pre_treat_code_roi_before_ocr(self, code):
        code = cv.adaptiveThreshold(
            code, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 9)
        code = cv.GaussianBlur(code, (3, 3), 5)
        return code

    def get_invoice_number(self):
        numbers = self.rois[1]
        acc = ""
        for num in numbers:
            num = self.pre_treat_number_roi_before_ocr(num)
            chars = do_ocr(num)
            for char in chars:
                if char.isdigit():
                    acc += char
        return acc

    def pre_treat_number_roi_before_ocr(self, num):
        num = cv.adaptiveThreshold(
            num, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 19, 7)
        # num = cv.GaussianBlur(num, (5, 5), 1)
        return num


def pre_treat_roi(img):
    ret, img = cv.threshold(img, 130, 255, cv.THRESH_BINARY)
    kernel = cv.getStructuringElement(
        cv.MORPH_RECT, (5, 5))
    closed = cv.erode(img, kernel, iterations=1)
    closed = cv.GaussianBlur(closed, (3, 3), 1)
    return closed


def get_width_by_projection(img, roi_width, char_width):
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

    width = get_num_width(z_list,roi_width, char_width)
   
    return width


def get_num_width(z_list,roi_width, width):
    length = len(z_list)
    num_width = [(z_list[0], z_list[-1])]

    for x in range(1, length):
        p_pre = z_list[x-1]
        p_now = z_list[x]
        if p_pre + 1 != p_now:
            pt_pre = num_width[-1]
            if pt_pre[1] == z_list[-1]:
                pt_pre = (pt_pre[0], p_pre)
                del num_width[-1]
                num_width.append(pt_pre)
            num_width.append((p_now, z_list[-1]))
    acc = [pt for pt in num_width if pt[1] - pt[0] >= width]
    acc = [pt for pt in acc if acc[0][0] + roi_width >= pt[0]]
    return acc


def do_ocr(roi):
    config = "--psm 13 digits"
    return tesseract.image_to_string(roi, config=config)


if __name__ == '__main__':
    # name = "C:\\Users\\Think\\Desktop\\scanner-images\\91320205MA1NRA389K\\1557114656622\\2019_05_06_155711466034091.jpg"
    # de = Detector(name)
    # number = de.get_invoice_number()
    # code = de.get_invoice_code()
    # print(number)
    # print(code)
    # img = cv.imread(name, 0)
    # code = de.rois[0]
    # for x in code:
        # util.show_img_in_pl(x)
    # code = de.rois[1]
    # for x in code:
        # util.show_img_in_pl(x)
    # print(de.get_invoice_code())
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
    fileName = "C:\\Users\\Think\\Desktop\\scanner-images"
    for root, dirs, files in os.walk(fileName):
        for f in files:
            if f.endswith(".jpg"):
                path = os.path.join(root, f)
                de = Detector(path)
                code = de.get_invoice_code()
                number = de.get_invoice_number()

                # roi_code = de.rois[0]
                # roi_number = de.rois[1]
    #             # cv.imwrite(
    #         # "/Users/yonoel/Desktop/PythonWorkspace/Python/Test/InvoiceDetection/coderois/"+f, roi_code)
    #             # util.show_img_in_pl(roi_code)
    # # util.show_img_in_pl(roi_number)
                print("file is %s and code is %s and number is %s " %
                      (f, code, number))
