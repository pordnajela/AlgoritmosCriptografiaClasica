#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import time
import os
import sys

from Utilidad import Utilidad
from Transposicion.TransposicionSimple import TransposicionSimple

class ControladorTrasposicionSD(object):
	def __init__(self):
		self.tSimple = TransposicionSimple()
		self.utilidad = Utilidad()

	def cifrarTransposicionSDTexto(self, archivo, n):
		nombre, extension, codificacion, so = self.utilidad.obtenerMetadatos(archivo)

		self.utilidad.crearArchivoMetadatos(nombre, nombre, extension, codificacion, so)
		self.utilidad.resolverCodificacion(codificacion, "UTF-8", archivo, "tmp")

		cadena = self.utilidad.leerArchivo(self.utilidad.dirSalida+"tmp","r")
		os.remove(self.utilidad.dirSalida+"tmp")
		
		cadena = cadena.split("\n")
		self.tSimple.cadena = cadena
		self.tSimple.cifrar()

		for x in range(0,n):
			self.tSimple.cadena = self.tSimple.textoCifrado.split("\n")
			self.tSimple.cifrar()
		
		criptograma = self.tSimple.textoCifrado
		self.utilidad.crearArchivo(nombre+extension+".CIF", criptograma, "w")

	def descifrarTransposicionSDTexto(self, archivo, n):
		metadatos = self.__obtenerArchivoMetadatos(archivo)
		metadatos = metadatos.split("\n")
		nombre = metadatos[0]
		extension = metadatos[1]
		codificacion = metadatos[2]
		so = metadatos[3]

		cadena = self.utilidad.leerArchivo(self.utilidad.dirSalida+nombre+extension+".CIF","r")
		cadena = cadena.split("\n")

		self.tSimple.cadena = cadena
		self.tSimple.descifrar()

		for x in range(0,n):
			self.tSimple.cadena = self.tSimple.textoClaro.split("\n")
			self.tSimple.descifrar()

		textoClaro = self.tSimple.textoClaro
		self.__crearArchivoDescifrado(textoClaro, codificacion, nombre, extension)
		self.__resolverSaltoLinea(nombre,extension,so)

	def cifrarTransposicionSDArchivo(self, archivo, n):
		#Saltar la excepcion del tipo de variable None
		try:
			nombre, extension, codificacion, so = self.utilidad.obtenerMetadatos(archivo)
			self.utilidad.crearArchivoMetadatos(nombre, nombre, extension, codificacion, so)
		except TypeError as te:
			pass

		cadenaB64 = self.utilidad.obtenerBase64(archivo)
		cadena = list()
		cadena.append(cadenaB64)
		
		self.tSimple.cadena = cadena
		self.tSimple.cifrar()

		for x in range(0,n):
			self.tSimple.cadena = self.tSimple.textoCifrado
			self.tSimple.cifrar()

		criptograma = self.tSimple.textoCifrado
		criptograma = self.utilidad.cadena_a_Base64(criptograma)

		self.utilidad.crearArchivo(nombre+extension+".CIF", criptograma, "wb")

	def descifrarTransposicionSDArchivo(self, archivo, n):
		try:
			metadatos = self.__obtenerArchivoMetadatos(archivo)
			metadatos = metadatos.split("\n")
			nombre = metadatos[0]
			extension = metadatos[1]
			codificacion = metadatos[2]
		except TypeError as te:
			pass

		cadenaB64 = self.utilidad.obtenerBase64(self.utilidad.dirSalida+nombre+extension+".CIF")
		cadena = list()
		cadena.append(cadenaB64)

		self.tSimple.cadena = cadena
		self.tSimple.descifrar()

		for x in range(0,n):
			self.tSimple.cadena = self.tSimple.textoClaro
			self.tSimple.descifrar()

		textoClaro = self.tSimple.textoClaro
		textoClaro = self.utilidad.cadena_a_Base64(textoClaro)

		self.utilidad.crearArchivo(nombre+extension, textoClaro, "wb")

	#--------------------------------------------------------------------------------Métodos privados
	def __resolverSaltoLinea(self,nombre,extension,so):
		if so == "WINDOWS":
			direccion = self.utilidad.dirSalida+nombre+extension
			self.utilidad.resolverSaltoLinea(direccion)

	def __obtenerArchivoMetadatos(self, archivo):
		#Obtener el archivo de metadatos según el nombre del archivo Cifrado
		direccion = os.path.splitext(archivo)
		nombre = direccion[0].split("/")[-1]
		nombre = os.path.splitext(nombre)[0]

		#Leer el archivo de metadatos -> metadatos = [nombre, extension, codificacion, so]
		metadatos = self.utilidad.leerArchivo(self.utilidad.dirSalida+nombre+".mtd", "r")
		return metadatos

	def __crearArchivoDescifrado(self, textoClaro, codificacion, nombre, extension):
		self.utilidad.crearArchivo("tmp", textoClaro, "w")
		self.utilidad.resolverCodificacion("UTF-8", codificacion, self.utilidad.dirSalida+"tmp", nombre+extension)
		os.remove(self.utilidad.dirSalida+"tmp")

class ControladorTrasposicionBloque(object):
	def __init__(self):
		self.utilidad = Utilidad()
	
		

c = ControladorTrasposicionSD()
archivo = sys.argv[1]

ini = time.time()
print("Procesando...")
print(a)
#c.cifrarTransposicionTexto(archivo,0)
#c.cifrarTransposicionTexto(archivo,0)
#c.descifrarTransposicionTexto("./salida/a.txt.CIF",1)
fin = time.time()-ini
print(fin)
#c.descifrarTransposicionArchivo("./salida/PropuestaProyecto-Version-1.2.odt.CIF",0)
#c.descifrarTransposicionDobleTexto(archivo, 1)

#u = Utilidad()
#u.obtenerBase64(archivo)