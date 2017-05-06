#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os

from Utilidad import Utilidad
from Sustitucion_Monoalfabetica.Cesar import Cesar
from Sustitucion_Monoalfabetica.Playfair import Playfair
from Sustitucion_Monoalfabetica.Polybios import Polybios

class ControladorSustitucionMonoTemplate(object):
	"""
	Clase "abstracta" que utiliza el patrón TemplateMethod.

	Los métodos cifrarTexto, cifrarArchivo, descifrarTexto, descifrarArchivo, son métodos que
	tienen pasos en común, lo único que cambia es el modo en que se va a cifrar los diferentes
	algoritmos de Transposicion.

	Los métodos modoCifrar y modoDescifrar, son los métodos que van a cambiar según el algoritmo
	a utilzar, estos se definen en las clases concretas.

	"""

	def __init__(self):
		self.utilidad = Utilidad()

	def modoDefinicionAlfabeto(self, *argumentos):
		raise NotImplementedError

	def modoCifrar(self, *argumentos):
		raise NotImplementedError
	
	def modoDescifrar(self, *argumentos):
		raise NotImplementedError

	def definirAlfabeto(self, alfabeto):
		self.alfabeto = alfabeto
		self.modoDefinicionAlfabeto(alfabeto)
		self.modoDefinicionAlfabeto(self.alfabeto)
	
	def cifrarTexto(self, archivo, relleno, clave):
		"""
		Método que se encarga de cifrar un archivo de texto (archvo plano).

		Parámetros:
		archivo: archivo plano que se desea cifrar.
		n: la cantidad de iteraciones con la que se desea cifrar el archivo plano.
		   Por ahora éste parámetro se utiliza para la Transposicion Doble.
		"""
		nombre, extension, codificacion, so = self.utilidad.obtenerMetadatos(archivo)
		#print(nombre, nombre, extension, codificacion, so)
		self.utilidad.crearArchivoMetadatos(nombre, nombre, extension, codificacion, so)
		
		self.utilidad.resolverCodificacion(codificacion, "UTF-8", archivo, "tmp")

		cadena = self.utilidad.leerArchivo(self.utilidad.dirSalida+"tmp","r")
		os.remove(self.utilidad.dirSalida+"tmp")
		cadena = cadena.split("\n")

		criptograma = self.modoCifrar(cadena, relleno, clave)

		self.utilidad.crearArchivo(nombre+extension+".CIF", criptograma, "w")

	def descifrarTexto(self, archivo, relleno, clave):
		"""
		Método que se encarga de descifrar un archivo de texto (archvo plano).

		Parámetros:
		archivo: archivo plano que se desea descifrar.
		n: la cantidad de iteraciones con la que se desea descifrar el archivo plano.
		   Por ahora éste parámetro se utiliza para la Transposicion Doble.
		"""
		metadatos = self.obtenerArchivoMetadatos(archivo)
		
		nombre = metadatos[0]
		extension = metadatos[1]
		codificacion = metadatos[2]
		so = metadatos[3]

		cadena = self.utilidad.leerArchivo(self.utilidad.dirSalida+nombre+extension+".CIF","r")
		cadena = cadena.split("\n")

		textoClaro = self.modoDescifrar(cadena, relleno, clave)
		self.__crearArchivoDescifrado(textoClaro, codificacion, nombre, extension)
		self.__resolverSaltoLinea(nombre,extension,so)

	def cifrarArchivo(self, archivo, n, clave):
		"""
		Método que se encarga de cifrar un archivo con codificación binaria.

		Parámetros:
		archivo: Dirección del archivo plano que se desea descifrar.
		n: la cantidad de iteraciones con la que se desea cifrar el archivo plano.
		   Por ahora éste parámetro se utiliza para la Transposicion Doble.
		"""
		#Saltar la excepcion del tipo de variable None
		try:
			nombre, extension, codificacion, so = self.utilidad.obtenerMetadatos(archivo)
			self.utilidad.crearArchivoMetadatos(nombre, nombre, extension, codificacion, so)
		except TypeError:
			pass
		
		cadenaB64 = self.utilidad.obtenerBase64(archivo)
		cadena = list()
		cadena.append(cadenaB64)

		#**************
		#**************

		criptograma = self.modoCifrar(cadena, 0, clave)


		#*****
		self.utilidad.crearArchivo(nombre+extension+".CIF", criptograma.encode(), "wb")
		#self.utilidad.crearArchivo(nombre+".txt"+".CIF", criptograma.encode(), "wb")
		#*****

		cantidadRelleno = len(criptograma) - len(cadenaB64)
		#if cantidadRelleno > 0:
		self.utilidad.crearArchivo(nombre+".mtd", str(cantidadRelleno), "a")
	
	def descifrarArchivo(self, archivo, n, clave):
		"""
		Método que se encarga de descifrar un archivo con codificación binaria.

		Parámetros:
		archivo: Dirección del archivo plano que se desea descifrar.
		n: la cantidad de iteraciones con la que se desea descifrar el archivo plano.
		   Por ahora éste parámetro se utiliza para la Transposicion Doble.
		"""
		try:
			metadatos = self.obtenerArchivoMetadatos(archivo)
			nombre = metadatos[0]
			extension = metadatos[1]
		except TypeError as te:
			print(te , " descifrarArchivo -- Template")

		
		#*****
		cadenaB64 = self.utilidad.leerArchivo(self.utilidad.dirSalida+nombre+extension+".CIF", "r")
		#cadenaB64 = self.utilidad.leerArchivo(self.utilidad.dirSalida+nombre+".txt"+".CIF", "r")
		#*****

		cadena = list()
		cadena.append(cadenaB64)

		textoClaro = self.modoDescifrar(cadena, 0, clave)
		textoClaro = self.utilidad.cadena_a_Base64(textoClaro)
		self.utilidad.crearArchivo(nombre+extension, textoClaro, "wb")
			
	#-----------------------------------------------------------------------------Métodos adicionales
	
	def obtenerArchivoMetadatos(self, archivo):
		"""
		Método que se encarga de obtener los metadatos del archivo (tanto texto como binario)
		para poder realizar el proceso de descifrado.
		"""
		#Obtener el archivo de metadatos según el nombre del archivo Cifrado
		direccion = os.path.splitext(archivo)
		nombre = direccion[0].split("/")[-1]
		nombre = os.path.splitext(nombre)[0]

		#Leer el archivo de metadatos -> metadatos = [nombre, extension, codificacion, so]
		metadatos = self.utilidad.leerArchivo(self.utilidad.dirSalida+nombre+".mtd", "r")
		return metadatos.split("\n")
	
	def __crearArchivoDescifrado(self, textoClaro, codificacion, nombre, extension):
		"""
		Método que se encarga de crear el ArchivoDescifrado, cambiando la codificación si es
		necesario. Este método por ahora se usa sólo para descifrarTexto.
		"""
		self.utilidad.crearArchivo("tmp", textoClaro, "w")
		self.utilidad.resolverCodificacion("UTF-8", codificacion, self.utilidad.dirSalida+"tmp", nombre+extension)
		os.remove(self.utilidad.dirSalida+"tmp")
	
	def __resolverSaltoLinea(self,nombre,extension,so):
		"""
		Método que se encarga de resolver el salto de línea, cuando el archivo original era proveniente
		de un sistema Windos (LF-> CLRF). Este método por ahora se utiliza sólo para descifrarTexto.
		"""
		if so == "WINDOWS":
			direccion = self.utilidad.dirSalida+nombre+extension
			self.utilidad.resolverSaltoLinea(direccion)
	#------------------------------------------------------------------------------------------------

    #Controlador Cesar especifico
