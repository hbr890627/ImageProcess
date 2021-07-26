# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VGG16.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtWidgets
import code


class Ui_MainWindow(object):
    def setbtn(self):
        self.btn1.clicked.connect(code.ShowImage)
        self.btn2.clicked.connect(code.PrintHyperparameters)
        self.btn3.clicked.connect(code.ShowModel)
        self.btn4.clicked.connect(code.ShowAL)
        self.btn5.clicked.connect(self.startTest)

    def startTest(self):
        num = self.spinBox.text()
        code.Test(int(num))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(270, 70, 241, 371))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btn1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn1.setObjectName("btn1")
        self.verticalLayout.addWidget(self.btn1)
        self.btn2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn2.setObjectName("btn2")
        self.verticalLayout.addWidget(self.btn2)
        self.btn3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn3.setObjectName("btn3")
        self.verticalLayout.addWidget(self.btn3)
        self.btn4 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn4.setObjectName("btn4")
        self.verticalLayout.addWidget(self.btn4)
        self.spinBox = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setMaximum(9999)
        self.verticalLayout.addWidget(self.spinBox)
        self.btn5 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn5.setObjectName("btn5")
        self.verticalLayout.addWidget(self.btn5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
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
        self.btn1.setText(_translate("MainWindow", "Show Train Images"))
        self.btn2.setText(_translate("MainWindow", "Show Hyperparameters"))
        self.btn3.setText(_translate("MainWindow", "Show Model Structure"))
        self.btn4.setText(_translate("MainWindow", "Show Accuracy"))
        self.btn5.setText(_translate("MainWindow", "Test"))

        self.setbtn()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())