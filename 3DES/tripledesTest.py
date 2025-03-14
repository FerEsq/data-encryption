'''
 * Nombre: tripledesTest.py
 * Descripción: Programa que implementa tests unitarios para el cifrado y descifrado 3DES.
 * Programadora: Fernanda Esquivel (esq21542@uvg.edu.gt)
 * Lenguaje: Python
 * Recursos: VSCode
 * Historial:
    - Creado el 13.03.2025
    - Finalizado el 13.03.2025
'''

import unittest
import os
import sys
import binascii

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#Importar funciones del módulo TripleDES
from tripledes import generateKey, generateIV, encrypt3des, decrypt3des

class TestTripleDESFunctions(unittest.TestCase):
    
    def setUp(self):
        # Crear directorio de prueba si no existe
        if not os.path.exists("test_3DES"):
            os.makedirs("test_3DES")
    
    def tearDown(self):
        # Eliminar archivos de prueba
        for file in ['test_3DES/test_encrypted.txt', 'test_3DES/test_decrypted.txt']:
            if os.path.exists(file):
                os.remove(file)
        
        # Eliminar directorio de prueba
        if os.path.exists("test_3DES"):
            os.rmdir("test_3DES")
    
    def test_key_generation(self):
        # Verificar que la clave generada tiene la longitud correcta (24 bytes para 3DES)
        key = generateKey()
        self.assertEqual(len(key), 24, "La clave generada no tiene la longitud correcta")
    
    def test_iv_generation(self):
        # Verificar que el IV generado tiene la longitud correcta (8 bytes para 3DES)
        iv = generateIV()
        self.assertEqual(len(iv), 8, "El IV generado no tiene la longitud correcta")
    
    def test_encryption_decryption_simple(self):
        # Texto de prueba
        plaintext = "Esto es una prueba de cifrado 3DES"
        
        # Generar clave e IV
        key = generateKey()
        iv = generateIV()
        
        # Cifrar
        encrypted_hex, key_hex, iv_hex = encrypt3des(plaintext, key, iv)
        
        # Verificar resultados del cifrado
        self.assertIsNotNone(encrypted_hex, "El texto cifrado es None")
        self.assertTrue(len(encrypted_hex) > 0, "El texto cifrado está vacío")
        
        # Descifrar
        decrypted_text = decrypt3des(encrypted_hex, key_hex, iv_hex)
        
        # Verificar que el texto descifrado coincide con el original
        self.assertEqual(plaintext, decrypted_text, 
                        "El texto descifrado no coincide con el texto original")
    
    def test_encryption_decryption_special_chars(self):
        # Texto con caracteres especiales
        plaintext = "¡Caracteres especiales: áéíóúñ@#$%^&*(){}[]!"
        
        # Generar clave e IV
        key = generateKey()
        iv = generateIV()
        
        # Cifrar
        encrypted_hex, key_hex, iv_hex = encrypt3des(plaintext, key, iv)
        
        # Descifrar
        decrypted_text = decrypt3des(encrypted_hex, key_hex, iv_hex)
        
        # Verificar que el texto descifrado coincide con el original
        self.assertEqual(plaintext, decrypted_text, 
                        "El texto descifrado con caracteres especiales no coincide con el original")
    
    def test_encryption_decryption_long_text(self):
        # Texto largo
        plaintext = "Este es un texto más largo para probar el cifrado y descifrado 3DES. " * 20
        
        # Generar clave e IV
        key = generateKey()
        iv = generateIV()
        
        # Cifrar
        encrypted_hex, key_hex, iv_hex = encrypt3des(plaintext, key, iv)
        
        # Descifrar
        decrypted_text = decrypt3des(encrypted_hex, key_hex, iv_hex)
        
        # Verificar que el texto descifrado coincide con el original
        self.assertEqual(plaintext, decrypted_text, 
                        "El texto largo descifrado no coincide con el original")
    
    def test_wrong_key(self):
        # Texto de prueba
        plaintext = "Esto es una prueba de cifrado 3DES"
        
        # Generar clave e IV correctos
        key = generateKey()
        iv = generateIV()
        
        # Cifrar
        encrypted_hex, key_hex, iv_hex = encrypt3des(plaintext, key, iv)
        
        # Generar una clave incorrecta
        wrong_key = generateKey()
        wrong_key_hex = binascii.hexlify(wrong_key).decode('ascii')
        
        # Intentar descifrar con clave incorrecta
        decrypted_text = decrypt3des(encrypted_hex, wrong_key_hex, iv_hex)
        
        # El resultado debería ser None o diferente al texto original
        self.assertNotEqual(plaintext, decrypted_text, 
                            "El descifrado con clave incorrecta produjo el texto original")
    
    def test_wrong_iv(self):
        # Texto de prueba
        plaintext = "Esto es una prueba de cifrado 3DES"
        
        # Generar clave e IV correctos
        key = generateKey()
        iv = generateIV()
        
        # Cifrar
        encrypted_hex, key_hex, iv_hex = encrypt3des(plaintext, key, iv)
        
        # Generar un IV incorrecto
        wrong_iv = generateIV()
        wrong_iv_hex = binascii.hexlify(wrong_iv).decode('ascii')
        
        # Intentar descifrar con IV incorrecto
        decrypted_text = decrypt3des(encrypted_hex, key_hex, wrong_iv_hex)
        
        # El resultado debería ser None o diferente al texto original
        self.assertNotEqual(plaintext, decrypted_text, 
                            "El descifrado con IV incorrecto produjo el texto original")
    
    def test_malformed_input(self):
        # Texto de prueba
        plaintext = "Esto es una prueba de cifrado 3DES"
        
        # Generar clave e IV
        key = generateKey()
        iv = generateIV()
        
        # Cifrar
        encrypted_hex, key_hex, iv_hex = encrypt3des(plaintext, key, iv)
        
        # Modificar el texto cifrado para que sea malformado (truncar)
        malformed_encrypted = encrypted_hex[:-2]
        
        # Intentar descifrar con texto malformado
        decrypted_text = decrypt3des(malformed_encrypted, key_hex, iv_hex)
        
        # El resultado debería ser None o diferente al texto original
        if decrypted_text is not None:
            self.assertNotEqual(plaintext, decrypted_text, 
                                "El descifrado con texto cifrado malformado produjo el texto original")

if __name__ == '__main__':
    unittest.main()