#Controlador Playfair especifico
class ControladorCesarSD(ControladorSustitucionMonoTemplate):
	"""
	Clase concreta que va a implementar el modoCifrar y modoDescifrar de la clase Template.
	"""
	def __init__(self):
		super(ControladorCesarSD, self).__init__()
		self.cesar = Cesar()
		self.utilidad = Utilidad()

	def modoCifrar(self, *argumentos):
		try:
			argumentos = list(argumentos)
			cadena = argumentos[0]	
			cantidadRellenoB64 = argumentos[1]
			clave = argumentos[2]			 
		except IndexError:
			cantidadRellenoB64 = 0

		self.cesar.cadena = cadena
		largo = len(cadena)
		#print(largo-1)
		for x in range(0, largo):			
			if(x<largo):
				self.cesar.textoCifrado= self.cesar.textoCifrado + self.cesar.cifrar(cadena[x], cantidadRellenoB64, clave) + "\n"
			else:
				self.cesar.textoCifrado= self.cesar.textoCifrado + self.cesar.cifrar(cadena[x], cantidadRellenoB64, clave)
				for p in self.cesar.cadena:
						if(p>len(self.cesar.cadena - 3)):
							if(p=='='):									
								self.cesar.textoCifrado = + '='
		return self.cesar.textoCifrado
		
	
	def modoDescifrar(self, *argumentos):
		try:
			argumentos = list(argumentos)
			cadena = argumentos[0]	
			cantidadRellenoB64 = argumentos[1]
			clave = argumentos[2]
		except IndexError:
			cantidadRellenoB64 = 0
			
		self.cesar.cadena = cadena
		largo = len(cadena)
		#print(largo)
		for x in range(0, largo):
			if(x<largo):
				self.cesar.textoClaro= self.cesar.textoClaro + self.cesar.descifrar(cadena[x], cantidadRellenoB64, clave) + "\n" 
			else:
				self.cesar.textoClaro= self.cesar.textoClaro + self.cesar.descifrar(cadena[x], cantidadRellenoB64, clave)
				for p in self.cesar.cadena:
						if(p>len(self.cesar.cadena - 3)):
							if(p=='='):									
								self.cesar.textoClaro = + '='
		return self.cesar.textoClaro

	def modoDefinicionAlfabeto(self, *argumentos):
		try:
			argumentos = list(argumentos)
			alfabeto = argumentos[0]
			#print (alfabeto)
		except IndexError:
			alfabeto = "B64"
		self.cesar.definirAlfabeto(alfabeto)


    #Controlador Playfair especifico
