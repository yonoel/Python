# coding:utf-8
import cv2 as cv
import pytesseract as tesseract
import os
class Detector:
    width = 1200
    temp_no = cv.imread("NO.jpeg", 0)

   

    def __init__(self, path):
        self.image = cv.imread(path, 0)
        if self.image is None:raise FileNotFoundError(path)
        self.rois = []
        self.pre_treat_image()
        self.set_rois()

    def pre_treat_image(self):
        self.resize()

    def resize(self):
        height, width = self.image.shape[:2]
        ratio = float(width / height)
        self.image = cv.resize(self.image, (int(self.width * ratio), self.width))

    def set_rois(self):

        match_point = self.get_match_point()
        temp_width, temp_height = self.temp_no.shape

        num_top_left = (match_point[0] + temp_width, match_point[1])
        num_bottom_right = (num_top_left[0] + 7 * temp_width, num_top_left[1] + temp_height)
        code_top_left = (match_point[0] - temp_width * 23, match_point[1])
        code_bottom_right = (code_top_left[0] + 9 * temp_width, code_top_left[1] + 2 * temp_height)

        roi_num = self.image[num_top_left[1]:num_bottom_right[1], num_top_left[0]:num_bottom_right[0]]
        roi_code = self.image[code_top_left[1]:code_bottom_right[1], code_top_left[0]:code_bottom_right[0]]
        self.rois.append(roi_code)
        self.rois.append(roi_num)
      

    def get_match_point(self):
        no_res = cv.matchTemplate(self.image, self.temp_no, cv.TM_CCOEFF)
        min_val, max_val, min_loc, max_lox = cv.minMaxLoc(no_res)
        match_point = max_lox
        if match_point[1] > self.image.shape[1] / 2:
            self.image = cv.rotate(self.image, cv.ROTATE_180)
            no_res = cv.matchTemplate(self.image, self.temp_no, cv.TM_CCOEFF)
            min_val, max_val, min_loc, max_lox = cv.minMaxLoc(no_res)
            match_point = max_lox
        return match_point

    def get_invoice_code(self):
        code = self.rois[0]
        code = self.pre_treat_roi(code)
        return self.do_ocr(code)

    def get_invoice_number(self):
        number = self.rois[1]
        number = self.pre_treat_roi(number)
        return self.do_ocr(number)  

   
    def pre_treat_roi(self,img):
        # 最好根据投影法分割数字，一个个去比对
        img = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 9, 7)
        kernel = cv.getStructuringElement(cv.MORPH_RECT, (2, 2))  # 形态学处理:定义矩形结构
        closed = cv.erode(img, kernel, iterations=2)
        closed = cv.GaussianBlur(closed, (3, 3), 1)
        return closed


    def do_ocr(self,roi):
        config = "--psm 13 digits"
        return tesseract.image_to_string(roi, config=config)


if __name__ == '__main__':
    fileName = "C://Users//Think//Desktop//scanner-images"
    for root,dirs,files in os.walk(fileName):
       for f in files:
           if f.endswith(".jpg"):
               path = os.path.join(root,f)
               de = Detector(path)
               code = de.get_invoice_code()
               number = de.get_invoice_number()
               print("file is %s and code is %s and number is %s "%(f,code,number))
