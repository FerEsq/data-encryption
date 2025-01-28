'''
 * Nombre: script1.py
 * Programadora: Fernanda Esquivel (esq21542@uvg.edu.gt)
 * Lenguaje: Python
 * Recursos: VSCode
 * Historial: 
    - Finalizado el 27.01.2025
'''

def asciiToBinary(text):
    binary = ""
    asciiCodes = {char: ord(char) for char in text} #Obtener el valor ASCII de cada char
    
    #Convertir cada valor ASCII a binario
    for char, asciiValue in asciiCodes.items():
        binaryValue = ""
        temp = asciiValue
        while temp > 0:
            binaryValue = str(temp % 2) + binaryValue  #Agregar el residuo a la izquierda
            temp //= 2  #Reducir el número dividiendo por 2
        
        #Asegurar que sean 8 bits
        binaryValue = binaryValue.zfill(8)
        
        #Concatenar el binario al resultado
        binary += binaryValue + " "
    
    return binary

'''
Función principal que maneja la interacción con el usuario.
'''
def main():
    while True:
        #Imprimir menú
        print("\n1. Convertir de ASCII a BINARIO")
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
            binary = asciiToBinary(text)
            print(f"\nTexto en binario: {binary}")          

if __name__ == "__main__":
    main()
