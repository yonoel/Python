# encoding:utf-8
import cv2
import numpy as np


# 将img的高度调整为28，先后对图像进行如下操作：直方图均衡化，形态学，阈值分割
def pre_treat(img):
    height_ = 28
    ratio_ = float(img.shape[1]) / float(img.shape[0])
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, (int(ratio_ * height_), height_))
    gray = cv2.equalizeHist(gray)
    _, binary = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)
    img_ = 255 - binary  # 反转：文字置为白色，背景置为黑色
    return img_


def get_roi_list(contours):
    rect_list = []
    for i in range(len(contours)):
        rect2 = cv2.boundingRect(contours[i])
        if rect2[3] > 10:
            rect_list.append(rect2)
    return rect_list


def get_img_list(rect_list):
    # 保存所有初轮筛选出的图片于img_list中
    img_list = []
    for rect2 in rect_list:
        w1, w2 = rect2[0], rect2[0] + rect2[2]
        h1, h2 = rect2[1], rect2[1] + rect2[3]
        img_list.append(change_(img.copy()[h1:h2, w1:w2]))
    return img_list


def change_(img):
    length = 28
    h, w = img.shape
    H = np.float32([[1, 0, (length - w) / 2], [0, 1, (length - h) / 2]])
    img = cv2.warpAffine(img, H, (length, length))
    M = cv2.getRotationMatrix2D((length / 2, length / 2), 0, 26 / float(img.shape[0]))
    return cv2.warpAffine(img, M, (length, length))


# 获取目标区域的最小外接矩形
def get_rect(img):
    _, contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    rect_list = get_roi_list(contours)
    # 消除内部轮廓，比如“0”内外各有1个轮廓
    rect_list = deleteNull(rect_list)
    return rect_list


def deleteNull(list):
    for rect in list:
        print(rect)
    return list


def get_num_by_SVM(img_list):
    # 通过SVM判断矩形框内的图片是否文数字
    # 加载已经训练好的m文件。（训练过程在下面）
    svm_judge = joblib.load("train_model.m")
    num_list = []
    for img in img_list:
        if svm_judge.predict(img) == 1:
            num_list.append(img)
    return num_list


def showImgInCV(img):
    cv2.imshow("原图", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def seg_num(img):
    img = pre_treat(img)
    rect_list = get_rect(img)
    # 保存所有初轮筛选出的图片于img_list中
    img_list = get_img_list(rect_list)
    img_num = get_num_by_SVM(img_list)


if __name__ == "__main__":
    img = cv2.imread("代码区域.jpg")
    img = pre_treat(img)
    contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    rect_list = get_roi_list(contours)
    for rect in rect_list:
        x = rect[0]
        y = rect[1]
        w = rect[2]
        h = rect[3]
        # cv2.rectangle(img, (x, y), (x + w, y + h), 255, 1)
        print("the rect is ", x, y, x + w, y + h)
    # img_list = get_img_list(rect_list)
    showImgInCV(img)
    # img_num = seg_num(img)
