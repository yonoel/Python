# 测试投影法切割
import cv2 as cv
import numpy
from matplotlib import pyplot as plt
from utils import util

if __name__ == "__main__":
    path = "./numrois/"
    fileName = "110num.jpg"
    img = cv.imread(path + fileName, 0)
    # img = cv.Canny(img, 100, 200)
    # img = 255 - img
    img = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 9, 7)
    # util.show_img_in_cv(img)
    # height, width = img.shape[:2]
    # ret, thresh = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (2, 2))  # 形态学处理:定义矩形结构
    closed = cv.erode(img, kernel, iterations=2)
    closed = cv.GaussianBlur(closed, (3, 3), 1)
    cv.imwrite("test.jpg", closed)
    # util.show_img_in_cv(img)
    # height, width = closed.shape
    # v = [0] * width
    # z = [0] * height
    # a = 0
    # # 垂直投影
    # # 统计并存储每一列的黑点数
    # for x in range(0, width):
    #     for y in range(0, height):
    #         if closed[y, x] == 0:
    #             a = a + 1
    #         else:
    #             continue
    #     v[x] = a
    #     a = 0
    #
    # 创建空白图片，绘制垂直投影图
    # emptyImage = numpy.zeros((height, width, 3), numpy.uint8)
    # for x in range(0, width):
    #     for y in range(0, v[x]):
    #         b = (255, 255, 255)
    #         emptyImage[y, x] = b
    # util.show_img_in_cv(emptyImage)
