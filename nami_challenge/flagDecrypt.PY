#!/usr/bin/env python3

import sys
import binascii
from Crypto.Cipher import ChaCha20

def generate_key_nonce(user_id):
    """Genera la clave y el nonce a partir del ID de usuario"""
    key = (user_id.encode() * 32)[:32]  # Derivar clave de 256 bits del ID
    nonce = (user_id.encode() * 8)[:8]  # Derivar nonce de 64 bits del ID
    return key, nonce

def chacha20_decrypt(ciphertext, user_id):
    """Descifra el texto usando ChaCha20"""
    key, nonce = generate_key_nonce(user_id=user_id)
    cipher = ChaCha20.new(key=key, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

def main():
    """Función principal del script"""
    if len(sys.argv) != 3:
        print(f"Uso: {sys.argv[0]} <ruta_del_archivo> <user_id>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    user_id = sys.argv[2]
    
    try:
        # Leer el contenido del archivo
        with open(file_path, 'r') as file:
            hex_content = file.read().strip()
        
        # Verificar que el contenido sea hexadecimal válido
        try:
            ciphertext = binascii.unhexlify(hex_content)
        except binascii.Error:
            print(f"Error: El contenido del archivo no es un hexadecimal válido")
            sys.exit(1)
        
        # Descifrar el contenido
        plaintext = chacha20_decrypt(ciphertext, user_id)
        
        # Intentar mostrar como texto
        try:
            decoded = plaintext.decode('utf-8')
            print(f"Texto descifrado: {decoded}")
        except UnicodeDecodeError:
            print(f"El texto descifrado no es UTF-8 válido.")
            print(f"Bytes descifrados: {plaintext}")
            print(f"Representación ASCII: {''.join(chr(b) if 32 <= b < 127 else '.' for b in plaintext)}")
    
    except FileNotFoundError:
        print(f"Error: El archivo {file_path} no existe")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()