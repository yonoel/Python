import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# All the 6 methods for comparison in a list
methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
           'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']


def templateMatch(template, src):
    width, height = template.shape[::-1]
    for meth in methods:
        img = src.copy()
        method = eval(meth)

        res = cv.matchTemplate(img, template, method)
        min_val, max_val, min_loc, max_lox = cv.minMaxLoc(res)

        if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_lox
        bottom_right = (top_left[0] + width, top_left[1] + height)

        cv.rectangle(img, top_left, bottom_right, 255, 2)

        plt.subplot(121), plt.imshow(res, cmap="gray")
        plt.title('matching result'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(img, cmap="gray")
        plt.title("detected point"), plt.xticks([]), plt.yticks([])
        plt.suptitle(meth)

        plt.show()


if __name__ == '__main__':
    img = cv.imread("messi5.jpg", 0)
    template = cv.imread("template.jpg", 0)
    templateMatch(template, img)
