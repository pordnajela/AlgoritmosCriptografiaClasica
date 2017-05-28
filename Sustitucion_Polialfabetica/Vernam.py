#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

class Vernam(object):
	def __init__(self, clave=None, cadena=None):
		self.clave 			= clave #contiene solo un elemento 
		self.cadena 		= cadena
		self.textoCifrado 	= ""
		self.textoClaro 	= ""

	def cifrar(self):
		self.textoCifrado = self.__cif_desc()
		return self.textoCifrado

	def descifrar(self):
		self.textoClaro = self.__cif_desc()
		return self.textoClaro

	def __cif_desc(self):
		claveNueva = self.texto_a_bits(self.clave)
		cadenaNueva = self.texto_a_bits(self.cadena)
		#-------------------------------------------
		claveNueva = self.adecuarClave(cadenaNueva, claveNueva)
		resultadoOP = self.operacion(cadenaNueva, claveNueva)
		textoCifrado = self.bits_a_texto(resultadoOP)
		return textoCifrado

	def texto_a_bits(self, cadenaTxt):
		cadenaBinario = [ bin(ord(ch))[2:].zfill(8) for ch in cadenaTxt ]
		return ''.join(cadenaBinario)

	def bits_a_texto(self, cadenaBin):
		return ''.join(chr(int(cadenaBin[i*8:i*8+8],2)) for i in range(len(cadenaBin)//8))

	def adecuarClave(self, linea, clave):
		longitudClave = len(clave)
		j = 0
		claveNueva = ""
		for bit in linea:
			if j == longitudClave:
				j = 0
			claveNueva += clave[j]
			j += 1
		return claveNueva

	def operacion(self, linea, clave):
		cadenaXOR = [ord(a) ^ ord(b) for a,b in zip(linea, clave)]
		return ''.join(str(x) for x in cadenaXOR)

'''
v = Vernam("XD", "HABÍA UNA VEZ")
v.cifrar()
print(v.textoCifrado)
v.cadena = v.textoCifrado
b = v.descifrar()
print(v.textoClaro)
'''