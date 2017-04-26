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
	def __init__(self):
	    self.utilidad = Utilidad()

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

		cadena_aux = self.utilidad.leerArchivo(self.utilidad.dirSalida+"tmp","r")
		os.remove(self.utilidad.dirSalida+"tmp")
		cadena = cadena_aux.split("\n")

		criptograma = self.modoCifrar(cadena, n)

		self.utilidad.crearArchivo(nombre+extension+".CIF", criptograma, "w")

		cantidadRelleno = len(criptograma) - len(cadena_aux)
		if cantidadRelleno > 0:
			self.utilidad.crearArchivo(nombre+".mtd", str(cantidadRelleno), "a")

	def descifrarTexto(self, archivo, n=None):
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
		cadena = list()
		cadena.append(cadenaB64)
		criptograma = self.modoCifrar(cadena, n, 0)
		self.utilidad.crearArchivo(nombre+extension+".CIF", criptograma.encode(), "wb")

		cantidadRelleno = len(criptograma) - len(cadenaB64)
		if cantidadRelleno > 0:
			self.utilidad.crearArchivo(nombre+".mtd", str(cantidadRelleno), "a")
	
	def descifrarArchivo(self, archivo, n=None):
		"""
		Método que se encarga de descifrar un archivo con codificación binaria.

		Parámetros:
		archivo: archivo plano que se desea descifrar.
		n: la cantidad de iteraciones con la que se desea descifrar el archivo plano.
		   Por ahora éste parámetro se utiliza para la Transposicion Doble.
		"""
		try:
			metadatos = self.obtenerArchivoMetadatos(archivo)
			nombre = metadatos[0]
			extension = metadatos[1]
		except TypeError as te:
			print(te , " descifrarArchivo -- Template")

		cadenaB64 = self.utilidad.leerArchivo(self.utilidad.dirSalida+nombre+extension+".CIF", "r")
		cadena = list()
		cadena.append(cadenaB64)

		textoClaro = self.modoDescifrar(cadena, n, 0)
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

class ControladorTransposicionSD(ControladorTransposicionTemplate):
	"""
	Clase concreta que va a implementar el modoCifrar y modoDescifrar de la clase Template.
	"""
	def __init__(self):
	    super(ControladorTransposicionSD, self).__init__()
	    self.tSimple = TransposicionSimple()
	
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

	#------------------------------------------------------------------------------------------------

class ControladorTransposicionGrupo(ControladorTransposicionTemplate):
	"""
	Clase concreta que va a implementar el modoCifrar y modoDescifrar de la clase Template.
	"""
	def __init__(self, clave, archivoOriginal):
		super(ControladorTransposicionGrupo, self).__init__()
		self.tGrupo = TransposicionGrupo(None, clave, archivoOriginal)

	def modoCifrar(self, *argumentos):
		try:
			argumentos = list(argumentos)
			cadena = argumentos[0]
		except IndexError:
			pass

		self.tGrupo.cadena = cadena
		self.tGrupo.cifrar()	
		return self.tGrupo.textoCifrado

	def modoDescifrar(self, *argumentos):
		try:
			argumentos = list(argumentos)
			cadena = argumentos[0]
		except IndexError:
			pass

		nombre = ControladorTransposicionTemplate.obtenerArchivoMetadatos(self,self.tGrupo.archivoOriginal)[0]
		relleno = self.utilidad.leerArchivo(self.utilidad.dirSalida+nombre+".mtd", "r").split("\n")[-1]
		codificacion = self.utilidad.leerArchivo(self.utilidad.dirSalida+nombre+".mtd", "r").split("\n")[2]

		self.tGrupo.cadena = cadena
		self.tGrupo.descifrar()

		cadena = self.tGrupo.textoClaro
		if self.utilidad.esTxt(codificacion):
			limite = ( len(cadena)-int(relleno) ) -1
		else:
			limite = ( len(cadena)-int(relleno) )

		cadena = cadena[:limite]+"\n"
		self.tGrupo.textoClaro = cadena

		return self.tGrupo.textoClaro

	#------------------------------------------------------------------------------------------------

class ControladorTransposicionSerie(ControladorTransposicionTemplate):
	"""
	Clase concreta que va a implementar el modoCifrar y modoDescifrar de la clase Template.
	"""
	def __init__(self, arg):
		super(ControladorTransposicionSD, self).__init__()
	
	def modoCifrar(self, *argumentos):
		pass

	def modoDescifrar(self, *argumentos):
		pass

archivo = sys.argv[1]
cSD = ControladorTransposicionSD()
#cSD.cifrarTexto(archivo,0)
#cSD.descifrarTexto("./salida/PRUEBA.txt.CIF",0)
#cSD.cifrarArchivo(archivo,0)
#cSD.descifrarArchivo("./salida/Crepusculo.pdf.CIF",0)
cG = ControladorTransposicionGrupo(43521, archivo)
#cG.cifrarTexto(archivo)
#cG.descifrarTexto("./salida/PRUEBA.txt.CIF")
#cG.cifrarArchivo(archivo)
#cG.descifrarArchivo("./salida/Crepusculo.pdf.CIF")
cS = ControladorTransposicionSerie()
