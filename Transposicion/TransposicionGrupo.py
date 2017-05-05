#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

class TransposicionGrupo(object):
	"""
	"""
	def __init__(self, cadena=None, clave=None):
		self.cadena = cadena #Recibe una lista, la longitud de cada elemento es a longitud de la clave
		self.clave = clave
		self.textoClaro = ""
		self.textoCifrado = ""
		self.caracterRelleno = "₫" #₫

	def cifrar(self, cantidadRellenoB64=0):
		textoCifrado = ""
		linea_a_cifrar = None
		saltosLinea = len(self.cadena)-1
		i = 0
		for linea in self.cadena:
			if i < saltosLinea:
				linea_a_cifrar = self.dividirGrupos(linea,cantidadRellenoB64)
				textoCifrado = textoCifrado + self.__cifrar(linea_a_cifrar) + "\n"
				i += 1
			else:
				linea_a_cifrar = self.dividirGrupos(linea, cantidadRellenoB64)
				textoCifrado = textoCifrado + self.__cifrar(linea_a_cifrar)
		
		self.textoCifrado = textoCifrado

	def descifrar(self, cantidadRellenoB64=0):
		textoDescifrado = ""
		linea_a_descifrar = None
		saltosLinea = len(self.cadena)-1
		i = 0
		for linea in self.cadena:
			if i < saltosLinea:
				linea_a_descifrar = self.dividirGrupos(linea)
				textoDescifrado = textoDescifrado + self.__descifrar(linea_a_descifrar) + "\n"
				i += 1
			else:
				linea_a_descifrar = self.dividirGrupos(linea, cantidadRellenoB64)
				textoDescifrado = textoDescifrado + self.__descifrar(linea_a_descifrar)

		self.textoClaro = textoDescifrado
	
	#---------------------------------------------------------- Métodos complementarios
	def dividirGrupos(self, linea, cantidadRellenoB64=0):
		lineaNueva = linea
		tamanioLinea = len(linea)-cantidadRellenoB64
		tamanioBloque = len(str(self.clave))

		#print(tamanioLinea, tamanioBloque)
		if tamanioLinea % tamanioBloque != 0:
			lineaNueva = self.adicionarRelleno(linea, tamanioLinea, tamanioBloque)
			tamanioLinea = len(lineaNueva)

		nuevaCadena = list()
		bloque = ""
		i = 0
		
		while i < tamanioLinea:
			bloque = bloque + lineaNueva[i]
			i += 1
			if i % tamanioBloque == 0 and i > 0:
				nuevaCadena.append(bloque)
				bloque = ""

		return nuevaCadena

	def adicionarRelleno(self, linea, tamanioLinea, tamanioBloque):
		if tamanioLinea % tamanioBloque == 0:
			return linea
		else:
			linea = linea + self.caracterRelleno
			return self.adicionarRelleno(linea ,len(linea), tamanioBloque)

	def intercambiar_cifrar(self, bloque, clave):
		tamanioBloque = len(bloque)
		claveStr = str(clave)
		nuevoBloque = list()
		i = 0
		pos = 0
		while i < tamanioBloque:
			pos = int(claveStr[i])-1
			nuevoBloque.insert(i, bloque[pos])  
			i += 1

		nuevoBloque = ''.join(nuevoBloque)
		return nuevoBloque

	def intercambiar_descifrar(self, bloque, clave):
		tamanioBloque = len(bloque)
		claveStr = str(clave)
		nuevoBloque = {}
		bloqueDescifrado = list()
		i = 0
		pos = 0
		while i < tamanioBloque:
			pos = int(claveStr[i])-1
			nuevoBloque.update({pos:bloque[i]})
			i += 1

		for llave, valor in nuevoBloque.items():
			bloqueDescifrado.append(valor)

		bloqueDescifrado = ''.join(bloqueDescifrado)
		return bloqueDescifrado
	
	#----------------------------------------------------------------- Métodos privados
	def __cifrar(self, linea_a_cifrar, cantidadRellenoB64=0):
		lineaNueva = list()
		for bloque in linea_a_cifrar:
			lineaNueva.append(self.intercambiar_cifrar(bloque, self.clave))

		lineaNueva = ''.join(lineaNueva)
		return lineaNueva
	
	def __descifrar(self, linea_a_descifrar, cantidadRellenoB64=0):
		lineaNueva = list()
		for bloque in linea_a_descifrar:
			lineaNueva.append(self.intercambiar_descifrar(bloque, self.clave))

		lineaNueva = ''.join(lineaNueva)
		return lineaNueva