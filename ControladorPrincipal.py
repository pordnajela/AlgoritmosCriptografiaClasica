#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys

from ControladorTransposicion import ControladorTransposicionSD, ControladorTransposicionSerie, ControladorTransposicionGrupo

class ControladorPrincipal(object):
	"""docstring for ControladorPrincipal"""
	def __init__(self):
		self.cTSD = ControladorTransposicionSD()
		self.cTS = ControladorTransposicionSerie()
		self.cTG = ControladorTransposicionGrupo ()

	def cifrarTSD(self, n, archivo):
		self.cTSD.n = int(n)
		self.cTSD.archivoOriginal = archivo

		self.cTSD.cifrarTexto(self.cTSD.archivoOriginal)

	def descifrarTSD(self, archivoClave):
		self.cTSD.n = int(n)
		self.cTSD.archivoOriginal = archivo

		self.cTSD.descifrarTexto(archivoClave)

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
cP = ControladorPrincipal()
cP.cifrarTSD(n, archivo)
cP.descifrarTSD("./salida/PRUEBA.txt.CIF")
"""
archivo = sys.argv[1]
cSD = ControladorTransposicionSD(5)
#cSD.cifrarTexto(archivo)
#cSD.descifrarTexto("./salida/PRUEBA.txt.CIF")
#cSD.cifrarArchivo(archivo)
#cSD.descifrarArchivo("./salida/Crepusculo.pdf.CIF")
cG = ControladorTransposicionGrupo(43521, archivo)
#cG.cifrarTexto(archivo)
#cG.descifrarTexto("./salida/PRUEBA.txt.CIF")
#cG.cifrarArchivo(archivo)
#cG.descifrarArchivo("./salida/Crepusculo.pdf.CIF")

'''
#Contenido del archivo => Ojalaquelluevacafenelcampo
serie = list()
serie.append("2,3,5,7,11,13,17,19,23,27".split(","))
serie.append("4,6,8,10,12,14,16,18,20,22,24,26".split(","))
serie.append("1,9,15,21,25".split(","))
'''

#cS = ControladorTransposicionSerie(serie, archivo)
#cS.cifrarTexto(archivo)
#cS.descifrarTexto("./salida/prueba.txt.CIF")
#cS.cifrarArchivo(archivo)
#cS.descifrarArchivo("./salida/Crepusculo.pdf.CIF")
"""