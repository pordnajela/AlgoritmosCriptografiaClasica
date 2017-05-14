#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

class Vigenere(object):
	def __init__(self, clave, alfabeto, cadena=None):
		self.cadena 		= cadena #Cada elemento es una línea
		self.alfabeto 		= alfabeto
		self.clave 			= clave
		self.textoCifrado 	= ""
		self.textoClaro 	= ""

	def cifrar(self):
		modulo 			= len(self.alfabeto)
		textoCifrado 	= ""
		saltosLinea 	= len(self.cadena)-1
		i = 0
		for linea in self.cadena:
			nuevaClave = self.adecuarClave(linea)
			if i < saltosLinea:
				textoCifrado = textoCifrado + self.aplicarAlgoritmo(modulo, nuevaClave, linea, True) + "\n"
				i += 1
			else:
				textoCifrado = textoCifrado + self.aplicarAlgoritmo(modulo, nuevaClave, linea, True)
		self.textoCifrado = textoCifrado
		print(textoCifrado)

	def descifrar(self):
		modulo 			= len(self.alfabeto)
		textoDescifrado = ""
		saltosLinea 	= len(self.cadena)-1
		i = 0
		for linea in self.cadena:
			nuevaClave = self.adecuarClave(linea)
			if i < saltosLinea:
				textoDescifrado = textoDescifrado + self.aplicarAlgoritmo(modulo, nuevaClave, linea, False) + "\n"
				i += 1
			else:
				textoDescifrado = textoDescifrado + self.aplicarAlgoritmo(modulo, nuevaClave, linea, False)
		self.textoClaro = textoDescifrado
		print(textoDescifrado)

	def adecuarClave(self, linea):
		nuevaClave = ""
		longitudClave = len(self.clave)
		i = 0
		for letra in linea:
			if i == longitudClave:
				i = 0
			if letra == " " or letra == "=":
				nuevaClave = nuevaClave + letra
				continue
			else:
				nuevaClave = nuevaClave+self.clave[i]
			i +=1
		return nuevaClave

	def aplicarAlgoritmo(self, modulo, nuevaClave, linea, cif):
		lineaNueva = ""
		valor = 0
		for clave, letra in zip(nuevaClave, linea):
			if letra == " " or letra == "= ":
				lineaNueva = lineaNueva + letra
				continue
			valor = self.operacion(self.alfabeto.index(letra), self.alfabeto.index(clave), modulo, cif)
			lineaNueva = lineaNueva + self.alfabeto[valor]
		return lineaNueva

	def operacion(self, Mi, Ki, modulo, cif):
		return (Mi + Ki) % modulo if cif == True else (Mi - Ki) % modulo


'''
a = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
cadena = ["XDAXJ LUQ TFUQEU CNÑY EZ NF CNUKO"]
vig = Vigenere("JUAN",a, cadena)
vig.descifrar()
'''
