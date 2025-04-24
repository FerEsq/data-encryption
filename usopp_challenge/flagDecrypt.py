#!/usr/bin/env python3

import sys
import random
import binascii

def generate_keystream(seed, length):
    """Genera un flujo de clave usando un generador de números pseudoaleatorios con la semilla dada"""
    random.seed(seed)  # PRNG débil
    return bytes([random.randint(0, 255) for _ in range(length)])

def decrypt_with_seed(ciphertext, seed):
    """Intenta descifrar usando una semilla específica"""
    cipherbytes = bytes.fromhex(ciphertext)
    keystream = generate_keystream(seed, len(cipherbytes))
    plaintext = bytes([c ^ k for c, k in zip(cipherbytes, keystream)])
    return plaintext

def brute_force_decrypt(ciphertext, max_seed=100000, prefix=b"FLAG_"):
    """Fuerza bruta para encontrar la semilla correcta"""
    cipherbytes = bytes.fromhex(ciphertext)
    
    for seed in range(max_seed):
        keystream = generate_keystream(seed, len(cipherbytes))
        plaintext = bytes([c ^ k for c, k in zip(cipherbytes, keystream)])
        
        if plaintext.startswith(prefix):
            return seed, plaintext
    
    return None, None

def main():
    """Función principal del script"""
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print(f"Uso: {sys.argv[0]} <ruta_del_archivo> [semilla]")
        sys.exit(1)
    
    file_path = sys.argv[1]
    
    try:
        # Leer el contenido del archivo
        with open(file_path, 'r') as file:
            hex_content = file.read().strip()
        
        # Verificar que el contenido sea hexadecimal válido
        try:
            binascii.unhexlify(hex_content)
        except binascii.Error:
            print(f"Error: El contenido del archivo no es un hexadecimal válido")
            sys.exit(1)
        
        # Verificar si se proporcionó una semilla
        seed, plaintext = brute_force_decrypt(hex_content)
        
        if seed is not None:
            print(f"Semilla encontrada: {seed}")
            try:
                decoded = plaintext.decode('utf-8')
                print(f"Texto descifrado: {decoded}")
            except UnicodeDecodeError:
                print(f"Texto descifrado (bytes): {plaintext}")
                print(f"Representación ASCII: {''.join(chr(b) if 32 <= b < 127 else '.' for b in plaintext)}")
        else:
            print("No se pudo encontrar una semilla válida (probando prefijo 'FLAG_')")
            
            # Intentar sin buscar un prefijo específico
            for seed in range(10):  # Probar algunas semillas bajas
                plaintext = decrypt_with_seed(hex_content, seed)
                try:
                    decoded = plaintext.decode('utf-8')
                    if all(32 <= ord(c) < 127 for c in decoded):
                        print(f"Posible texto con semilla {seed}: {decoded}")
                except UnicodeDecodeError:
                    pass
                
            
    except FileNotFoundError:
        print(f"Error: El archivo {file_path} no existe")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()