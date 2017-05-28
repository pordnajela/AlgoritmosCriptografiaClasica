#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from Plantilla import Template
from Sustitucion_Polialfabetica.Vernam import Vernam
from Sustitucion_Polialfabetica.Vigenere import Vigenere

class ControladorVernam(Template):
	"""docstring for ClassName"""
	def __init__(self, clave=None):
		Template.__init__(self)
		self.vernam = Vernam(clave)

	def modoCifrar(self, *argumentos):
		try:
			argumentos = list(argumentos)
			cadena = argumentos[0]
		except IndexError:
			pass

		self.vernam.cadena = cadena[0]
		self.vernam.cifrar()

		return self.vernam.textoCifrado

	def modoDescifrar(self, *argumentos):
		try:
			argumentos = list(argumentos)
			cadena = argumentos[0]
			clave = argumentos[1]
		except IndexError:
			pass

		self.vernam.clave = clave
		self.vernam.cadena = cadena[0]
		self.vernam.descifrar()
		return self.vernam.textoClaro

	#------------------------------------------------------------------------------------------------

class ControladorVigenere(Template):
	"""docstring for ControladorVigenere"""
	def __init__(self, clave=None, alfabeto=None):
		Template.__init__(self)
		self.clave = clave
		self.alfabeto = alfabeto
		self.vigenere = Vigenere(clave, alfabeto)

	def modoCifrar(self, *argumentos):
		try:
			argumentos = list(argumentos)
			cadena = argumentos[0]
		except IndexError:
			pass

		self.vigenere.cadena = cadena
		self.vigenere.cifrar()
		return self.vigenere.textoCifrado

	def modoDescifrar(self, *argumentos):
		try:
			argumentos = list(argumentos)
			cadena = argumentos[0]
			clave = argumentos[1]
		except IndexError:
			pass

		self.vigenere.cadena = cadena
		self.vigenere.clave = clave
		self.vigenere.descifrar()
		return self.vigenere.textoClaro
