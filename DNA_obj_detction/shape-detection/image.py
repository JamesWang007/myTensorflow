import cv2

class image:
    #__helloworld = "hello world"
    image = None



    def __init__(self, im = None):
        #print (self.__helloworld)
        self.image = im




def main():
    img = cv2.imread('../images/isolated_images/6.jpg')
    im_obj = image(img)


if __name__ == "__main__":
    main()


