'''
 * Nombre: script1.py
 * Descripción: Programa que realiza el XOR entre una imagen en b64 y una key.
 * Programadora: Fernanda Esquivel (esq21542@uvg.edu.gt)
 * Lenguaje: Python
 * Recursos: VSCode
 * Historial: 
    - Finalizado el 11.02.2025
'''

import numpy as np
from PIL import Image
import base64
from io import BytesIO

base64Chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

'''
Funciones auxiliares
'''
def base64ToBinary(b64STR):
    # Agregar verificación de padding antes de eliminarlo
    padding_length = b64STR.count('=')
    b64STR = b64STR.rstrip('=')
    
    binary = ''
    for char in b64STR:
        if char in base64Chars:
            index = base64Chars.index(char)
            binary += format(index, '06b')  # Usar format es más seguro
            
    # Ajustar longitud según el padding
    if padding_length > 0:
        binary = binary[:-padding_length * 2]
        
    return binary

def textToBinary(text):
    binary = ""

    #Iterar sobre cada carácter del texto
    for char in text:
        asciiValue = ord(char)
        binaryValue = ""
        temp = asciiValue
        
        while temp > 0:
            binaryValue = str(temp % 2) + binaryValue
            temp //= 2
            
        binary += binaryValue.zfill(8)
        binary = str(binary)
    
    return binary

def binaryToBase64(binary):   
    #Eliminar espacios entre bloques de 8 bits
    binary = binary.replace(" ", "")
    
    #Asegurarse de que el binario tenga un número de bits divisible por 6
    while len(binary) % 6 != 0:
        binary += "0"  #Agregar ceros al final 
    
    #Dividir el binario en bloques de 6 bits
    chunks = [binary[i:i+6] for i in range(0, len(binary), 6)]
    
    #Convertir cada bloque a su valor decimal y mapear al carácter Base64
    b64 = "".join(base64Chars[int(chunk, 2)] for chunk in chunks)
    
    #Agregar padding "=" si el número original de bits no era múltiplo de 24
    while len(b64) % 4 != 0:
        b64 += "="
    
    return b64

def completeBinary(binary, length):
    #Si el binario es más largo que target_length, lo cortamos
    if len(binary) > length:
        return binary[:length]
    
    #Si el binario es más corto, lo repetimos
    repetitions = length // len(binary) + 1
    repeated = binary * repetitions
    
    # Cortamos al tamaño exacto
    return repeated[:length]

'''
Imagen a B64
'''
def fileToBytes(filepath):
    try:
        with open(filepath, 'rb') as f:
            return f.read()
    except Exception as e:
        print(f"Error leyendo archivo: {e}")
        return None

def bytesToB64(byte_data):
    try:
        return base64.b64encode(byte_data).decode('utf-8')
    except Exception as e:
        print(f"Error en conversión a base64: {e}")
        return None

'''
XOR de Binarios
'''
def xorBinary(bin1, bin2):
    #Verificar que ambos binarios tengan la misma longitud
    maxLength = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(maxLength)  #Rellenar con ceros a la izquierda
    bin2 = bin2.zfill(maxLength)
    
    #Aplicar XOR
    xorResult = ''
    for b1, b2 in zip(bin1, bin2):
        xorResult += '1' if b1 != b2 else '0'

    return xorResult

'''
Base64 a Imagen
'''
def b64ToImage(b64Str, outputPath):
    try:
        image_bytes = base64.b64decode(b64Str)
        with open(outputPath, 'wb') as f:
            f.write(image_bytes)
        return True
    except Exception as e:
        print(f"Error guardando imagen: {e}")
        return False

'''
Función principal que maneja la interacción con el usuario.
'''
def main():    
    #Convertir imagen a base64
    imgBytes = fileToBytes("Exercise1/imagen_xor.png")
    imgb64 = bytesToB64(imgBytes)

    #Convertir imagen a binario
    imgbin = base64ToBinary(imgb64)

    #Convertir llave a binario
    binaryKey = textToBinary("cifrados_2025")
    binaryKey = completeBinary(binaryKey, len(imgbin))

    #XOR de los binarios
    xor = xorBinary(imgbin, binaryKey)

    #Convertir el resultado a base64
    result = binaryToBase64(xor)

    #Crear imagen a partir del resultado
    flag = b64ToImage(result, "Exercise1/xor_result.png")
    print("\nImagen guardada como 'Exercise1/xor_result.png'")

if __name__ == "__main__":
    main()