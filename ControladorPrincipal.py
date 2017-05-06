#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#import sys

#from Utilidad import Utilidad
from ControladorTransposicion import ControladorTransposicionSD, ControladorTransposicionSerie, ControladorTransposicionGrupo
from ControladorSustitucionMono import ControladorCesarSD, ControladorPolybiosSD, ControladorPlayfairSD


class ControladorStrategy(object):
	"""docstring for ControladorStrategy"""
	def __init__(self):
		self.CS = None
		self.PB = None
		self.PF = None
		self.cTSD = None
		self.cTG = None
		self.cTS = None

	def definirAlfabetoCesar(self, alfabeto):
		raise NotImplementedError

	def definirAlfabetoPolybios(self, alfabeto):
		raise NotImplementedError

	def definirAlfabetoPlayfair(self, alfabeto):
		raise NotImplementedError

	def cifrarCS(self, archivo, relleno, clave):
		raise NotImplementedError

	def cifrarPB(self, archivo, relleno, clave):
		raise NotImplementedError

	def cifrarPF(self, archivo, relleno, clave):
		raise NotImplementedError


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


	def descifrarCS(self, archivo, relleno, clave):
		raise NotImplementedError

	def descifrarPB(self, archivo, relleno, clave):
		raise NotImplementedError

	def descifrarPF(self, archivo, relleno, clave):
		raise NotImplementedError

class ControladorATexto(ControladorStrategy):
	"""docstring for ControladorATexto"""
	def __init__(self):
		super(ControladorATexto, self).__init__()

	def definirAlfabetoCesar(self, alfabeto):
		self.CS = ControladorCesarSD()
		self.CS.definirAlfabeto(alfabeto)

	def definirAlfabetoPolybios(self, alfabeto):
		self.PB = ControladorPolybiosSD()
		self.PB.definirAlfabeto(alfabeto)

	def definirAlfabetoPlayfair(self, alfabeto):
		self.PF = ControladorPlayfairSD()
		self.PF.definirAlfabeto(alfabeto)


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


	def cifrarCS(self, archivo, relleno, clave):
		self.CS = ControladorCesarSD()
		self.CS.cifrarTexto(archivo, relleno, clave)

	def cifrarPB(self, archivo, relleno, clave):
		self.PB = ControladorPolybiosSD()
		self.PB.cifrarTexto(archivo, relleno, clave)

	def cifrarPF(self, archivo, relleno, clave):
		self.PF = ControladorPlayfairSD()
		self.PF.cifrarTexto(archivo, relleno, clave)


	def descifrarCS(self, archivo, relleno, clave):
		self.CS = ControladorCesarSD()
		self.CS.descifrarTexto(archivo, relleno, clave)

	def descifrarPB(self, archivo, relleno, clave):
		self.PB = ControladorPolybiosSD()
		self.PB.descifrarTexto(archivo, relleno, clave)

	def descifrarPF(self, archivo, relleno, clave):
		self.PF = ControladorPlayfairSD()		
		self.PF.descifrarTexto(archivo, relleno, clave)

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

#n = sys.argv[1]
#archivo = sys.argv[2]
#archivo = sys.argv[1]

#cAT = ControladorABin()
#cAT = ControladorATexto()
#cAT.cifrarcTSD(n, archivo)
#cAT.descifrarcTSD("./salida/prueba.ppt.CIF", "./salida/prueba.mtd")

#cAT.cifrarcTG(int(n), archivo)
#cAT.descifrarcTG("./salida/prueba.ppt.CIF", "./salida/prueba.mtd")

#serie = establecerSeries(n)
#cAT.cifrarcTS(serie, archivo)
#cAT.descifrarcTS("./salida/prueba.txt.CIF", "./salida/prueba.mtd")

#cP.cifrarcTS(serie, archivo)
#cP.descifrarTS("./salida/prueba.txt.CIF", "./salida/prueba.mtd")

#Pruebas Cesar Polybios Playfair
#cAT.definirAlfabetoCesar("es_may")
#cAT.cifrarCS(archivo, 0, 2)
#cAT.descifrarCS("./salida/prueba.txt.CIF", 0,  2)
#cAT.definirAlfabetoPolybios("en_may")
#cAT.cifrarPB(archivo, 0, "vvv")
#cAT.descifrarPB("./salida/pruebaPB.txt.CIF", 0, "vvv")
#cAT.definirAlfabetoPolybios("en_may")
#cAT.cifrarTexto(archivo, 0, 4)
#cAT.descifrarTexto("./salida/pruebaPB.txt.CIF", 0, 4)
#cAT.definirAlfabetoPlayfair("es_may")
#cAT.cifrarPF(archivo, 0, "VWX")
#cAT.descifrarPF("./salida/pruebaPF.txt.CIF", 0, "VWX")


#pruebas Cesar Polybios Playfair
#cAT.cifrarCS(archivo, 0, 2)
#cAT.descifrarCS("./salida/prueba.txt.CIF", 0, 2)