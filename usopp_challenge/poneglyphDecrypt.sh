#!/bin/bash

#Verificar que se proporcione el carné como argumento
if [ $# -ne 1 ]; then
    echo "Uso: $0 <tu_carné>"
    exit 1
fi

STUDENT_ID=$1

#Definir los nombres de los directorios y archivos
IMAGE_PATH="poneglyph.jpeg"  # Asumiendo que está en el mismo directorio
OUTPUT_FILE="decrypted.txt"  # Archivo donde se guardará el texto descifrado

#Crear el archivo luffy_xor.py con el contenido correcto
cat > luffy_xor.py << 'EOF'
def xor_cipher(text, key):
    # Convertir tanto el texto como la clave a bytes
    if type(text) == str:
        text_bytes = text.encode()
    else:
        text_bytes = text
    key_bytes = key.encode()  # Convertir la clave a bytes

    # Cifrar con XOR
    cipher_text = bytes([text_bytes[i] ^ key_bytes[i % len(key_bytes)] for i in range(len(text_bytes))])
    
    return cipher_text
EOF

#Crear un script Python temporal para la extracción
cat > extract_script.py << 'EOF'
from PIL import Image
import piexif
import sys
from luffy_xor import xor_cipher

def extraer_texto_metadata(imagen_path):
    # Abrir la imagen
    img = Image.open(imagen_path)
    
    # Obtener los metadatos EXIF
    try:
        exif_data = img.info.get('exif')
        if not exif_data:
            return None
            
        exif_dict = piexif.load(exif_data)
        
        # Obtener el texto almacenado en 'Artist'
        texto = exif_dict['0th'].get(piexif.ImageIFD.Artist)
        if texto:
            return texto
        return None
    except Exception as e:
        print(f"Error al extraer metadatos: {e}")
        return None

# Obtener argumentos
if len(sys.argv) != 4:
    print("Uso: python script.py <imagen_path> <carné> <output_file>")
    sys.exit(1)

imagen_path = sys.argv[1]
student_id = sys.argv[2]
output_file = sys.argv[3]

# Extraer y descifrar
texto_cifrado = extraer_texto_metadata(imagen_path)
if texto_cifrado:
    try:
        # Aplicar XOR y decodificar si es posible
        texto_descifrado = xor_cipher(texto_cifrado, student_id)
        try:
            # Intentar decodificar como UTF-8
            decoded_text = texto_descifrado.decode('utf-8')
            
            # Guardar en archivo
            with open(output_file, 'w') as f:
                f.write(decoded_text)
                
            # Mostrar en pantalla
            print(decoded_text)
            
        except UnicodeDecodeError:
            # Si falla la decodificación UTF-8, guardar como bytes en archivo binario
            with open(output_file, 'wb') as f:
                f.write(texto_descifrado)
                
            # Mostrar en pantalla
            print(texto_descifrado)
            print(f"\nEl contenido binario descifrado se ha guardado en: {output_file}")
            
    except Exception as e:
        print(f"Error al descifrar: {e}")
else:
    print("No se encontraron metadatos EXIF o no hay campo Artist en la imagen.")
EOF

#Ejecutar el script en el mismo contenedor Docker
pip install pillow piexif

python3 extract_script.py "$IMAGE_PATH" "$STUDENT_ID" "$OUTPUT_FILE"

echo "Texto descifrado guardado en: $OUTPUT_FILE"

rm -f luffy_xor.py extract_script.py