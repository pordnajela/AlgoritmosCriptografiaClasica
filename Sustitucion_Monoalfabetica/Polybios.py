#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import copy

class Polybios(object):
	def __init__(self):
		self.cadena = ""
		self.textoCifrado = ''
		self.textoClaro = ''
		self.alfabeto = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
		self.alfabeto_en_may = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
		self.alfabeto_en_min = 'abcdefghiklmnopqrstuvwxyz'
		self.tabla = [[0] * 5 for row in range(5)]
				
	def crear_tabla(self):
		tabla = [[0] * 5 for row in range(5)]
		cont = 0	
		for y in range(5):
			for x in range(5):			
				tabla[y][x] = self.alfabeto[cont]
				cont = cont + 1
		self.tabla = tabla
		#return tabla

	def definirAlfabeto(self, alfabeto):
		if(alfabeto== "es_min"):
			self.alfabeto = copy.copy(self.alfabeto_es_min)
		if(alfabeto== "es_may"):
			self.alfabeto = copy.copy(self.alfabeto_es_may)
		if(alfabeto== "en_may"):
			self.alfabeto = copy.copy(self.alfabeto_en_may)
		if(alfabeto== "b64"):
			self.alfabeto = copy.copy(self.alfabeto_base64)
		self.crear_tabla()

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
		for ch in palabras.upper():
			for row in range(len(self.tabla)):
				if ch in self.tabla[row]:
					x = str((self.tabla[row].index(ch) + 1))
					y = str(row + 1)
					cifrado += y + x
		self.texto_cifrado = cifrado
		return self.texto_cifrado
	
	
	def descifrar(self, numeros, rellenoB64, tabla):
		texto = ''
		for index in range(0, len(numeros), 2):
			y = int(numeros[index]) - 1
			x = int(numeros[index + 1]) - 1
			texto += self.tabla[y][x]
		self.texto_claro = texto
		return self.texto_claro
	
	
	#tabla = generar_tabla()
	#imprimir_tabla(tabla)
	#texto_cifrado = cifrar(tabla, "POLYBIOS")
	#print(texto_cifrado)
	#print(descifrado(tabla, texto_cifrado))