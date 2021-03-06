﻿# Scripts, ficheros y esas cosas.

Los ficheros juegan un papel muy importante dentro de la programación tanto en MATLAB y Python, 
como en cualquier otro lenguaje, ya que sin estos sería un poco inútil pasarnos escribiendo en la 
consola interactiva y volver a reescribir en cada sesión. Pero además, no basta con saber crear 
un fichero, guardarlo y después utilizarlo, ¡no!, también se hace necesario saber organizarlos 
en una estructura de ficheros adecuada o cuando menos razonable. En este capítulo veremos cómo se 
organizan los ficheros en Python y las similitudes/diferencias respecto a MATLAB.

## De los ficheros y scripts

Vamos a comenzar con el tipo de archivo más simple tanto en MATLAB como Python. Un script es 
un fichero de texto plano, con extensión `.py` (Python) o `.m` (MATLAB) que contiene una serie 
de instrucciones o comandos que deberán ejecutarse de manera secuencial.

En este punto tenemos una diferencia fundamental respecto a los archivos MATLAB/Python: 

* En MATLAB en un fichero sólo podemos definir una serie de instrucciones, una función y subfunciones o
  una definición de clase; una de las opciones anteriores a la vez. Es decir, que si necesitas 
  programar un script que además utilice una función definida por el usuario, se tendrán que utilizar dos 
  ficheros: uno para el script y otro para la función.

* En Python la cuestión de los ficheros es más *razonable*. En un mismo archivo se pueden definir funciones, 
  clases, y lo que se nos ocurra. Eso es una gran ventaja cuando los proyectos van más allá de unos centenares 
  de líneas, permite establecer una estructura de ficheros acorde a la funcionalidad establecida por el 
  usuario y no limitada (caso MATLAB) por el propio lenguaje.

## Ejecutando scripts

En MATLAB los scripts se ejecutan tecleando el nombre en el *Command Window*, por ejemplo:

```matlab
>> script_01
```

Lo anterior ejecuta el script `script_01.m` siempre y cuando este se encuentre en el *Current Folder* 
o bien en el path de MATLAB.

En Python la cuestión es parecida, deberá abrir una consola/terminal y teclear:

```python
> python script_01.py
```

Claro, para esto deberá estar ubicado en el directorio que contiene al script `script_01.py`.

Si utiliza Microsoft Windows, incluso no es necesario abrir una consola, sino que puede *correr* directamente 
el script como cualquier otro ejecutable de Windows.


## Módulos y paquetes

En la programación MATLAB el concepto de módulo no es común, pero sí el de paquete, 
un paquete es un directorio ordinario que contiene un conjunto de definiciones de clases, 
funciones o scripts, teniendo la particularidad que el nombre del mismo debe comenzar 
con un signo de suma (`+`).

En Python, un módulo es un fichero con extensión `.py` que contienen definiciones de clases, 
funciones y/o instrucciones ejecutables. Y un paquete es un directorio que agrupa un conjunto 
de módulos y que además debe contener un fichero `__init__.py` para que Python lo reconozca como 
tal.

### Creando paquetes

En MATLAB un paquete  se crea utilizando un directorio cuyo nombre debe comenzar con un signo 
de suma (`+`). Por ejemplos, supongamos que tenemos un paquete `graficas` que debe contener las clases 
`Lineas`, `Barras` y `Puntos`, entonces se debe crear una estructura como la siguiente:

{linenos=off}
	└── +graficas
	    ├── Lineas.m
	    ├── Barras.m
	    └── Puntos.m

Para hacer esto en Python se puede proceder de manera muy similar:

{linenos=off}
	└── graficas 
	    ├── __init__.py 
	    ├── Lineas.py 
	    ├── Barras.py 
	    └── Puntos.py

Ya mencionabamos anteriormente las diferencias de sintaxis: en Python se debe colocar un fichero `__init__.py` 
dentro del paquete.

