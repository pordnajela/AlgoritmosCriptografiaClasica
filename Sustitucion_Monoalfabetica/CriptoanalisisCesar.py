#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import math

from Cesar import Cesar

class AnalisisFrecuencia(object):
	"""docstring for AnalisisFrecuencia"""
	def __init__(self, mensaje):
		super(AnalisisFrecuencia, self).__init__()
		self.frecuenciaIngles = {
			'A': 0.08167, 'B': 0.01492, 'C': 0.02782, 'D': 0.04253, 'E': 0.130001, 'F': 0.02228, 'G': 0.02015,
			'H': 0.06094, 'I': 0.06966, 'J': 0.00153, 'K': 0.00772, 'L': 0.04025, 'M': 0.02406, 'N': 0.06749,
			'O': 0.07507, 'P': 0.01929, 'Q': 0.00095, 'R': 0.05987, 'S': 0.06327, 'T': 0.09056, 'U': 0.02758,
			'V': 0.00978, 'W': 0.02360, 'X': 0.00150, 'Y': 0.01974, 'Z': 0.00074}

		self.frecuenciaEspaniol = {
			'A': 0.12181, 'B': 0.02215, 'C': 0.04019, 'D': 0.05010, 'E': 0.12181, 'F': 0.00692, 'G': 0.01768,
			'H': 0.00703, 'I': 0.06247, 'J': 0.00493, 'K': 0.00011, 'L': 0.04967, 'M': 0.03157, 'N': 0.06712,
			'Ñ': 0.00311, 'O': 0.08683, 'P': 0.02510, 'Q': 0.00877, 'R': 0.06871, 'S': 0.07977, 'T': 0.04632,
			'U': 0.02927, 'V': 0.01138, 'W': 0.00017, 'X': 0.00215, 'Y': 0.01008, 'Z': 0.00467}

		self.alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		self.mensaje = mensaje
		self.cesar = Cesar()

		self.cesar.definirAlfabeto("en_may")

	def contarLetras(self):
		letra_count = {}
		for letra in self.mensaje.upper():
			if letra in [' ', ',', '.', '\n', '\r\n']:
				continue
			if letra not in letra_count:
				letra_count[letra] = 1
			else:
				letra_count[letra] += 1
		return letra_count

	def calcularFitness(self, cadenaCif):
		"""
		Calcula el fitness de la cadena, con base en la frecuencia, por ahora sirve con Inglés

		cadenaCif: Cadena cifrada con cesar

		Valor a retornar:
			total: Dato flotante negativo (entre más alto es mejor)
		"""
		total = 0
		for ch in cadenaCif:
			try:
				if self.alfabeto.index(ch.upper()):
					probabilidad = self.frecuenciaIngles[ch.upper()]
					total += -math.log(probabilidad) / math.log(2)
			except:
				continue
		return total

	def generarPoblacion(self):
		cadenas = list()
		for i in range(26):
			cadenas.append(self.cesar.cifrar(self.mensaje.upper(), 0, i))
		return cadenas

	def criptonalizar(self):
		cadenas = self.generarPoblacion()
		fitness = {}
		tmp = ""
		for i in range(25):
			tmp = cadenas[i]
			fitness.update({self.calcularFitness(tmp):i})

		#print(sorted(fitness.items())[0])
		return sorted(fitness.items())[0] 

af = AnalisisFrecuencia('qdflr xqd ioru d ruloodv gh xqd ixhqwh pdv sxud txh od ioru gh odloxvlrq b xq kxudfdq wurqfkrod gh uhshqwh fdbhqgr do djxd od suhflrvd ioru')
#af.establecerAlfbeto("en")
print(af.criptonalizar())
