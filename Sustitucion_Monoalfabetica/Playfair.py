#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

llave='ABCDEFGHIKLMNOPQRSTUVWXYZ'
llave = [k.upper() for k in llave]
        
def cifrar_pareja(a, b):
    if a == b:
        b = 'X'
    afila, acolumna = int(llave.index(a) / 5), llave.index(a) % 5
    bfila, bcolumna = int(llave.index(b) / 5), llave.index(b) % 5
    if afila == bfila:
        return llave[afila * 5 + (acolumna + 1) % 5] + llave[bfila * 5 + (bcolumna + 1) % 5]
    elif acolumna == bcolumna:
        return llave[((afila + 1) % 5) * 5 + acolumna] + llave[((bfila + 1) % 5) * 5 + bcolumna]
    else:
        return llave[afila * 5 + bcolumna] + llave[bfila * 5 + acolumna]
        
def descifrar_pareja(a, b):
    assert a != b, 'two of the same letters occurred together, illegal in playfair'
    afila, acolumna = int(llave.index(a) / 5), llave.index(a) % 5
    bfila, bcolumna = int(llave.index(b) / 5), llave.index(b) % 5
    if afila == bfila:
        return llave[afila * 5 + (acolumna - 1) % 5] + llave[bfila * 5 + (bcolumna - 1) % 5]
    elif acolumna == bcolumna:
        return llave[((afila - 1) % 5) * 5 + acolumna] + llave[((bfila - 1) % 5) * 5 + bcolumna]
    else:
        return llave[afila * 5 + bcolumna] + llave[bfila * 5 + acolumna]
        
def cifrar(string):
    """Encipher string using Playfair cipher according to initialised key. Punctuation and whitespace
    are removed from the input. If the input plaintext is not an even number of characters, an 'X' will be appended.
    Ejemplo::
    ciphertext = Playfair(llave='zgptfoihmuwdrcnykeqaxvsbl').encriptar(texto plano)     
    :parametro string: El string a cifrar.
    :retorna:El string cifrado.
    """    
    #string = self.remove_punctuation(string)  
    #string = re.sub(r'[J]', 'I', string)
    if len(string) % 2 == 1:
        string += 'X' #"""Caracter de relleno X"""
    ret = ''
    for cont in range(0, len(string), 2):
        ret += cifrar_pareja(string[cont], string[cont + 1])
    return ret    

def descifrar(string):
    """Se deebn ingresar caracteres validos dentro del alfabeto, si no es asi los
    caracteres que no son validos seran rellenados con un X
    Example::
    plaintext = Playfair(key='zgptfoihmuwdrcnykeqaxvsbl').decipher(ciphertext)     
    :param string: The string to decipher.
    :returns: The deciphered string.
    """    
    #string = self.remove_punctuation(string)  
    if len(string) % 2 == 1:
        string += 'X'
    ret = ''
    for cont in range(0, len(string), 2):
        ret += descifrar_pareja(string[cont], string[cont + 1])
    return ret    
        
texto_cifrado = cifrar("RIGTHLEFTKBDLV")
print (texto_cifrado)
texto_claro = descifrar("TGIRFNAKUICEQA")
print (texto_claro)
#if __name__ == '__main__': 
#    print('use "import pycipher" to access functions')
