#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#llave='ABCDEFGHIKLMNOPQRSTUVWXYZ'
#llave = [k.upper() for k in llave]

import copy

class Playfair(object):
	def __init__(self):
		self.cadena = ""
		self.alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		self.alfabeto_en_may = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		self.alfabeto = [k.upper() for k in self.alfabeto]
		self.textoCifrado = ""
		self.textoClaro = ""          

	def definirAlfabeto(self, alfabeto):
		if(alfabeto== "es_min"):
			self.alfabeto = copy.copy(self.alfabeto_es_min)
		if(alfabeto== "en_may"):
			self.alfabeto = copy.copy(self.alfabeto_en_may)
		if(alfabeto== "en_min"):
			self.alfabeto = copy.copy(self.alfabeto_en_min)
		if(alfabeto== "b64"):
			self.alfabeto = copy.copy(self.alfabeto_base64)
		self.alfabeto = [k.upper() for k in self.alfabeto]

	
	def __cifrar_pareja(self, a, b):
		if a == b:
			b = 'X'
		afila, acolumna = int(self.alfabeto.index(a) / 5), self.alfabeto.index(a) % 5
		bfila, bcolumna = int(self.alfabeto.index(b) / 5), self.alfabeto.index(b) % 5
		if afila == bfila:
			return self.alfabeto[afila * 5 + (acolumna + 1) % 5] + self.alfabeto[bfila * 5 + (bcolumna + 1) % 5]
		elif acolumna == bcolumna:
			return self.alfabeto[((afila + 1) % 5) * 5 + acolumna] + self.alfabeto[((bfila + 1) % 5) * 5 + bcolumna]
		else:
			return self.alfabeto[afila * 5 + bcolumna] + self.alfabeto[bfila * 5 + acolumna]
		
	def __descifrar_pareja(self, a, b):
		assert a != b, 'two of the same letters occurred together, illegal in playfair'
		afila, acolumna = int(self.alfabeto.index(a) / 5), self.alfabeto.index(a) % 5
		bfila, bcolumna = int(self.alfabeto.index(b) / 5), self.alfabeto.index(b) % 5
		if afila == bfila:
			return self.alfabeto[afila * 5 + (acolumna - 1) % 5] + self.alfabeto[bfila * 5 + (bcolumna - 1) % 5]
		elif acolumna == bcolumna:
			return self.alfabeto[((afila - 1) % 5) * 5 + acolumna] + self.alfabeto[((bfila - 1) % 5) * 5 + bcolumna]
		else:
			return self.alfabeto[afila * 5 + bcolumna] + self.alfabeto[bfila * 5 + acolumna]

	def cifrar(self, string, relleno, clave):
		self.cadena = string
		if len(string) % 2 == 1:
			string += 'X' #"""Caracter de relleno X"""
		ret = ''
		for cont in range(0, len(string), 2):
			ret += self.__cifrar_pareja(string[cont], string[cont+1])
		self.textoCifrado = ret
		return ret    

	def descifrar(self, string, relleno, clave):
		"""Se deebn ingresar caracteres validos dentro del alfabeto, si no es asi los
		caracteres que no son validos seran rellenados con un X
		Example::
		plaintext = Playfair(key='zgptfoihmuwdrcnykeqaxvsbl').decipher(ciphertext)     
		:param string: The string to decipher.
		:returns: The deciphered string.
		"""    
		#string = self.remove_punctuation(string) 
		self.cadena = string 
		if len(string) % 2 == 1:
			string += 'X'
		ret = ''
		for cont in range(0, len(string), 2):
			ret += self.__descifrar_pareja(string[cont], string[cont + 1])
		self.textoClaro = ret
		return ret