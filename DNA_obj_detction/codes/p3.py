import cv2

class A:
    def __init__(self):
        self.__a__ = 0
        self.b = 3.14159262323


    def setA(self, a):
        self.__a__ = a
    def getA(self):
        return self.__a__


def fun1(a1):
    a1.b = 3

def fun2(l):
    img = cv2.imread("../images/proteins.jpg")
    l.append(img)
    print(id(img))

def main():
    a1 = A()
    #a1.setA(12)
    #print(a1.getA())

    #print(id(a1.b))
    #fun1(a1)
    #print(id(a1.b))

    '''
    i_list = []
    a = 30.234
    i_list.append(a)
    print (id(a))
    print (id(i_list[0]))
    '''

    img_list = []
    fun2(img_list)
    print(id(img_list[0]))

if __name__ == "__main__":
    main()