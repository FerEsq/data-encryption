'''
 * Nombre: script3.py
 * Programadora: Fernanda Esquivel (esq21542@uvg.edu.gt)
 * Lenguaje: Python
 * Recursos: VSCode
 * Historial: 
    - Finalizado el 27.01.2025
'''

base64Chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

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
Función principal que maneja la interacción con el usuario.
'''
def main():
    while True:
        #Imprimir menú
        print("\n1. Convertir de BINARIO a BASE64")
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
        text = input("\nIngrese el texto para convertir (colocar un espacio entr cada byte): ")
        
        #Validar texto
        if not text:
            print("El texto no puede estar vacío.")
            continue
        
        #Convertir a binario
        if choice == "1":
            b64 = binaryToBase64(text)
            print(f"Texto en binario: {b64}")          

if __name__ == "__main__":
    main()
