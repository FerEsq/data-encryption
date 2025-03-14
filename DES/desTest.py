'''
 * Nombre: desTest.py
 * Descripción: Programa que implementa tests unitarios para el cifrado y descifrado DES.
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

#Importar funciones del módulo DES
from des import generateKey, manualPadding, deletePadding, encryptDES, decryptDES

class TestDESFunctions(unittest.TestCase):
    
    def setUp(self):
        # Crear directorio de prueba si no existe
        if not os.path.exists("test_DES"):
            os.makedirs("test_DES")
    
    def tearDown(self):
        # Eliminar archivos de prueba
        for file in ['test_DES/test_encrypted.txt', 'test_DES/test_decrypted.txt']:
            if os.path.exists(file):
                os.remove(file)
        
        # Eliminar directorio de prueba
        if os.path.exists("test_DES"):
            os.rmdir("test_DES")
    
    def test_key_generation(self):
        # Verificar que la clave generada tiene la longitud correcta (8 bytes para DES)
        key = generateKey()
        self.assertEqual(len(key), 8, "La clave generada no tiene la longitud correcta")
    
    def test_manual_padding(self):
        # Prueba de padding para texto de longitud exacta de bloque
        text_exact_block = "12345678"  # 8 bytes (tamaño de bloque DES)
        padded_exact = manualPadding(text_exact_block)
        # Debería agregar un bloque completo de padding
        self.assertEqual(len(padded_exact), 16, "El padding para texto de tamaño exacto de bloque no es correcto")
        self.assertEqual(padded_exact[-1], 8, "El último byte de padding para texto de tamaño exacto no es correcto")
        
        # Prueba de padding para texto más corto que un bloque
        text_short = "1234"  # 4 bytes
        padded_short = manualPadding(text_short)
        # Debería agregar 4 bytes de padding
        self.assertEqual(len(padded_short), 8, "El padding para texto corto no es correcto")
        self.assertEqual(padded_short[-1], 4, "El último byte de padding para texto corto no es correcto")
        
        # Prueba de padding para texto más largo que un bloque
        text_long = "123456789012"  # 12 bytes
        padded_long = manualPadding(text_long)
        # Debería agregar 4 bytes de padding
        self.assertEqual(len(padded_long), 16, "El padding para texto largo no es correcto")
        self.assertEqual(padded_long[-1], 4, "El último byte de padding para texto largo no es correcto")
    
    def test_padding_removal(self):
        # Crear datos con padding manual
        data_original = b"12345678"  # 8 bytes
        padding_byte = 8
        padded_data = data_original + bytes([padding_byte] * padding_byte)
        
        # Eliminar padding
        unpadded_data = deletePadding(padded_data)
        
        # Verificar resultado
        self.assertEqual(unpadded_data, data_original, "El padding no se eliminó correctamente")
    
    def test_encryption_decryption_simple(self):
        # Texto de prueba
        plaintext = "Esto es una prueba de cifrado DES"
        
        # Generar clave
        key = generateKey()
        
        # Cifrar
        encrypted_hex, key_hex = encryptDES(plaintext, key)
        
        # Verificar resultados del cifrado
        self.assertIsNotNone(encrypted_hex, "El texto cifrado es None")
        self.assertTrue(len(encrypted_hex) > 0, "El texto cifrado está vacío")
        
        # Descifrar
        decrypted_text = decryptDES(encrypted_hex, key_hex)
        
        # Verificar que el texto descifrado coincide con el original
        self.assertEqual(plaintext, decrypted_text, 
                        "El texto descifrado no coincide con el texto original")
    
    def test_encryption_decryption_special_chars(self):
        # Texto con caracteres especiales
        plaintext = "¡Caracteres especiales: áéíóúñ@#$%^&*(){}[]!"
        
        # Generar clave
        key = generateKey()
        
        # Cifrar
        encrypted_hex, key_hex = encryptDES(plaintext, key)
        
        # Descifrar
        decrypted_text = decryptDES(encrypted_hex, key_hex)
        
        # Verificar que el texto descifrado coincide con el original
        self.assertEqual(plaintext, decrypted_text, 
                        "El texto descifrado con caracteres especiales no coincide con el original")
    
    def test_encryption_decryption_long_text(self):
        # Texto largo
        plaintext = "Este es un texto más largo para probar el cifrado y descifrado DES. " * 10
        
        # Generar clave
        key = generateKey()
        
        # Cifrar
        encrypted_hex, key_hex = encryptDES(plaintext, key)
        
        # Descifrar
        decrypted_text = decryptDES(encrypted_hex, key_hex)
        
        # Verificar que el texto descifrado coincide con el original
        self.assertEqual(plaintext, decrypted_text, 
                        "El texto largo descifrado no coincide con el original")
    
    def test_wrong_key(self):
        # Texto de prueba
        plaintext = "Esto es una prueba de cifrado DES"
        
        # Generar clave
        key = generateKey()
        
        # Cifrar
        encrypted_hex, key_hex = encryptDES(plaintext, key)
        
        # Generar una clave incorrecta
        wrong_key = generateKey()
        wrong_key_hex = binascii.hexlify(wrong_key).decode('ascii')
        
        try:
            # Intentar descifrar con clave incorrecta
            # Nota: en algunos casos podría lanzar una excepción debido a un padding incorrecto
            decrypted_text = decryptDES(encrypted_hex, wrong_key_hex)
            
            # Si no lanzó excepción, verificar que el resultado es diferente al original
            self.assertNotEqual(plaintext, decrypted_text, 
                                "El descifrado con clave incorrecta produjo el texto original")
        except ValueError:
            # Si lanza una excepción ValueErrpr por padding inválido, la prueba pasa
            pass
        except Exception as e:
            # Cualquier otra excepción debería fallar
            self.fail(f"Descifrado con clave incorrecta lanzó una excepción inesperada: {e}")
    
    def test_malformed_ciphertext(self):
        # Texto de prueba
        plaintext = "Esto es una prueba de cifrado DES"
        
        # Generar clave
        key = generateKey()
        
        # Cifrar
        encrypted_hex, key_hex = encryptDES(plaintext, key)
        
        # Modificar el texto cifrado para que sea malformado (truncar)
        malformed_encrypted = encrypted_hex[:-2]
        
        try:
            # Intentar descifrar con texto malformado
            # Debería fallar con una excepción
            decrypted_text = decryptDES(malformed_encrypted, key_hex)
            
            # Si llegamos aquí, podría ser porque el texto malformado aún es procesable
            # pero debería ser diferente al original
            self.assertNotEqual(plaintext, decrypted_text,
                                "El descifrado con texto cifrado malformado produjo el texto original")
        except binascii.Error:
            # Excepción esperada para longitud de hex incorrecta
            pass
        except ValueError:
            # Excepción esperada para padding incorrecto
            pass
        except Exception as e:
            # Cualquier otra excepción podría ser aceptable
            pass

if __name__ == '__main__':
    unittest.main()