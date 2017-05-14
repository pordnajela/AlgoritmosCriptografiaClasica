#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os

from Utilidad import Utilidad
from Transposicion.TransposicionSimple import TransposicionSimple
from Transposicion.TransposicionGrupo import TransposicionGrupo
from Transposicion.TransposicionSerie import TransposicionSerie

class ControladorTransposicionTemplate(object):
	"""
	Clase "abstracta" que utiliza el patrón TemplateMethod.

	Los métodos cifrarATexto, cifrarArchivoBin, descifrarATexto, descifrarArchivoBin, son métodos que
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
	
	def cifrarATexto(self, archivo):
		"""
		Método que se encarga de cifrar un archivo de texto (archvo plano).

		Parámetros:
		archivo: Dirección del archivo plano que se desea cifrar.
		n: la cantidad de iteraciones con la que se desea cifrar el archivo plano.
		   Por ahora éste parámetro se utiliza para la Transposicion Doble.
		"""
		nombre, extension, codificacion, so = self.utilidad.obtenerMetadatos(archivo)
		self.utilidad.crearArchivoMetadatos(nombre, nombre, extension, codificacion, so)
		self.utilidad.resolverCodificacion(codificacion, "UTF-8", archivo, "tmp")

		cadena_aux = self.utilidad.leerArchivo(self.utilidad.dirSalida+"tmp","r")
		os.remove(self.utilidad.dirSalida+"tmp")
		cadena = cadena_aux.split("\n")

		criptograma = self.modoCifrar(cadena)

		self.utilidad.crearArchivo(nombre+extension+".CIF", criptograma, "w")

	def descifrarATexto(self, archivo, clave):
		"""
		Método que se encarga de descifrar un archivo de texto (archvo plano).

		Parámetros:
		archivo: Dirección del archivo plano que se desea descifrar.
		n: la cantidad de iteraciones con la que se desea descifrar el archivo plano.
		   Por ahora éste parámetro se utiliza para la Transposicion Doble.
		"""
		#metadatos = [ nombre, extension, codificación, so ]
		metadatos = self.obtenerArchivoMetadatos(archivo)
		nombre = metadatos[0]
		extension = metadatos[1]
		codificacion = metadatos[2]
		so = metadatos[3]

		cadena = self.utilidad.leerArchivo(self.utilidad.dirSalida+nombre+extension+".CIF","r").split("\n")
		textoClaro = self.modoDescifrar(cadena, clave)
		self.__crearArchivoDescifrado(textoClaro, codificacion, nombre, extension)
		self.__resolverSaltoLinea(nombre,extension,so)
	
	def cifrarArchivoBin(self, archivo):
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
			self.utilidad.crearArchivoMetadatos(nombre, nombre, extension, codificacion)
		except TypeError:
			pass
		
		cadenaB64 = self.utilidad.obtenerBase64(archivo)
		cadena = list()
		cadena.append(cadenaB64)
		criptograma = self.modoCifrar(cadena)
		self.utilidad.crearArchivo(nombre+extension+".CIF", criptograma.encode(), "wb")
		
	
	def descifrarArchivoBin(self, archivo, clave):
		"""
		Método que se encarga de descifrar un archivo con codificación binaria.

		Parámetros:
		archivo: Dirección del archivo plano que se desea descifrar.
		n: la cantidad de iteraciones con la que se desea descifrar el archivo plano.
		   Por ahora éste parámetro se utiliza para la Transposicion Doble.
		"""
		metadatos = self.obtenerArchivoMetadatos(archivo)
		nombre = metadatos[0]
		extension = metadatos[1]
		cadenaB64 = self.utilidad.leerArchivo(self.utilidad.dirSalida+nombre+extension+".CIF", "r")
		cadena = list()
		cadena.append(cadenaB64)

		textoClaro = self.modoDescifrar(cadena, clave)
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
		necesario. Este método por ahora se usa sólo para descifrarATexto.
		"""
		self.utilidad.crearArchivo("tmp", textoClaro, "w")
		self.utilidad.resolverCodificacion("UTF-8", codificacion, self.utilidad.dirSalida+"tmp", nombre+extension)
		os.remove(self.utilidad.dirSalida+"tmp")
	
	def __resolverSaltoLinea(self,nombre,extension,so):
		"""
		Método que se encarga de resolver el salto de línea, cuando el archivo original era proveniente
		de un sistema Windos (LF-> CLRF). Este método por ahora se utiliza sólo para descifrarATexto.
		"""
		if so == "WINDOWS":
			direccion = self.utilidad.dirSalida+nombre+extension
			self.utilidad.resolverSaltoLinea(direccion)
	#------------------------------------------------------------------------------------------------