class ControladorPlayfairSD(ControladorSustitucionMonoTemplate):
	"""
	Clase concreta que va a implementar el modoCifrar y modoDescifrar de la clase Template.
	"""
	def __init__(self):
		super(ControladorPlayfairSD, self).__init__()
		self.playfair = Playfair()
		self.utilidad = Utilidad()

	def modoCifrar(self, *argumentos):
		try:
			argumentos = list(argumentos)	
			cadena = argumentos[0]	
			cantidadRellenoB64 = argumentos[1]
			clave = argumentos[2]			 
		except IndexError:
			cantidadRellenoB64 = 0

		self.playfair.cadena = cadena
		largo = len(cadena)
		#print(largo-1)
		for x in range(0, largo):
			if(x<largo):
				self.playfair.textoCifrado= self.playfair.textoCifrado + self.playfair.cifrar(cadena[x], cantidadRellenoB64, clave) + "\n"
			else:
				self.playfair.textoCifrado= self.playfair.textoCifrado + self.playfair.cifrar(cadena[x], cantidadRellenoB64, clave)
		return self.playfair.textoCifrado
		
	
	def modoDescifrar(self, *argumentos):
		try:
			argumentos = list(argumentos)
			#cadena_aux = argumentos[0].split(" ")
			#cadena1 = argumentos[0]
			cadena = argumentos[0]	
			cantidadRellenoB64 = argumentos[1]
			clave = argumentos[2]
		except IndexError:
			cantidadRellenoB64 = 0
		#return self.playfair.descifrar(cadena[0], cantidadRelleno, clave)
		self.playfair.cadena = cadena
		largo = len(cadena)
		#print(largo)
		for x in range(0, largo):
			#print('x:')
			#print(x)
			#print('largo:')
			#print(largo)
			if(x<largo):
				self.playfair.textoClaro= self.playfair.textoClaro + self.playfair.descifrar(cadena[x], cantidadRellenoB64, clave) + "\n" 
			else:
				self.playfair.textoClaro= self.playfair.textoClaro + self.playfair.descifrar(cadena[x], cantidadRellenoB64, clave)
		return self.playfair.textoClaro

	def modoDefinicionAlfabeto(self, *argumentos):
		try:
			argumentos = list(argumentos)
			alfabeto = argumentos[0]
		except IndexError:
			alfabeto = "B64"
		self.playfair.definirAlfabeto(alfabeto)

