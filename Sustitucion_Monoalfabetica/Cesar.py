#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#class Cesar(object):

import copy

class Cesar(object):

	def __init__(self):
		'''
		Se definen los alfabetos que se deben utilizar para el cifrado y descifrado
		dependiendo si se utiliza un texto o un archivo con su respectivo idima
		para los textos
		'''		
		self.cadena = ""
		self.alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
		'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0'
		, '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']
		
		self.alfabeto_es_min = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
		'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0'
		, '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']
		
		self.alfabeto_es_may = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
		'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0'
		, '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ']
		
		self.alfabeto_base64 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
		'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b',
		'd', 'e' 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
		'u', 'v', 'w', 'k', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+',
		'/' ]

		self.textoCifrado = ""
		self.textoClaro = ""

	
	def definirAlfabeto(self, alfabeto):
		'''
		Metodo que copia el tipo de alfabeto dependiento la cadena que llega
		desde el controlador a self.alfabeto
		'''
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

			
	def cifrar(self, cadena, cantidadRellenoB64, Avance):
		'''
		Metodo que cifra le llega la cadena a cifrar, el relleno y el avance
		que en este caso es la clave, para este caso el avance es correr 
		posiciones hacia adelante en el alfabeto (self_alfabeto), el tope
		es el tamaño del alfabeto, es necesario para moverse en este y saber
		el limite superior, la variable Pos es la que tiene el avance para
		la letra en la que se esta iterando de la cadena a cifrary que 
		coincidira en una posicion del alfabeto, pos se utiliza para ir 
		almacenando las letras cifradas
		'''
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
				#if(letra == '='):
				#	clave = clave + '='			
		self.textoCifrado = clave
		return self.textoCifrado		

	def descifrar(self, cadena, cantidadRellenoB64, Retroceso):
		'''
		Metodo que descifra, le llega la cadena a descifrar, el relleno y 
		el retroceso que en este caso es la clave, para este caso el retroceso
		es mover posiciones hacia atras en el alfabeto (self_alfabeto), el tope
		es el tamaño del alfabeto, es necesario para moverse en este y saber
		el limite superior, la variable Pos es la que tiene el retroceso para
		la letra en la que se esta iterando de la cadena a descifrar y que 
		coincidira en una posicion del alfabeto, pos se utiliza para ir 
		almacenando las letras descifradas
		'''
		clave= ""
		self.cadena = cadena
		Tope=len(self.alfabeto)		 
		Pos=0
		for letra in self.cadena:
			for i in range(Tope):				
				if(i - Retroceso >= 0):
					Pos=i-Retroceso					
				else:
					Pos=abs((Tope+i)-Retroceso)	
				if letra == self.alfabeto[i]:																			
					clave = clave + self.alfabeto[Pos]								

		self.textoClaro = clave
		#self.textoClaro = self.__adicionarRellenoB64(self.textoClaro, cantidadRellenoB64)
		return self.textoClaro