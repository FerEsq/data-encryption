#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Uso: $0 <ruta_del_archivo> <clave_xor>"
    exit 1
fi

FILE_PATH=$1
XOR_KEY=$2

HEX_CONTENT=$(cat "$FILE_PATH")

echo "$HEX_CONTENT" | xxd -r -p | python3 -c "
import sys
key='$XOR_KEY'
data=sys.stdin.buffer.read()
print(''.join(chr(data[i]^ord(key[i%len(key)])) for i in range(len(data))))
"