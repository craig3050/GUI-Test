# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test6.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(764, 676)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(365, 31, 381, 571))
        self.listWidget.setObjectName("listWidget")
        self.Title_lablel = QtWidgets.QLabel(self.centralwidget)
        self.Title_lablel.setGeometry(QtCore.QRect(10, 30, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Title_lablel.setFont(font)
        self.Title_lablel.setObjectName("Title_lablel")
        self.button_to_print_list = QtWidgets.QPushButton(self.centralwidget)
        self.button_to_print_list.setGeometry(QtCore.QRect(30, 110, 271, 41))
        self.button_to_print_list.setObjectName("button_to_print_list")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 764, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.button_to_print_list.clicked.connect(self.pressed)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Title_lablel.setText(_translate("MainWindow", "List print test"))
        self.button_to_print_list.setText(_translate("MainWindow", "Press button to print the list"))

    def pressed(self):
        list_to_print = ["bum", "willy", "poop", "arse", "winkie"]
        for item in list_to_print:
            self.listWidget.addItem(item)
        return

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())