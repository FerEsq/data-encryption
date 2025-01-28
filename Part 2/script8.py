'''
 * Nombre: script8.py
 * Programadora: Fernanda Esquivel (esq21542@uvg.edu.gt)
 * Lenguaje: Python
 * Recursos: VSCode
 * Historial: 
    - Finalizado el 28.01.2025
'''

'''
ASCII a Binario
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
            
        binary += binaryValue.zfill(8)
        binary = str(binary)
    
    return binary

'''
XOR de los Binarios
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

def encrypt(text, key):
    #Convertir texto y key a binario
    textBinary = asciiToBinary(text)
    keyBinary = asciiToBinary(key)
    
    #Aplicar XOR
    encryptedBinary = xorBinary(textBinary, keyBinary)

    blocks = [encryptedBinary[i:i+8] for i in range(0, len(encryptedBinary), 8)]
    
    #Unir los bloques separados por un espacio
    result = " ".join(blocks)
    
    return result

'''
Binario a ASCII
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
        print("\n1. Encriptar texto")
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
        text = input("\nIngrese el texto para encriptar: ")
        key = input("Ingrese la key para encriptar: ")
        
        #Validar texto
        if not text or not key:
            print("El texto o key no puede estar vacío")
            continue
        elif len(text) != len(key):
            print("La longitud no es válida")
            continue
        
        #Convertir a binario
        if choice == "1":
            encryptedBin = encrypt(text, key)
            encrypted, ascii = binaryToAscii(encryptedBin)
            print(f"\nTexto encriptado en binario: {encryptedBin}")
            print(f"Texto encriptado en ASCII: {encrypted}")   

if __name__ == "__main__":
    main()
