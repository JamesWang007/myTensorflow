# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 12:57:19 2019

@author: bejin
"""
## 
import cv2
import numpy as np
import matplotlib.pyplot as plt

##
image_path = 'images/';
img_c = cv2.imread(image_path + 'proteins.jpg', cv2.IMREAD_COLOR);

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img_c)
cv2.waitKey(0);
cv2.destroyAllWindows();



