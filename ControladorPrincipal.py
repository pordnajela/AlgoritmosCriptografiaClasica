#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys

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

	def descifrarTS(self, archivo, archivoClave):
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

	def descifrarTS(self, archivo, archivoClave):
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

n = sys.argv[1]
archivo = sys.argv[2]
cAT = ControladorATexto()
cAT.cifrarcTSD(n, archivo)
#cP = ControladorPrincipal(True)
#cP.cifrarTSD(n, archivo)
#cP.descifrarTSD("./salida/PRUEBA.txt.CIF", "./salida/PRUEBA.mtd")
#cP.cifrarcTG(n, archivo)
#cP.descifrarTG("./salida/Crepusculo.pdf.CIF", "./salida/Crepusculo.mtd")
serie = list()
serie.append("2,3,5,7,11,13,17,19,23,27".split(","))
serie.append("4,6,8,10,12,14,16,18,20,22,24,26".split(","))
serie.append("1,9,15,21,25".split(","))
#cP.cifrarcTS(serie, archivo)
#cP.descifrarTS("./salida/prueba.txt.CIF", "./salida/prueba.mtd")
"""
'''
#Contenido del archivo => Ojalaquelluevacafenelcampo
serie = list()
serie.append("2,3,5,7,11,13,17,19,23,27".split(","))
serie.append("4,6,8,10,12,14,16,18,20,22,24,26".split(","))
serie.append("1,9,15,21,25".split(","))
'''

#cS = ControladorTransposicionSerie(serie, archivo)
#cS.cifrarATexto(archivo)
#cS.descifrarATexto("./salida/prueba.txt.CIF")
#cS.cifrarArchivoBin(archivo)
#cS.descifrarArchivoBin("./salida/Crepusculo.pdf.CIF")
"""