# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Jedzpetch\Desktop\Python\ui\addorder.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_addorder(object):
    def setupUi(self, addorder):
        addorder.setObjectName("addorder")
        addorder.resize(778, 598)
        addorder.setMinimumSize(QtCore.QSize(778, 598))
        addorder.setMaximumSize(QtCore.QSize(778, 598))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\Jedzpetch\\Desktop\\Python\\ui\\../../image/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        addorder.setWindowIcon(icon)
        addorder.setStyleSheet("background-color : rgb(255, 218, 212)")
        self.pushButton = QtWidgets.QPushButton(addorder)
        self.pushButton.setGeometry(QtCore.QRect(200, 350, 181, 81))
        self.pushButton.setStyleSheet("font: 14pt \"Segoe UI\";\n"
"background-color : rgb(255, 216, 215)")
        self.pushButton.setObjectName("pushButton")
        self.image1_2 = QtWidgets.QLabel(addorder)
        self.image1_2.setGeometry(QtCore.QRect(460, 60, 181, 161))
        self.image1_2.setMaximumSize(QtCore.QSize(181, 161))
        self.image1_2.setStyleSheet("image: url(:/image/icon.png);")
        self.image1_2.setText("")
        self.image1_2.setObjectName("image1_2")
        self.lineEdit = QtWidgets.QLineEdit(addorder)
        self.lineEdit.setGeometry(QtCore.QRect(170, 50, 251, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(addorder)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 110, 251, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(addorder)
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 170, 251, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(addorder)
        self.lineEdit_4.setGeometry(QtCore.QRect(170, 240, 251, 41))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label = QtWidgets.QLabel(addorder)
        self.label.setGeometry(QtCore.QRect(70, 60, 61, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(addorder)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 121, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(addorder)
        self.label_3.setGeometry(QtCore.QRect(20, 170, 141, 51))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(addorder)
        self.label_4.setGeometry(QtCore.QRect(50, 230, 91, 51))
        self.label_4.setObjectName("label_4")
        self.image1_2.raise_()
        self.pushButton.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_4.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()

        self.retranslateUi(addorder)
        QtCore.QMetaObject.connectSlotsByName(addorder)

    def retranslateUi(self, addorder):
        _translate = QtCore.QCoreApplication.translate
        addorder.setWindowTitle(_translate("addorder", "เพิ่มรายการสินค้า"))
        self.pushButton.setText(_translate("addorder", "เพิ่มรายการ"))
        self.label.setText(_translate("addorder", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">ID :</span></p></body></html>"))
        self.label_2.setText(_translate("addorder", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">ชื่อสินค้า :</span></p></body></html>"))
        self.label_3.setText(_translate("addorder", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">รายละเอียด :</span></p></body></html>"))
        self.label_4.setText(_translate("addorder", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">ราคา    :</span></p></body></html>"))
