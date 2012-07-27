import sys
sys.path.append("..")
from ui.ui import Ui_MainWindow
from ui.about import Ui_About
from PyQt4 import QtCore, QtGui
import functions.negApi as mon

class monPy (QtGui.QMainWindow):
	"""Este programa permite realizar conversiones entre
	Monedas soportadas por Google Calculator, el valor de
	cada moneda esta sujeto los datos que google tenga
	actualizados"""

	monEx=sorted(["USD","MXN","EUR","GBP","INR","AUD","CAD","JPY","RMB","THB","SGD"])
	query=mon.negApi()
	mainWindow=None
	inputTo=None
	inputFrom=None
	comboFrom=None
	comboTo=None

	def __init__(self):
		self.setupUI()
		self.connectUi()
		self.centrarVentana()
		#Desplegar interfaz
		self.show()
		sys.exit(self.app.exec_())
		pass


	def setupUI(self):
		self.app=QtGui.QApplication(sys.argv)
		QtGui.QMainWindow.__init__(self)
		self.mainWindow=Ui_MainWindow()
		self.mainWindow.setupUi(self)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("images/flags/MXN.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.setWindowIcon(icon)
		self.inputFrom=self.mainWindow.inputFrom
		self.inputTo=self.mainWindow.inputTo
		self.comboFrom=self.mainWindow.comboFrom
		self.comboTo=self.mainWindow.comboTo

		self.inputFrom.setValidator(QtGui.QDoubleValidator())
		self.inputTo.setValidator(QtGui.QDoubleValidator())
		self.inputFrom.setText("1")
		self.fillCombos()
		self.comboTo.setCurrentIndex(self.monEx.index("MXN"))
		self.comboFrom.setCurrentIndex(self.monEx.index("USD"))
		self.convert()

		pass
	def fillCombos(self):
		for country in self.monEx:
			self.comboFrom.addItem(QtGui.QIcon("images/flags/"+country+".png"),country)
			self.comboTo.addItem(QtGui.QIcon("images/flags/"+country+".png"),country)
		pass

	def connectUi(self):
		self.comboFrom.currentIndexChanged.connect(self.convert)
		self.comboTo.currentIndexChanged.connect(self.convert)
		self.inputFrom.textChanged.connect(self.convert)
		self.mainWindow.btnAbout.clicked.connect(self.showAbout)
		pass

	def convert(self):
		mFrom=self.monEx[self.comboFrom.currentIndex()]
		mTo=self.monEx[self.comboTo.currentIndex()]
		if self.inputFrom.text()=="":
			mcant=0
		else:
			mcant=float(self.inputFrom.text())
		res=self.doConvert(mFrom,mTo,mcant)
		if res==None:
			self.inputTo.setText(str("%.2f"%0.0))			
			dlg=QtGui.QMessageBox(self)
			dlg.setText("Error de Conexion")
			dlg.setIcon(QtGui.QMessageBox.Warning)
			dlg.open()
			return
		self.inputTo.setText(str("%.2f"%res))
		pass

	def doConvert(self,mFrom,mTo,cant):
		r=float(self.query.convert(cant,mFrom,mTo))
		return r

	def showAbout(self):
		dlgAbout=QtGui.QDialog()
		dlgUI=Ui_About()
		dlgUI.setupUi(dlgAbout)
		pic=QtGui.QPixmap("images/logo.jpg")
		dlgUI.label.setPixmap(pic)
		dlgAbout.exec_()
		pass

	def centrarVentana(self):
		g=self.frameGeometry()
		c=QtGui.QDesktopWidget().availableGeometry().center()
		g.moveCenter(c)
		self.move(g.topLeft())
		pass

if __name__ == '__main__':
	monPy()
