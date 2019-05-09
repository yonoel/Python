# encoding: utf-8
import numpy as np
import cv2 as cv
from utils import util

def test():
    img0 = cv.imread("./numbers.jpg")
    _, img0 = cv.threshold(img0, 100, 255, cv.THRESH_BINARY)
    img0 = 255 - img0
    element1 = cv.getStructuringElement(cv.MORPH_RECT, (5, 1))
    element2 = cv.getStructuringElement(cv.MORPH_RECT, (1, 3))
    element3 = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))

    img1 = cv.dilate(img0, element1, iterations=1)
    img2 = cv.dilate(img0, element2, iterations=1)
    img3 = cv.dilate(img0, element3, iterations=1)
    img = [img0, img1, img2, img3]
    return img


def cal_hist(img_, flag=0):
    return np.sum(img_, axis=flag)


class Find_num_region:
    def __init__(self, img, hist):
        self.cursor = -1
        self.hist = hist
        self.img = img

    def next(self):
        self.cursor = self.cursor + 1
        return self.hist[self.cursor]

    def hasNext(self):
        # 判断是否已经检查完了所有矩形框
        return len(self.hist) > self.cursor + 1

    def find_start(self):
        while (self.hasNext()):
            hist_num = self.next()
            if hist_num > 0:
                return self.cursor

    def find_end(self):
        while (self.hasNext()):
            hist_num = self.next()
            if hist_num == 0:
                return self.cursor

    def get_num_region(self, flag=0):
        start = self.find_start()
        end = self.find_end()
        if flag == 0:
            return self.img.copy()[:, start:end]
        else:
            return self.img.copy()[start:end, :]


def seg_num(img_):
    hist_1 = cal_hist(img_, 1)
    # 计算1唯的sum
    find_num_ = Find_num_region(img_, hist_1)
    img = find_num_.get_num_region(1)
    hist_2 = cal_hist(img_)
    find_num = Find_num_region(img_, hist_2)
    img_number = []
    for i in range(10):
        print
        i
        img_number.append(find_num.get_num_region())
    return img_number

if __name__ == '__main__':
    img_list = test()
    # 对img0、img1、img2、img3进行分割，并保存分割后的图片
    img_seg = []
    for img_ in img_list:
        img_seg.append(seg_num(img_))