import codes
from codes import (cv03, cv04, cv05, typeSelection as ts, MyWindow as mwin)

#cv03.operating()   # takes 3 minutes
                    # genereate object mask - removed outliers


#cv04.operating(1000, 1000)  # generate image mask - it will work on original image


#cv05.operating()    # create isolated small images which contain small objects


        ## should filter images


#ts.main()   # GUI -


#mwin.main()


import cv2
b1 = cv2.imread("images/b/b1.bmp")
b1 = cv2.resize(b1, (1000, 1000))
cv2.imwrite("images/b/b1.jpg", b1)

cv03.operating('images/b/', 'b1.jpg')
cv04.operating()
cv05.operating('images/b/', 'b1.jpg')


