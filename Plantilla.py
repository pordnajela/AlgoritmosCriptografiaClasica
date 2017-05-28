#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os

from Utilidad import Utilidad

class Template(object):
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
		#self.alfabeto = None

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
		
	'''
	def definirAlfabeto(self, archAlfabeto):
		self.alfabeto = self.utilidad.formatearAlfabeto(archAlfabeto)
	'''
	
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