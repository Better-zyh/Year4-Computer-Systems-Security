from pyqt5_plugins.examplebutton import QtWidgets
from pyqt5_plugins.examplebuttonplugin import QtGui
from mainwindow import Ui_MainWindow
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from can304 import *


class CamShow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(CamShow, self).__init__(parent)
        self.setupUi(self)
        self.encryptBtn.clicked.connect(self.encrypt)
        self.decryptBtn.clicked.connect(self.decrypt)



    def encrypt(self):
        if self.plaintext_input.toPlainText() != "":
            if self.key.toPlainText() != "":
                self.encrypted_data.setPlainText(encryption(
                    self.plaintext_input.toPlainText(),self.key.toPlainText()))


    def decrypt(self):
        if self.encrypted_data.toPlainText() != "":
            if self.key.toPlainText() != "":
                self.plaintext_output.setPlainText(
                    decryption(self.encrypted_data.toPlainText(), self.key.toPlainText()))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = CamShow()
    ui.show()
    sys.exit(app.exec_())
