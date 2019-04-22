# USAGE
# python detect_shapes.py --image shapes_and_colors.png

# import the necessary packages
from pyimagesearch.shapedetector import ShapeDetector
import imutils
import cv2
import numpy as np
import math

# load the image and resize it to a smaller factor so that
# the shapes can be approximated better
image = cv2.imread('../images/isolated_images/6.jpg')    # 'shapes_and_colors.png'
resized = imutils.resize(image, width=300)
ratio = image.shape[0] / float(resized.shape[0])


# convert the resized image to grayscale, blur it slightly,
# and threshold it
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]


# find contours in the thresholded image and initialize the
# shape detector
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
	cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
sd = ShapeDetector()


def findAreaRotRect(box):
    v1 = box[0]
    v2 = box[1]
    v3 = box[2]

    d12 = math.sqrt((v1[0] - v2[0])**2 + (v1[1] - v2[1])**2)
    d23 = math.sqrt((v2[0] - v3[0])**2 + (v2[1] - v3[1])**2)

    area = d12 * d23

    return area

# loop over the contours
for c in cnts:
    #area = cv2.contourArea(c)
    #print('area is:', area)

    # compute the center of the contour, then detect the name of the
    # shape using only the contour
    M = cv2.moments(c)
    cX = int((M["m10"] / M["m00"]) * ratio)
    cY = int((M["m01"] / M["m00"]) * ratio)
    shape = sd.detect(c)

    # multiply the contour (x, y)-coordinates by the resize ratio,
    # then draw the contours and the name of the shape on the image
    c = c.astype("float")
    c *= ratio
    c = c.astype("int")
    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
    cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
        0.5, (255, 255, 255), 2)

    # show the output image
    #cv2.imshow("Image", image)
    #cv2.waitKey(0)

    # Straight Bounding Rectangle
    #x,y,w,h = cv2.boundingRect(c)
    #img = cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,0), 2)
    #cv2.imshow("img_rect", img)
    #cv2.waitKey(0)

    # Rotated Rectangle
    rect = cv2.minAreaRect(c)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    imgRotRect = cv2.drawContours(image, [box], 0, (0, 0, 255), 2)


    # calculate the area
    area_obj = cv2.contourArea(c)
    area_box = findAreaRotRect(box)

    print ("area obj: %.2f" % area_obj)
    print ("area box: %.2f" % area_box)
    print ("area ratio: %.2f" % (area_obj/area_box))

    cv2.imshow("img_rot_rect", imgRotRect)
    cv2.waitKey(0)


