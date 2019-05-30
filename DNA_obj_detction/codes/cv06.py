import cv2
import numpy as np
import matplotlib.pyplot as plt


M, N = 1000, 1000
img_seg_list = []
pt_st_list = []
img_mark = []


def operating_cv03(image_path=None, image_name=None):
    # --- step 2. load an image
    if image_path == None:
        if image_name == None:
            image_name = 'proteins.jpg'
        image_path = 'images/'

    img = cv2.imread(image_path + image_name, cv2.IMREAD_GRAYSCALE);

    '''
    plt.imshow(img, cmap='gray')
    plt.show()
    '''

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
    ret, img_th1 = cv2.threshold(img, 68, 255, cv2.THRESH_BINARY)
    '''
    plt.imshow(img_th1, 'gray')
    plt.show()
    '''
    cv2.imwrite(image_path + 'img_th1.jpg', img_th1)

    # --- step 4. resize an image
    # resize the image to (1/2, 1/2)
    h, w = img_th1.shape

    img_half = cv2.resize(img_th1, ((int)(h / 2), (int)(w / 2)))
    # (int) (h/2), (int) (w/2))
    '''
    plt.imshow(img_half, 'gray')
    plt.show()
    '''
    # --- step 5. filter
    # remove outliers

    # apply : remove outliers method
    # takes a while
    img_rm_ol = rm_outliers(img_half);

    '''
    plt.imshow(img_rm_ol, 'gray')
    plt.show()              
    '''

    # --- step 6. resize back
    # rezise (*2, *2)
    img_rs_back = cv2.resize(img_rm_ol, (h, w))
    '''
    plt.imshow(img_rs_back, 'gray')
    plt.show()
    '''

    # --- step 7. threshold
    # threshold [152 ~ 255]
    ret, img_res = cv2.threshold(img_rs_back, 152, 255, cv2.THRESH_BINARY)
    '''
    plt.imshow(img_res, 'gray')
    plt.show()
    '''
    cv2.imwrite(image_path + 'img_res.jpg', img_res)


def rm_outliers(img, r=2.0, th=50):
    h, w = img.shape[:2]  # load the height and width

    # create a mask with (radius) r is 2
    if r != 2:  # currently we don't consider other radius
        return

    # when the radius is 2

    # assign values to the 4 cornors
    # when radius is 2, the 4 cornors are not included
    mask = np.zeros((5, 5))
    mask[4][0] = 255
    mask[4][4] = 255

    for ih in range(2, h - 2):
        for jw in range(2, w - 2):

            for i in range(5):
                for j in range(5):

                    if (i == 0 and j == 0) \
                            or (i == 0 and j == 4) \
                            or (i == 4 and j == 0) \
                            or (i == 4 and j == 4):
                        continue;

                    mask[i][j] = img[ih - 2 + i][jw - 2 + j]

            med = np.median(mask)

            if img[ih][jw] > med + th:
                img[ih][jw] = med;

    return img


def operating_cv04(_M=None, _N=None):
    global M, N
    if _M:
        M = _M
    if _N:
        N = _N

    img_mark = np.ones((M, N))

    img = cv2.imread('images/gray.jpg', -1);
    img_flt = cv2.imread('images/img_res.jpg', cv2.IMREAD_GRAYSCALE);
    img_thd1 = cv2.imread('images/img_th1.jpg', cv2.IMREAD_GRAYSCALE);
    '''
    plt.imshow(img_flt, cmap='gray');
    plt.imshow(img_thd1, cmap='gray');
    '''

    # --- prepare the filter and threshold images
    # ret,f = cv2.threshold(img_flt,127,255,cv2.THRESH_BINARY);
    f = np.uint8(img_flt > 127);  # convert the data type

    # ret,th = cv2.threshold(img_thd1, 127, 255, cv2.THRESH_BINARY);
    th = np.uint8(img_thd1 > 127);

    for i in range(2, M - 2):
        for j in range(2, N - 2):
            # ...
            if f[i, j] == 1:
                # img_thd1[i, j]
                if f[i, j] and img_mark[i, j]:
                    pin_img(th, img_mark, i, j);

    '''
    plt.imshow(img_mark, cmap='gray')
    plt.show()

    '''
    cv2.imwrite('images/img_mark.jpg', img_mark * 255)

    # print(sys.__path__)


