import cv2


class dna_object:
    contours = None
    area_cnt = None         # area with contours
    area_minRect = None     # area of minRect
    area_ratio = None       # cnt_area / minRect_area

    ftr_minRect_size = None
    ftr_ratio = None
    ftr_area_cnt = None
    ftr_area_minRect = None


    def __init__(self):
        pass

    def getAttributes(self, cnts, a_c, a_m):
    # assign value for class properties
        try:
            if cnts is not None:
                self.contours = cnts
            else:
                raise TypeError('cnts is None')

            if a_c is not None:
                self.area_cnt = a_c
            else:
                raise TypeError('a_c is None')

            if a_m is not None:
                self.area_minRect = a_m
            else:
                raise TypeError('a_m is None')

            if a_m != 0:
                self.area_ratio = (a_c / a_m)
            else:
                self.area_ratio = 0.0

        except:
            print ("error in func : getAttributes")
            raise

class image:
    ## attributes
    image = None
    obj_list = [] # each image make contain multiple objects



    ## methods
    def __init__(self, im = None):
        #print (self.__helloworld)
        self.image = im

    def get_object(self, obj):
        self.obj_list.append(obj)



def main():
    img = cv2.imread('../images/isolated_images/6.jpg')
    im_obj = image(img)


if __name__ == "__main__":
    main()


