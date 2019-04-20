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


# 5. Convex Hull
# syntax : hull = cv2.convexHull(points[, hull[, clockwise[, returnPoints]]])
hull = cv2.convexHull(cnt)


# 6. Checking Convexity
k = cv2.isContourConvex(cnt)


# 7.Bounding Rectangle
#   7.a. Straight Bounding Rectangle
x,y,w,h = cv2.boundingRect(cnt)
img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)


#   7.b. Rotated Rectangle
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
img = cv2.drawContours(img, [box], 0, (0, 0, 255), 2)


# 8.Minimum Enclosing Circle
(x, y), radius = cv2.minEnclosingCircle(cnt)
center = (int(x), int(y))
radius = int(radius)
img = cv2.circle(img, center, radius, (0, 255, 0), 2)


# 9.Fitting an Ellipse
ellipse = cv2.fitEllipse(cnt)
img = cv2.ellipse(img, ellipse, (0, 255, 0), 2)



# 10.Fitting a Line
rows, cols = img.shape[:2]
[vx, vy, x, y] = cv2.fitLine(cnt, cv2.DIST_L2, 0, 0.01, 0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx) + y)
img = cv2.line(img, (cols-1, righty), (0, lefty), (0, 255, 0), 2)







