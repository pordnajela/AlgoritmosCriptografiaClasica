#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import time
import threading
import os
import sys
from Utilidad import Utilidad
import base64

from Transposicion.TransposicionSimple import TransposicionSimple

class ControladorTrasposicion(object):
	"""docstring for Controlador"""
	def __init__(self):
		self.tSimple = TransposicionSimple()
		self.utilidad = Utilidad()

	def cifrarTransposicionSimpleTexto(self, archivo):
		nombre, extension, codificacion, so = self.utilidad.obtenerMetadatos(archivo)
		self.utilidad.crearArchivoMetadatos(nombre, extension, codificacion, so)

		hilo = threading.Thread(target=self.utilidad.resolverCodificacion(codificacion, "UTF-8", archivo, "tmp"))
		hilo.start()
		time.sleep(1/1000)

		with open(self.utilidad.dirSalida+"tmp", "rb") as archivoUTF:
			cadena = archivoUTF.read().decode("utf8").split("\n")
		archivoUTF.close()
		os.remove(self.utilidad.dirSalida+"tmp")


		self.tSimple.cadena = cadena
		criptograma = self.tSimple.cifrar()
		print(criptograma)
		self.utilidad.crearArchivoCifrado(nombre+extension,criptograma)

	def descifrarTransposicionSimpleTexto(self):
		pass

	def cifrarTransposicionDobleTexto(self):
		pass


c = ControladorTrasposicion()
archivo = sys.argv[1]
ini = time.time()
c.cifrarTransposicionSimpleTexto(archivo)
fin = time.time()-ini
print(fin)
