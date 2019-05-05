# USAGE
# python detect_shapes.py --image shapes_and_colors.png

# import the necessary packages
from pyimagesearch.shapedetector import ShapeDetector
import imutils
import cv2
import numpy as np
import math
from LoadImages import LoadImages
from image import image, dna_object

class image_shape_detect:
    def __init__(self):
        self.images_list = []
        self.image_obj_list = []
        self.dna_object_list = []

    def findAreaRotRect(self, box):
        v1 = box[0]
        v2 = box[1]
        v3 = box[2]

        d12 = math.sqrt((v1[0] - v2[0])**2 + (v1[1] - v2[1])**2)
        d23 = math.sqrt((v2[0] - v3[0])**2 + (v2[1] - v3[1])**2)

        area = d12 * d23

        return area

    def detectAreaRatio(self, folder = None):

        loadImg = LoadImages()

        if folder == None:
            folder = "../images/isolated_images/"

        self.image_list = loadImg.load(folder)


        # load the image and resize it to a smaller factor so that
        # the shapes can be approximated better
        index = 0
        index_obj = 0
        for img in self.image_list:
            resized = imutils.resize(img, width=300)
            ratio = img.shape[0] / float(resized.shape[0])


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

            # create image objects
            img_obj = image(img)
            img_obj.id = index
            self.image_obj_list.append(img_obj)

            # loop over the contours
            for c in cnts:
                #area = cv2.contourArea(c)
                #print('area is:', area)
                if cv2.contourArea(c) <= 200:
                    continue

                # compute the center of the contour, then detect the name of the
                # shape using only the contour
                M = cv2.moments(c)
                cX = 0
                cY = 0
                if M["m00"] != 0:
                    cX = int((M["m10"] / M["m00"]) * ratio)
                    cY = int((M["m01"] / M["m00"]) * ratio)
                shape = sd.detect(c)


                # multiply the contour (x, y)-coordinates by the resize ratio,
                # then draw the contours and the name of the shape on the image
                c = c.astype("float")
                c *= ratio
                c = c.astype("int")
                cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
                #cv2.putText(img, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX,
                #    0.5, (255, 255, 255), 2)


                # Rotated Rectangle
                rect = cv2.minAreaRect(c)
                box = cv2.boxPoints(rect)
                box = np.int0(box)
                imgRotRect = cv2.drawContours(img, [box], 0, (0, 0, 255), 2)


                # calculate the area
                area_obj = cv2.contourArea(c)
                area_box = self.findAreaRotRect(box)

                # create dna_object
                d_obj = dna_object()
                d_obj.id = index_obj
                d_obj.getAttributes(c, area_obj, area_box)

                self.dna_object_list.append(d_obj)

                r = d_obj.area_ratio


                print ("# ", index)
                print ("area obj: %.2f" % area_obj)
                print ("area box: %.2f" % area_box)
                print ("area ratio: %.2f" % r)


                index_obj += 1


                #cv2.imshow(str(index), imgRotRect)
                #cv2.waitKey(0)


            index += 1

    # filter object function, base on contour
    def filter_image_contour(self, c):
        if cv2.contourArea(c) < 200:
            return False
        return True


    def save_3features(self):
        try:
            with open("../statistics/3features.txt", 'w') as file:
                for o in self.dna_object_list:
                    s = '{0: <10.2f}{1: <10.2f}{2: <10.2f}\n'
                    """
                        ftr_area_cnt 
                        ftr_area_minRect 
                        ftr_ratio
                    """

                    file.write(s.format(o.ftr_area_cnt, o.ftr_area_minRect, o.ftr_ratio))
        except:
            print ("save_3_features")



    #def save(self):
        #with open("../txtData/image_detect_result.txt", 'w') as f:
            #index = 0
            #for s in self.images_list:
                #self.images_

def main():
    img_sd = image_shape_detect()
    img_sd.detectAreaRatio()
    img_sd.save_3features()


    #cv2.imshow("", img_sd.image_list[9])
    #cv2.waitKey(0)



if __name__ == "__main__":
    main()