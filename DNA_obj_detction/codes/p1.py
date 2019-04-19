# contour feature analysis
# https://docs.opencv.org/3.4/dd/d49/tutorial_py_contour_features.html


# 1. Moments
import cv2
import numpy as np

img = cv2.imread('../images/isolated_images/6.jpg', 0)

ret, thresh = cv2.threshold(img, 127, 255, 0)
thresh_ret, contours, hierarchy = cv2.findContours(thresh, 1, 2)

cnt = contours[0]
M = cv2.moments(cnt)
#print(M)


# Centroid
cx = int(M['m10'] / M['m00'])
cy = int(M['m01'] / M['m00'])


# 2. Contour Area
area = cv2.contourArea(cnt)
print ("area is:", area)


# 3. Contour Perimeter (arc length)
perimeter = cv2.arcLength(cnt, True)
print ("arc length:", perimeter)


# 4. Contour Approximation
epsilon = 0.1 * cv2.arcLength(cnt, True)            # epsilon = 10% of arc length
approx = cv2.approxPolyDP (cnt, epsilon, True)      # epsilon = 1% of the arc length








