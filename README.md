# Laboratotio 2 - Parte B

## 📜 Descripción
Este laboratorio busca implementar operaciones XOR, Base64 y binario en Python, además de utilizar Pillow para manipular imágenes y combinar dos en una mediante matrices de bits.

## ✨ Características
- Implementación de funciones XOR, Base64 y binario
- Uso de la librería Pillow para procesamiento de imágenes
- Representación y transformación de imágenes con matrices de bits
- Unificación de imágenes mediante técnicas específicas

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
### Ejercicio 1
Puede consultar el código haciendo clic [aquí](https://github.com/FerEsq/data-encryption/blob/lab2/partB/Exercise1).
#### Resultado
<img width='300' src="https://github.com/FerEsq/data-encryption/blob/lab2/partB/Exercise1/xor_result.png" alt="Result" />

### Ejercicio 2
#### ¿Porque al aplicar XOR con una llave de texto a una imagen esta se corrompe?
La corrupción de una imagen al aplicar XOR con una clave de texto ocurre principalmente porque esta operación modifica indiscriminadamente todos los bytes del archivo, incluyendo los encabezados críticos que definen el formato y estructura de la imagen. Los visualizadores de imágenes ya no pueden interpretar correctamente el archivo porque su estructura fundamental ha sido alterada.

Además, mientras que el texto utiliza un rango limitado de valores de bytes (ASCII o UTF-8), las imágenes utilizan todo el rango posible (0-255) para representar colores y otra información. Esta diferencia hace que la operación XOR genere valores que rompen las relaciones necesarias entre bytes consecutivos que representan los datos de la imagen, resultando en una corrupción del archivo.
#### Referencias
1. Khan Academy. (s. f.). https://es.khanacademy.org/computing/computer-science/cryptography/ciphers/a/xor-bitwise-operation

### Ejercicio 3
Puede consultar el código haciendo clic [aquí](https://github.com/FerEsq/data-encryption/blob/lab2/partB/Exercise2).
#### Resultado
<img width='300' src="https://github.com/FerEsq/data-encryption/blob/lab2/partB/Exercise2/result.png" alt="Result" />


## 🤖 Uso de IA
* Se utilizó Claude 3.5 Sonnet.
* Puede consultar la conversación haciendo clic [aquí](https://shareclaude.pages.dev/c/u5pi2vv9105c2vfvbfuo8y5u).


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
