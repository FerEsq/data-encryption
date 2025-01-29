'''
 * Nombre: script2.py
 * Programadora: Fernanda Esquivel (esq21542@uvg.edu.gt)
 * Lenguaje: Python
 * Recursos: VSCode
 * Historial: 
    - Finalizado el 27.01.2025
'''

base64Chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def charToBase64(char):    
    #Buscar el índice del carácter
    return str(base64Chars.index(char))

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
            
            binary += bits + " "
            
    return binary

'''
Función principal que maneja la interacción con el usuario.
'''
def main():
    while True:
        #Imprimir menú
        print("\n1. Convertir de BASE64 a BINARIO")
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
            binary = base64ToBinary(text)
            print(f"Texto en binario: {binary}")          

if __name__ == "__main__":
    main()
