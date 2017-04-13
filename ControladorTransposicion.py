#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import time
import os
import sys
import base64

from Utilidad import Utilidad

from Transposicion.TransposicionSimple import TransposicionSimple

class ControladorTrasposicion(object):
	def __init__(self):
		self.tSimple = TransposicionSimple()
		self.utilidad = Utilidad()

	def cifrarTransposicionTexto(self, archivo, n):
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

	def descifrarTransposicionTexto(self, archivo, n):
		metadatos = self.__obtenerArchivoMetadatos(archivo)
		metadatos = metadatos.split("\n")
		nombre = metadatos[0]
		extension = metadatos[1]
		codificacion = metadatos[2]
		so = metadatos[3]

		cadena = self.utilidad.leerArchivo(self.utilidad.dirSalida+nombre+extension+".CIF","r")
		cadena = cadena.split("\n")

		self.tSimple.cadena = cadena
		self.tSimple.descifrar(so)

		for x in range(0,n):
			self.tSimple.cadena = self.tSimple.textoClaro.split("\n")
			self.tSimple.descifrar(so)

		textoClaro = self.tSimple.textoClaro
		self.__crearArchivoDescifrado(textoClaro, codificacion, nombre, extension)
		self.__resolverSaltoLinea(nombre,extension,so)

	#TO-DO
	def cifrarTransposicionArchivo(self, archivo):
		#Saltar la excepcion del tipo de variable None
		try:
			nombre, extension, codificacion, so = self.utilidad.obtenerMetadatos(archivo)
			self.utilidad.crearArchivoMetadatos(nombre, nombre, extension, codificacion, so)
		except TypeError as te:
			pass

		cadenaB64 = self.utilidad.obtenerBase64(archivo)
		cadena = list()
		cadena.append(cadenaB64)
		print(cadena)

		self.tSimple.cadena = cadena
		self.tSimple.cifrar()

		criptograma = self.tSimple.textoCifrado
		criptograma = criptograma.encode()
		self.utilidad.crearArchivo(nombre+extension+".bin", criptograma, "wb")

	def descifrarTransposicionArchivo(self):
		pass

	#Métodos privados
	def __resolverSaltoLinea(self,nombre,extension,so):
		if so == "WINDOWS":
			direccion = self.utilidad.dirSalida+nombre+extension
			self.utilidad.resolverSaltoLinea(direccion)

	def __obtenerArchivoMetadatos(self, archivo):
		#Obtener el archivo de metadatos según el nombre del archivo Cifrado
		direccion = os.path.splitext(archivo)
		nombre = direccion[0].split("/")[-1].split(".")[0]

		#Leer el archivo de metadatos -> metadatos = [nombre, extension, codificacion, so]
		metadatos = self.utilidad.leerArchivo(self.utilidad.dirSalida+nombre+".mtd", "r")
		return metadatos

	def __crearArchivoDescifrado(self, textoClaro, codificacion, nombre, extension):
		self.utilidad.crearArchivo("tmp", textoClaro, "w")
		self.utilidad.resolverCodificacion("UTF-8", codificacion, self.utilidad.dirSalida+"tmp", nombre+extension)
		os.remove(self.utilidad.dirSalida+"tmp")


c = ControladorTrasposicion()
archivo = sys.argv[1]

ini = time.time()
print("Procesando...")
c.cifrarTransposicionArchivo(archivo)
#c.cifrarTransposicionTexto(archivo,0)
#c.descifrarTransposicionTexto("./salida/a.txt.CIF",1)
fin = time.time()-ini
print(fin)
#c.descifrarTransposicionDobleTexto(archivo, 1)

#u = Utilidad()
#u.obtenerBase64(archivo)