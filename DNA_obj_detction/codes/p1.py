# contour feature analysis
# https://docs.opencv.org/3.4/dd/d49/tutorial_py_contour_features.html

import cv2
import numpy as np

img = cv2.imread('../images/isolated_images/6.jpg', 0)

ret, thresh = cv2.threshold(img, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, 1, 2)

cnt = contours[0]
M = cv2.moments(cnt)
print(M)



