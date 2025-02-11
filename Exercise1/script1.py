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
    #Dict para mapear caracteres base64 a sus índices
    base64Index = {char: index for index, char in enumerate(base64Chars)}
    
    #Eliminar padding si existe
    b64STR = b64STR.rstrip('=')
    
    #Convertir cada carácter base64 a su binario de 6 bits
    binary = ''
    for char in b64STR:
        if char in base64Index:
            #Obtener el índice del carácter en la tabla base64
            index = base64Index[char]
            
            #Convertir el índice a binario
            bits = ''
            num = index
            for _ in range(6):
                bits = ('1' if num & 1 else '0') + bits 
                num >>= 1
            
            binary += bits
            
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

'''
Imagen a B64
'''
def imageToB64(imagepath):
    #Abrir la imagen usando Pillow
    img = Image.open(imagepath)
    
    #Convertir la imagen a un array de bytes usando BytesIO
    buffer = BytesIO()
    img.save(buffer, format=img.format or 'PNG')
    imgBytes = buffer.getvalue()
    
    #Convertir los bytes a base64
    base64String = base64.b64encode(imgBytes).decode('utf-8')
    
    return base64String

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
    """Intenta convertir un string base64 a imagen"""
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

    #Convertir llave a binario
    binaryKey = textToBinary("cifrados_2025")

    #XOR de los binarios
    xor = xorBinary(imgb64, binaryKey)

    #Convertir el resultado a base64
    result = binaryToBase64(xor)

    #Crear imagen a partir del resultado
    flag = b64ToImage(result, "Exercise1/xor_result.jpg")
    print("\nImagen guardada como xor_result.jpg")



if __name__ == "__main__":
    main()