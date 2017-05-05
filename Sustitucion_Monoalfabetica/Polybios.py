#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import copy

class Polybios(object):
	def __init__(self):
		self.cadena = ''
		self.textoCifrado = ''
		self.textoClaro = ''		
		self.alfabeto = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
		self.alfabeto_en_may = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'		
		self.alfabeto_numeros =['11', '12', '13', '14', '15', '21', '22', '23',
		'24', '25', '31', '32', '33', '34', '35', '41', '41', '43', '44',
		'45', '51', '52', '53', '54', '55']		
		self.tabla = [[0] * 5 for row in range(5)]
		tabla = [[0] * 5 for row in range(5)]
		cont = 0	
		for y in range(5):
			for x in range(5):			
				tabla[y][x] = self.alfabeto[cont]
				cont = cont + 1
		self.tabla = tabla
		
				
	def definirAlfabeto(self, alfabeto):
		if(alfabeto== "es_min"):
			self.alfabeto = copy.copy(self.alfabeto_es_min)
		if(alfabeto== "es_may"):
			self.alfabeto = copy.copy(self.alfabeto_es_may)
		if(alfabeto== "en_may"):
			self.alfabeto = copy.copy(self.alfabeto_en_may)
		if(alfabeto == "num"):
			self.alfabeto = copy.copy(self.alfabeto_num)
		if(alfabeto== "b64"):
			self.alfabeto = copy.copy(self.alfabeto_base64)
				

	def getStr(x, format='%02s'):
		return ''.join(format % i for i in x)	
	
	def imprimir_tabla(tabla):
		print(' ' + getStr(range(1, 6)))
		for row in range(0, len(tabla)):
			print(str(row + 1) + getStr(tabla[row]))	
	
	def cifrar(self, palabras, rellenoB64, tabla): 
	#cadena, cantidadRelleno, clave
		string = self.tabla
		cifrado = ''	
		for ch in palabras:
			for row in range(len(self.tabla)):
				if ch in self.tabla[row]:
					x = str((self.tabla[row].index(ch) + 1))
					y = str(row + 1)
					cifrado += y + x
		#self.textoCifrado = cifrado
		print(cifrado)
		return cifrado	
	
	def descifrar(self, numeros, rellenoB64, tabla):
		texto = ''
		for index in range(0, len(numeros), 2):
			y = int(numeros[index]) - 1
			x = int(numeros[index + 1]) - 1
			texto += self.tabla[y][x]
		#self.textoClaro = texto
		print(texto)
		return texto
		