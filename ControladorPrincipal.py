#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys

from Utilidad import Utilidad
from ControladorTransposicion import ControladorTransposicionSD, ControladorTransposicionSerie, ControladorTransposicionGrupo

class ControladorStrategy(object):
	"""docstring for ControladorStrategy"""
	def __init__(self):
		self.cTSD = None
		self.cTG = None
		self.cTS = None

	def cifrarcTSD(self, n, archivo):
		raise NotImplementedError

	def cifrarcTG(self, clave, archivo):
		raise NotImplementedError

	def cifrarcTS(self, series, archivo):
		raise NotImplementedError

	def descifrarcTSD(self, archivo, archivoClave):
		raise NotImplementedError

	def descifrarcTG(self, archivo, archivoClave):
		raise NotImplementedError

	def descifrarTS(self, archivo, archivoClave):
		raise NotImplementedError

class ControladorATexto(ControladorStrategy):
	"""docstring for ControladorATexto"""
	def __init__(self):
		super(ControladorATexto, self).__init__()

	def cifrarcTSD(self, n, archivo):
		self.cTSD = ControladorTransposicionSD(int(n), archivo)
		self.cTSD.cifrarATexto(self.cTSD.archivoOriginal)

	def cifrarcTG(self, clave, archivo):
		self.cTG = ControladorTransposicionGrupo(int(clave), archivo)
		self.cTG.cifrarATexto(self.cTG.archivoOriginal)

	def cifrarcTS(self, series, archivo):
		self.cTS = ControladorTransposicionSerie(series, archivo)
		#Mirar la longitud de las funciones
		self.cTS.cifrarATexto(archivo)

	def descifrarcTSD(self, archivo, archivoClave):
		self.cTSD = ControladorTransposicionSD(None, archivo)
		self.cTSD.descifrarATexto(archivo, archivoClave)

	def descifrarcTG(self, archivo, archivoClave):
		self.cTG = ControladorTransposicionGrupo(None, archivo)
		self.cTG.descifrarATexto(archivo, archivoClave)

	def descifrarcTS(self, archivo, archivoClave):
		self.cTS = ControladorTransposicionSerie(None, archivo)
		#Mirar la longitud de las funciones
		self.cTS.descifrarATexto(archivo, archivoClave)

class ControladorABin(ControladorStrategy):
	"""docstring for ControladorABin"""
	def __init__(self):
		super(ControladorABin, self).__init__()

	def cifrarcTSD(self, n, archivo):
		self.cTSD = ControladorTransposicionSD(int(n), archivo)
		self.cTSD.cifrarArchivoBin(self.cTSD.archivoOriginal)

	def cifrarcTG(self, clave, archivo):
		self.cTG = ControladorTransposicionGrupo(int(clave), archivo)
		self.cTG.cifrarArchivoBin(self.cTG.archivoOriginal)

	def cifrarcTS(self, series, archivo):
		self.cTS = ControladorTransposicionSerie(series, archivo)
		#Mirar la longitud de las funciones
		self.cTS.cifrarArchivoBin(self.cTS.archivoOriginal)

	def descifrarcTSD(self, archivo, archivoClave):
		self.cTSD = ControladorTransposicionSD(None, archivo)
		self.cTSD.descifrarArchivoBin(archivo, archivoClave)

	def descifrarcTG(self, archivo, archivoClave):
		self.cTG = ControladorTransposicionGrupo(None, archivo)
		self.cTG.descifrarArchivoBin(archivo, archivoClave)

	def descifrarcTS(self, archivo, archivoClave):
		self.cTS = ControladorTransposicionSerie(None, archivo)
		#Mirar la longitud de las funciones
		self.cTS.descifrarArchivoBin(archivo)
		
'''
	def generarFunciones(self, archivo):
		cadenaB64 = self.cTS.utilidad.obtenerBase64(archivo)
		longitud = len(cadenaB64)
		s1 = list()
		s2 = list()
		i = 1

		while i <= longitud:
			if i % 2 == 0:
				s1.append(str(i))
			elif i % 2 != 0:
				s2.append(str(i))
			i += 1
		return s1, s2
	'''

def establecerSeries(archivo):
	utilidad = Utilidad()
	series = utilidad.leerArchivo(archivo, "r").split("\n")
	serie = list()
	funcion = list()
	for i in series:
		funcion = i.split(",")
		serie.append(funcion)
	return serie

n = sys.argv[1]
archivo = sys.argv[2]
#archivo = sys.argv[1]
serie = list()

#cAT = ControladorABin()
cAT = ControladorATexto()
#cAT.cifrarcTSD(n, archivo)
#cAT.descifrarcTSD("./salida/PRUEBA.txt.CIF", "./salida/PRUEBA.mtd")

cAT.cifrarcTG(int(n), archivo)
cAT.descifrarcTG("./salida/PRUEBA.txt.CIF", "./salida/PRUEBA.mtd")
#cAT.cifrarcTS(serie, archivo)
#cAT.descifrarcTS("./salida/prueba.txt.CIF", "./salida/prueba.mtd")
#cP.cifrarcTS(serie, archivo)
#cP.descifrarTS("./salida/prueba.txt.CIF", "./salida/prueba.mtd")