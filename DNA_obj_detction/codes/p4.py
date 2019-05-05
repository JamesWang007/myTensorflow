'''
    load files from a folder, and sort files by file name

'''

import glob
import re
import cv2



file_folder = '../images/isolated_images/'
files =glob.glob1(file_folder, '*.jpg')
# if you want sort files according to the digits included in the filename,
# you can do as following:
files = sorted(files, key=lambda x: float(re.findall("(\d+)", x)[0]))

index = 0
for f in files:
    img_name = cv2.imread(file_folder + f)
    cv2.imshow(str(index), img_name)
    cv2.waitKey(0)
    index += 1

