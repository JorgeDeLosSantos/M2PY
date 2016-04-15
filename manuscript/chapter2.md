# Los tipos de datos y operadores

En este breve capítulo veremos los tipos de datos que tenemos disponibles en Python para sustituir a 
sus equivalentes de MATLAB. La descripción de los tipos de datos es muy *superficial*, en todo caso 
sólo para efectos comparativos con los tipos de datos de MATLAB, para una referencia más completa 
sobre los tipos de datos en Python, puede consultar la documentación oficial[^types]

[^types]: <https://docs.python.org/2/library/stdtypes.html>

## Tipos numéricos

### Enteros

En MATLAB existen enteros de 8, 16, 32 y 64 bits, que para declararlos como tal hace falta una conversión 
explícita utilizando las funciones `int8`, `int16`, `int32`, e `int64`.

Python proporciona dos tipos de enteros: los tipos `int` y `long`. Generalmente int es un entero de 32 bits
y long un entero de 64 bits (sujeto al equipo en que se esté ejecutando Python).

Puede consultar el máximo entero soportado ejecutando las siguientes instrucciones en el intérprete de Python:

```python
>>> import sys
>>> max_int = sys.maxint 
>>> max_long = sys.maxsize
```

### De coma flotante

MATLAB dispone de dos tipos de datos de coma flotante: `double` y `single`, de doble y simple precisión 
respectivamente. El tipo double no hace falta declararlo explícitamente, dado que todo tipo numérico en MATLAB
se considera de tipo double, a menos que se especifique lo contrario.

En Python existe únicamente el tipo `float`. Para que un número sea considerado de coma flotante debe utilizarse
la función `float`, o bien, colocar la parte decimal del número, aún cuando esta sea nula, por ejemplo:

```pyhon
>>> a=3.0
>>> b=float(3)
>>> c=7.5
>>> type(a)
<type 'float'>
>>> type(b)
<type 'float'>
>>> type(c)
<type 'float'>
```


### Números complejos

En MATLAB los números complejos no son estrictamente un tipo de dato, si no que son considerados como tipos
``double`, diferenciándolos mediante la característica *attributes*, por ejemplo:

```matlab
>> whos(complex(2,3))
```

En Python, de igual manera se usa la función `complex` para definir un número complejo, pero aquí si que 
retorna un objeto de tipo `complex`, y desde luego es considerado un *built-in type*:

```
>>> type(complex(2,3))
<type 'complex'>
```


## Tipo booleano

La siguiente tabla resume las diferencias en ambos lenguajes:


|MATLAB   | Python|
| Constantes | |
|`true`   | `True`|
|`false` | `False`|
|Funciones| |
|logical(n) | bool(n)|


## Cadenas de caracteres

En Python las cadenas de caracteres pueden crearse utilizando las comillas dobles o simples, por ejemplo:

```python
>>> cad1='Esto es una cadena de caracteres'
>>> cad2="Y esto también"
>>> type(cad1)
<type 'str'>
>>> type(cad2)
<type 'str'>
```

En MATLAB, como sabemos, la única forma es utilizando las comillas simples.

## Arrays

En MATLAB, fundamentalmente, todo es un array, incluso los escalares son arreglos de 1x1. Pero, siendo 
un poco más flexibles consideraremos que existen tres tipos de arrays o estructuras de datos que sirven 
para almacenar datos de manera agrupada:

* Matrices
* Arreglos de celdas (cell arrays)
* Estructuras (struct)

Las **matrices** son arreglos de valores numéricos dispuestos en filas y columnas. Las matrices de MATLAB 
pueden emularse utilizando una lista de listas, pero obviamente con esto no se podría operar 
de manera satisfactoria. Para ello existe la librería NumPy, que provee algunas 
clases/tipos de datos orientados al manejo de matrices y/o arreglos numéricos. Puede revisar el 
capítulo referente a [Vectores y matrices]({#vectores-y-matrices}) para obtener una referencia 
más completa al respecto.

Los **arreglos de celdas** permiten almacenar datos *heterogéneos*, es decir, podemos almacenar tanto 
valores numéricos como strings, e inclusive otros arreglos dentro del mismo cell array. 
En Python, las listas tienen un comportamiento similar:

```python
>>> c=["Hola",1,0.5,[1,2,3],(0,1),{"a":1,"b":2}]
>>> c
['Hola', 1, 0.5, [1, 2, 3], (0, 1), {'a': 1, 'b': 2}]
```

En la lista anterior podemos observar que almacenamos tanto cadenas de caracteres, enteros, 
reales, listas, tuplas y diccionarios, es decir, diversos tipos de datos, como lo haríamos 
en un cell array de MATLAB.

Las **estructuras** de MATLAB se pueden reemplazar/emular utilizando diccionarios, el concepto 
es muy similar, ambos utilizan el modelo clave-valor para almacenar datos.

Por ejemplo para guardar la información de nombre, edad y nacionalidad  acerca de una persona 
podríamos hacer lo siguiente:

En MATLAB (usando estructuras):

```MATLAB
>> persona.Nombre = 'Jorge';
>> persona.Edad = 20;
>> persona.Nacionalidad = 'Mexicana';
```

En Python (utilizando diccionarios):

```python
>>> persona=dict()
>>> persona['Nombre']='Jorge'
>>> persona['Edad']=20
>>> persona['Nacionalidad']='Mexicana'
```

Bastante similar ¿verdad?. Bueno, en Python hay otras formas de definir un diccionario que quizá 
en determinados casos resulten más cómodas:

Utilizando notación de llaves:

```python
>>> persona={'Nombre':'Jorge','Edad':20,'Nacionalidad':'Mexicana'}
```

Utilizando directamente el constructor y pasando las claves-valor como *keyword arguments*:


```python
>>> persona=dict(Nombre='Jorge',Edad=20,Nacionalidad='Mexicana')
```

## Operadores

### Operadores aritméticos


### Operadores relacionales


### Operadores lógicos