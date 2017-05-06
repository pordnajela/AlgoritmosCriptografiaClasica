#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#llave='ABCDEFGHIKLMNOPQRSTUVWXYZ'
#llave = [k.upper() for k in llave]

import copy

class Playfair(object):

	def __init__(self):
		self.cadena = ""
		self.clave =""
		self.alfabeto=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L',
		'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
		
		self.alfabeto_en_may=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J' 'L',
		'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
		
		self.alfabeto_en_min=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j''l',
		'm', 'n', 'q', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
		
		self.alfabeto_es_may=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L',
		'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
		
		self.alfabeto_es_min=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l',
		'm', 'n', 'q', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
		
		#self.alfabeto_base64 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
		#'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b',
		#'d', 'e' 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
		#'u', 'v', 'w', 'k', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+',
		#'/', ' ']

		self.alfabeto_base64 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
		'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b',
		'd', 'e' "'", '[', ']', '=', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
		'u', 'v', 'w', 'k', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+',
		'/' ' ']
				
		self.textoCifrado = ""
		self.textoClaro = ""
		self.bandera = 0
		self.claveaux = ''
		self.alfabeto_aux = ''
		self.div = 5
	
	def set_clave(self, clave):           
		self.clave=clave
		tam_alfabeto = len(self.alfabeto)
		cadena_aux = ''
		tam_clave = len(clave)
		cont = 0      
		for letra in self.clave:
			for i in range(tam_alfabeto):
				if letra == self.alfabeto[i]:
					self.alfabeto[i]=''
			cont = cont + 1
		self.alfabeto_aux = clave
		for i in range(tam_alfabeto):
			self.alfabeto_aux = self.alfabeto_aux + self.alfabeto[i]
		self.alfabeto = self.alfabeto_aux
		

	def definirAlfabeto(self, alfabeto):
		if(alfabeto== "es_min"):
			self.alfabeto = copy.copy(self.alfabeto_es_min)
		if(alfabeto== "es_may"):
			self.alfabeto = copy.copy(self.alfabeto_es_may)
		if(alfabeto== "en_min"):
			self.alfabeto = copy.copy(self.alfabeto_en_min)
		if(alfabeto== "en_may"):
			self.alfabeto = copy.copy(self.alfabeto_en_may)
		if(alfabeto== "B64"):
			self.alfabeto = copy.copy(self.alfabeto_base64)
			self.div = 8          

	def __cifrar_pareja(self, a, b):
		'''
		Cifra una pareja de letras que llegan como parametro desde el
		metodo cifrar
		'''
		if a == b:
			b = 'X'
		d=self.div
		afila, acolumna = int(self.alfabeto.index(a) / d), self.alfabeto.index(a) % d
		bfila, bcolumna = int(self.alfabeto.index(b) / d), self.alfabeto.index(b) % d
		if afila == bfila:                    
			return self.alfabeto[afila * d + (acolumna + 1) % d] + self.alfabeto[bfila * d + (bcolumna + 1) % d]
		elif acolumna == bcolumna:
			return self.alfabeto[((afila + 1) % d) * d + acolumna] + self.alfabeto[((bfila + 1) % d) * d + bcolumna]
		else:
			return self.alfabeto[afila * d + bcolumna] + self.alfabeto[bfila * d + acolumna]
	
	def __descifrar_pareja(self, a, b):
		'''d cambia segun sea un alfabeto 5*5 o 8*8 (letras o base 64 res
		pectivamente)        
		'''
		d=self.div
		assert a != b 
		afila, acolumna = int(self.alfabeto.index(a) / d), self.alfabeto.index(a) % d
		bfila, bcolumna = int(self.alfabeto.index(b) / d), self.alfabeto.index(b) % d
		if afila == bfila:
			return self.alfabeto[afila * d + (acolumna - 1) % d] + self.alfabeto[bfila * d + (bcolumna - 1) % d]
		elif acolumna == bcolumna:
			return self.alfabeto[((afila - 1) % d) * d + acolumna] + self.alfabeto[((bfila - 1) % d) * d + bcolumna]
		else:
			return self.alfabeto[afila * d + bcolumna] + self.alfabeto[bfila * d + acolumna]

	def cifrar(self, string, relleno, clave):
		self.bandera = self.bandera + 1
		if (self.bandera == 1):
			self.set_clave(clave)
		self.cadena = string
		if len(string) % 2 == 1:
			string += 'X' #"""Caracter de relleno X"""
		ret = ''
		for cont in range(0, len(string), 2):
			ret += self.__cifrar_pareja(string[cont], string[cont+1])
		self.textoCifrado = ret
		return ret    

	def descifrar(self, string, relleno, clave):
		self.cadena = string 
		if len(string) % 2 == 1:
			string += 'X'            
		ret = ''
		for cont in range(0, len(string), 2):
			ret += self.__descifrar_pareja(string[cont], string[cont + 1])
					
		self.textoClaro = ret 
		return ret