# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Test5.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.combox = QtWidgets.QComboBox(self.centralwidget)
        self.combox.setGeometry(QtCore.QRect(110, 80, 221, 191))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.combox.setFont(font)
        self.combox.setObjectName("combox")
        self.combox.addItem("")
        self.combox.addItem("")
        self.comboy = QtWidgets.QComboBox(self.centralwidget)
        self.comboy.setGeometry(QtCore.QRect(450, 80, 221, 191))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.comboy.setFont(font)
        self.comboy.setObjectName("comboy")
        self.comboy.addItem("")
        self.comboy.addItem("")
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(280, 390, 201, 111))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.submit.setFont(font)
        self.submit.setObjectName("submit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 300, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.submit.clicked.connect(self.pressed)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.combox.setItemText(0, _translate("MainWindow", "0"))
        self.combox.setItemText(1, _translate("MainWindow", "1"))
        self.comboy.setItemText(0, _translate("MainWindow", "0"))
        self.comboy.setItemText(1, _translate("MainWindow", "1"))
        self.submit.setText(_translate("MainWindow", "Submit"))
        self.label.setText(_translate("MainWindow", "X OR Y = "))

    def pressed(self):
        x = int(self.combox.currentText())
        y = int(self.comboy.currentText())
        xor = (x and not y) or (not x and y)

        self.label.setText("X XOR Y = " + " " + str(xor))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
