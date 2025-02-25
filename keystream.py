'''
 * Nombre: keystream.py
 * Descripción: Programa que genera un keystream aleatorio.
 * Programadora: Fernanda Esquivel (esq21542@uvg.edu.gt)
 * Lenguaje: Python
 * Recursos: VSCode
 * Historial:
    - Creado el 21.02.2025
    - Finalizado el 24.02.2025
'''

import random

def keystreamGenerator(messageLen, seed):
    #Inicializa el generador con la semilla proporcionada
    random.seed(seed)
    
    #Genera bytes pseudoaleatorios y los convierte a string hexadecimal
    keystream = ''
    for _ in range(messageLen):
        #Genera un byte aleatorio y lo convierte a hexadecimal
        random_byte = random.randint(0, 255)
        keystream += format(random_byte, '02x')  # '02x' formatea el número como hex con 2 dígitos
    
    return keystream

'''
Función principal que maneja la interacción con el usuario.
'''
def main():
    while True:
        #Imprimir menú
        print("\n1. Generar keystream")
        print("2. Salir")
        choice = input("\nSeleccione una opción (1-2): ")
        
        #Salir
        if choice == "2":
            break
        
        #Validar opción
        if choice not in ["1"]:
            print("Opción no válida. Por favor, seleccione 1 o 2.")
            continue
        
        #Obtener texto
        text = input("\nIngrese el texto a cifrar: ")
        seed = input("Ingrese la contraseña (seed): ")
        
        #Validar texto
        if not text or not seed:
            print("El texto o seed no puede estar vacío")
            continue
        
        #Convertir a binario
        if choice == "1":            
            # Genera un keystream de la misma longitud que el mensaje
            stream = keystreamGenerator(len(text), seed)
            print(f"Longitud del mensaje: {len(text)}")
            print(f"Keystream generado: {stream}")  

if __name__ == "__main__":
    main()