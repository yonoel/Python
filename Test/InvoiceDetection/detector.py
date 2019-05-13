# coding:utf-8
import cv2 as cv
import pytesseract as tesseract


class Detector:
    width = 1200
    temp_no = cv.imread("NO.jpeg", 0)

    def __init__(self, path):
        self.image = cv.imread(path, 0)
        self.pre_treat()

    def pre_treat_image(self):
        self.resize()

    def resize(self):
        height, width = self.image.shape[:2]
        ratio = float(width / height)
        self.image = cv.resize(self.image, (int(self.width * ratio), self.width))

    def get_roi_list(self):
        roi_list = []
        match_point = self.get_match_point()
        temp_width, temp_height = self.temp_no.shape

        num_top_left = (match_point[0] + temp_width, match_point[1])
        num_bottom_right = (num_top_left[0] + 7 * temp_width, num_top_left[1] + temp_height)
        code_top_left = (match_point[0] - temp_width * 23, match_point[1])
        code_bottom_right = (code_top_left[0] + 9 * temp_width, code_top_left[1] + 2 * temp_height)

        roi_num = self.image[num_top_left[1]:num_bottom_right[1], num_top_left[0]:num_bottom_right[0]]
        roi_code = self.image[code_top_left[1]:code_bottom_right[1], code_top_left[0]:code_bottom_right[0]]
        roi_list.append(roi_num)
        roi_list.append(roi_code)
        return roi_list

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

    @staticmethod
    def pre_treat_roi(img):
        # 最好能垂直图片，并根据投影法分割数字，一个个去比对
        img = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 9, 7)
        kernel = cv.getStructuringElement(cv.MORPH_RECT, (2, 2))  # 形态学处理:定义矩形结构
        closed = cv.erode(img, kernel, iterations=2)
        closed = cv.GaussianBlur(closed, (3, 3), 1)
        return closed

    @staticmethod
    def get_nums(roi):
        config = "--psm 13 digits"
        return tesseract.image_to_string(roi, config=config)


if __name__ == '__main__':
    resize_path_suffix = "./resize/"
    resources_path_suffix = "./resources/"
    image = "2019_04_18_155557571564410.jpg"
    roi = cv.imread("test.jpg")
    num = Detector.get_nums(roi)
    print(num)
