# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Tue Aug  7 01:09:49 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(345, 156)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(308, 142))
        MainWindow.setMaximumSize(QtCore.QSize(345, 156))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../MonPy/images/flags/MXN.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.inputFrom = QtGui.QLineEdit(self.centralwidget)
        self.inputFrom.setGeometry(QtCore.QRect(10, 30, 131, 23))
        self.inputFrom.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.inputFrom.setObjectName(_fromUtf8("inputFrom"))
        self.comboFrom = QtGui.QComboBox(self.centralwidget)
        self.comboFrom.setGeometry(QtCore.QRect(150, 29, 81, 27))
        self.comboFrom.setObjectName(_fromUtf8("comboFrom"))
        self.inputTo = QtGui.QLineEdit(self.centralwidget)
        self.inputTo.setGeometry(QtCore.QRect(110, 80, 131, 21))
        self.inputTo.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.inputTo.setReadOnly(True)
        self.inputTo.setObjectName(_fromUtf8("inputTo"))
        self.comboTo = QtGui.QComboBox(self.centralwidget)
        self.comboTo.setGeometry(QtCore.QRect(260, 30, 81, 27))
        self.comboTo.setObjectName(_fromUtf8("comboTo"))
        self.btnAbout = QtGui.QPushButton(self.centralwidget)
        self.btnAbout.setGeometry(QtCore.QRect(10, 116, 61, 21))
        self.btnAbout.setObjectName(_fromUtf8("btnAbout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 10, 56, 15))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(237, 36, 21, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.btnConf = QtGui.QPushButton(self.centralwidget)
        self.btnConf.setGeometry(QtCore.QRect(300, 121, 24, 20))
        self.btnConf.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("../MonPy-Qt/images/gear.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnConf.setIcon(icon1)
        self.btnConf.setFlat(True)
        self.btnConf.setObjectName(_fromUtf8("btnConf"))
        self.lblStatus = QtGui.QLabel(self.centralwidget)
        self.lblStatus.setGeometry(QtCore.QRect(90, 120, 181, 16))
        self.lblStatus.setText(_fromUtf8(""))
        self.lblStatus.setObjectName(_fromUtf8("lblStatus"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MonPy", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Convertir:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "a:", None, QtGui.QApplication.UnicodeUTF8))
        self.btnConf.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><span style=\" vertical-align:sub;\">Establecer monedas actuales como predeterminadas</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

