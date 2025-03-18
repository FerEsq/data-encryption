# Laboratorio 3 - Cifrados Simétricos

## 📜 Descripción
Este laboratorio tiene como objetivo implementar y analizar distintos métodos de cifrado, evaluando su seguridad y aplicación en protocolos de comunicación.

## ✨ Características
- Implementación de AES en modos ECB y CBC.
- Uso de ChaCha20 como cifrado de flujo.
- Analisis de riesgos de ECB y CBC en imágenes.
- Aplicación de cifrados en protocolos con Wireshark.
- Exploración de vulnerabilidades en cifrados mal implementados.

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

### 1️⃣ Rompiendo ECB en Imágenes
Puedes acceder al script de la parte 1 haciendo clic [aquí](https://github.com/FerEsq/data-encryption/tree/lab3/partA/Part1).

#### Imagen original
<img width='300' src="https://github.com/FerEsq/data-encryption/blob/lab3/partA/Part1/decrypted.png" alt="Result" />

#### Resultado en modo CBC
<img width='300' src="https://github.com/FerEsq/data-encryption/blob/lab3/partA/Part1/cbcEncrypted.png" alt="Result" />

#### Resultado en modo ECB
<img width='300' src="https://github.com/FerEsq/data-encryption/blob/lab3/partA/Part1/ecbEncrypted.png" alt="Result" />

#### Preguntas para reflexión
##### ¿Por qué el cifrado ECB revela los patrones de la imagen?
* ECB revela patrones porque cifra bloques idénticos de la misma manera, sin aleatorización, por lo que se mantienen estructuras visibles en imágenes.
##### ¿Cómo cambia la apariencia con CBC?
* CBC cambia la apariencia al encadenar bloques con un vector de inicialización (IV) aleatorio, eliminando patrones visibles y mejorando la seguridad.
##### ¿Qué tan seguro es usar ECB para cifrar datos estructurados?
* ECB es inseguro para datos estructurados, ya que no oculta repeticiones y permite inferir información a partir de patrones cifrados.

### 2️⃣ Capturando Cifrado en Red con Wireshark
Puedes acceder al script de la parte 2 haciendo clic [aquí](https://github.com/FerEsq/data-encryption/tree/lab3/partA/Part2).

### 3️⃣ Implementando un Cifrado de Flujo con ChaCha20
Puedes acceder al script de la parte 3 haciendo clic [aquí](https://github.com/FerEsq/data-encryption/tree/lab3/partA/Part3).

### 4️⃣ Implementación de un Ransomware Simulado
Puedes acceder al script de la parte 4 haciendo clic [aquí](https://github.com/FerEsq/data-encryption/tree/lab3/partA/Part4).

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
