from PyQt5 import QtCore, QtWidgets
import cv2
import numpy as np
# import matplotlib.pyplot as plt


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


class Ui_MainWindow(object):
    def setbtn(self):
        self.b11.clicked.connect(self.LoadImage)
        self.b12.clicked.connect(self.ColorSeperation)
        self.b13.clicked.connect(self.Flipping)
        self.b14.clicked.connect(self.Blending)

        self.b21.clicked.connect(self.MedianFilter)
        self.b22.clicked.connect(self.GaussianBlur)
        self.b23.clicked.connect(self.BilateralFilter)

        self.b31.clicked.connect(self.GaussianBlur3)
        self.b32.clicked.connect(self.SobelX)
        self.b33.clicked.connect(self.SobelY)
        self.b34.clicked.connect(self.Magnitude)

        self.b41.clicked.connect(self.Transformation)

    # region 1
    def LoadImage(self):
        img = cv2.imread("Uncle_Roger.jpg")

        width = int(img.shape[1])
        height = int(img.shape[0])
        print("width =", width, "height =", height)

        cv2.imshow("Uncle_Roger", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        # self.Form = QtWidgets.QWidget()
        # self.ui = Ui_Form()
        # self.ui.setupUi(self.Form)
        # self.Form.show()

    def ColorSeperation(self):
        img = cv2.imread("Flower.jpg")
        B, G, R = cv2.split(img)
        zeros = np.zeros(img.shape[:2], dtype=np.uint8)

        cv2.imshow("Original", img)
        # cv2.waitKey(0)
        cv2.imshow("Red", cv2.merge([zeros, zeros, R]))
        # cv2.waitKey(0)
        cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
        # cv2.waitKey(0)
        cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def Flipping(self):
        img = cv2.imread("Uncle_Roger.jpg")
        cv2.imshow("Original", img)
        # row, col, ht = img.shape
        # matrix = cv2.getRotationMatrix2D((row/2, col/2), 180, 1)
        # newimg = cv2.warpAffine(img, matrix, (row, col))
        newimg = cv2.flip(img, 1)
        cv2.imshow("Flipping", newimg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def Blending(self):
        self.img = cv2.imread("Uncle_Roger.jpg")
        # row, col, ht = img.shape
        # matrix = cv2.getRotationMatrix2D((row/2, col/2), 180, 1)
        # newimg = cv2.warpAffine(img, matrix, (row, col))
        self.img2 = cv2.flip(self.img, 1)
        # self.blendimg = cv2.addWeighted(self.img, 0.5, self.img2, 0.3, 0)
        cv2.imshow("Blending", self.img)
        cv2.createTrackbar("Ratio", "Blending", 0, 100, self.subBlending)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def subBlending(self, x):
        ratio = cv2.getTrackbarPos("Ratio", "Blending")
        self.blendimg = cv2.addWeighted(
            self.img, (100-ratio)*0.01, self.img2, ratio*0.01, 0)
        cv2.imshow("Blending", self.blendimg)

    # endregion

    # region 2
    def MedianFilter(self):
        img = cv2.imread("Cat.png")
        newimg = cv2.medianBlur(img, 7)
        cv2.imshow("Cat", img)
        cv2.imshow("Median", newimg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def GaussianBlur(self):
        img = cv2.imread("Cat.png")
        newimg = cv2.GaussianBlur(img, (3, 3), 0)
        cv2.imshow("Cat", img)
        cv2.imshow("Gaussian", newimg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def BilateralFilter(self):
        img = cv2.imread("Cat.png")
        newimg = cv2.bilateralFilter(img, 9, 90, 90)
        cv2.imshow("Cat", img)
        cv2.imshow("Bilateral", newimg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # endregion

    # region 3
    def GaussianBlur3(self):
        img = cv2.imread("Chihiro.jpg")
        newimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        x, y = np.mgrid[-1:2, -1:2]
        kernel = np.exp(-(x*x+y*y))/(2*np.pi)
        kernel = kernel/kernel.sum()
        print(kernel)
        gimg = cv2.filter2D(newimg, -1, kernel)
        # plt.imshow(kernel, cmap=plt.get_cmap(newimg),
        # interpolation='nearest')
        # plt.colorbar()
        # plt.show()
        cv2.imshow("asd", newimg)
        cv2.imshow("GaussianBlur", gimg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def SobelX(self):
        img = cv2.imread("Chihiro.jpg")
        newimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        kernel = np.mat([
            [-1, 0, 1],
            [-2, 0, 2],
            [-1, 0, 1]
        ])
        ximg = cv2.filter2D(newimg, -1, kernel)
        cv2.imshow("SobelX", ximg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def SobelY(self):
        img = cv2.imread("Chihiro.jpg")
        newimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        kernel = np.mat([
            [1, 2, 1],
            [0, 0, 0],
            [-1, -2, -1]
        ])
        yimg = cv2.filter2D(newimg, -1, kernel)
        cv2.imshow("SobelY", yimg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def Magnitude(self):
        img = cv2.imread("Chihiro.jpg")
        newimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        kernel = np.mat([
            [-1, 0, 1],
            [-2, 0, 2],
            [-1, 0, 1]
        ])
        ximg = cv2.filter2D(newimg, -1, kernel)
        kernel = np.mat([
            [1, 2, 1],
            [0, 0, 0],
            [-1, -2, -1]
        ])
        yimg = cv2.filter2D(newimg, -1, kernel)

        mimg = cv2.add(ximg, yimg)
        cv2.imshow("Magnitude", mimg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # endregion

    # region 4
    def Transformation(self):
        img = cv2.imread("Parrot.png")

        row, col, ch = img.shape

        temp = self.line1.text() if self.line1.text() else 0
        if is_number(temp):
            rotate = float(temp)
        else:
            print("please enter a number")
            rotate = 0

        temp = self.line2.text() if self.line2.text() else 1
        if is_number(temp):
            scale = float(temp)
        else:
            print("please enter a number")
            scale = 1

        temp = self.line3.text() if self.line3.text() else 0
        if is_number(temp):
            transx = float(temp)
        else:
            print("please enter a number")
            transx = 0

        temp = self.line4.text() if self.line4.text() else 0
        if is_number(temp):
            transy = float(temp)
        else:
            print("please enter a number")
            transy = 0

        cx = 160
        cy = 84
        cx = cx+transx
        cy = cy+transy

        matrixt = np.float32([[1, 0, transx], [0, 1, transy]])
        matrixr = cv2.getRotationMatrix2D((cx, cy), rotate, scale)

        newimg = cv2.warpAffine(img, matrixt, (col, row))
        newimg = cv2.warpAffine(newimg, matrixr, (col, row))

        # cv2.imshow("Parrot", img)
        cv2.imshow("Parrot_Trans", newimg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # endregion

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        QtWidgets.qApp.setStyleSheet("QPushButton{text-align : left;}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(60, 60, 691, 481))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(20, 0, 20, 0)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.b11 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.b11.setObjectName("b11")
        self.verticalLayout_2.addWidget(self.b11)
        self.b12 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.b12.setObjectName("b12")
        self.verticalLayout_2.addWidget(self.b12)
        self.b13 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.b13.setObjectName("b13")
        self.verticalLayout_2.addWidget(self.b13)
        self.b14 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.b14.setObjectName("b14")
        self.verticalLayout_2.addWidget(self.b14)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.line = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.b21 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.b21.setObjectName("b21")
        self.verticalLayout_3.addWidget(self.b21)
        self.b22 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.b22.setObjectName("b22")
        self.verticalLayout_3.addWidget(self.b22)
        self.b23 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.b23.setObjectName("b23")
        self.verticalLayout_3.addWidget(self.b23)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.line2 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line2.setObjectName("line2")
        self.horizontalLayout.addWidget(self.line2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.b31 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.b31.setObjectName("b31")
        self.verticalLayout.addWidget(self.b31)
        self.b32 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.b32.setObjectName("b32")
        self.verticalLayout.addWidget(self.b32)
        self.b33 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.b33.setObjectName("b33")
        self.verticalLayout.addWidget(self.b33)
        self.b34 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.b34.setObjectName("b34")
        self.verticalLayout.addWidget(self.b34)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.line3 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line3.setObjectName("line3")
        self.horizontalLayout.addWidget(self.line3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(0, 22, -1, 26)
        self.verticalLayout_4.setSpacing(17)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.line1 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.line1.sizePolicy().hasHeightForWidth())
        self.line1.setSizePolicy(sizePolicy)
        self.line1.setObjectName("line1")
        self.horizontalLayout_3.addWidget(self.line1)
        self.label_14 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_3.addWidget(self.label_14)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(7)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.line2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.line2.sizePolicy().hasHeightForWidth())
        self.line2.setSizePolicy(sizePolicy)
        self.line2.setObjectName("line2")
        self.horizontalLayout_6.addWidget(self.line2)
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(13)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_6.addWidget(self.label_11)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_8.addWidget(self.label_10)
        self.line3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.line3.sizePolicy().hasHeightForWidth())
        self.line3.setSizePolicy(sizePolicy)
        self.line3.setObjectName("line3")
        self.horizontalLayout_8.addWidget(self.line3)
        self.label_12 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_8.addWidget(self.label_12)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_7.addWidget(self.label_9)
        self.line4 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.line4.sizePolicy().hasHeightForWidth())
        self.line4.setSizePolicy(sizePolicy)
        self.line4.setObjectName("line4")
        self.horizontalLayout_7.addWidget(self.line4)
        self.label_13 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_7.addWidget(self.label_13)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.b41 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.b41.setObjectName("b41")
        self.verticalLayout_4.addWidget(self.b41)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(
            QtCore.QRect(60, -30, 691, 151))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(26, 0, 83, 0)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.setbtn()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # MainWindow.setTabOrder(self.b33, self.b34)
        # MainWindow.setTabOrder(self.b34, self.b11)
        # MainWindow.setTabOrder(self.b11, self.b13)
        # MainWindow.setTabOrder(self.b13, self.b14)
        # MainWindow.setTabOrder(self.b14, self.b21)
        # MainWindow.setTabOrder(self.b21, self.b22)
        # MainWindow.setTabOrder(self.b22, self.b23)
        # MainWindow.setTabOrder(self.b23, self.b12)
        # MainWindow.setTabOrder(self.b12, self.b32)
        # MainWindow.setTabOrder(self.b32, self.b31)
        # # MainWindow.setTabOrder(self.b31, MainWindow.lineEdit_2)
        # # MainWindow.setTabOrder(MainWindow.lineEdit_3, self.line2)
        # MainWindow.setTabOrder(self.b31, self.line1)
        # MainWindow.setTabOrder(self.line2, self.line4)
        # MainWindow.setTabOrder(self.line4, self.line3)
        # MainWindow.setTabOrder(self.line3, self.b41)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.b11.setText(_translate("MainWindow", "Load Image"))
        self.b12.setText(_translate("MainWindow", "Color Sparation"))
        self.b13.setText(_translate("MainWindow", "Image Flipping"))
        self.b14.setText(_translate("MainWindow", "Blemding"))
        self.b21.setText(_translate("MainWindow", "Median Fliter"))
        self.b22.setText(_translate("MainWindow", "Gaussian Blur"))
        self.b23.setText(_translate("MainWindow", "Bilateral Filter"))
        self.b31.setText(_translate("MainWindow", "Gaussian Blur"))
        self.b32.setText(_translate("MainWindow", "Sobel X"))
        self.b33.setText(_translate("MainWindow", "Sobel Y"))
        self.b34.setText(_translate("MainWindow", "Magnitude"))
        self.label_5.setText(_translate("MainWindow", "Rotation"))
        self.label_14.setText(_translate("MainWindow", "deg"))
        self.label_8.setText(_translate("MainWindow", "Scaling"))
        self.label_10.setText(_translate("MainWindow", "Tx"))
        self.label_12.setText(_translate("MainWindow", "pixel"))
        self.label_9.setText(_translate("MainWindow", "Ty"))
        self.label_13.setText(_translate("MainWindow", "pixel"))
        self.b41.setText(_translate("MainWindow", "Trasformation"))
        self.label.setText(_translate("MainWindow", "1. Image Processing"))
        self.label_2.setText(_translate("MainWindow", "2. Image Smoothing"))
        self.label_3.setText(_translate("MainWindow", "3. Edge Detection"))
        self.label_4.setText(_translate("MainWindow", "4. Transformation"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
