
# testGen
testGen es un sencillo script que permite generar tests de preguntas en masa, únicos, con fichero de soluciones. 

Con testGen podemos generar miles de test completamente únicos a partir de un único banco de preguntas. Permite la inserción de fotografías como pregunta y/o respuesta y tantas respuestas como se desee.


## Instalación
1. Instalar las dependencias
```bash
    pip install fpdf
```
2. Clonar el proyecto

```bash
    git clone https://github.com/carlosdelolmo/testGen.git
```

## Uso

Ejecutaremos el script *main.py* para generar los tests.



Los parametros a pasar deben ser los siguientes:

    1. banco_de_preguntas 
    2. número_de_preguntas_por_test 
    3. número_de_versiones_del_test 
    4. nombre_del_test

Podemos usar el banco de preguntas de ejemplo que se facilita para hacer la prueba.

```bash
cd ~/testGen
python3 main.py cultura_general 5 5 prueba\ de\ test
```
Esto generará cinco tests aleatorios en el directorio *~/testGen/output* con cinco preguntas cada una. En total, diez ficheros pdf, cinco sin solución y los mismos cinco pero con solución.
## Sintaxis del banco de preguntas

El banco de preguntas es un simple fichero de texto plano. 

Cada linea del fichero representa una posible pregunta del test. Separamos la pregunta de la respuesta con el carácter #. Igualmente, separamos las respuestas con el carácter #. 

La respuesta correcta debe ser obligatoriamente la primera respuesta dada, el resto de respuestas serán incorrectas. 

Si deseamos introducir una imagen, lo indicaremos con un $ seguido de la ruta de la imagen, justo tras el texto de la pregunta o respuesta en la que queramos introducir la imagen. 

Las preguntas y respuestas **no deben** ser numeradas. Esto se realiza posteriormente de forma automática.

Véase los siguientes ejemplos de sintaxis:

```
Pregunta#Respuesta correcta#Respuesta incorrecta#Otra respuesta incorrecta
Pregunta$imagen_pregunta.jpg#Respuesta correcta$imagen_respuesta1.jpg#Respuesta incorrecta$imagen_respuesta2.jpg
Pregunta#Respuesta correcta$imagen_respuesta3.jpg#Respuesta incorrecta
Pregunta$imagen_pregunta.jpg#Respuesta correcta#Respuesta incorrecta
```
## Ejemplo de uso
Click para ir al [video](https://youtu.be/V04RHIDHhlo)
[![Watch the video](https://i.imgflip.com/7z639g.gif)](https://youtu.be/V04RHIDHhlo)



## Autor

- [@carlosdelolmo](https://github.com/carlosdelolmo)


## Licencia

[MIT](https://choosealicense.com/licenses/mit/)

