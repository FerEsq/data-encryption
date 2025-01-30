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

    #Iterar sobre cada carácter del texto
    for char in text:
        asciiValue = ord(char)
        binaryValue = ""
        temp = asciiValue
        
        while temp > 0:
            binaryValue = str(temp % 2) + binaryValue
            temp //= 2
            
        binary += binaryValue.zfill(8) + " "
        binary = str(binary)
    
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