# from PIL import Image
def ori_img_masked(img, img_mask, x, y):
    # x, y = pt_list[index];
    abs_st_x, abs_st_y, abs_end_x, abs_end_y = x - 100, y - 100, x + 200, y + 200;
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

    img_mask = img_mask[x1: x2, y1: y2];

    # the img may be 3 channels
    if len(cv2.split(img)) > 1:
        img_mask = img_mask.reshape(img_mask.shape[0], img_mask.shape[1], 1);
        t_img = t_img * img_mask;

    else:
        t_img = np.multiply(t_img, img_mask);

    lx, ly = t_img.shape[:2]
    if lx < 300 or ly < 300:
        top, bottom = 0, 300 - lx;
        left, right = 0, 300 - ly;

        bottom = 0 if bottom < 0 else bottom;
        right = 0 if right < 0 else right;

        color = [0, 0, 0];

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
        # print(x, y)
        x, y = ps.remove();
        if img[x, y]:
            if x > 0 and img_mark[x - 1, y] and (img[x - 1, y]):
                ps.add((x - 1, y))
                img_mark[x - 1, y] = 0
                img_seg[x + 99 - x0, 100 + y - y0] = 1

            if x < M - 1 and img_mark[x + 1, y] and (img[x + 1, y]):
                ps.add((x + 1, y))
                img_mark[x + 1, y] = 0
                img_seg[x + 101 - x0, 100 + y - y0] = 1

            if y > 0 and img_mark[x, y - 1] and (img[x, y - 1]):
                ps.add((x, y - 1))
                img_mark[x, y - 1] = 0
                img_seg[x + 100 - x0, 99 + y - y0] = 1

            if y < N - 1 and img_mark[x, y + 1] and (img[x, y + 1]):
                ps.add((x, y + 1))
                img_mark[x, y + 1] = 0
                img_seg[x + 100 - x0, 101 + y - y0] = 1

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


def operating_cv05(image_path=None, image_name=None, _M=None, _N=None):
    global M, N
    if _M:
        M = _M

    if _N:
        N = _N

    # --- load an image
    if image_path == None:
        image_path = 'images/'
    if image_name == None:
        image_name = 'proteins.jpg'

    img = cv2.imread(image_path + image_name, cv2.IMREAD_GRAYSCALE)
    img_c = cv2.imread(image_path + image_name, cv2.IMREAD_COLOR)
    # Find object blocks in the original image
    # --- step 1. apply thresholds
    ret, img_thd1 = cv2.threshold(img, 68, 255, cv2.THRESH_BINARY)

    # --- step 2. resize an image
    # resize the image to (1/2, 1/2)
    h, w = img_thd1.shape
    img_half = cv2.resize(img_thd1, ((int)(h / 2), (int)(w / 2)))

    # --- step 3. filter
    # apply : remove outliers method
    img_rm_ol = rm_outliers(img_half);  # takes a time

    # --- step 4. resize back
    # rezise (*2, *2)
    img_rs_back = cv2.resize(img_rm_ol, (h, w))

    # --- step 5(last). threshold
    # threshold [152 ~ 255]
    ret, img_flt = cv2.threshold(img_rs_back, 152, 255, cv2.THRESH_BINARY)

    '''
        Execution  
    '''

    ##
    # --- prepare the filter and filter images with a threshold
    f = np.uint8(img_flt > 127);  # convert the data type
    th = np.uint8(img_thd1 > 127);

    isolated_imgs, orientation_pt_list = isolating_imgs(f, th);

    '''
    for i in range(10, 20):
        show_imglist(isolated_imgs, i);
    '''
    '''
    ##  save the isolated images into a folder
    iso_img_ori_gray = []
    for i in range(len(isolated_imgs)):       #len(isolated_imgs)
        iso_img_ori_gray.append(ori_img_masked(img, isolated_imgs[i], orientation_pt_list[i][0], orientation_pt_list[i][1]));              
        cv2.imwrite("images/isolated_images/" + str(i) +  ".jpg", iso_img_ori_gray[i]);
    '''

    ##
    iso_img_ori = []
    for i in range(len(isolated_imgs)):  # len(isolated_imgs)
        iso_img_ori.append(
            ori_img_masked(img_c, isolated_imgs[i], orientation_pt_list[i][0], orientation_pt_list[i][1]));
        cv2.imwrite(image_path + "isolated_images/" + str(i) + ".jpg", iso_img_ori[i]);


def main():
    operating_cv03()
    operating_cv04()
    operating_cv05()



if __name__ == "__main__":
    main()