class ControladorPolybiosSD(ControladorSustitucionMonoTemplate):
	"""
	Clase concreta que va a implementar el modoCifrar y modoDescifrar de la clase Template.
	"""
	def __init__(self):
		super(ControladorPolybiosSD, self).__init__()
		self.polybios = Polybios()
		self.utilidad = Utilidad()

	def modoCifrar(self, *argumentos):
		try:
			argumentos = list(argumentos)
			#print (argumentos[0])	
			cadena = argumentos[0]	
			cantidadRellenoB64 = argumentos[1]
			clave = argumentos[2]			 
		except IndexError:
			cantidadRellenoB64 = 0

		self.polybios.cadena = cadena
		largo = len(cadena)
		#print(largo-1)
		for x in range(0, largo):
			if(x<largo):
				self.polybios.textoCifrado= self.polybios.textoCifrado + self.polybios.cifrar(cadena[x], cantidadRellenoB64, clave) + "\n"
			else:
				self.polybios.textoCifrado= self.polybios.textoCifrado + self.polybios.cifrar(cadena[x], cantidadRellenoB64, clave)
		return self.polybios.textoCifrado
		
	
	def modoDescifrar(self, *argumentos):
		try:
			argumentos = list(argumentos)
			#cadena_aux = argumentos[0].split(" ")
			#cadena1 = argumentos[0]
			cadena = argumentos[0]	
			cantidadRellenoB64 = argumentos[1]
			clave = argumentos[2]
		except IndexError:
			cantidadRellenoB64 = 0
		self.polybios.cadena = cadena
		#self.cesar.cifrar(cadena[0], cantidadRellenoB64, clave)
		largo = len(cadena)
		#print(largo)
		for x in range(0, largo):
			if(x<largo):
				self.polybios.textoClaro= self.polybios.textoClaro + self.polybios.descifrar(cadena[x], cantidadRellenoB64, clave) + "\n"
			else:
				self.polybios.textoClaro= self.polybios.textoClaro + self.polybios.descifrar(cadena[x], cantidadRellenoB64, clave)
		return self.polybios.textoClaro

	def modoDefinicionAlfabeto(self, *argumentos):
		try:
			argumentos = list(argumentos)
			alfabeto = argumentos[0]
			#print (alfabeto)
		except IndexError:
			alfabeto = "B64"
		self.polybios.definirAlfabeto(alfabeto)

#archivo = sys.argv[1]

#cSD = ControladorTransposicionSD()
#cSD.cifrarTexto(archivo,0)
#cSD.descifrarTexto("./salida/binario.txt.CIF",0)


#Pruebas Cesar
#cJC = ControladorCesarSD()
#cJC.definirAlfabeto("es_may")
#cJC.definirAlfabeto("B64")
#cJC.cifrarTexto(archivo, 0, 2)
#cJC.descifrarTexto("./salida/prueba.txt.CIF", 0, 2)
#cJC.cifrarArchivo(archivo, 0, 2)
#cJC.descifrarArchivo("./salida/informatica.jpg.CIF", 0, 2)
#cJC.descifrarArchivo("./salida/binarioCR.txt.CIF", 0, 2)

#Pruebas Playfair
#cPF = ControladorPlayfairSD()
#cPF.definirAlfabeto("B64")
#cPF.cifrarTexto(archivo, 0, 'VWXY')
#cPF.descifrarTexto("./salida/pruebaPF.txt.CIF", 0, 'VWXY')
#cPF.cifrarArchivo(archivo, 0, 'VWXY')
#cPF.descifrarArchivo("./salida/pruebaPF.txt.CIF", 0, 'VWXY')

#Pruebas Polybios
#cPB = ControladorPolybiosSD()
#cPB.definirAlfabeto("en_may")
#cPB.cifrarTexto(archivo, 0, 4)
#cPB.descifrarTexto("./salida/pruebaPB.txt.CIF", 0, 4)
#cPB.cifrarArchivo(archivo, 0, 'VWXY')
#cPB.descifrarArchivo("./salida/prueba.txt.CIF", 0, 'VWXY')
