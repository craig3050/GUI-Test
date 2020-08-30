# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Drawing_Renamer.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(758, 589)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(340, 10, 401, 531))
        self.listWidget.setObjectName("listWidget")
        self.Title_lablel = QtWidgets.QLabel(self.centralwidget)
        self.Title_lablel.setGeometry(QtCore.QRect(20, 10, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.Title_lablel.setFont(font)
        self.Title_lablel.setObjectName("Title_lablel")
        self.lineEdit_enter_path = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_enter_path.setGeometry(QtCore.QRect(10, 80, 251, 20))
        self.lineEdit_enter_path.setObjectName("lineEdit_enter_path")
        self.label_enter_path = QtWidgets.QLabel(self.centralwidget)
        self.label_enter_path.setGeometry(QtCore.QRect(10, 60, 231, 21))
        self.label_enter_path.setObjectName("label_enter_path")
        self.pushButton_enter_path = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_enter_path.setGeometry(QtCore.QRect(263, 79, 75, 23))
        self.pushButton_enter_path.setObjectName("pushButton_enter_path")
        self.pushButton_rename = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_rename.setGeometry(QtCore.QRect(10, 490, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_rename.setFont(font)
        self.pushButton_rename.setObjectName("pushButton_rename")
        self.lineEdit_enter_beginningtext = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_enter_beginningtext.setGeometry(QtCore.QRect(10, 140, 251, 20))
        self.lineEdit_enter_beginningtext.setObjectName("lineEdit_enter_beginningtext")
        self.pushButton_enter_beginningtext = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_enter_beginningtext.setGeometry(QtCore.QRect(263, 139, 75, 23))
        self.pushButton_enter_beginningtext.setObjectName("pushButton_enter_beginningtext")
        self.label_enter_beginningtext = QtWidgets.QLabel(self.centralwidget)
        self.label_enter_beginningtext.setGeometry(QtCore.QRect(10, 120, 231, 21))
        self.label_enter_beginningtext.setObjectName("label_enter_beginningtext")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 758, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
###
        self.pushButton_enter_path.clicked.connect(self.enter_path)
        self.pushButton_enter_beginningtext.clicked.connect(self.enter_beginningtext)
###
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Title_lablel.setText(_translate("MainWindow", "Drawing Renamer V1"))
        self.label_enter_path.setToolTip(_translate("MainWindow", "<html><head/><body><p>e.g. \'C:/Users/Craig/Desktop/Foldername\'</p></body></html>"))
        self.label_enter_path.setText(_translate("MainWindow", "Enter the path to the folder of drawings:"))
        self.pushButton_enter_path.setText(_translate("MainWindow", "Load"))
        self.pushButton_rename.setText(_translate("MainWindow", "Rename"))
        self.pushButton_enter_beginningtext.setText(_translate("MainWindow", "Preview"))
        self.label_enter_beginningtext.setToolTip(_translate("MainWindow", "<html><head/><body><p>e.g. &quot;Your_Filename&quot; becomes &quot;Additional Text Your Filename&quot;</p></body></html>"))
        self.label_enter_beginningtext.setText(_translate("MainWindow", "Enter text to add to the start of the filename:"))
###
    def enter_path(self):
        #list_to_print = ["bum", "willy", "poop", "arse", "winkie", "bum", "willy", "poop", "arse", "winkie", "bum", "willy", "poop", "arse", "winkie", "bum", "willy", "poop", "arse", "winkie", "bum", "willy", "poop", "arse", "winkie", "bum", "willy", "poop", "arse", "winkie", "bum", "willy", "poop", "arse", "winkie", "bum", "willy", "poop", "arse", "winkie", "bum", "willy", "poop", "arse", "winkie", "bum", "willy", "poop", "arse", "winkie", "bum", "willy", "poop", "arse", "winkie", "bum", "willy", "poop", "arse", "winkie", "bum", "willy", "poop", "arse", "winkie", "bum", "willy", "poop", "arse", "winkie"]
        file_path = self.lineEdit_enter_path.text()
        self.listWidget.addItem(file_path)
        #for item in list_to_print:
            #self.listWidget.addItem(item)
        return

    def enter_beginningtext(self):
        beginning_text = self.lineEdit_enter_beginningtext.text()
        self.listWidget.addItem(beginning_text)
        #self.listWidget.clear()
        return

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

###