from PIL import Image
import glob
import re
import cv2

class LoadImages:

    def __init__(self):
        pass

    def load(self, folder=None):

        if folder == None:
            folder = '../images/isolated_images/'

        image_list = []

        '''
        image_path = folder + '*.jpg'
        
        for filename in glob.glob(image_path):
            #im = Image.open(filename)
            im = cv2.imread(filename)  # using opencv2
            image_list.append(im)
        '''

        # sort the files by file name
        files = glob.glob1(folder, '*.jpg')
        # if you want sort files according to the digits included in the filename,
        # you can do as following:
        files = sorted(files, key=lambda x: float(re.findall("(\d+)", x)[0]))

        for f in files:
            im = cv2.imread(folder + f)
            image_list.append(im)

            #cv2.imshow(f, img_name)
            #cv2.waitKey(0)
        return image_list
#print(len(image_list))

