# Ejercicio 3- Block Cipher

## 📜 Descripción
Este ejercicio tiene como objetivo reforzar los conocimientos sobre los modos de operación en los cifrados de bloque y su importancia en la seguridad de la información.

## ✨ Características
- Implementación de funciones de cifrado y descifrado utilizando DES (ECB), 3DES (CBC) y AES (CBC y ECB).
- Generación aleatoria de claves y vectores de inicialización cuando corresponda.
- Uso de funciones de relleno de bits, tanto manualmente como con las herramientas de librerías especializadas.
- Análisis de las diferencias entre los algoritmos y modos de operación.

## 📦 Dependencias Principales
Las principales dependencias del proyecto incluyen:
* [![Python][Python]][Python-url]
* [![Markdown][Markdown]][Markdown-url]

## 👥 Developer

<a href="https://github.com/FerEsq">
  <img width='175' src="https://github.com/FerEsq/FerEsq/blob/main/assets/headset.png" alt="Fernanda Esquivel" />
</a>

* [![Linkedin][Linkedin]][Linkedin-fer]
* [![GitHub][GitHub]][GitHub-fer]

## 📞 Contacto
Si tienes preguntas o comentarios, puedes contactarme a traves de:

* [![Website][Website]][Website-fer]
* [![Mail][Mail]][Mail-fer]

## 📖 Ejercicios
### DES
Puedes acceder al script para el encriptado haciendo clic [aquí](https://github.com/FerEsq/data-encryption/tree/ex/block-cipher/DES).
#### Ejemplo de uso
##### Texto a cifrar
```bash
Hola Mundo!
```

##### Texto cifrado
```bash
1c9ce450674db6dc58bae60d203a9e7a
```

##### Llave generada
```bash
67376fcd56268506
```


### 3DES
Puedes acceder al script para el desencriptado haciendo clic [aquí](https://github.com/FerEsq/data-encryption/tree/ex/block-cipher/3DES).
#### Ejemplo de uso
##### Texto a cifrar
```bash
Hola Mundo!
```

##### Texto cifrado
```bash
f44a808af3906e79fbffe3d0f130fa62
```

##### Llave generada
```bash
325746048094739d07ae4c16e37a23a43d2c0746e5103b7f
```

##### IV generado
```bash
d3e39cdd75af6c2c
```


### AES
Puedes acceder al script para el desencriptado haciendo clic [aquí](https://github.com/FerEsq/data-encryption/tree/ex/block-cipher/AES).
#### Resultado en modo CBC
<img width='300' src="https://github.com/FerEsq/data-encryption/blob/ex/block-cipher/AES/cbcEncrypted.png" alt="Result" />

#### Resultado en modo ECB
<img width='300' src="https://github.com/FerEsq/data-encryption/blob/ex/block-cipher/AES/ecbEncrypted.png" alt="Result" />


### Unit Testing
Puedes acceder a los scripts para el unit testing en la carpeta correspondiente al algoritmo.
#### Ejecución
```bash
python [algoritmo]Test.py
```

#### Resultado DES
![image](https://github.com/user-attachments/assets/38249757-49f4-428d-87e7-b8a154a784ad)

#### Resultado 3DES
![image](https://github.com/user-attachments/assets/91773e52-2e00-4349-99ef-cd1d928a3770)

#### Resultado AES
![image](https://github.com/user-attachments/assets/052f405b-b181-48d2-9246-906555bc048a)


## ❓ Preguntas
### ¿Qué tamaño de clave se está usando para DES, 3DES y AES?
* DES: 64 bits (8 bytes)
* 3DES: 192 bits (24 bytes)
* AES: 256 bits (32 bytes)

### ¿Qué modo de operación está implementado?
* DES: ECB (Electronic Codebook)
* 3DES: CBC (Cipher Block Chaining)
* AES: CBC y ECB (ambos)

### ¿Por qué no debemos usar ECB en datos sensibles?
* ECB cifra cada bloque de forma independiente con la misma clave, lo que hace que bloques idénticos de texto plano generen bloques idénticos de texto cifrado. Esto revela patrones en los datos, comprometiendo la confidencialidad.
* Por ejemplo, para las imagenes cifradas en este ejercicio se puede notar la "silueta" de Bill.

### ¿Cual es la diferencia entre ECB vs CBC, se puede notar directamente en una imagen?
* ECB: Cifra cada bloque independientemente
* CBC: Utiliza el bloque cifrado anterior para modificar el siguiente bloque antes del cifrado

### ¿Que es el IV?
* El IV es un bloque aleatorio usado para asegurar que bloques de texto plano idénticos produzcan diferentes bloques cifrados.
* Se utiliza en CBC y otros modos para añadir aleatoriedad al primer bloque.

### ¿Que es el PADDING?
* El padding son bytes adicionales que se añaden al final del mensaje para completar un bloque entero.
* Se utiliza gracias a que existen ciertos algoritmos de cifrado por bloques requieren datos de longitud múltiplo del tamaño del bloque.

### ¿En qué situaciones se recomienda cada modo de operación?
* ECB: Solo para datos pequeños y no sensibles
* CBC: Datos donde la seguridad es importante, pero no hay necesidad de acceso aleatorio

### ¿Cómo elegir un modo seguro en cada lenguaje de programación?
Basado en los lenguajes de programación mencionados en las instrucciones del ejercicio:
* Python: Usar bibliotecas como cryptography o pycryptodome que implementan correctamente los modos recomendados
* Java: Utilizar javax.crypto con modos seguros como CBC o GCM
* C#: Clases AesCng con CipherMode.CBC y un IV adecuado
* Go: Usar el paquete estándar crypto/aes junto con los paquetes crypto/cipher para implementar modos como CBC, GCM, y CTR

<!-- MARKDOWN LINKS & IMAGES -->
[Python]: https://img.shields.io/badge/Python-4B8BBE?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org
[Markdown]: https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white
[Markdown-url]: https://www.markdownguide.org
[Linkedin-fer]: https://www.linkedin.com/in/feresq
[Linkedin]: https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white
[Github-fer]: https://github.com/FerEsq
[GitHub]: https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white
[Website]: https://img.shields.io/badge/Website-226946?style=for-the-badge&logo=opera&logoColor=white
[Website-fer]: https://fer-esq.web.app
[Mail]: https://img.shields.io/badge/Gmail-DC143C?style=for-the-badge&logo=gmail&logoColor=white
[Mail-fer]: mailto:feresq.gt@gmail.com
