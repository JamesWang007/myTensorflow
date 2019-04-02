import glob
import sys

path = '../images/isolated_images/*.jpg'
files=glob.glob(path)
for file in files:
    s = file.split('\\')
    print (s[-1])

