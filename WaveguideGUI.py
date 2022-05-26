# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WaveGUI.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1347, 1058)
        font = QtGui.QFont()
        font.setFamily("Noto Sans Mono CJK SC")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setWindowOpacity(10.0)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color:rgb(85, 87, 83)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1100, 890, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background-color:rgb(54, 55, 55);\n"
"border-radius: 20px;\n"
"color: rgb(243, 243, 243);")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(950, 830, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("border: 2px solid rgb(85, 87, 83);\n"
"border-radius: 20px;\n"
"background-color: rgb(54, 55, 55);\n"
"padding-left:22px;\n"
"color: rgb(255, 255, 255)\n"
"")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(1200, 730, 48, 26))
        self.spinBox.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color:rgb(54, 55, 55)")
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(1200, 670, 48, 26))
        self.spinBox_2.setStyleSheet("color:rgb(255, 255, 255);\n"
"\n"
"background-color:rgb(54, 55, 55)")
        self.spinBox_2.setObjectName("spinBox_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1190, 650, 67, 17))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1190, 710, 67, 17))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 0, 501, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 70, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:rgb(255, 255, 255)")
        self.label_5.setObjectName("label_5")
        self.MplWidget1 = MplWidget(self.centralwidget)
        self.MplWidget1.setGeometry(QtCore.QRect(50, 100, 801, 261))
        self.MplWidget1.setStyleSheet("background-color:rgb(52, 56, 55);\n"
"border-radius:20px")
        self.MplWidget1.setObjectName("MplWidget1")
        self.MplWidget2 = MplWidget(self.centralwidget)
        self.MplWidget2.setGeometry(QtCore.QRect(50, 380, 801, 261))
        self.MplWidget2.setAutoFillBackground(False)
        self.MplWidget2.setStyleSheet("background-color: rgb(52, 56, 55);\n"
"border-radius:20px;\n"
"padding: 20px;")
        self.MplWidget2.setObjectName("MplWidget2")
        self.MplWidget3 = MplWidget(self.centralwidget)
        self.MplWidget3.setGeometry(QtCore.QRect(50, 660, 801, 261))
        self.MplWidget3.setStyleSheet("background-color: rgb(52, 56, 55);\n"
"border-radius:20px")
        self.MplWidget3.setObjectName("MplWidget3")
        self.verticalWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalWidget.setGeometry(QtCore.QRect(950, 670, 91, 91))
        self.verticalWidget.setStyleSheet("background-color:     rgb(54, 55, 55);\n"
"border-radius: 20px;")
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("color:rgb(255, 255, 255);\n"
"padding-left:16px\n"
"")
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("color:rgb(255, 255, 255);\n"
"padding-left:16px\n"
"")
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(60, 950, 571, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("border: 2px solid rgb(85, 87, 83);\n"
"border-radius: 20px;\n"
"background-color: rgb(54, 55, 55);\n"
"padding-left:22px;\n"
"color: rgb(255, 255, 255)")
        self.label_6.setObjectName("label_6")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(1150, 610, 101, 21))
        self.comboBox.setStyleSheet("background-color: rgb(54, 55, 55);\n"
"color: rgb(255, 255, 255)")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1176, 580, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(255, 255, 255)")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Start Building"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Input frequence value in GHz"))
        self.label_2.setText(_translate("MainWindow", "n-mode"))
        self.label_3.setText(_translate("MainWindow", "m-mode"))
        self.label_4.setText(_translate("MainWindow", "Wave Propagation in Rectangular Waveguide"))
        self.label_5.setText(_translate("MainWindow", "Results:"))
        self.radioButton_2.setText(_translate("MainWindow", "TE"))
        self.radioButton.setText(_translate("MainWindow", "TM"))
        self.label_6.setText(_translate("MainWindow", "Let\'s start"))
        self.comboBox.setItemText(0, _translate("MainWindow", "low"))
        self.comboBox.setItemText(1, _translate("MainWindow", "medium"))
        self.comboBox.setItemText(2, _translate("MainWindow", "high"))
        self.label.setText(_translate("MainWindow", "Density"))
from mplwidget import MplWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
