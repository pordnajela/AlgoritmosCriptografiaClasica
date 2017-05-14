#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

class AnalisisFrecuencia(object):
	"""docstring for AnalisisFrecuencia"""
	def __init__(self, mensaje):
		super(AnalisisFrecuencia, self).__init__()
		"""
		Frecuencias alfabeto Esañol
		"E":13.11, "A":10.60, "S":8.47, "O":8.23, "I":7.16, "N":7.14,
		"R":6.95, "D":5.87, "T":5.40, "C":4.85, "L":4.42, "U":4.34,
		"M":3.11, "P":2.71, "G":1.40, "B":1.16, "F":1.13, "V":0.82,
		"Y":0.79, "Q":0.74, "H":0.60, "Z":0.26, "J":0.25, "X":0.15,
		"W":0.12, "K":0.11, "Ñ":0.10
		"""

		self.alfUtilizar = ""
		self.mensaje = mensaje
		self.frecuencias = {}

	def establecerAlfbeto(self, opc):
		if opc == "es":
			self.alfUtilizar = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
		elif opc == "en":
			self.alfUtilizar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		return self.alfUtilizar

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

	def obtenerLetraMasFrecuente(self):
		valor_mas_frecuente = 0
		indice_mas_frecuente = None
		for letras in self.mensaje:
			if self.mensaje[letras] >= valor_mas_frecuente:
				valor_mas_frecuente = self.mensaje[letras]
				indice_mas_frecuente = letras
		return indice_mas_frecuente, valor_mas_frecuente

	def hipotesis(self, posiblesClaves=None, letraComun1=None, letraComun2=None):
		contar = af.contarLetras()
		frec = self.ordenarLetrasComunes(contar)
		print(frec)
		
		posicionE = self.alfUtilizar.index("E")
		posicionF = self.alfUtilizar.index(frec[0][0])
		clave = (posicionF - posicionE)

		if clave < 0:
			print("Entra")
			clave = clave + len(self.alfUtilizar)

		print("Posibles claves: ",posicionF, clave)

	def operacionHipotesis(self, clave, posLetraComun1, posLetraComun2):
		e = 4
		a = 0
		if (e + clave) % len(self.alfUtilizar) == posLetraComun1 and (a + clave) % len(self.alfUtilizar) == posLetraComun2:
			return clave
		else:
			return -1

	def ordenarLetrasComunes(self, letrasComunes):
		lComunes = sorted(letrasComunes.items() , key=lambda k:k[1], reverse=True)
		return lComunes





af = AnalisisFrecuencia('GERF GEVFGRF GVTERF GBZNONA RA GERF GEVFGRF GENFGRF')
af.establecerAlfbeto("es")
af.hipotesis()
'''
af = AnalisisFrecuencia()
LETTERS = af.establecerAlfbeto("en")
#cipher = 'WJGYHTUMYKJMXYWCMNJVMYFJNXCUNSUIJNXYGCCHZUHWCULOYGCOHCWJKYMNJHUDYCHJFPCXUVFYZOYFUFFOPCUFUAMUHFFOPCUUONMUFLOYWUYWJGJOHUWUUMUUXYFKJFJXYNXYFJNWCYFJNXYFWUVJXYBJMHJNBUNUFUZMJHYMUYHYNUZMJHYMUJZUMQYNXYGCKUMCUHUWCUFUPCXUUFUCYMMUUFUKJYNCUSUFUFFOPCUKJMGOWBJLOYBYWUGCHUXJGYKUMYWYLOYNYBUKYMXCXJYNYUMYXYFFJPYMLOYNYYDYMWCUWJGJOHKJXYMYMMCVFYSNOCFYHGCUMUOWUHCUHUUFFFJPCUGYNYNYHYMJNUIJNYHYMJNFUFFOPCUWUCUYHBCFJNWJGJFUMAUNUAODUNXYPCXMCJLOYNYMJGKCUHYHFJNYWBJNJFFYAUVUHYHJFUNMUHNKUMYHYNWJHMUFUNPYHUHUNSWUXUWUNUYMUOHUHUPYLOYXCZCWCFGYHYFFYAUVUUKOYMJYHULOYFJWYUHJXYCHPCYMHJYNUFFOPCUZMCUXYFNOMXYUGYMCWUHJCYHYFUNMUWBUNCGKOFNCPUNXYFUFFOPCUWUFCYHYLOYWUYWJGJOHFUCAJSKUNUXYDUHXJYFWCYFJUTOFKJMYFWJHMUMCJFUFFOPCUUONMUFCYHYKUWCYHWCUSWJHCHOUNCHYMGCHJWUSYHXJXYNXYYFWCYFJAMCN'
cipher = 'qdflr xqd ioru d ruloodv gh xqd ixhqwh pdv sxud txh od ioru gh od loxvlrq b xq kxudfdq wurqfkrod gh uhshqwh fdbhqgr do djxd od suhflrvd ioru'.upper()
contar = af.contarLetras(cipher)
print(contar)
af.ordenarLetrasComunes(contar)
frec = af.obtenerLetraMasFrecuente(contar)

posicionE = LETTERS.index("E")
posicionF = LETTERS.index(frec[0])
clave = (posicionF - posicionE)

if clave < 0:
	print("Entra")
	clave = clave + len(LETTERS)

print(frec[0], frec[1], posicionE)
print("claves posibles: ",posicionF, clave)

plaintext = ''

#af.operacionHipotesis(clave, letraComun1, letraComun2)

for symbol in cipher:
	try:
		position = LETTERS.index(symbol)
		position = position - posicionF
		if position < 0:
			position = position + len(LETTERS)
		plaintext = plaintext + LETTERS[position]
	except:
		plaintext = plaintext + symbol

print(plaintext)
'''