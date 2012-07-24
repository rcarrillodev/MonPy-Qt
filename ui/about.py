# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created: Sun Jul 15 02:38:24 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName(_fromUtf8("About"))
        About.resize(400, 300)
        About.setMinimumSize(QtCore.QSize(400, 300))
        About.setMaximumSize(QtCore.QSize(400, 300))
        self.verticalLayout = QtGui.QVBoxLayout(About)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(About)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout_2 = QtGui.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(110, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtGui.QLabel(self.tab)
        self.label.setText(_fromUtf8(""))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtGui.QSpacerItem(110, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.Licencia = QtGui.QWidget()
        self.Licencia.setObjectName(_fromUtf8("Licencia"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.Licencia)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.scrollArea = QtGui.QScrollArea(self.Licencia)
        self.scrollArea.setStyleSheet(_fromUtf8("border:0px;"))
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 360, 233))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.txtLicence = QtGui.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.txtLicence.setEnabled(True)
        self.txtLicence.setGeometry(QtCore.QRect(0, 0, 351, 221))
        self.txtLicence.setAutoFillBackground(False)
        self.txtLicence.setReadOnly(True)
        self.txtLicence.setOverwriteMode(False)
        self.txtLicence.setObjectName(_fromUtf8("txtLicence"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_4.addWidget(self.scrollArea)
        self.tabWidget.addTab(self.Licencia, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setOpenExternalLinks(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_5.addWidget(self.label_3)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(About)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        About.setWindowTitle(QtGui.QApplication.translate("About", "About MonPy", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("About", "<html><head/><body><p align=\"center\">MonPy V1.0</p><p align=\"center\">Por Rafael Carrillo de Focus Development</p><p align=\"center\">2012</p><p align=\"center\"><a href=\"http://focusdevelop.wordpress.com\"><span style=\" text-decoration: underline; color:#0000ff;\">FocusDevelopment</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("About", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.txtLicence.setPlainText(QtGui.QApplication.translate("About", "Este programa es software libre: Puedes redistribuirlo y/o modificarlo bajo los terminos de la Licencia GNU/GPL publicados en la FSF.\n"
"\n"
"Es desarrollado y distribuido con la esperanza de que te sea util y no nos hacemos responsables de ningun tipo de garantía.\n"
"\n"
"Puedes ver una copia completa de la licencia en  : http://www.gnu.org/licenses/", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Licencia), QtGui.QApplication.translate("About", "Licencia", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("About", "<html><head/><body><p>Puedes mirar el codigo fuente en el siguiente repositorio de github:</p><p><br/><a href=\"https://github.com/rafuru/MonPy-Qt\"><span style=\" text-decoration: underline; color:#0000ff;\">https://github.com/rafuru/MonPy-Qt</span></a></p><p><br/></p><p>Para dudas, sugerencias y comentarios  puedes visitarnos en la pagina de la aplicacion:</p><p><a href=\"http://rafuru.github.com/MonPy-Qt\"><span style=\" text-decoration: underline; color:#0000ff;\">MonPy en GitHub</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("About", "Source", None, QtGui.QApplication.UnicodeUTF8))

