# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowIcon(QIcon("./icon/siom.ico"))
        MainWindow.resize(804, 609)
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height())
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 500, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_PV = QtWidgets.QLabel(self.centralwidget)
        self.label_PV.setGeometry(QtCore.QRect(280, 100, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_PV.setFont(font)
        self.label_PV.setObjectName("label_PV")
        self.label_Power = QtWidgets.QLabel(self.centralwidget)
        self.label_Power.setGeometry(QtCore.QRect(280, 180, 72, 15))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Power.setFont(font)
        self.label_Power.setObjectName("label_Power")
        self.label_Time = QtWidgets.QLabel(self.centralwidget)
        self.label_Time.setGeometry(QtCore.QRect(30, 100, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Time.setFont(font)
        self.label_Time.setObjectName("label_Time")
        self.label_Astmag = QtWidgets.QLabel(self.centralwidget)
        self.label_Astmag.setGeometry(QtCore.QRect(280, 240, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Astmag.setFont(font)
        self.label_Astmag.setObjectName("label_Astmag")
        self.label_PXJ = QtWidgets.QLabel(self.centralwidget)
        self.label_PXJ.setGeometry(QtCore.QRect(30, 180, 72, 15))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_PXJ.setFont(font)
        self.label_PXJ.setObjectName("label_PXJ")
        self.label_RS = QtWidgets.QLabel(self.centralwidget)
        self.label_RS.setGeometry(QtCore.QRect(30, 240, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_RS.setFont(font)
        self.label_RS.setObjectName("label_RS")
        self.label_expectPV = QtWidgets.QLabel(self.centralwidget)
        self.label_expectPV.setGeometry(QtCore.QRect(530, 110, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_expectPV.setFont(font)
        self.label_expectPV.setObjectName("label_expectPV")
        self.lineEdit_Power = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Power.setGeometry(QtCore.QRect(380, 170, 113, 30))
        self.lineEdit_Power.setObjectName("lineEdit_Power")
        self.lineEdit_PV = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_PV.setGeometry(QtCore.QRect(380, 100, 113, 30))
        self.lineEdit_PV.setObjectName("lineEdit_PV")
        self.label_expectAstmag = QtWidgets.QLabel(self.centralwidget)
        self.label_expectAstmag.setGeometry(QtCore.QRect(530, 240, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_expectAstmag.setFont(font)
        self.label_expectAstmag.setObjectName("label_expectAstmag")
        self.label_expectPower = QtWidgets.QLabel(self.centralwidget)
        self.label_expectPower.setGeometry(QtCore.QRect(530, 180, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_expectPower.setFont(font)
        self.label_expectPower.setObjectName("label_expectPower")
        self.label_nextTime = QtWidgets.QLabel(self.centralwidget)
        self.label_nextTime.setGeometry(QtCore.QRect(10, 390, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_nextTime.setFont(font)
        self.label_nextTime.setObjectName("label_nextTime")
        self.label_nextRS = QtWidgets.QLabel(self.centralwidget)
        self.label_nextRS.setGeometry(QtCore.QRect(530, 390, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_nextRS.setFont(font)
        self.label_nextRS.setObjectName("label_nextRS")
        self.label_nextPXJ = QtWidgets.QLabel(self.centralwidget)
        self.label_nextPXJ.setGeometry(QtCore.QRect(270, 390, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_nextPXJ.setFont(font)
        self.label_nextPXJ.setObjectName("label_nextPXJ")
        self.lineEdit_Time = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Time.setGeometry(QtCore.QRect(130, 100, 113, 30))
        self.lineEdit_Time.setObjectName("lineEdit_Time")
        self.lineEdit_PXJ = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_PXJ.setGeometry(QtCore.QRect(130, 170, 113, 30))
        self.lineEdit_PXJ.setObjectName("lineEdit_PXJ")
        self.lineEdit_RS = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_RS.setGeometry(QtCore.QRect(130, 240, 113, 30))
        self.lineEdit_RS.setObjectName("lineEdit_RS")
        self.lineEdit_expectPV = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_expectPV.setGeometry(QtCore.QRect(650, 100, 113, 30))
        self.lineEdit_expectPV.setObjectName("lineEdit_expectPV")
        self.lineEdit_expectPower = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_expectPower.setGeometry(QtCore.QRect(650, 170, 113, 30))
        self.lineEdit_expectPower.setObjectName("lineEdit_expectPower")
        self.lineEdit_expectAstmag = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_expectAstmag.setGeometry(QtCore.QRect(650, 240, 113, 30))
        self.lineEdit_expectAstmag.setObjectName("lineEdit_expectAstmag")
        self.lineEdit_nextTime = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nextTime.setGeometry(QtCore.QRect(130, 380, 113, 30))
        self.lineEdit_nextTime.setObjectName("lineEdit_nextTime")
        self.lineEdit_nextPXJ = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nextPXJ.setGeometry(QtCore.QRect(380, 380, 113, 30))
        self.lineEdit_nextPXJ.setObjectName("lineEdit_nextPXJ")
        self.lineEdit_nextRS = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nextRS.setGeometry(QtCore.QRect(650, 380, 113, 30))
        self.lineEdit_nextRS.setObjectName("lineEdit_nextRS")
        self.lineEdit_Astmag = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Astmag.setGeometry(QtCore.QRect(380, 240, 113, 30))
        self.lineEdit_Astmag.setObjectName("lineEdit_Astmag")
        self.labelCompany = QtWidgets.QLabel(self.centralwidget)
        self.labelCompany.setGeometry(QtCore.QRect(10, 10, 771, 31))
        self.labelCompany.setObjectName("labelCompany")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(380, 310, 50, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_state = QtWidgets.QLabel(self.centralwidget)
        self.label_state.setGeometry(QtCore.QRect(300, 310, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_state.setFont(font)
        self.label_state.setObjectName("label_state")
        self.lineEdit_nextPV = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nextPV.setGeometry(QtCore.QRect(130, 440, 113, 30))
        self.lineEdit_nextPV.setObjectName("lineEdit_nextPV")
        self.lineEdit_nextPower = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nextPower.setGeometry(QtCore.QRect(380, 440, 113, 30))
        self.lineEdit_nextPower.setObjectName("lineEdit_nextPower")
        self.lineEdit_nextAstmag = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nextAstmag.setGeometry(QtCore.QRect(650, 440, 113, 30))
        self.lineEdit_nextAstmag.setObjectName("lineEdit_nextAstmag")
        self.label_nextPV = QtWidgets.QLabel(self.centralwidget)
        self.label_nextPV.setGeometry(QtCore.QRect(10, 450, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_nextPV.setFont(font)
        self.label_nextPV.setObjectName("label_nextPV")
        self.label_nextPower = QtWidgets.QLabel(self.centralwidget)
        self.label_nextPower.setGeometry(QtCore.QRect(270, 450, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_nextPower.setFont(font)
        self.label_nextPower.setObjectName("label_nextPower")
        self.label_nextAstmag = QtWidgets.QLabel(self.centralwidget)
        self.label_nextAstmag.setGeometry(QtCore.QRect(530, 450, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_nextAstmag.setFont(font)
        self.label_nextAstmag.setObjectName("label_nextAstmag")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 804, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "??????????????????????????????"))
        self.pushButton.setText(_translate("MainWindow", "??????"))
        self.label_PV.setText(_translate("MainWindow", "PV/wave"))
        self.label_Power.setText(_translate("MainWindow", "Power/wave"))
        self.label_Time.setText(_translate("MainWindow", "????????????/min"))
        self.label_Astmag.setText(_translate("MainWindow", "Astmag/wave"))
        self.label_PXJ.setText(_translate("MainWindow", "?????????/mm"))
        self.label_RS.setText(_translate("MainWindow", "????????????/rpm"))
        self.label_expectPV.setText(_translate("MainWindow", "??????PV/wave"))
        self.label_expectAstmag.setText(_translate("MainWindow", "??????Astmag/wave"))
        self.label_expectPower.setText(_translate("MainWindow", "??????Power/wave"))
        self.label_nextTime.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">??????????????????/min</span></p></body></html>"))
        self.label_nextRS.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">??????????????????/rpm</span></p></body></html>"))
        self.label_nextPXJ.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">???????????????/mm</span><br/></p></body></html>"))
        self.labelCompany.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">????????????????????????????????????????????????</p></body></html>"))
        self.comboBox.setItemText(0, _translate("MainWindow", "T"))
        self.comboBox.setItemText(1, _translate("MainWindow", "L"))
        self.label_state.setText(_translate("MainWindow", "????????????"))
        self.label_nextPV.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">??????PV/wave</span></p></body></html>"))
        self.label_nextPower.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">??????Power/wave</span></p></body></html>"))
        self.label_nextAstmag.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">??????Astmag/wave</span></p></body></html>"))
