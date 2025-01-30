'''
 * Nombre: script2.py
 * Programadora: Fernanda Esquivel (esq21542@uvg.edu.gt)
 * Lenguaje: Python
 * Recursos: VSCode
 * Historial: 
    - Finalizado el 27.01.2025
'''

base64Chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def textToBase64(char):
    #Manejo de ñ y Ñ
    byte_val = char.encode('utf-8')
    bits = ''.join(format(b, '08b') for b in byte_val)
    
    #Agrupar en 6 bits
    while len(bits) % 6:
        bits += '0'
    
    b64Value = ''
    for i in range(0, len(bits), 6):
        chunk = bits[i:i+6]
        index = int(chunk, 2)
        b64Value += base64Chars[index]
    
    while len(b64Value) % 4:
        b64Value += '='
        
    return b64Value


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

def sixToEightBlocks(binary_input):
    # Unir todos los bits en una sola cadena
    all_bits = binary_input.replace(" ", "")

    #Separar en bloques de 8 bits
    blocksOf8 = []
    for i in range(0, len(all_bits) - 7, 8):
        block = all_bits[i:i+8]
        blocksOf8.append(block)
    
    #Formatear la salida
    result = " ".join(blocksOf8)
    
    return result

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
            #b64 = textToBase64(text)
            binary = base64ToBinary(text)
            binary = sixToEightBlocks(binary)
            #print(f"\nTexto en base64: {b64}")  
            print(f"Texto en binario: {binary}")          

if __name__ == "__main__":
    main()