T> La filosofía de Python dice que *simple es mejor que complejo*, así que, dada la flexibilidad de Python, 
T> podríamos agrupar las clases `Lineas`, `Barras` y `Puntos` dentro de un mismo fichero `.py`, evitando crear 
T> un paquete, reduciendo el número de ficheros necesarios y consecuentemente una mejor organización y 
T> estructura del proyecto.

### Importar y utilizar módulos

Normalmente cuando se inicia el entorno de MATLAB, se tienen disponibles todas las funciones incluidas en los 
Toolboxs que se tengan instalados, sin necesidad de importar librerías o paquetes, esto puede considerarse una 
ventaja (en principio, talvez), pero también una enorme desventaja, algo paradójico. Vamos, que si necesita 
utilizar algunas funciones matemáticas elementales, no hace falta más que escribirlas, por ejemplo:

```matlab
% Algunas funciones matemáticas elementales en MATLAB
>> exp(1)
>> cos(0)
>> theta = pi/6
>> cos(theta)^2+sin(theta)^2
```

No obstante, en Python, cuando se inicia el interpréte no se tienen disponibles todas estas funciones, sino 
sólo algunas que son consideradas como *built-in functions*. Para utilizar cualquier otro tipo de funciones 
hace falta importar el módulo en el cual se encuentren estas. Por ejemplo, para ejecutar el ejemplo anterior 
en Python habría que importar el módulo **math** tal cómo se indica a continuación:

```python
>>> from math import *
>>> exp(1)
2.718281828459045
>>> cos(0)
1.0
>>> theta=pi/6
>>> cos(theta)**2+sin(theta)**2
1.0
```

Si no se hubiese importado el módulo **math**, Python lanza un error de tipo *NameError*, indicando que una 
función o variable no está definida:

```python
>>> exp(1)

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    exp(1)
NameError: name 'exp' is not defined
```

Existen, generalmente, tres formas de importar un módulo, a saber:


1) `import modulo`
2) `import modulo as md`
3) `from modulo import algo`

**Primer forma**

La primer forma es la más común y, sobre todo, recomendable, de importar un módulo. Se coloca la palabra 
clave `import` seguida del nombre del módulo que habrá de importarse. Vamos a repetir el ejemplo anterior de las funciones matemáticas:

```
>>> import math
>>> math.exp(1)
2.718281828459045
>>> math.cos(0)
1.0
>>> theta=math.pi/6
>>> math.cos(theta)**2+math.sin(theta)**2
1.0
```

Cómo habrá notado, es necesario anteponer a cada función utilizada el nombre del módulo al cual pertenecen, en este
caso **math**. La ventaja de este tipo de notación es que evita cometer errores cuando se tienen dos funciones o 
clases con el mismo nombre, provenientes de módulos diferentes.

**Segunda forma**

Similar a la primera, con la única diferencia que se especifica un *alias* para el nombre del módulo, lo cual lo hace 
muy conveniente si se importan nombres de módulos muy largos.

Siguiendo con el ejemplo del módulo `math`:

```python
>>> import math as m
>>> m.exp(1)
2.718281828459045
>>> m.cos(0)
1.0
```

Lo anterior importa el módulo `math` con el alias `m`, y entonces para referir al módulo debemos utilizar 
el alias que hemos indicado.

**Tercera forma**

Esta forma es conveniente cuando solamente se necesitarán unas pocas funciones, clases o constantes de un 
determinado módulo. 

Por ejemplo, si del módulo `math` sólo vamos a utilizar la constante {$$}\pi{/$$} y la función coseno:

```python
>>> from math import pi,cos
>>> cos(pi)
-1.0
```

Aunque esto no siempre es así, muchos acostumbran a importar todo el contenido de un módulo post-poniendo 
un asterisco (`*`).

```python
>>> from math import *
```

Pero esto normalmente no es recomendable, puede conducir a errores cuando se *mezclan* módulos 
que contienen clases, funciones o constantes de nombres iguales o al menos similares.

