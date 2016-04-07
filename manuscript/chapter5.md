# Los módulos en Python

## ¿Qué es un módulo?

En términos informales un módulo es un fichero con extensión .py o bien un conjunto de ficheros, que contienen 
definiciones de clases, funciones y constantes.

Los módulos constituyen la base de la programación en Python (...)

## Importar y utilizar módulos

Normalmente cuando se inicia el entorno de MATLAB, se tienen disponibles todas las funciones incluidas en los 
Toolboxs que se tengan instalados, sin necesidad de importar librerías o paquetes, esto puede considerarse una 
ventaja, pero también una enorme desventaja, algo paradójico. Vamos, que si necesita utilizar algunas
funciones matemáticas elementales, no hace falta más que escribirlas, por ejemplo:

```matlab
% Algunas funciones matemáticas elementales en MATLAB
>> exp(1)
>> cos(0)
>> theta = pi/6
>> cos(theta)^2+sin(theta)^2
```

No obstante, en Python, cuando se inicia el interpréte no se tienen disponibles todas estas funciones, sino 
sólo algunas que son consideradas como *built-in functions*. Para utilizar cualquier otro tipo de funciones 
hace falta importar el módulo en el cual se encuentren estas. Por ejemplo para ejecutar el ejemplo anterior 
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

```
1) import modulo
2) import modulo as md
3) from modulo import algo
```

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

