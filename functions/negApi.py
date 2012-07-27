import urllib2, ast,json,re

class negApi():
	"""Modulo para realizar conversiones monetarias via Google Calculator"""
	monFrom=None
	monTo=None
	mCant=None
	conv=0.0

	def __init__(self):
		self.monFrom="USD"
		self.monTo="MXN"
		self.mCant=1
		pass

	
	def doConvertion(self):
		val=0
		self.mCant=str(self.mCant)
		try:
			resp=urllib2.urlopen("http://www.google.com/ig/calculator?hl=en&q=1"+self.monFrom+"=?"+self.monTo+"").read()		
		except urllib2.URLError as error:
			print ("Error al consultar el tipo de cambio, error de conexion")
			print (error)
			return None

		d = {} #Tupla para guardar claves y valores 
		for pair in resp[1:-1].split(','): #Para cada separacion por , ...
    			(k,v) = pair.split(':') #Tupla : k=key , v=val
    			v = v.strip()  #Elimina espacios
    			if v == "true": #Si el valor es "true" cambiarlo a True, legible para Python
        			v = "True"
    			try:
        			v = ast.literal_eval(v) #Evalua si la literal es un valor entendible para Python
    			except:
        			print "Couldn't eval " + v 
    			d[k] = v #Agrega el valor a la tupla
		try:
			val= float(re.sub("\D+.\D+","", d["rhs"].decode('utf-8','ignore')))
			conv=val*float(self.mCant)
		except ValueError as valErr:
			print ("Ha introducido un numero enorme!")
		return conv

	def convert(self,mCant,monFrom,monTo):
		if(self.monFrom==None and self.monTo==None):
			return doConvertion()
		self.monFrom=monFrom
		self.monTo=monTo
		self.mCant=mCant
		return self.doConvertion()

if __name__ == '__main__':
	convert=negApi()
	print convert.convert(1,"USD","MXN")	



