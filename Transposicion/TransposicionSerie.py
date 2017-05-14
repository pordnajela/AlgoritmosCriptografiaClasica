#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

class TransposicionSerie(object):
	def __init__(self, series, cadena=None):
		self.cadena = cadena
		self.series = series
		self.textoClaro = ""
		self.textoCifrado = ""

	def cifrar(self):
		textoCifrado = ""
		linea_a_cifrar = ""
		saltosLinea = len(self.cadena)-1
		numFunciones = len(self.series)
		i = 0
		j = 0

		for linea in self.cadena:
			while i < numFunciones:
				if len(linea) == 0:
					i += 1
					break
				linea_a_cifrar += self.aplicarSeries_cifrar(linea, i, len(self.series[i]))
				i += 1

			if j < saltosLinea:
				textoCifrado += linea_a_cifrar + "\n"
				j += 1
			else:
				textoCifrado += linea_a_cifrar
			linea_a_cifrar = ""
			i = 0

		self.textoCifrado = textoCifrado

	def descifrar(self):
		textoDescifrado = ""
		linea_a_descifrar = ""
		saltosLinea = len(self.cadena)-1
		funciones = self.concatenarFunciones()
		i = 0
		j = 0

		for linea in self.cadena:
			if len(linea) == 0:
				i += 1
				break
			if j < saltosLinea:
				linea_a_descifrar += self.aplicarSeries_descifrar(linea, funciones, len(funciones))
				textoDescifrado += linea_a_descifrar + "\n"
			else:
				linea_a_descifrar += self.aplicarSeries_descifrar(linea, funciones, len(funciones))
				textoDescifrado += linea_a_descifrar

			linea_a_descifrar = ""
			i = 0
		self.textoClaro = textoDescifrado

	def aplicarSeries_cifrar(self, linea, i, tamanioFuncion):
		lineaNueva = ""
		j = 0
		while j < tamanioFuncion:
			lineaNueva += linea[ int(self.series[i][j])-1 ]
			j += 1
		return lineaNueva

	def aplicarSeries_descifrar(self, linea, funciones, lenFunciones):
		nuevoBloque = {}
		bloqueDescifrado = list()
		pos = 0
		i = 0
		while i < lenFunciones:
			pos = int(funciones[i])-1
			nuevoBloque.update({pos:linea[i]})
			i += 1
		
		for llave, valor in nuevoBloque.items():
			bloqueDescifrado.append(valor)
		bloqueDescifrado = ''.join(bloqueDescifrado)

		return bloqueDescifrado

	def concatenarFunciones(self):
		#[ [], [], [] ]
		funciones = list()
		longSeries = len(self.series)
		tmp = list()
		i = 0
		j = 0
		while i < longSeries:
			tmp = self.series[i]
			while j < len(tmp):
				funciones.append(tmp[j])
				j += 1
			i += 1
			j = 0

		return funciones