class ControladorTransposicionSD(ControladorTransposicionTemplate):
	"""
	Clase concreta que va a implementar el modoCifrar y modoDescifrar de la clase Template.
	"""
	def __init__(self, n=None, archivoOriginal=None):
		super(ControladorTransposicionSD, self).__init__()
		self.tSimple = TransposicionSimple()
		self.n = n
		self.archivoOriginal = archivoOriginal
	
	def modoCifrar(self, *argumentos):
		try:
			argumentos = list(argumentos)
			cadena = argumentos[0]
		except IndexError:
			pass

		self.tSimple.cadena = cadena
		self.tSimple.cifrar()

		for x in range(0, self.n):
			self.tSimple.cadena = self.tSimple.textoCifrado.split("\n")
			self.tSimple.cifrar()

		return self.tSimple.textoCifrado
	
	def modoDescifrar(self, *argumentos):
		try:
			argumentos = list(argumentos)
			cadena = argumentos[0]
			clave = argumentos[1]
		except IndexError:
			pass

		self.n = int(clave)
		self.tSimple.cadena = cadena
		self.tSimple.descifrar()
		
		for x in range(0, self.n):
			self.tSimple.cadena = self.tSimple.textoClaro.split("\n")
			self.tSimple.descifrar()

		return self.tSimple.textoClaro

	#------------------------------------------------------------------------------------------------

class ControladorTransposicionGrupo(ControladorTransposicionTemplate):
	"""
	Clase concreta que va a implementar el modoCifrar y modoDescifrar de la clase Template.
	"""
	def __init__(self, clave=None, archivoOriginal=None):
		super(ControladorTransposicionGrupo, self).__init__()
		self.tGrupo = TransposicionGrupo(None, clave)
		self.archivoOriginal = archivoOriginal

	def modoCifrar(self, *argumentos):
		try:
			argumentos = list(argumentos)
			cadena = argumentos[0]
		except IndexError:
			pass
		'''
		nombre = ControladorTransposicionTemplate.obtenerArchivoMetadatos(self,self.archivoOriginal)[0]
		self.utilidad.crearArchivo(nombre+".mtd", str(self.tGrupo.clave)+"\n", "a")
		'''
		self.tGrupo.cadena = cadena
		self.tGrupo.cifrar()
		return self.tGrupo.textoCifrado

	def modoDescifrar(self, *argumentos):
		try:
			argumentos = list(argumentos)
			cadena = argumentos[0]
			clave = argumentos[1]
		except IndexError:
			pass

		self.tGrupo.clave = int(clave)
		self.tGrupo.cadena = cadena
		self.tGrupo.descifrar()

		cadenaDescifradaRelleno =self.tGrupo.textoClaro.split("\n")
		cadenaSinRelleno = self.tGrupo.eliminarRelleno(cadenaDescifradaRelleno)
		self.tGrupo.textoClaro = cadenaSinRelleno
		
		return self.tGrupo.textoClaro

	#------------------------------------------------------------------------------------------------

class ControladorTransposicionSerie(ControladorTransposicionTemplate):
	"""
	Clase concreta que va a implementar el modoCifrar y modoDescifrar de la clase Template.
	"""
	def __init__(self, funciones=None, archivoOriginal=None):
		super(ControladorTransposicionSerie, self).__init__()
		'''Funciones es una lista, donde cada posición es una lista de números que 
		corresponde a una función en particular. Ej: [ [1,2,3,5,7], [4,6,8], [9] ]'''
		self.tSerie = TransposicionSerie(funciones)
		self.archivoOriginal = archivoOriginal
	
	def modoCifrar(self, *argumentos):
		try:
			argumentos = list(argumentos)
			cadena = argumentos[0]
		except IndexError:
			pass

		self.tSerie.cadena = cadena
		self.tSerie.cifrar()
		
		return self.tSerie.textoCifrado

	def modoDescifrar(self, *argumentos):
		try:
			argumentos = list(argumentos)
			cadena = argumentos[0]
			clave = argumentos[1]
		except IndexError:
			pass

		self.tSerie.series = clave
		self.tSerie.cadena = cadena
		self.tSerie.descifrar()
		return self.tSerie.textoClaro