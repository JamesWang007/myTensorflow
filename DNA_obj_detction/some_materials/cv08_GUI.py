# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 23:04:19 2019

    PyQt5 load image (QPixmap)
    https://pythonspot.com/pyqt5-image/
    
@author: bejin
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
 
class App(QWidget):
 
    def __init__(self, img_path):
        super().__init__()
        self.title = 'PyQt5 image - pythonspot.com'
        self.left = 100
        self.top = 100
        self.width = 1000
        self.height = 1000
        self.img_path = img_path
        self.initUI()
        
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
         
        # Create widget
        label = QLabel(self)
        pixmap = QPixmap(self.img_path)
        label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())
         
        self.show()

'''
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
'''

if __name__ == '__main__':
    img_path = 'images/isolated_images/';
    for i in range(20):
        app = QApplication(sys.argv);
        ex = App(img_path + str(i) + '.jpg')
        sys.exit(app.exec_())
