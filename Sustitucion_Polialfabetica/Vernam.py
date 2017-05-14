#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

class Vernam(object):
	def __init__(self, clave, cadena):
		self.clave = clave #contiene solo un elemento 
		self.cadena = cadena
		self.textoCifrado = ""
		self.textoClaro = ""

	def cifrar(self):
		textoCifrado 	= ""
		saltosLinea 	= len(self.cadena)-1
		clave = self.text_to_bits(self.clave)
		i = 0
		for linea in self.cadena:
			print(clave)
			if i < saltosLinea:
				#textoCifrado = textoCifrado + self.aplicarAlgoritmo(modulo, nuevaClave, linea, True) + "\n"
				i += 1
			else:
				#textoCifrado = textoCifrado + self.aplicarAlgoritmo(modulo, nuevaClave, linea, True)
				pass
		self.textoCifrado = textoCifrado
		print(textoCifrado)

	def descifrar(self):
		pass

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
		lineaNueva = ""
		for i, j in zip(linea, clave):
			lineaNueva += str( int(i) ^ int(j) )
		return lineaNueva

	def text_to_bits(self, text, encoding='utf-8', errors='surrogatepass'):
		bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
		return bits.zfill(8 * ((len(bits) + 7) // 8))

	def text_from_bits(self, bits, encoding='utf-8', errors='surrogatepass'):
		n = int(bits, 2)
		return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

ver = Vernam("a", "Wiki")
print("01010111011010010110101101101001")
print(ver.adecuarClave("01010111011010010110101101101001", "11110011"))
#print(int(0) ^ int(1))