import numpy as np
import cv2
import matplotlib
from matplotlib import pyplot as plt

img = cv2.imread('../images/isolated_images/6.jpg')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
thresh, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(contours)

# To draw contours
#img_with_cnt = cv2.drawContours(imgray, contours, -1, (0, 255, 0), 3)
#plt.imshow(img_with_cnt, cmap='gray')
#plt.show()


## To draw an individual contour, say 4th contour:
#cv2.drawContours(img, contours, 3, (0,255,0), 3)


## But most of the time, below method will be useful:
#cnt = contours[4]
#cv2.drawContours(img, [cnt], 0, (0,255,0), 3)


#
cnt = contours[2]
eps = 0.1 * cv2.arcLength(cnt, True)
approx = cv2.approxPolyDP(cnt, eps, True)
img_with_cnt = cv2.drawContours(imgray, approx, -1, (0, 255, 0), 3)
plt.imshow(img_with_cnt, cmap='gray')
plt.show()
