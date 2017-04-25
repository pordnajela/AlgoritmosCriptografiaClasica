#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import random
	
#def rand(min, max):
#	return int((max - min) * random.random() + min)
	
def generar_tabla():
	alfabeto = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
	tabla = [[0] * 5 for row in range(5)]
	cont = 0	
	for y in range(5):
		for x in range(5):			
			#table[x][y] = alphabet[rand(0, len(alphabet))]
			#alphabet = alphabet.replace(table[x][y], '')
			tabla[y][x] = alfabeto[cont]
			cont = cont + 1
	return tabla
	
def getStr(x, format='%02s'):
	return ''.join(format % i for i in x)	
	
def imprimir_tabla(tabla):
	print(' ' + getStr(range(1, 6)))
	for row in range(0, len(tabla)):
		print(str(row + 1) + getStr(tabla[row]))	
	
def cifrar(tabla, palabras):
	string = tabla
	cifrado = ''
	
	for ch in palabras.upper():
		for row in range(len(tabla)):
			if ch in tabla[row]:
				x = str((tabla[row].index(ch) + 1))
				y = str(row + 1)
				cifrado += y + x
	return cifrado
	
	
def descifrado(tabla, numeros):
	texto = ''
	for index in range(0, len(numeros), 2):
		y = int(numeros[index]) - 1
		x = int(numeros[index + 1]) - 1
		texto += tabla[y][x]
	return texto
	
	
tabla = generar_tabla()
imprimir_tabla(tabla)
texto_cifrado = cifrar(tabla, "POLYBIOS")
print(texto_cifrado)
print(descifrado(tabla, texto_cifrado))