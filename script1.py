'''
 * Nombre: script1.py
 * Descripción: Función que convierte un string en su representación binaria ASCII (8 bits por carácter).
 * Programadora: Fernanda Esquivel (esq21542@uvg.edu.gt)
 * Lenguaje: Python
 * Recursos: VSCode
 * Historial: 
    - Finalizado el 09.02.2025
'''

def asciiToBinary(text):
    binary = ""
    asciiCodes = []

    #Iterar sobre cada carácter del texto
    for char in text:
        asciiValue = ord(char)
        asciiCodes.append(asciiValue)
        binaryValue = ""
        temp = asciiValue
        
        while temp > 0:
            binaryValue = str(temp % 2) + binaryValue
            temp //= 2
            
        binary += binaryValue.zfill(8) + " "
        binary = str(binary)
    
    return binary, asciiCodes

'''
Función principal que maneja la interacción con el usuario.
'''
def main():
    while True:
        #Imprimir menú
        print("\n1. Convertir de STRING a BINARIO")
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
        text = input("\nIngrese el texto para convertir: ")
        
        #Validar texto
        if not text:
            print("El texto no puede estar vacío.")
            continue
        
        #Convertir a binario
        if choice == "1":
            binary, ascii = asciiToBinary(text)
            print(f"\nTexto en binario: {binary}")
            print(f"Valores ASCII: {ascii}")   

if __name__ == "__main__":
    main()