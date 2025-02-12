'''
 * Nombre: script2.py
 * Descripción: Programa que realiza el XOR entre dos imágenes.
 * Programadora: Fernanda Esquivel (esq21542@uvg.edu.gt)
 * Lenguaje: Python
 * Recursos: VSCode
 * Historial: 
    - Finalizado el 11.02.2025
'''

import numpy as np
from PIL import Image
import time

'''
Procesamiento de la imagen
'''
def processImg(path):
    #Abrir imagen y convertir a RGB
    img = Image.open(path).convert('RGB')
    
    #Convertir a array de numpy
    return np.array(img)

def saveImg(array, outputPath):
    #Asegurar que los valores estén en el rango correcto (0-255)
    array = array.astype(np.uint8)
    
    #Convertir array a imagen
    img = Image.fromarray(array)
    
    #Guardar imagen
    img.save(outputPath)

def main():
    start = time.time()

    #Cargar primera imagen
    img1Array = processImg("Exercise2/image1.png")
    
    #Cargar segunda imagen y redimensionarla
    img2Array = processImg("Exercise2/image2.png")
    
    #Realizar XOR
    xor = np.bitwise_xor(img1Array, img2Array)
    
    #Invertir colores
    xor = 255 - xor
    
    #Guardar resultado
    saveImg(xor, "Exercise2/result.png")
    
    end = time.time()
    timelapse = round(end - start, 2)

    print("\nImagen guardada como 'Exercise2/result.png'")
    print(f"\nTiempo: {timelapse} segundos")

if __name__ == "__main__":
    main()