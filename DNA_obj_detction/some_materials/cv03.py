# -*- coding: utf-8 -*-
# 

# --- step 1. libraries 
import cv2
import numpy as np
import matplotlib.pyplot as plt


# --- step 2. load an image
image_path = 'images/';
img = cv2.imread(image_path + 'proteins.jpg', cv2.IMREAD_GRAYSCALE);


plt.imshow(img, cmap='gray')
plt.show()

'''
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
'''

# --- step 3. apply a threshold
ret,img_th1 = cv2.threshold(img,68,255,cv2.THRESH_BINARY)
plt.imshow(img_th1, 'gray')
plt.show()

#cv2.imwrite(image_path + 'img_th1.jpg', img_th1)


# --- step 4. resize an image
# resize the image to (1/2, 1/2)
h,w = img_th1.shape

img_half = cv2.resize(img_th1, ((int) (h/2), (int) (w/2)) )
#(int) (h/2), (int) (w/2))

plt.imshow(img_half, 'gray')
plt.show()

# --- step 5. filter
# remove outliers
def rm_outliers(img, r=2.0, th = 50):
    h, w = img.shape[:2] # load the height and width
    
    #create a mask with (radius) r is 2
    if r != 2:  # currently we don't consider other radius
        return
    
    
    # when the radius is 2
    
    # assign values to the 4 cornors
    # when radius is 2, the 4 cornors are not included
    mask = np.zeros((5, 5))
    mask[4][0] = 255
    mask[4][4] = 255
    
    for ih in range(2, h-2):
        for jw in range(2, w-2):
            
            for i in range(5):
                for j in range(5):
                        
                    if (i == 0 and j == 0) \
                    or (i == 0 and j == 4) \
                    or (i == 4 and j == 0) \
                    or (i == 4 and j == 4):
                        continue;
                    
                    mask[i][j] = img[ih-2 + i][jw-2 + j] 
            
            med = np.median(mask)
            
            if img[ih][jw] > med + th:
                img[ih][jw] = med;

    return img                

# apply : remove outliers method
# takes a while
img_rm_ol = rm_outliers(img_half);


plt.imshow(img_rm_ol, 'gray')
plt.show()              


# --- step 6. resize back
# rezise (*2, *2)
img_rs_back = cv2.resize(img_rm_ol, (h, w))

plt.imshow(img_rs_back, 'gray')
plt.show()


# --- step 7. threshold
# threshold [152 ~ 255]
ret,img_res = cv2.threshold(img_rs_back,152,255,cv2.THRESH_BINARY)

plt.imshow(img_res, 'gray')
plt.show()

cv2.imwrite(image_path + 'img_res.jpg', img_res)







