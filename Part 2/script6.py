'''
 * Nombre: script6.py
 * Programadora: Fernanda Esquivel (esq21542@uvg.edu.gt)
 * Lenguaje: Python
 * Recursos: VSCode
 * Historial: 
    - Finalizado el 28.01.2025
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

'''
Función principal que maneja la interacción con el usuario.
'''
def main():
    while True:
        #Imprimir menú
        print("\n1. Aplicar XOR a un BINARIO")
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
        bin1 = input("\nIngrese el primer binario (sin espacios): ")
        bin2 = input("Ingrese el segundo binario (sin espacios): ")
        
        #Validar texto
        if not bin1 or not bin2:
            print("El texto no puede estar vacío.")
            continue
        
        #Convertir a binario
        if choice == "1":
            xor = xorBinary(bin1, bin2)
            print(f"\nXOR de los binarios: {xor}")        

if __name__ == "__main__":
    main()
