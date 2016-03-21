Los tipos de datos
==================

Tipos numéricos
---------------

Enteros
^^^^^^^

En MATLAB existen enteros de 8, 16, 32 y 64 bits, que para declararlos como tal hace falta una conversión 
explícita utilizando las funciones ``int8``, ``int16``, ``int32``, e ``int64``.

Python proporciona dos tipos de enteros: los tipos ``int`` y ``long``. Generalmente int es un entero de 32 bits
y long un entero de 64 bits (sujeto al equipo en que se esté ejecutando Python).

Puede consultar el máximo entero soportado ejecutando las siguientes instrucciones en el intérprete de Python:

.. code:: python

	>>> import sys
	>>> max_int = sys.maxint 
	>>> max_long = sys.maxsize


De coma flotante
^^^^^^^^^^^^^^^^

MATLAB dispone de dos tipos de datos de coma flotante: ``double`` y ``single``, de doble y simple precisión 
respectivamente. El tipo double no hace falta declararlo explícitamente, dado que todo tipo numérico en MATLAB
se considera de tipo double, a menos que se especifique lo contrario.

En Python existe únicamente el tipo ``float``. Para que un número sea considerado de coma flotante debe utilizarse
la función ``float``, o bien, colocar la parte decimal del número, aún cuando esta sea nula, por ejemplo:

.. code:: python

	>>> a=3.0
	>>> b=float(3)
	>>> c=7.5
	>>> type(a)
	<type 'float'>
	>>> type(b)
	<type 'float'>
	>>> type(c)
	<type 'float'>


Números complejos
^^^^^^^^^^^^^^^^^

En MATLAB los números complejos no son estrictamente un tipo de dato, si no que son considerados como tipos
``double``, diferenciándolos mediante la característica *attributes*, por ejemplo:

.. code:: matlab

	>> whos(complex(2,3))


En Python, de igual manera se usa la función ``complex`` para definir un número complejo, pero aquí si que 
retorna un objeto de tipo ``complex``, y desde luego es considerado un *built-in type*:

.. code:: python

	>>> type(complex(2,3))
	<type 'complex'>


Tipo booleano
-------------

La siguiente tabla resume las diferencias en ambos lenguajes:

+------------+-----------+
| MATLAB     | Python    |
+============+===========+
| Constantes             |
+------------+-----------+
| ``true``   | ``True``  |
+------------+-----------+
| ``false``  | ``False`` |
+------------+-----------+
| Funciones              |
+------------+-----------+
| logical(n) | bool(n)   |
+------------+-----------+



Cadenas de caracteres
---------------------

En Python las cadenas de caracteres pueden crearse utilizando las comillas dobles o simples, por ejemplo:

.. code:: python

	>>> cad1='Esto es una cadena de caracteres'
	>>> cad2="Y esto también"
	>>> type(cad1)
	<type 'str'>
	>>> type(cad2)
	<type 'str'>

En MATLAB, como sabemos, la única forma es utilizando las comillas simples.

Estructuras de datos
--------------------
