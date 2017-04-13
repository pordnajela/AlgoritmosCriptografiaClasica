#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from itertools import zip_longest

class TransposicionSimple(object):
	def __init__(self, cadena=None):
		self.cadena = cadena
		self.bloque1 = list()
		self.bloque2 = list()
		self.textoCifrado = ""
		self.textoClaro = ""

	def cifrar(self):
		textoCifrado = ""
		saltosLinea = len(self.cadena)-1
		i = 0
		for linea in self.cadena:
			if i < saltosLinea:
				textoCifrado = textoCifrado + self.__cifrarTexto(linea) + "\n"
				i += 1
			else:
				textoCifrado = textoCifrado + self.__cifrarTexto(linea)
		self.textoCifrado = textoCifrado

	def descifrar(self, so):
		textoDescifrado = ""
		saltosLinea = len(self.cadena)-1
		i = 0
		for linea in self.cadena:
			if i < saltosLinea:
				textoDescifrado = textoDescifrado + self.__descifrarTexto(linea) + "\n"
				i += 1
			else:
				textoDescifrado = textoDescifrado + self.__descifrarTexto(linea)
		self.textoClaro = textoDescifrado

	#Métodos privados

	def __cifrarTexto(self,linea):
		i = 0
		longitudCadena = len(linea)
		while i < longitudCadena:
			if i%2 == 0:
				self.bloque1.append(linea[i])
			else:
				self.bloque2.append(linea[i])
			i += 1
		textoBloque1 = ''.join(self.bloque1)
		textoBloque2 = ''.join(self.bloque2)
		textoCifrado = textoBloque1+textoBloque2

		self.__vaciarLista(self.bloque1)
		self.__vaciarLista(self.bloque2)
		return textoCifrado

	def __descifrarTexto(self,linea):
		i = 0
		longitudCadena = len(linea)
		mitad = longitudCadena/2

		#Llenar los bloques con sus mitades
		while i < mitad:
			self.bloque1.append(linea[i])
			i += 1
		while i < longitudCadena:
			self.bloque2.append(linea[i])
			i += 1

		#Intercalar caracteres
		textoClaro = []
		i = 0
		for a,b in zip_longest(self.bloque1, self.bloque2):
			if a == None:
				textoClaro.append('')
			else:
				textoClaro.append(a)
			if b == None:
				textoClaro.append('')
			else:
				textoClaro.append(b)
		self.__vaciarLista(self.bloque1)
		self.__vaciarLista(self.bloque2)
		return ''.join(textoClaro)

	def __vaciarLista(self,lista):
		del lista[:]
