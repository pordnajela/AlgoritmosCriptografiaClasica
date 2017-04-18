#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from itertools import zip_longest

class Cesar(object):
	alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
	'ñ','o','p','q','r','s','t','u','v','w','x','y','z']	
	
	def encriptar(cadena, Avance):
	clave=''
	Tope=len(alfabeto)
	Pos=0
	for letra in cadena:
		for i in range(Tope):
			if(i + clave < Tope):
				Pos=i+clave
			else:
				Pos=abs((Tope-i)-Avance)
			clave=clave+alfabeto[Pos]
	return Clave

clave=encriptar("upper", 4)
print (clave)
		
	
