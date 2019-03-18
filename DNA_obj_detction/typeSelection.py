###
#       image index : 0 ~ #
#       image type : 1 ~ 5
#       image types will be saved into a .txt file locally: imageTypes.txt
##



import sys
import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

###########################
# class 
###########################

class TypeSelection(QWidget):

    def __init__(self, parent = None):
        super(TypeSelection, self).__init__(parent)

        ## - configuration
        self.W, self.H = 2000, 1000
        self.lbl_W, self.lbl_H = 1000, 1000
        self.imgDir = "images/isolated_images/"
        self.imgName = "0.jpg"
        self.index = 0
        self.numImgs = 153
        self.typeArray = []
        

		## - layout
        layout = QHBoxLayout()
        ## - add a label
        self.label = QLabel()        
        fileName = self.imgDir + self.imgName        
        self.label.setPixmap(QPixmap(fileName).scaled(self.lbl_H, self.lbl_W))
        self.label.resize(self.lbl_H, self.lbl_W)        
        layout.addWidget(self.label)

        """
        ##  - add a btn to load any image
        self.btn = QPushButton()
        self.btn.clicked.connect(self.loadFile)
        self.btn.setText("从文件中获取照片")
        layout.addWidget(self.btn)
        """

        ## - 5 radio buttons
        
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)

        self.b1 = QRadioButton("Type1")
        self.b1.setFont(font)
        #self.b1.setChecked(True)
        self.b1.toggled.connect(lambda:self.btnstate(self.b1))
        layout.addWidget(self.b1, 0 , Qt.AlignHCenter)
        
        self.b2 = QRadioButton("Type2")
        self.b2.setFont(font)
        self.b2.toggled.connect(lambda:self.btnstate(self.b2))
        layout.addWidget(self.b2, 0 , Qt.AlignHCenter)

        self.b3 = QRadioButton("Type3")
        self.b3.setFont(font)
        self.b3.toggled.connect(lambda:self.btnstate(self.b3))
        layout.addWidget(self.b3, 0 , Qt.AlignHCenter)

        self.b4 = QRadioButton("Type4")
        self.b4.setFont(font)
        self.b4.toggled.connect(lambda:self.btnstate(self.b4))
        layout.addWidget(self.b4, 0 , Qt.AlignHCenter)

        self.b5 = QRadioButton("Type5")
        self.b5.setFont(font)
        self.b5.toggled.connect(lambda:self.btnstate(self.b5))
        layout.addWidget(self.b5, 0 , Qt.AlignHCenter)

        self.b6 = QRadioButton("Other")
        self.b6.setFont(font)
        self.b6.toggled.connect(lambda:self.btnstate(self.b6))
        layout.addWidget(self.b6, 0 , Qt.AlignHCenter)


        ## - btn "submit"
        font = QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)

        self.btn_smt = QPushButton()
        self.btn_smt.setFont(font)
        self.btn_smt.setText("Submit")
        self.btn_smt.setFixedSize(300, 150)
        self.btn_smt.clicked.connect(self.btnSubmit)
        layout.addWidget(self.btn_smt, 0, Qt.AlignBottom)

        ##
        self.setLayout(layout)
        self.setWindowTitle("Type Selection")

        ## - set up window arrangement
        self.resize(self.W, self.H)

        self.Controller()


###########################
# functions
###########################



    ## - set up some data structure
    def Controller(self):

        for i in range(self.numImgs):
            self.typeArray.append([i, 0])


    
    def loadFile(self):
        print("load--file")
        fname, _ = QFileDialog.getOpenFileName(self, '选择图片', 'c:\\', 'Image files(*.jpg *.gif *.png)')
        self.label.setPixmap(QPixmap(fname))
    

    ## - submit
    #  - assign the type to an image
    #  - and load next image
    def btnSubmit(self):
        if self.index + 1 < self.numImgs:         
            # assign a type value
            if self.b1.isChecked():
                self.typeArray[self.index] = [self.index, 1]
                print( "submit the result" + "object type: {}".format(self.typeArray[self.index][1]) )
            elif self.b2.isChecked():
                self.typeArray[self.index] = [self.index, 2]
                print( "submit the result" + "object type: {}".format(self.typeArray[self.index][1]) )
            elif self.b3.isChecked():
                self.typeArray[self.index] = [self.index, 3]
                print( "submit the result" + "object type: {}".format(self.typeArray[self.index][1]) )
            elif self.b4.isChecked():
                self.typeArray[self.index] = [self.index, 4]
                print( "submit the result" + "object type: {}".format(self.typeArray[self.index][1]) )
            elif self.b5.isChecked():
                self.typeArray[self.index] = [self.index, 5]
                print( "submit the result" + "object type: {}".format(self.typeArray[self.index][1]) )
            else:
                self.typeArray[self.index] = [self.index, 6]
                print( "submit the result\n" + "object type: Others".format(self.typeArray[self.index][1]) )

            

            # index ++, load next image; 
            self.index += 1
            fileName = self.imgDir + str(self.index) + ".jpg"
            self.label.setPixmap(QPixmap(fileName).scaled(self.lbl_W, self.lbl_H))
        else:
            print("image index out of bound!")


    def btnstate(self,b):
        if b.text() == "Type1":
            if b.isChecked() == True:
                print (b.text()+" is selected")
                #self.typeArray[self.index] = [self.index, 1]
            else:
                print (b.text()+" is deselected")
                
        if b.text() == "Type2":
            if b.isChecked() == True:
                print (b.text()+" is selected")
                #self.typeArray[self.index] = [self.index, 2]
            else:
                print (b.text()+" is deselected")
            
        if b.text() == "Typ3":
            if b.isChecked() == True:
                print (b.text()+" is selected")
                #self.typeArray[self.index] = [self.index, 3]
            else:
                print (b.text()+" is deselected")
                
        if b.text() == "Type4":
            if b.isChecked() == True:
                print (b.text()+" is selected")
                #self.typeArray[self.index] = [self.index, 4]
            else:
                print (b.text()+" is deselected")
                      
        if b.text() == "Type5":
            if b.isChecked() == True:
                print (b.text()+" is selected")
                #self.typeArray[self.index] = [self.index, 5]
            else:
                print (b.text()+" is deselected")

        if b.text() == "Other":
            if b.isChecked() == True:
                print (b.text()+" is selected")
                #self.typeArray[self.index] = [self.index, 6]
            else:
                print (b.text()+" is deselected")


################################
# Project Entrance: main method
################################


def main():

   app = QApplication(sys.argv)
   ex = TypeSelection()
   ex.show()
   sys.exit(app.exec_())


if __name__ == '__main__':
   main()