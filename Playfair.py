
class Playfair(object):
    """ :clave: alfabeto de 25 caracteres ordenado en 5 filas y 5 columnas.
    """
    def __clave__(self, key='ABCDEFGHIKLMNOPQRSTUVWXYZ'):
        self.llave = [k.upper() for k in key]
        
    def cifrar_pareja(self, a, b):
        if a == b:
            b = 'X'
        afila, acolumna = int(self.llave.index(a) / 5), self.llave.index(a) % 5
        bfila, bcolumna = int(self.llave.index(b) / 5), self.llave.index(b) % 5
        if afila == bfila:
            return self.llave[afila * 5 + (acolumna + 1) % 5] + self.llave[bfila * 5 + (bcolumna + 1) % 5]
        elif acolumna == bcolumna:
            return self.llave[((afila + 1) % 5) * 5 + acolumna] + self.llave[((bfila + 1) % 5) * 5 + bcolumna]
        else:
            return self.llave[afila * 5 + bcolumna] + self.key[bfila * 5 + acolumna]
        
    def descifrar_pareja(self, a, b):
        assert a != b, 'two of the same letters occurred together, illegal in playfair'
        arow, acol = int(self.key.index(a) / 5), self.key.index(a) % 5
        brow, bcol = int(self.key.index(b) / 5), self.key.index(b) % 5
        if arow == brow:
            return self.key[arow * 5 + (acol - 1) % 5] + self.key[brow * 5 + (bcol - 1) % 5]
        elif acol == bcol:
            return self.llave[((afila - 1) % 5) * 5 + acolumna] + self.llave[((bfila - 1) % 5) * 5 + bcolumna]
        else:
            return self.llave[afila * 5 + bcolumna] + self.llave[bfila * 5 + acolumna]
        
    def cifrar(self, string):
        """Encipher string using Playfair cipher according to initialised key. Punctuation and whitespace
        are removed from the input. If the input plaintext is not an even number of characters, an 'X' will be appended.

        Ejemplo::

            ciphertext = Playfair(llave='zgptfoihmuwdrcnykeqaxvsbl').encriptar(texto plano)     

        :parametro string: El string a cifrar.
        :retorna:El string cifrado.
        """    
        string = self.remove_punctuation(string)  
        string = re.sub(r'[J]', 'I', string)
        if len(string) % 2 == 1:
            string += 'X' """Caracter de relleno X"""
        ret = ''
        for cont in range(0, len(string), 2):
            ret += self.cifrar_pareja(string[cont], string[cont + 1])
        return ret    

    def descifrar(self, string):
        """Se deebn ingresar caracteres validos dentro del alfabeto, si no es asi los
        caracteres que no son validos seran rellenados con un X

        Example::

            plaintext = Playfair(key='zgptfoihmuwdrcnykeqaxvsbl').decipher(ciphertext)     

        :param string: The string to decipher.
        :returns: The deciphered string.
        """    
        string = self.remove_punctuation(string)  
        if len(string) % 2 == 1:
            string += 'X'
        ret = ''
        for cont in range(0, len(string), 2):
            ret += self.descifrar_pareja(string[c], string[c + 1])
        return ret    
        
if __name__ == '__main__': 
    print('use "import pycipher" to access functions')
