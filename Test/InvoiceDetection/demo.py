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
    mask = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 7, 7)
    return mask


def morphological(img):
    ele1 = cv.getStructuringElement(cv.MORPH_RECT, (9, 7))
    ele2 = cv.getStructuringElement(cv.MORPH_RECT, (9, 1))
    dilation = cv.dilate(img, ele1, iterations=1)
    erosion = cv.erode(dilation, ele1, iterations=1)
    dilation = cv.dilate(erosion, ele2, iterations=1)
    return dilation


def draw_contours(src):
    contours, hierarchy = cv.findContours(src, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)
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


img_path_suffix = "./resources/"

if __name__ == '__main__':
    # 正的图片取minlox厚切,不正的反过来
    qr = image_read("QR.jpg", 0)
    # qr = cv.cvtColor(qr, cv.COLOR_BGR2GRAY)
    qr = cv.adaptiveThreshold(qr, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 7, 7)
    src = image_read(img_path_suffix + "110.jpg", 0)
    # src = cv.cvtColor(src, cv.COLOR_GRAY2RGB)
    res = cv.matchTemplate(src, qr, cv.TM_CCOEFF)
    # res = template_match(qr, src)
    a, b, minLoc, maxLox = cv.minMaxLoc(res)
    cv.circle(src, minLoc, 10, 255, thickness=10)
    # top = b
    # x, y, n = qr.shape
    # img = src[top[1]:y, top[0]:x]
    # show_img_in_cv(src)
    show_img_in_cv(src)
    # for root, dirs, files in os.walk("./numrois"):
    #     for file in files:
    #         path = os.path.join(root, file)
    #         src = cv.imread(path)
    #         config = "--psm 13"
    #         print(path, "  ", pytesseract.image_to_string(to_binary(src), lang="eng", config=config))
    # src = image_read(path)
    # res = template_match(no, src)
    # num_rect = get_invoice_num_roi(res, no, src)

    # x = num_rect[0]
    # y = num_rect[1]
    # w = num_rect[2]
    # h = num_rect[3]
    # cv.imwrite("./numrois/"+file.replace(".jpg", "")+"num.jpg", src[y:h, x:w])
    #
    # num_rect = get_invoice_num_roi(res, no, src)
    #
    # x = num_rect[0]
    # y = num_rect[1]
    # w = num_rect[2]
    # h = num_rect[3]

    # print(x, y, w, h)
    # cv.circle(src, (max_lox[0], max_lox[1]), 30, 255)
    # cv.rectangle(src, (x, y), (w, h), 255, 3)
    # show_img_in_ply(src)
#
# inner_img = src[y:h, x:w]
# inner_img = to_binary(inner_img)
# cv.imwrite("num.jpg", inner_img)
# contours, hierarchy = cv.findContours(out, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

#     try:
#         w = rect[2]
#         h = rect[3]
#         ratio = w / h
#         if 5.5 < ratio < 6:
#             print("1")
#     except TypeError:
#         print("发生异常")
# showImgInCV(out)

# print(len(region))
# showImgInCV(out)
# no = toBinary(no)
# output = drawFpdmROI()
