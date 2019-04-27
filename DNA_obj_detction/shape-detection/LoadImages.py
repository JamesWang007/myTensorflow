from PIL import Image
import glob
import cv2

class LoadImages:

    def __init__(self):
        pass

    def load(self, folder=None):

        if folder == None:
            folder = '../images/isolated_images/*.jpg'

        image_path = folder + '*.jpg'
        image_list = []
        for filename in glob.glob(image_path):
            #im = Image.open(filename)
            im = cv2.imread(filename)  # using opencv2
            image_list.append(im)

        return image_list
#print(len(image_list))