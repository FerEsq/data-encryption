'''
 * Nombre: chacha.py
 * Descripción: Programa que implementa un cifrado ChaCha20 y lo compara con un cifrado AES.
 * Programadora: Fernanda Esquivel (esq21542@uvg.edu.gt)
 * Lenguaje: Python
 * Recursos: VSCode
 * Historial:
    - Creado el 17.03.2025
    - Finalizado el 18.03.2025
'''

import os
import time
import psutil
import threading
import matplotlib.pyplot as plt
from Crypto.Cipher import ChaCha20, AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from concurrent.futures import ThreadPoolExecutor

'''
Obtiene el uso de memoria del proceso actual en MB
'''
def getMemoryUsage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 / 1024  #Convertir a MB


def chacha20Encrypt(data, key):
    cipher = ChaCha20.new(key=key)
    ciphertext = cipher.encrypt(data)
    return cipher.nonce + ciphertext


def chacha20Decrypt(encryptedData, key):
    nonce = encryptedData[:8]
    ciphertext = encryptedData[8:]
    cipher = ChaCha20.new(key=key, nonce=nonce)
    return cipher.decrypt(ciphertext)


def aesEncrypt(data, key):
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    #Asegurarse de que los datos son múltiplos de 16 bytes (bloque AES)
    paddedData = pad(data, AES.block_size)
    ciphertext = cipher.encrypt(paddedData)
    return iv + ciphertext


def aesDecrypt(encrypted_data, key):
    iv = encrypted_data[:AES.block_size]
    ciphertext = encrypted_data[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    paddedData = cipher.decrypt(ciphertext)
    return unpad(paddedData, AES.block_size)


def getEncryptionStats(algorithm_name, encrypt_func, decrypt_func, data, key):
    start_memory = getMemoryUsage()
    
    #Medir tiempo de cifrado
    start_time = time.time()
    encrypted = encrypt_func(data, key)
    encrypt_time = time.time() - start_time
    
    #Medir uso de memoria
    memory_used = getMemoryUsage() - start_memory
    
    #Medir tiempo de descifrado
    start_time = time.time()
    decrypted = decrypt_func(encrypted, key)
    decrypt_time = time.time() - start_time
    
    #Verificar que el descifrado funciona correctamente
    if decrypted != data:
        raise ValueError(f"{algorithm_name} - Error en descifrado: los datos no coinciden")
    
    return {
        'encrypt_time': encrypt_time,
        'decrypt_time': decrypt_time,
        'memory': memory_used
    }


def threadStats(data_sizes, repetitions=5):
    results = {
        'data_sizes': data_sizes,
        'chacha20': {'encrypt_time': [], 'decrypt_time': [], 'memory': []},
        'aes': {'encrypt_time': [], 'decrypt_time': [], 'memory': []}
    }
    
    for size in data_sizes:        
        # Resultados para este tamaño de datos
        chacha_results = []
        aes_results = []
        
        for _ in range(repetitions):
            # Generar datos y claves aleatorias para cada repetición
            data = get_random_bytes(size)
            chacha_key = get_random_bytes(32)  # ChaCha20 usa llaves de 256 bits
            aes_key = get_random_bytes(32)     # AES-256
            
            # Usar ThreadPoolExecutor para ejecutar ambos algoritmos en paralelo
            with ThreadPoolExecutor(max_workers=2) as executor:
                chacha_future = executor.submit(
                    getEncryptionStats, 
                    "ChaCha20", chacha20Encrypt, chacha20Decrypt, 
                    data, chacha_key
                )
                
                aes_future = executor.submit(
                    getEncryptionStats, 
                    "AES-CBC", aesEncrypt, aesDecrypt, 
                    data, aes_key
                )
                
                # Obtener resultados
                chacha_results.append(chacha_future.result())
                aes_results.append(aes_future.result())
        
        # Calcular promedios para este tamaño de datos
        results['chacha20']['encrypt_time'].append(
            sum(res['encrypt_time'] for res in chacha_results) / repetitions
        )
        results['chacha20']['decrypt_time'].append(
            sum(res['decrypt_time'] for res in chacha_results) / repetitions
        )
        results['chacha20']['memory'].append(
            sum(res['memory'] for res in chacha_results) / repetitions
        )
        
        results['aes']['encrypt_time'].append(
            sum(res['encrypt_time'] for res in aes_results) / repetitions
        )
        results['aes']['decrypt_time'].append(
            sum(res['decrypt_time'] for res in aes_results) / repetitions
        )
        results['aes']['memory'].append(
            sum(res['memory'] for res in aes_results) / repetitions
        )
    
    return results


def plotResults(results):
    data_sizes_kb = [size/1024 for size in results['data_sizes']]
    
    # Configuración de subplots
    fig, axes = plt.subplots(3, 1, figsize=(10, 15))
    
    # Gráfico de tiempo de cifrado
    axes[0].plot(data_sizes_kb, results['chacha20']['encrypt_time'], 'o-', label='ChaCha20')
    axes[0].plot(data_sizes_kb, results['aes']['encrypt_time'], 's-', label='AES-CBC')
    axes[0].set_xlabel('Tamaño de datos (KB)')
    axes[0].set_ylabel('Tiempo (segundos)')
    axes[0].set_title('Tiempo de cifrado')
    axes[0].legend()
    axes[0].grid(True)
    
    # Gráfico de tiempo de descifrado
    axes[1].plot(data_sizes_kb, results['chacha20']['decrypt_time'], 'o-', label='ChaCha20')
    axes[1].plot(data_sizes_kb, results['aes']['decrypt_time'], 's-', label='AES-CBC')
    axes[1].set_xlabel('Tamaño de datos (KB)')
    axes[1].set_ylabel('Tiempo (segundos)')
    axes[1].set_title('Tiempo de descifrado')
    axes[1].legend()
    axes[1].grid(True)
    
    # Gráfico de uso de memoria
    axes[2].plot(data_sizes_kb, results['chacha20']['memory'], 'o-', label='ChaCha20')
    axes[2].plot(data_sizes_kb, results['aes']['memory'], 's-', label='AES-CBC')
    axes[2].set_xlabel('Tamaño de datos (KB)')
    axes[2].set_ylabel('Memoria (MB)')
    axes[2].set_title('Consumo de memoria')
    axes[2].legend()
    axes[2].grid(True)
    
    plt.tight_layout()
    plt.savefig('Part3/comparationResults.png')
    print("\nGráficos guardados en 'Part3/comparationResults.png'")


def main():
    #Tamaños de datos a probar (desde 10KB hasta 10MB)
    dataSizes = [10*1024, 100*1024, 500*1024, 1*1024*1024, 5*1024*1024, 10*1024*1024]

    results = threadStats(dataSizes)
    
    #Mostrar resultados
    print("\nResultados:")
    for i, size in enumerate(results['data_sizes']):
        print(f"\nTamaño de datos: {size/1024:.2f} KB")
        print(f"ChaCha20 - Tiempo de cifrado: {results['chacha20']['encrypt_time'][i]:.6f}s, "
                f"Tiempo de descifrado: {results['chacha20']['decrypt_time'][i]:.6f}s, "
                f"Memoria: {results['chacha20']['memory'][i]:.4f} MB")
        print(f"AES-CBC  - Tiempo de cifrado: {results['aes']['encrypt_time'][i]:.6f}s, "
                f"Tiempo de descifrado: {results['aes']['decrypt_time'][i]:.6f}s, "
                f"Memoria: {results['aes']['memory'][i]:.4f} MB")
    
    #Generar gráficos
    plotResults(results)


if __name__ == "__main__":
    main()