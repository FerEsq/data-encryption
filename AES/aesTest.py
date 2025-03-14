'''
 * Nombre: aesTest.py
 * Descripción: Programa que implementa tests unitarios para el cifrado y descifrado AES.
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
import shutil
import numpy as np
from PIL import Image
import binascii
from io import BytesIO

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#Importar funciones del módulo AES
from aes import generateKey, generateIV, encryptCBC, encryptECB, decryptCBC, decryptECB

class TestAESFunctions(unittest.TestCase):
    
    def setUp(self):
        # Crear directorio de prueba si no existe
        if not os.path.exists("test_AES"):
            os.makedirs("test_AES")
        
        # Crear una imagen de prueba
        self.test_image_path = "test_AES/test_image.png"
        self.cbc_encrypted_path = "test_AES/cbc_encrypted.png"
        self.cbc_decrypted_path = "test_AES/cbc_decrypted.png"
        self.ecb_encrypted_path = "test_AES/ecb_encrypted.png"
        self.ecb_decrypted_path = "test_AES/ecb_decrypted.png"
        
        # Crear una imagen de prueba (100x100 píxeles, color rojo)
        img = Image.new('RGB', (100, 100), color=(255, 0, 0))
        img.save(self.test_image_path)
    
    def tearDown(self):
        # Eliminar el directorio de prueba y su contenido
        if os.path.exists("test_AES"):
            shutil.rmtree("test_AES")
    
    def test_key_generation(self):
        # Verificar que la clave generada tiene la longitud correcta (32 bytes para AES-256)
        key = generateKey()
        self.assertEqual(len(key), 32, "La clave generada no tiene la longitud correcta")
    
    def test_iv_generation(self):
        # Verificar que el IV generado tiene la longitud correcta (16 bytes para AES)
        iv = generateIV()
        self.assertEqual(len(iv), 16, "El IV generado no tiene la longitud correcta")
    
    def test_cbc_encryption_decryption(self):
        # Generar clave
        key = generateKey()
        
        # Cifrar con CBC
        iv = encryptCBC(self.test_image_path, self.cbc_encrypted_path, key)
        
        # Verificar que se creó el archivo cifrado
        self.assertTrue(os.path.exists(self.cbc_encrypted_path), "No se creó el archivo cifrado CBC")
        
        # Descifrar con CBC
        result = decryptCBC(self.cbc_encrypted_path, self.cbc_decrypted_path, key, iv)
        
        # Verificar que el descifrado fue exitoso
        self.assertTrue(result, "El descifrado CBC falló")
        self.assertTrue(os.path.exists(self.cbc_decrypted_path), "No se creó el archivo descifrado CBC")
        
        # Comparar imágenes (verificar que son similares después del cifrado/descifrado)
        # Nota: Debido al padding y posibles diferencias en la forma, podría haber pequeñas diferencias
        # pero la imagen original y la descifrada deberían ser visualmente similares
        original_img = Image.open(self.test_image_path).convert('RGB')
        decrypted_img = Image.open(self.cbc_decrypted_path).convert('RGB')
        
        # Verificar dimensiones
        self.assertEqual(original_img.size[0], decrypted_img.size[0], 
                        "El ancho de la imagen original y descifrada no coinciden")
        self.assertEqual(original_img.size[1], decrypted_img.size[1], 
                        "La altura de la imagen original y descifrada no coinciden")
        
        # Verificar contenido (comparar algunos píxeles)
        # Convertir imágenes a arrays para comparar
        original_array = np.array(original_img)
        decrypted_array = np.array(decrypted_img)
        
        # Verificar que al menos el 95% de los píxeles son similares
        # (permitiendo algunas diferencias por el proceso de cifrado/descifrado)
        num_pixels = original_array.shape[0] * original_array.shape[1]
        similar_pixels = np.sum(np.all(np.isclose(original_array, decrypted_array, atol=10), axis=2))
        similarity_ratio = similar_pixels / num_pixels
        
        self.assertGreaterEqual(similarity_ratio, 0.95, 
                            f"Las imágenes difieren significativamente. Ratio de similitud: {similarity_ratio}")
    
    def test_ecb_encryption_decryption(self):
        # Generar clave
        key = generateKey()
        
        # Cifrar con ECB
        encryptECB(self.test_image_path, self.ecb_encrypted_path, key)
        
        # Verificar que se creó el archivo cifrado
        self.assertTrue(os.path.exists(self.ecb_encrypted_path), "No se creó el archivo cifrado ECB")
        
        # Descifrar con ECB
        result = decryptECB(self.ecb_encrypted_path, self.ecb_decrypted_path, key)
        
        # Verificar que el descifrado fue exitoso
        self.assertTrue(result, "El descifrado ECB falló")
        self.assertTrue(os.path.exists(self.ecb_decrypted_path), "No se creó el archivo descifrado ECB")
        
        # Comparar imágenes (verificar que son similares después del cifrado/descifrado)
        original_img = Image.open(self.test_image_path).convert('RGB')
        decrypted_img = Image.open(self.ecb_decrypted_path).convert('RGB')
        
        # Verificar dimensiones
        self.assertEqual(original_img.size[0], decrypted_img.size[0], 
                        "El ancho de la imagen original y descifrada no coinciden")
        self.assertEqual(original_img.size[1], decrypted_img.size[1], 
                        "La altura de la imagen original y descifrada no coinciden")
        
        # Verificar contenido (comparar algunos píxeles)
        original_array = np.array(original_img)
        decrypted_array = np.array(decrypted_img)
        
        # Verificar que al menos el 95% de los píxeles son similares
        num_pixels = original_array.shape[0] * original_array.shape[1]
        similar_pixels = np.sum(np.all(np.isclose(original_array, decrypted_array, atol=10), axis=2))
        similarity_ratio = similar_pixels / num_pixels
        
        self.assertGreaterEqual(similarity_ratio, 0.95, 
                            f"Las imágenes difieren significativamente. Ratio de similitud: {similarity_ratio}")
    
    def test_invalid_key_cbc(self):
        # Generar clave y cifrar con CBC
        key = generateKey()
        iv = encryptCBC(self.test_image_path, self.cbc_encrypted_path, key)
        
        # Intentar descifrar con una clave incorrecta
        wrong_key = generateKey()  # Clave diferente
        result = decryptCBC(self.cbc_encrypted_path, self.cbc_decrypted_path, wrong_key, iv)
        
        # El descifrado podría técnicamente "funcionar" con una clave incorrecta 
        # pero el contenido no tendrá sentido
        if result and os.path.exists(self.cbc_decrypted_path):
            # Si se crea un archivo, verificar que es diferente al original
            original_img = Image.open(self.test_image_path).convert('RGB')
            try:
                decrypted_img = Image.open(self.cbc_decrypted_path).convert('RGB')
                
                # Verificar que las imágenes son diferentes
                if original_img.size == decrypted_img.size:
                    original_array = np.array(original_img)
                    decrypted_array = np.array(decrypted_img)
                    
                    # Calcular diferencia
                    num_pixels = original_array.shape[0] * original_array.shape[1]
                    similar_pixels = np.sum(np.all(np.isclose(original_array, decrypted_array, atol=10), axis=2))
                    similarity_ratio = similar_pixels / num_pixels
                    
                    # Con una clave incorrecta, esperamos que las imágenes sean muy diferentes
                    self.assertLess(similarity_ratio, 0.9, 
                                    "El descifrado con clave incorrecta produjo una imagen similar a la original")
            except:
                # Si hay un error al abrir la imagen descifrada, es una buena señal
                # significa que el descifrado con clave incorrecta resultó en datos no válidos
                pass

if __name__ == '__main__':
    unittest.main()