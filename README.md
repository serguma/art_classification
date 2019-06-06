# Art classification

## Descripción

El objetivo del proyecto es entrenar un módelo que pueda diferenciar estilos 
de pinturas.  

En un principio se optó por cuatro estilos (abstracto, realismo, surrealismo y pop-art). Dado que las primeras métricas obtenidas estaban entre un 55 y 63 por ciento.  
Se decidió entrenar al clasificador con dos estilos diferentes (abstracto, realismo).
Para posteriormente ir aumentando el número de estilos.  

En este proyecto podemos ver el desarrollo para diferenciar dos estilos de arte  

## Datos utilizados

Las imágenes han sido obtenidas de la siguiente url:
[wikiart.org](https://www.wikiart.org)  

Se han obtenido:  
 2400 para el train  
 480 para el test  
 480 para la validación y pruebas posteriores  

Además de las imágenes se han guardado el autor, título de la obra y el año de esta.  

## Procedimiento

Para los modelos de clasificación se ha optado por utilizar ciertas features de las imágenes  
En el caso de CNN se ha utilizado las imágnes tal cual con un generador.  


## Estructura del repositorio

**backup/**: Archivos de jupyter notebook, durante el desarrollo del proyecto  
**api/** : Api web  
**training/** : Archivos donde se almacena el entrenamiento de los modelos  
**images/** : Imágenes informativas para el readme  

Carpetas no incluidas en el repositorio  

**data/**: Archivos csv con información sobre las imágenes  
**features/** : Features obtenidas de las imágenes  
**imagenes_color/**: Imágenes utilizadas para el proyecto

## Api

**data/**: Archivos csv con información de las imágenes a validar  
**src/** : Archivos de funciones  
**static/** : Archivos Js y css  
**templates/** : Plantilla html  
**training/** : Modelos guardados para utilizarlos en la api  
**uploads/** : Imágenes que sube el usuario para probar  
**main.py** : Archivo principal para ejecutar la api  

Para ejecutar la api, ejecutar "python main.py"  
Cargar en un navegador la url http://127.0.0.1:5000/  

Para realizar la api se ha utilizado Flask  

## Anotaciones
Los jupyter notebook han sido tratados de forma independiente  
por los que existen varias funciones iguales en ellos.  

Se ha creado un archivo funciones.py que puede ser importado por estos,  
en el cual están declaradas varias funciones comunes y variables  

Para la api se ha utilizado un csv con datos de las obras y poder  
comparar si el resultado es el correcto  

Por lo que la api utiliza los datos de este csv en el que aparecen las url de las  
imágenes para poder ser descargadas y utilizadas para validar el clasificador.  

## Imágenes

Se pueden encontrar varias imágenes con gráficas y métricas de la CNN y de los clasificadores

## Mejoras y ampliación

Unas de las mejoras principales es conseguir un modelo que pueda diferenciar 
más estilos de pinturas.  

Entrenar con más obras de otras épocas  

Utilizar la api desde una app móvil




