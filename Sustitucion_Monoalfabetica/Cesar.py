#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#class Cesar(object):

from itertools import zip_longest
import copy

class Cesar(object):
	def __init__(self):
		self.cadena = ""

		self.alfabeto = ['a', 'b', 'c']
		
		self.alfabeto_es_min = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
		'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0'
		, '1', '2', '3', '4', '5', '6', '7', '8', '9']
		
		self.alfabeto_es_may = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
		'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0'
		, '1', '2', '3', '4', '5', '6', '7', '8', '9']
		
		self.alfabeto_base64 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
		'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b',
		'd', 'e' 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
		'u', 'v', 'w', 'k', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+',
		'/']

		self.textoCifrado = ""
		self.textoClaro = ""

	
	def definirAlfabeto(self, alfabeto):
		if(alfabeto== "es_min"):
			self.alfabeto = copy.copy(self.alfabeto_es_min)
		if(alfabeto== "es_may"):
			self.alfabeto = copy.copy(self.alfabeto_es_may)
		if(alfabeto== "b64"):
			self.alfabeto = copy.copy(self.alfabeto_base64)

	def cifrar(self, cadena, cantidadRellenoB64, Avance):
		clave= ''
		self.cadena = cadena
		Tope=len(self.alfabeto)
		Pos=0
		for letra in self.cadena:
			for i in range(Tope):
				if(i + Avance < Tope):
					Pos=i+Avance
				else:
					Pos=abs((Tope-i)-Avance)
				if letra == self.alfabeto[i]:					
					clave = clave + self.alfabeto[Pos]
		self.textoCifrado = clave
		return self.textoCifrado		

	def descifrar(self, cadena, cantidadRellenoB64, Retroceso):
		clave= ""
		self.cadena = cadena
		Tope=len(self.alfabeto) - 1
		Pos=0
		for letra in self.cadena:
			for i in range(Tope):
				if(i - Retroceso > 0):
					Pos=i-Retroceso
				else:
					Pos=abs((Tope+i)-Retroceso)
				if letra == self.alfabeto[i]:
					clave = clave + self.alfabeto[Pos]
		self.textoClaro = clave
		return self.textoClaro


	
