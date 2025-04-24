#!/usr/bin/env python3

import sys
import binascii

def KSA(key):
    """Algoritmo de programación de clave (Key Scheduling Algorithm)"""
    keylength = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % keylength]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def PRGA(S, data_length):
    """Algoritmo pseudo-aleatorio de generación (Pseudo-Random Generation Algorithm)"""
    i = 0
    j = 0
    keystream = []
    for _ in range(data_length):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        keystream.append(K)
    return keystream

def RC4(key, data):
    """Implementación del algoritmo RC4"""
    key = [ord(c) for c in key]
    S = KSA(key)
    keystream = PRGA(S, len(data))
    return bytes([data[i] ^ keystream[i] for i in range(len(data))])

def main():
    """Función principal del script"""
    if len(sys.argv) != 3:
        print(f"Uso: {sys.argv[0]} <ruta_del_archivo> <clave_rc4>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    rc4_key = sys.argv[2]
    
    try
        with open(file_path, 'r') as file:
            hex_content = file.read().strip()
       
        try:
            binary_data = binascii.unhexlify(hex_content)
        except binascii.Error:
            print(f"Error: El contenido del archivo no es un hexadecimal válido")
            sys.exit(1)
       
        decrypted_data = RC4(rc4_key, binary_data)
        
        try:
            print(decrypted_data.decode('utf-8'))
        except UnicodeDecodeError
            print(''.join(chr(b) if 32 <= b < 127 else '.' for b in decrypted_data))
        
    except FileNotFoundError:
        print(f"Error: El archivo {file_path} no existe")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()