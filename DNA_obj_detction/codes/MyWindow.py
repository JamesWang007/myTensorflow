###################
# main window ui
###################
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from codes import imgDecUI as ui


class MyWindow(QMainWindow, ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())

############################

