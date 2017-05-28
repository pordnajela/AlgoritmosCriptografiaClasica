#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

class Afin(object):
	def __init__(self, clave, alfabeto, cadena=None):
		self.cadena 		= cadena #Cada elemento es una línea ["HOLA", "SOLEDAD"]
		self.alfabeto 		= alfabeto
		self.clave 			= clave #Los dos elementos son a y b [a,b]
		self.textoCifrado 	= ""
		self.textoClaro 	= ""

	def cifrar(self):
		modulo 			= len(self.alfabeto)
		textoCifrado 	= ""
		saltosLinea 	= len(self.cadena)-1
		i = 0
		for linea in self.cadena:
			if i < saltosLinea:
				textoCifrado = textoCifrado + self.aplicarAlgoritmo(modulo, linea, True) + "\n"
				i += 1
			else:
				textoCifrado = textoCifrado + self.aplicarAlgoritmo(modulo, linea, True)
		self.textoCifrado = textoCifrado
		print(textoCifrado)

	def descifrar(self):
		modulo 			= len(self.alfabeto)
		textoDescifrado = ""
		saltosLinea 	= len(self.cadena)-1
		i = 0
		for linea in self.cadena:
			if i < saltosLinea:
				textoDescifrado = textoDescifrado + self.aplicarAlgoritmo(modulo, linea, False) + "\n"
				i += 1
			else:
				textoDescifrado = textoDescifrado + self.aplicarAlgoritmo(modulo, linea, False)
		self.textoClaro = textoDescifrado
		print(textoDescifrado)

	def aplicarAlgoritmo(self, modulo, linea, cif):
		lineaNueva = ""
		valor = 0
		for letra in linea:
			if letra == " " or letra == "=":
				lineaNueva += letra
				continue
			valor = self.operacion(self.alfabeto.index(letra), modulo, cif)
			lineaNueva += self.alfabeto[valor]
		return lineaNueva

	def operacion(self, Mi, mod, cif):
		if cif:
			return (( self.clave[0] * Mi ) + self.clave[1]) % mod
		else:
			i = 1
			resultado = ( self.clave[0] * i) - mod
			return (self.inversoModular(resultado, self.clave[0], mod, i) * (Mi - self.clave[1])) % mod

	def inversoModular(self, resultado, a, b, i):
		if resultado == 1:
			return i
		elif resultado < 0:
			i = i+1
			return self.inversoModular( (a*i)-b , a , b , i)
		elif resultado > 0:
			return self.inversoModular(resultado-b,a,b,i)

'''
alf = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
clave = [15,3]
cadena = ["OJALA QUE LLUEVA CAFE EN EL CAMPO"]
#cadena = ["FIDMD JRL MMRLGD HDAL LQ LM HDBUF"]
af = Afin(clave, alf, cadena)
af.cifrar()
#af.descifrar()
'''