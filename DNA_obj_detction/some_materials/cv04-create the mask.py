#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 20:00:14 2019

@author: haiyangwang
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt



img = cv2.imread('images/gray.jpg', -1);
img_flt = cv2.imread('images/img_res.jpg', cv2.IMREAD_GRAYSCALE);
img_thd1 = cv2.imread('images/threshold01.jpg', cv2.IMREAD_GRAYSCALE);

plt.imshow(img_flt, cmap='gray');
plt.imshow(img_thd1, cmap='gray');


# --- prepare the filter and threshold images
#ret,f = cv2.threshold(img_flt,127,255,cv2.THRESH_BINARY);
f = np.uint8(img_flt > 127);        #convert the data type

#ret,th = cv2.threshold(img_thd1, 127, 255, cv2.THRESH_BINARY);
th = np.uint8(img_thd1 > 127);


M, N = 1000, 1000


img_mark = np.ones((M, N))
img_seg_list = []
pt_st_list = []


for i in range(2, M-2):
    for j in range(2, N-2):
        # ...
        if f[i, j] == 1:
            #img_thd1[i, j]
            if f[i, j] and img_mark[i, j]:
                pin_img(th, img_mark, i, j);


plt.imshow(img_mark, cmap='gray')
plt.show()
cv2.imwrite('images/img_mark.jpg', img_mark*255)




for i in range(10, 20):
    show_imglist(img_seg_list, i);


for i in range(10, 20):
    ori_img_masked(img, img_seg_list, pt_st_list, i);

#------------------------------------
# from PIL import Image
def ori_img_masked(img, img_mask, x, y):
    # x, y = pt_list[index];
    abs_st_x, abs_st_y, abs_end_x, abs_end_y = x-100, y-100, x+200, y+200;
    # for the mask
    x1 = 0;
    y1 = 0;
    x2 = 300;
    y2 = 300;
    
    
    if x < 100:
        abs_st_x = 0;
        x1 = 100 - x;
        
    if y < 100:
        abs_st_y = 0;
        y1 = 100 - y;
        
    if x > 800:
        abs_end_x = 1000;
        x2 = 1100 - x;
        
    if y > 800:
        abs_end_y = 1000;
        y2 = 1100 - y;
        
    t_img = img[abs_st_x:abs_end_x, abs_st_y:abs_end_y];
    
    img_mask = img_mask[x1 : x2, y1 : y2];
    
    
    # the img may be 3 channels
    if len(cv2.split(img)) > 1:
        img_mask = img_mask.reshape(img_mask.shape[0], img_mask.shape[1], 1);
        t_img = t_img * img_mask;
      
    else:
        t_img = np.multiply(t_img,img_mask);
    
    
    lx, ly = t_img.shape[:2]
    if lx < 300 or ly < 300 :
        top, bottom = 0, 300 - lx;
        left, right = 0, 300 - ly;
        
        bottom = 0 if bottom < 0 else bottom;
        right = 0 if right < 0 else right;
        
        color = [0,0,0];
        
        t_img = cv2.copyMakeBorder(t_img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color);
    
    return t_img;



# --- plotting an image from a list
def show_imglist(img_list, index):
    plt.imshow(img_list[index], cmap='gray')
    plt.show();


# --- pin img function
def pin_img(img, img_mark, x0, y0):
    
    if not img[x0, y0]:
        return;
        
    x, y = x0, y0;
    img_mark[x0, y0] = 0;    
    pt_st_list.append((x0, y0));
    img_seg = np.zeros((300, 300))
    
    ps = Stack();   
    ps.add((x0, y0));
    
    while not ps.isEmpty():
        #print(x, y)
        x,y = ps.remove();
        if img[x, y]:
            if x > 0 and img_mark[x-1, y] and (img[x-1, y]): 
                ps.add((x-1, y))
                img_mark[x-1, y] = 0
                img_seg[x+99-x0, 100+y-y0] = 1
                
            if  x < M-1 and img_mark[x+1, y] and (img[x+1, y]):
                ps.add((x+1, y))
                img_mark[x+1, y] = 0
                img_seg[x+101-x0 , 100+y-y0] = 1
                
            if y > 0 and img_mark[x, y-1] and (img[x, y-1]):
                ps.add((x, y-1))
                img_mark[x, y-1] = 0
                img_seg[x+100-x0 , 99+y-y0] = 1
                
            if y < N-1 and img_mark[x, y+1] and (img[x, y+1]):
                ps.add((x, y+1))
                img_mark[x, y+1] = 0
                img_seg[x+100-x0, 101+y-y0] = 1
    
    img_seg_list.append(img_seg);

# -------------
class Stack:

    def __init__(self):
        self.stack = []

    def add(self, dataval):
# Use list append method to add element
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
        
# Use list pop method to remove element
    def remove(self):
        if len(self.stack) <= 0:
            return ("No element in the Stack")
        else:
            return self.stack.pop()
        
# Use peek to look at the top of the stack
    def peek(self):     
	    return self.stack[0]    
        
    def isEmpty(self):
        if len(self.stack) <= 0:
            return True;
        else:
            return False;
        
        
'''
AStack = Stack()
AStack.add("Mon")
AStack.add("Tue")
print(AStack.remove())
AStack.add("Wed")
AStack.add("Thu")
print(AStack.remove())
'''





