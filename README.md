# Proyecto-Integrado
Vamos a crear un sistema de sensores usando raspberry que puede medir muchas características físicas de un paciente. Los datos se guardarán en un servidor central para analisis usando una IA para analizar el estado de un paciente. 

# Método de desarrollo de proyecto

## Requisitos

## Analisis

## Diseño

## Implementación 

## Pruebas

## Implementación



# Arquitectura mental

## Sensor

## Arduino

## USB

## Servidor (PC)

## Archivo CSV



# Sensor: Electrocardíaco

### 1. Descripción
- una herramienta electrocardíaca mida las pulsas electricas del corazón y usa sensores eléctricos sobre puntos clave en el cuerpo

![Alt text](diagramaPulsasCorazon.png)
- el movimiento del corazón se divide en 2 fases: PR y QT
- PR es antes de la contracción 
- QT mientras antes de la contracción

#### Para calcular la frecuencia cardíaca 
- El arduino nos da un voltaje en minivoltios cómo medida 
valores 
- se mide entre 0 y 1023 voltios
- El sensor que usamos normalmente tiene un range entre 300 y 700 voltios
- para obtener una medida más adecuada tenemos que añadir filtros para quitar el ruido y hacer la curva más suave
- Hay varias librerías en arduino que miden PPM y arreglan la curva


...

### 2. Especificaciones técnicas
#### Descripción Pines
- GND - tierra
- 3.3v - fuente de alimentación 
- OUTPUT - conexión de entrada analógica
- Leads off + - comprobación de polo norte
- Leads off - - comprobación de polo sur

#### Diagrama sencilla del cableado
![Alt text](diagrama.jpg)

#### Diagrama más sencilla sin breadboard (directamente al arduino)
![Alt text](diagramaSinBreadboard.jpg)


...

### 3. Conexionado


...

### 4. Código de prueba

```
C++



```


...

### 5. Pruebas realizadas
...

### 6. Aplicación en RaspiAlarm
...
