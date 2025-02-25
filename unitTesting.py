'''
 * Nombre: unitTesting.py
 * Descripción: Pruebas unitarias para validar las funciones de cifrado y descifrado. 
 * Programadora: Fernanda Esquivel (esq21542@uvg.edu.gt)
 * Lenguaje: Python
 * Recursos: VSCode
 * Historial:
    - Creado el 25.02.2025
    - Finalizado el 25.02.2025
'''

import unittest
import sys
import random
import string
from encryption import encryptMessage, keystreamGenerator, stringToBinary, xorBinary, binaryToString
from decryption import decryptMessage

class TestEncryptionDecryption(unittest.TestCase):
    
    '''
    Prueba estándar de cifrado y descifrado con un mensaje simple.
    '''
    def test_standard(self):
        text = "Hello World"
        seed = "key123"
        
        #Cifrar el mensaje
        encrypted, keystream = encryptMessage(text, seed)
        
        #Descifrar el mensaje
        decrypted = decryptMessage(encrypted, keystream)
        
        #Verificar que el texto descifrado coincide con el original
        self.assertEqual(text, decrypted, 
                        f"El texto descifrado '{decrypted}' no coincide con el original '{text}'")
    
    '''
    Prueba cifrado y descifrado con un string vacío.
    '''
    def test_emptyText(self):
        text = ""
        seed = "key123"
        
        #Cifrar el mensaje
        encrypted, keystream = encryptMessage(text, seed)
        
        #Verificar que el keystream tiene la longitud correcta
        self.assertEqual(len(keystream), len(text),
                        "La longitud del keystream no coincide con la longitud del texto original")
        
        #Verificar que el texto cifrado es vacío
        self.assertEqual(encrypted, "", "El texto cifrado debería ser vacío")
    
    '''
    Prueba cifrado y descifrado con caracteres especiales.
    '''
    def test_specialChars(self):
        text = "!@#$%^&*()_+-=[]{}|;:,.<>?/~`"
        seed = "key123"
        
        #Cifrar el mensaje
        encrypted, keystream = encryptMessage(text, seed)
        
        #Descifrar el mensaje
        decrypted = decryptMessage(encrypted, keystream)
        
        #Verificar que el texto descifrado coincide con el original
        self.assertEqual(text, decrypted, 
                        "El texto descifrado no coincide con el original al usar caracteres especiales")
    
    '''
    Prueba que diferentes semillas producen diferentes resultados de cifrado.
    '''
    def test_multipleSeeds(self):
        text = "Test message"
        seed1 = "key1"
        seed2 = "key2"
        
        #Cifrar el mensaje con la primera semilla
        encrypted1, keystream1 = encryptMessage(text, seed1)
        
        #Cifrar el mensaje con la segunda semilla
        encrypted2, keystream2 = encryptMessage(text, seed2)
        
        #Verificar que los keystreams son diferentes
        self.assertNotEqual(keystream1, keystream2, 
                            "Los keystreams deberían ser diferentes para semillas diferentes")
        
        #Verificar que los textos cifrados son diferentes
        self.assertNotEqual(encrypted1, encrypted2, 
                            "Los textos cifrados deberían ser diferentes para semillas diferentes")
    
    '''
    Prueba con un texto largo.
    '''
    def test_longText(self):
        #Generar un texto aleatorio largo
        text = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation + ' ') 
                            for _ in range(1000))
        seed = "key123"
        
        #Cifrar el mensaje
        encrypted, keystream = encryptMessage(text, seed)
        
        #Verificar longitud del keystream
        self.assertEqual(len(keystream), len(text),
                        "La longitud del keystream no coincide con la longitud del texto original")
        
        #Descifrar el mensaje
        decrypted = decryptMessage(encrypted, keystream)
        
        # Verificar que el texto descifrado coincide con el original
        self.assertEqual(text, decrypted, 
                        "El texto descifrado no coincide con el original para un texto largo")
    
    '''
    Prueba las funciones auxiliares utilizadas en el proceso de cifrado/descifrado.
    '''
    def test_auxiliarFun(self):
        #Prueba StringToBinary
        text = "ABC"
        binary = stringToBinary(text)
        self.assertEqual(len(binary), len(text) * 8, "La longitud binaria debe ser 8 veces la longitud del texto")
        
        #Prueba XOR
        bin1 = "10101010"
        bin2 = "11110000"
        xor = xorBinary(bin1, bin2)
        self.assertEqual(xor, "01011010", "El resultado XOR es incorrecto")
        
        #Prueba BinaryToString
        binary = "010000010100001001000011"  # ABC en binario
        text = binaryToString(binary)
        self.assertEqual(text, "ABC", "La conversión de binario a string es incorrecta")
        
        #Prueba KeystreamGenerator
        seed = "key123"
        messageLen = 10
        keystream = keystreamGenerator(messageLen, seed)
        self.assertEqual(len(keystream), messageLen, 
                        f"La longitud del keystream ({len(keystream)}) no coincide con la solicitada ({messageLen})")
    
    '''
    Prueba que la misma semilla produce el mismo keystream.
    '''
    def test_sameSeed(self):
        text = "Test Message"
        seed = "key123"
        
        #Generar keystream directamente
        keystream1 = keystreamGenerator(len(text), seed)
        
        #Generar keystream a través de encryptMessage
        _, keystream2 = encryptMessage(text, seed)
        
        #Verificar que los keystreams son iguales
        self.assertEqual(keystream1, keystream2, 
                        "La misma semilla debería producir el mismo keystream")
    
    '''
    Prueba que cifrar y descifrar múltiples veces produce el resultado esperado.
    '''
    def test_multiple(self):
        text = "Multiple Test Message"
        seed = "key123"
        
        #Primera ronda: cifrar y descifrar
        encrypted1, keystream1 = encryptMessage(text, seed)
        decrypted1 = decryptMessage(encrypted1, keystream1)
        
        #Segunda ronda: cifrar y descifrar el resultado de la primera ronda
        encrypted2, keystream2 = encryptMessage(decrypted1, seed)
        decrypted2 = decryptMessage(encrypted2, keystream2)
        
        #Verificar que los textos descifrados son iguales al original
        self.assertEqual(text, decrypted1, 
                        "Primera ronda de descifrado falló")
        self.assertEqual(text, decrypted2, 
                        "Segunda ronda de descifrado falló")

if __name__ == '__main__':
    unittest.main()