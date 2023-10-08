# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(994, 552)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.encryptBtn = QtWidgets.QPushButton(self.centralwidget)
        self.encryptBtn.setGeometry(QtCore.QRect(440, 90, 93, 41))
        self.encryptBtn.setObjectName("encryptBtn")
        self.decryptBtn = QtWidgets.QPushButton(self.centralwidget)
        self.decryptBtn.setGeometry(QtCore.QRect(440, 360, 93, 41))
        self.decryptBtn.setObjectName("decryptBtn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 171, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(570, 10, 171, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 260, 171, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(580, 260, 171, 16))
        self.label_4.setObjectName("label_4")
        self.plaintext_input = QtWidgets.QTextEdit(self.centralwidget)
        self.plaintext_input.setGeometry(QtCore.QRect(20, 40, 381, 191))
        self.plaintext_input.setObjectName("plaintext_input")
        self.encrypted_data = QtWidgets.QTextEdit(self.centralwidget)
        self.encrypted_data.setGeometry(QtCore.QRect(570, 40, 381, 191))
        self.encrypted_data.setObjectName("encrypted_data")
        self.key = QtWidgets.QTextEdit(self.centralwidget)
        self.key.setGeometry(QtCore.QRect(20, 290, 381, 191))
        self.key.setObjectName("key")
        self.plaintext_output = QtWidgets.QTextEdit(self.centralwidget)
        self.plaintext_output.setGeometry(QtCore.QRect(570, 290, 381, 191))
        self.plaintext_output.setObjectName("plaintext_output")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 994, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.encryptBtn.setText(_translate("MainWindow", "Encrypt"))
        self.decryptBtn.setText(_translate("MainWindow", "Decrypt"))
        self.label.setText(_translate("MainWindow", "Input plaintext:"))
        self.label_2.setText(_translate("MainWindow", "Encrypted data:"))
        self.label_3.setText(_translate("MainWindow", "Key:"))
        self.label_4.setText(_translate("MainWindow", "Output plaintext:"))
        self.plaintext_input.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
