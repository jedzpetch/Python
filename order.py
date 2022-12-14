# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\order.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import aboutus
import addorder
import pymysql
import editorder
import imageorder



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(975, 816)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui\\../../resorce/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color : rgb(255, 218, 212)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 25pt \"Segoe UI\";\n"
"")
        self.label.setObjectName("label")
        self.addorder = QtWidgets.QPushButton(self.centralwidget)
        self.addorder.setGeometry(QtCore.QRect(710, 70, 241, 61))
        self.addorder.setStyleSheet("font: 14pt \"Segoe UI\";\n"
"background-color : rgb(255, 216, 215)")
        self.addorder.setObjectName("addorder")
        self.delorder = QtWidgets.QPushButton(self.centralwidget)
        self.delorder.setGeometry(QtCore.QRect(710, 140, 241, 61))
        self.delorder.setStyleSheet("font: 14pt \"Segoe UI\";\n"
"background-color : rgb(255, 216, 215)")
        self.delorder.setObjectName("delorder")
#         self.accept = QtWidgets.QPushButton(self.centralwidget)
#         self.accept.setGeometry(QtCore.QRect(710, 560, 251, 61))
#         self.accept.setMinimumSize(QtCore.QSize(251, 0))
#         self.accept.setStyleSheet("font: 14pt \"Segoe UI\";\n"
# "background-color : rgb(255, 216, 215)")
#         self.accept.setObjectName("accept")
        self.reset = QtWidgets.QPushButton(self.centralwidget)
        self.reset.setGeometry(QtCore.QRect(710, 630, 251, 61))
        self.reset.setStyleSheet("font: 14pt \"Segoe UI\";\n"
"background-color : rgb(255, 216, 215)")
        self.reset.setObjectName("reset")
        self.menutableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.menutableWidget.setGeometry(QtCore.QRect(30, 70, 661, 621))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menutableWidget.sizePolicy().hasHeightForWidth())
        self.menutableWidget.setSizePolicy(sizePolicy)
        self.menutableWidget.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.menutableWidget.setFont(font)
        self.menutableWidget.setTabletTracking(False)
        self.menutableWidget.setStyleSheet("")
        self.menutableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.menutableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.menutableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.menutableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.menutableWidget.setAutoScroll(True)
        self.menutableWidget.setEditTriggers(QtWidgets.QAbstractItemView.CurrentChanged|QtWidgets.QAbstractItemView.DoubleClicked)
        self.menutableWidget.setDragEnabled(False)
        self.menutableWidget.setAlternatingRowColors(False)
        self.menutableWidget.setTextElideMode(QtCore.Qt.ElideLeft)
        self.menutableWidget.setShowGrid(True)
        self.menutableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.menutableWidget.setObjectName("menutableWidget")
        self.menutableWidget.setColumnCount(5)
        self.menutableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.menutableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.menutableWidget.setHorizontalHeaderItem(1, item)
        self.menutableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.menutableWidget.setHorizontalHeaderItem(2, item)
        self.menutableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.menutableWidget.setHorizontalHeaderItem(3, item)
        self.menutableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.menutableWidget.setHorizontalHeaderItem(4, item)
        self.menutableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.showitem()
        self.menutableWidget.horizontalHeader().setVisible(True)
        self.menutableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.menutableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.menutableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.menutableWidget.horizontalHeader().setStretchLastSection(False)
        self.menutableWidget.verticalHeader().setVisible(True)
        self.menutableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.menutableWidget.verticalHeader().setSortIndicatorShown(False)
        self.menutableWidget.verticalHeader().setStretchLastSection(False)
        self.image2 = QtWidgets.QLabel(self.centralwidget)
        self.image2.setGeometry(QtCore.QRect(580, -20, 191, 131))
        self.image2.setStyleSheet("image: url(:/image/stars.png);")
        self.image2.setText("")
        self.image2.setObjectName("image2")
        self.image1 = QtWidgets.QLabel(self.centralwidget)
        self.image1.setGeometry(QtCore.QRect(200, -20, 71, 101))
        self.image1.setStyleSheet("image: url(:/image/icon.png);")
        self.image1.setText("")
        self.image1.setObjectName("image1")
        self.image6 = QtWidgets.QLabel(self.centralwidget)
        self.image6.setGeometry(QtCore.QRect(730, 700, 261, 131))
        self.image6.setStyleSheet("image: url(:/image/tea1.png);")
        self.image6.setText("")
        self.image6.setObjectName("image6")
        self.image4 = QtWidgets.QLabel(self.centralwidget)
        self.image4.setGeometry(QtCore.QRect(480, 690, 261, 131))
        self.image4.setStyleSheet("image: url(:/image/tea2.png);")
        self.image4.setText("")
        self.image4.setObjectName("image4")
        self.image3 = QtWidgets.QLabel(self.centralwidget)
        self.image3.setGeometry(QtCore.QRect(230, 690, 261, 131))
        self.image3.setStyleSheet("image: url(:/image/tea3.png);")
        self.image3.setText("")
        self.image3.setObjectName("image3")
        self.image5 = QtWidgets.QLabel(self.centralwidget)
        self.image5.setGeometry(QtCore.QRect(-20, 700, 261, 131))
        self.image5.setStyleSheet("image: url(:/image/tea1.png);")
        self.image5.setText("")
        self.image5.setObjectName("image5")
        self.image5.raise_()
        self.image3.raise_()
        self.image4.raise_()
        self.image6.raise_()
        self.image1.raise_()
        self.image2.raise_()
        self.label.raise_()
        self.addorder.raise_()
        self.delorder.raise_()
        # self.accept.raise_()
        self.reset.raise_()
        self.menutableWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 975, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuMain = QtWidgets.QMenu(self.menuBar)
        self.menuMain.setObjectName("menuMain")
        self.menuAboutus = QtWidgets.QMenu(self.menuBar)
        self.menuAboutus.setObjectName("menuAboutus")
        MainWindow.setMenuBar(self.menuBar)
        self.acadd = QtWidgets.QAction(MainWindow)
        self.acadd.setObjectName("acadd")
        self.acaboutus = QtWidgets.QAction(MainWindow)
        self.acaboutus.setObjectName("acaboutus")
        self.menuMain.addAction(self.acadd)
        self.menuAboutus.addAction(self.acaboutus)
        self.menuBar.addAction(self.menuMain.menuAction())
        self.menuBar.addAction(self.menuAboutus.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.acaboutus.triggered.connect(self.openaboutus)
        self.acadd.triggered.connect(self.openaddorder)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "????????????????????????????????????"))
        self.label.setText(_translate("MainWindow", "????????????????????????????????????"))
        self.addorder.setText(_translate("MainWindow", "??????????????????????????????????????????"))
        self.delorder.setText(_translate("MainWindow", "????????????????????????????????????????????????????????????"))
        # self.accept.setText(_translate("MainWindow", "????????????????????????????????????"))
        self.reset.setText(_translate("MainWindow", "??????????????????"))
        self.menutableWidget.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.menutableWidget.setSortingEnabled(False)
        item = self.menutableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "No"))
        item = self.menutableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ID"))
        item = self.menutableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "????????????????????????"))
        item = self.menutableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "??????????????????????????????"))
        item = self.menutableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "????????????"))
        self.menuMain.setTitle(_translate("MainWindow", "????????????????????????"))
        self.menuAboutus.setTitle(_translate("MainWindow", "???????????????????????????"))
        self.acadd.setText(_translate("MainWindow", "???????????????????????????????????????????????????"))
        self.acaboutus.setText(_translate("MainWindow", "About us"))
        self.addorder.clicked.connect(self.openaddorder)
        self.delorder.clicked.connect(self.openadelorder)
        self.reset.clicked.connect(self.refresh)
        
    def showitem(self):
        print('fetching data')
        con = pymysql.connect(host="localhost", database="app_python",
                                user='root', password='', charset="utf8")
        cursor = con.cursor()
        cursor.execute("SELECT NO,id,title,details,price FROM data")
        data = cursor.fetchall()
        print(data)
        tablerow = 0
        for i in data:
            self.menutableWidget.insertRow(tablerow)
            self.menutableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(i[0]))
            self.menutableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(i[1])))
            self.menutableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(i[2]))
            self.menutableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(i[3])))
            self.menutableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(i[4]))
            tablerow += 1
        con.close()

    def openaboutus(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = aboutus.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def openaddorder(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = addorder.Ui_addorder()
        self.ui.setupUi(self.window)
        self.window.show()

    def openadelorder(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = editorder.Ui_editorder()
        self.ui.setupUi(self.window)
        self.window.show()

    def refresh(self):
        self.menutableWidget.setRowCount(0)
        self.showitem()    




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
