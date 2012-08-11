# -*- coding: utf-8 -*-
"""
saving.py
V0.5a
Guarda los datos para funcionamiento Offline
@Rafael Carrillo
"""
import os

class saving():
	dLoc=""
	dTo=""
	dMon=0.0
	conf=None
	fName="conf.monpy"

	def __init__(self):
		pass

	def checkDir(self):
		if os.path.exists(self.fName):
			self.conf=open(self.fName,"r")
			return True
		else:
			return False
		return

	def read(self):
		try:
			if self.checkDir():
				self.dLoc=self.conf.readline().strip("From=\n")
				self.dTo=self.conf.readline().strip("To=\n")
				self.dMon=float(self.conf.readline().strip("val="))
				self.conf.close()
				return [self.dLoc,self.dTo,self.dMon]
			else:
				return None
		except IOError as ioe:
			print (ioe)
			return False
		pass

	def save(self,data):
		loc=data[0]
		conv=data[1]
		mon=data[2]
		try:
			self.conf=open(self.fName,"w")
			self.conf.seek(0)
			self.conf.write("From="+loc+"\n")
			self.conf.write("To="+conv+"\n")
			self.conf.write("val="+str(mon))
			self.conf.write("\n**********Archivo Generado Por MonPY**********")
			self.conf.close()
			return True
		except IOError as ioe:
			print (ioe)
			self.conf.close()
			return False
		pass



