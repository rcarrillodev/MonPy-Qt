"""
MonPY realiza cambios de divisa
Clase principal
@Rafael Carrillo
V1.5
"""
import sys
from ui.ui import Ui_MainWindow
from ui.about import Ui_About
try:
	from PyQt4 import QtCore, QtGui
except ImportError:
	print ("Error al importar PyQT4, revisa que esta instalado")
	exit()
import functions.negApi as mon
import functions.saving as sav
import datetime

class monPy (QtGui.QMainWindow):
	"""Este programa permite realizar conversiones entre
	Monedas soportadas por Google Calculator, el valor de
	cada moneda esta sujeto los datos que google tenga
	actualizados"""
	#Lista de Monedas
	monEx=sorted(["USD", "MXN", "EUR", "GBP", "INR", "AUD", "CAD", "JPY", "RMB", "THB", "SGD"])

	#Constructor de la clase de conversiones
	query=mon.negApi()

	#Constructor de la clase de guardado de datos
	save=sav.saving() 

	#Elementos de la Interfaz de Usuario
	mainWindow=None
	inputTo=None
	inputFrom=None
	comboFrom=None
	comboTo=None
	lblStatus=None

	#Variables
	prefs=None #Preferencias
	
	#Valor de la moneda actual
	valorActual=0.0
	#Moneda local 
	monFrom="" 
	#Moneda Extranjera
	monTo=""


	def __init__(self):
		self.setupUI()
		self.connectUi()
		self.centrarVentana()
		#Desplegar interfaz
		self.show()
		sys.exit(self.app.exec_())
		pass


	def setupUI(self):
		"""
		Carga los objetos de la interfaz en variables locales
		Carga la configuracion guardada y realiza la conversion inicial
		"""
		self.app=QtGui.QApplication(sys.argv)
		QtGui.QMainWindow.__init__(self)
		self.mainWindow=Ui_MainWindow()
		self.mainWindow.setupUi(self)
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(":Images/images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.setWindowIcon(icon)
		self.inputFrom=self.mainWindow.inputFrom
		self.inputTo=self.mainWindow.inputTo
		self.comboFrom=self.mainWindow.comboFrom
		self.comboTo=self.mainWindow.comboTo
		self.lblStatus=self.mainWindow.lblStatus

		self.inputFrom.setValidator(QtGui.QDoubleValidator())
		self.inputTo.setValidator(QtGui.QDoubleValidator())
		self.inputFrom.setText("1")
		self.fillCombos()
		self.loadPrefs()	
		self.update()	
		self.convert()

		pass

	#Ok
	def fillCombos(self):
		for country in self.monEx:
			self.comboFrom.addItem(QtGui.QIcon(":Flags/images/flags/"+country+".png"),country)
			self.comboTo.addItem(QtGui.QIcon(":Flags/images/flags/"+country+".png"),country)
		pass

	#Checar Convert
	def connectUi(self):
		self.comboFrom.currentIndexChanged.connect(self.comboChanged)
		self.comboTo.currentIndexChanged.connect(self.comboChanged)
		self.inputFrom.textChanged.connect(self.convert)
		self.mainWindow.btnAbout.clicked.connect(self.showAbout)
		self.mainWindow.btnConf.clicked.connect(self.configure)
		self.mainWindow.btnUpdate.clicked.connect(self.update)
		return

	#Ok
	def configure(self):
		data=[self.monFrom,self.monTo,self.valorActual]
		if self.save.save(data):
			self.lblStatus.setText("Configuracion Guardada")
		else:
			self.lblStatus.setText("Error al Configurar")
		return

	#Ok
	def comboChanged(self):
		self.monFrom=self.monEx[self.comboFrom.currentIndex()]
		self.monTo=self.monEx[self.comboTo.currentIndex()]
		if self.update():
			self.convert()
			return
		self.convert()
		return

	#Ok
	def loadPrefs(self):
		try:
			self.prefs=self.save.read()
			if not (self.prefs==None):
				self.monFrom=self.prefs[0]
				self.monTo=self.prefs[1]
				self.valorActual=self.prefs[2]
			else:
				self.monFrom="USD"
				self.monTo="MXN"
		except ValueError as badConf:
			print ("Error al Cargar Configuracion")
			self.monFrom="USD"
			self.monTo="MXN"
			self.valorActual=0
		finally:
			self.comboFrom.setCurrentIndex(self.monEx.index(self.monFrom))
			self.comboTo.setCurrentIndex(self.monEx.index(self.monTo))

		return

	def convert(self):

		self.lblStatus.setText("")
		txt=self.inputFrom.text()
		conv=0
		r=0.0
		if not(txt=="" or txt=="e"):
			r=float(txt)*self.valorActual

		self.inputTo.setText(str("%.2f"%r))
		return

	#Ok
	def update(self):
		self.lblStatus.setText("Actualizando....")
		r=self.query.convert(1,self.monFrom,self.monTo)
		if r==None:
			print("Error de Conexion")
			self.lblStatus.setText("Sin Conexion")
			return False

		self.valorActual=r
		self.convert()
		self.lblStatus.setText("Actualizado")
		return True


	#---------- Tareas de la Interfaz -------- #
	#OK
	def showAbout(self):
		dlgAbout=QtGui.QDialog()
		dlgUI=Ui_About()
		dlgUI.setupUi(dlgAbout)
		pic=QtGui.QPixmap(":Images/images/icon.png")
		dlgUI.label.setPixmap(pic)
		dlgAbout.exec_()
		pass

	#Ok
	def centrarVentana(self):
		g=self.frameGeometry()
		c=QtGui.QDesktopWidget().availableGeometry().center()
		g.moveCenter(c)
		self.move(g.topLeft())
		pass


if __name__ == '__main__':
	monPy()
