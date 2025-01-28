'''
 * Nombre: script4.py
 * Programadora: Fernanda Esquivel (esq21542@uvg.edu.gt)
 * Lenguaje: Python
 * Recursos: VSCode
 * Historial: 
    - Finalizado el 27.01.2025
'''

def byteToDecimal(byteSTR):
    decimal = 0
    potencia = 0
    
    #Iterar bits de derecha a izquierda
    for bit in reversed(byteSTR):
        if bit == '1':
            # Calculamos 2^potencia 
            valor = 1
            for _ in range(potencia):
                valor *= 2
            decimal += valor
        potencia += 1
        
    return decimal

def binaryToAscii(binary):
    #Dividir la cadena binaria en bloques de 8 bits
    blocks = binary.split(" ")
    
    #Convertir cada bloque de binario a decimal y luego a su carácter ASCII
    text = ""
    ascii = []
    for block in blocks:
        asciiCode = byteToDecimal(block)
        ascii.append(asciiCode)
        text += chr(asciiCode)
    
    return text, ascii

'''
Función principal que maneja la interacción con el usuario.
'''
def main():
    while True:
        #Imprimir menú
        print("\n1. Convertir de BINARIO a ASCII")
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
        text = input("\nIngrese el texto para convertir (colocar un espacio entre cada byte): ")
        
        #Validar texto
        if not text:
            print("El texto no puede estar vacío.")
            continue
        
        #Convertir a binario
        if choice == "1":
            text, ascii = binaryToAscii(text)
            print(f"Códigos ascii de cada carácter: {ascii}")    
            print(f"Texto en ascii: {text}")          

if __name__ == "__main__":
    main()
