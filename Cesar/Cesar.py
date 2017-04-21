#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

#class Cesar(object):
	
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
	 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def cifrar(cadena, Avance):
	clave= ''
	Tope=len(alfabeto)
	Pos=0
	for letra in cadena:
		for i in range(Tope):
			if(i + Avance < Tope):
				Pos=i+Avance
			else:
				Pos=abs((Tope-i)-Avance)
			if letra == alfabeto[i]:
				clave = clave + alfabeto[Pos]
	return clave

def descifrar(cadena, Retroceso):
	clave= ''
	Tope=len(alfabeto)
	Pos=0
	for letra in cadena:
		for i in range(Tope):
			if(i - Retroceso > 0):
				Pos=i-Retroceso
			else:
				Pos=abs((Tope+i)-Retroceso)
			if letra == alfabeto[i]:
				clave = clave + alfabeto[Pos]
	return clave	

clave = cifrar("upper", 4)
print (clave)
clave = descifrar("def", 2)
print (clave)
		
	
