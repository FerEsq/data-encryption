# Ejercicio 2 - Stream Cipher

## 📜 Descripción
Este ejercicio tiene como objetivo reforzar conocimientos sobre keystream y su importancia en los cifrados de flujo.

## ✨ Características
- Implementación de generador de keystreams
- Implementación de un esquema básico de cifrado y descifrado utilizando XOR
- Análisis de las implicaciones de la reutilización del keystream

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
### Encriptado
Puedes acceder al script para el encriptado haciendo clic [aquí](https://github.com/FerEsq/data-encryption/blob/ex/stream-cipher/encryption.py).
#### Ejemplo 1
```bash
Ingrese el texto a cifrar: Hola
Ingrese la contraseña (seed): f123 

Keystream generado: e082
Texto cifrado: -_TS
```

#### Ejemplo 2
```bash
Ingrese el texto a cifrar: Mundo
Ingrese la contraseña (seed): f123

Keystream generado: e0824
Texto cifrado: (EVV[
```

#### Ejemplo 3
```bash
Ingrese el texto a cifrar: Adios
Ingrese la contraseña (seed): f123

Keystream generado: e0824
Texto cifrado: $TQ]G
```

### Desencriptado
Puedes acceder al script para el desencriptado haciendo clic [aquí](https://github.com/FerEsq/data-encryption/blob/ex/stream-cipher/decryption.py).
#### Ejemplo 1
```bash
Ingrese el texto a descifrar: -_TS    
Ingrese el keystream: e082

Texto descifrado: Hola
```

#### Ejemplo 2
```bash
Ingrese el texto a descifrar: (EVV[ 
Ingrese el keystream: e0824

Texto descifrado: Mundo
```

#### Ejemplo 3
```bash
Ingrese el texto a descifrar: $TQ]G
Ingrese el keystream: e0824

Texto descifrado: Adios
```

### Unit Testing
Puedes acceder al script para el unit testing haciendo clic [aquí](https://github.com/FerEsq/data-encryption/blob/ex/stream-cipher/unitTesting.py).
#### Ejecución
```bash
python unitTesting.py
```

#### Resultados
![image](https://github.com/user-attachments/assets/2b03afa0-d9d7-4053-aee3-f6ccdb475948)

## ❓ Preguntas
### ¿Qué sucede cuando cambias la clave utilizada para generar el keystream?
* Se genera un keystream completamente diferente.

### ¿Qué riesgos de seguridad existen si reutilizas el mismo keystream para cifrar dos mensajes diferentes?
* Que sí alguien llegará a descubrir cuál es el keystream podría descifrar ambos mensajes.

### ¿Cómo afecta la longitud del keystream a la seguridad del cifrado?
* La longitud del keystream debe ser al menos de la misma longitud que el mensaje a cifrar. Si es más corto y se reutiliza (como repetir la clave), se introducen patrones predecibles que hacen vulnerable el cifrado a ataques estadísticos.

### ¿Qué consideraciones debes tener al generar un keystream en un entorno real?
* Usar generadores criptográficamente seguros en lugar de PRNGs estándar
* Asegurar que la semilla tenga suficiente entropía
* Nunca reutilizar la misma combinación de seed
* Proteger la semilla contra acceso no autorizado

### [Opcional] ¿Qué mejoras ofrecen algoritmos de cifrados de flujo modernos frente a un PRNG sencillo?
* Los algoritmos de cifrado de flujo modernos mejoran la seguridad y eficiencia frente a un PRNG sencillo al generar secuencias más impredecibles y resistentes a ataques. Utilizan claves secretas y mecanismos de retroalimentación para evitar patrones repetitivos y mejorar la aleatoriedad.
* Además, incorporan protección contra ataques de resincronización y están optimizados para un alto rendimiento con menor consumo de recursos, lo que los hace más adecuados para aplicaciones criptográficas.

## 🤖 Uso de IA
* Se utilizó Claude 3.5 Sonnet.
* Puede consultar la conversación haciendo clic [aquí](https://shareclaude.pages.dev/c/mknmjxx02v8px7t8tm3n61ca).

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
