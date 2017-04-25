#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import sys


from Utilidad import Utilidad
from Transposicion.TransposicionSimple import TransposicionSimple
from Transposicion.TransposicionGrupo import TransposicionGrupo

class ControladorTransposicionTemplate(object):
	"""
	Clase "abstracta" que utiliza el patrón TemplateMethod.

	Los métodos cifrarTexto, cifrarArchivo, descifrarTexto, descifrarArchivo, son métodos que
	tienen pasos en común, lo único que cambia es el modo en que se va a cifrar los diferentes
	algoritmos de Transposicion.

	Los métodos modoCifrar y modoDescifrar, son los métodos que van a cambiar según el algoritmo
	a utilzar, estos se definen en las clases concretas.

	"""
	def modoCifrar(self, *argumentos):
		raise NotImplementedError
	
	def modoDescifrar(self, *argumentos):
		raise NotImplementedError
	
	def cifrarTexto(self, archivo, n=None):
		"""
		Método que se encarga de cifrar un archivo de texto (archvo plano).

		Parámetros:
		archivo: archivo plano que se desea cifrar.
		n: la cantidad de iteraciones con la que se desea cifrar el archivo plano.
		   Por ahora éste parámetro se utiliza para la Transposicion Doble.
		"""
		nombre, extension, codificacion, so = self.utilidad.obtenerMetadatos(archivo)

		self.utilidad.crearArchivoMetadatos(nombre, nombre, extension, codificacion, so)
		self.utilidad.resolverCodificacion(codificacion, "UTF-8", archivo, "tmp")

		cadena = self.utilidad.leerArchivo(self.utilidad.dirSalida+"tmp","r")
		os.remove(self.utilidad.dirSalida+"tmp")
		cadena = cadena.split("\n")

		criptograma = self.modoCifrar(cadena, n)

		self.utilidad.crearArchivo(nombre+extension+".CIF", criptograma, "w")

	def descifrarTexto(self, archivo, n=None):
		"""
		Método que se encarga de descifrar un archivo de texto (archvo plano).

		Parámetros:
		archivo: archivo plano que se desea descifrar.
		n: la cantidad de iteraciones con la que se desea descifrar el archivo plano.
		   Por ahora éste parámetro se utiliza para la Transposicion Doble.
		"""
		metadatos = self.__obtenerArchivoMetadatos(archivo)
		metadatos = metadatos.split("\n")
		nombre = metadatos[0]
		extension = metadatos[1]
		codificacion = metadatos[2]
		so = metadatos[3]

		cadena = self.utilidad.leerArchivo(self.utilidad.dirSalida+nombre+extension+".CIF","r")
		cadena = cadena.split("\n")

		textoClaro = self.modoDescifrar(cadena, n)
		self.__crearArchivoDescifrado(textoClaro, codificacion, nombre, extension)
		self.__resolverSaltoLinea(nombre,extension,so)
	
	def cifrarArchivo(self, archivo, n=None):
		"""
		Método que se encarga de cifrar un archivo con codificación binaria.

		Parámetros:
		archivo: archivo plano que se desea descifrar.
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
		cantidadRellenoB64 = len(cadenaB64)-cadenaB64.index("=")
		cadena = list()
		cadena.append(cadenaB64)

		criptograma = self.modoCifrar(cadena, n, cantidadRellenoB64)
		criptograma = self.utilidad.cadena_a_Base64(criptograma)
		self.utilidad.crearArchivo(nombre+extension+".CIF", criptograma, "wb")
	
	def descifrarArchivo(self, archivo, n=None):
		"""
		Método que se encarga de descifrar un archivo con codificación binaria.

		Parámetros:
		archivo: archivo plano que se desea descifrar.
		n: la cantidad de iteraciones con la que se desea descifrar el archivo plano.
		   Por ahora éste parámetro se utiliza para la Transposicion Doble.
		"""
		try:
			metadatos = self.__obtenerArchivoMetadatos(archivo)
			metadatos = metadatos.split("\n")
			nombre = metadatos[0]
			extension = metadatos[1]
			#codificacion = metadatos[2]
		except TypeError as te:
			print(te , " descifrarArchivoTemplate")
			#codificacion = None

		cadenaB64 = self.utilidad.obtenerBase64(self.utilidad.dirSalida+nombre+extension+".CIF")
		cantidadRellenoB64 = len(cadenaB64)-cadenaB64.index("=")
		cadena = list()
		cadena.append(cadenaB64)

		textoClaro = self.modoDescifrar(cadena, n, cantidadRellenoB64)
		textoClaro = self.utilidad.cadena_a_Base64(textoClaro)

		self.utilidad.crearArchivo(nombre+extension, textoClaro, "wb")
	
	#-----------------------------------------------------------------------------Métodos privados
	def __obtenerArchivoMetadatos(self, archivo):
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
		return metadatos
	
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

class ControladorTransposicionSD(ControladorTransposicionTemplate):
	"""
	Clase concreta que va a implementar el modoCifrar y modoDescifrar de la clase Template.
	"""
	def __init__(self):
		self.tSimple = TransposicionSimple()
		self.utilidad = Utilidad()
	
	def modoCifrar(self, *argumentos):
		try:
			argumentos = list(argumentos)
			cadena = argumentos[0]
			n = argumentos[1]
			cantidadRellenoB64 = argumentos[2]
		except IndexError:
			cantidadRellenoB64 = 0

		self.tSimple.cadena = cadena
		self.tSimple.cifrar(cantidadRellenoB64)

		for x in range(0,n):
			self.tSimple.cadena = self.tSimple.textoCifrado.split("\n")
			self.tSimple.cifrar(cantidadRellenoB64)

		return self.tSimple.textoCifrado
	
	def modoDescifrar(self, *argumentos):
		try:
			argumentos = list(argumentos)
			cadena = argumentos[0]
			n = argumentos[1]
			cantidadRellenoB64 = argumentos[2]
		except IndexError:
			cantidadRellenoB64 = 0

		self.tSimple.cadena = cadena
		self.tSimple.descifrar(cantidadRellenoB64)

		for x in range(0,n):
			self.tSimple.cadena = self.tSimple.textoClaro.split("\n")
			self.tSimple.descifrar()

		return self.tSimple.textoClaro

class ControladorTransposicionGrupo(ControladorTransposicionTemplate):
	"""
	Clase concreta que va a implementar el modoCifrar y modoDescifrar de la clase Template.
	"""
	def __init__(self, clave):
		self.utilidad = Utilidad()
		self.tGrupo = TransposicionGrupo(None, clave)

	def modoCifrar(self, *argumentos):
		try:
			argumentos = list(argumentos)
			cadena = argumentos[0]
			cantidadRellenoB64 = argumentos[2]
		except IndexError:
			cantidadRellenoB64 = 0

		if cantidadRellenoB64 != 0:
			cadena2 = cadena[0]
			j = cadena2.index("=")
			cadena2 = cadena2[:j]
			while (len(cadena2) % len(str(self.tGrupo.clave)) != 0):
				cadena2 += "A"
			cadena.append(cadena2)
			del cadena[:]
			cadena.append(cadena2)
			print(cadena)
		
		self.tGrupo.cadena = cadena
		print(self.tGrupo.cadena)
		self.tGrupo.cifrar(cantidadRellenoB64)
		return self.tGrupo.textoCifrado

	def modoDescifrar(self, *argumentos):
		try:
			argumentos = list(argumentos)
			cadena = argumentos[0]
			cantidadRellenoB64 = argumentos[2]
		except IndexError:
			cantidadRellenoB64 = 0
		
		self.tGrupo.cadena = cadena
		self.tGrupo.descifrar(cantidadRellenoB64)
		return self.tGrupo.textoClaro

class ControladorTransposicionSerie(ControladorTransposicionTemplate):
	"""
	Clase concreta que va a implementar el modoCifrar y modoDescifrar de la clase Template.
	"""
	def __init__(self, arg):
		self.utilidad = Utilidad()
	
	def modoCifrar(self, *argumentos):
		pass

	def modoDescifrar(self, *argumentos):
		pass

archivo = sys.argv[1]
cSD = ControladorTransposicionSD()
#cSD.cifrarTexto(archivo,0)
#cSD.descifrarTexto("./salida/PRUEBA.txt.CIF",0)
cSD.cifrarArchivo(archivo,0)
cSD.descifrarArchivo("./salida/Crepusculo.pdf.CIF",0)
cG = ControladorTransposicionGrupo(43521)
#cG.cifrarTexto(archivo)
#cG.descifrarTexto("./salida/PRUEBA.txt.CIF")
#cG.cifrarArchivo(archivo)