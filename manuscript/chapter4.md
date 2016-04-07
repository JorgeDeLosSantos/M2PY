# Funciones

## Definiendo funciones

Como sabrá, las funciones en MATLAB deben definirse una a la vez por cada fichero y tener el nombre de este. Aunque 
pueden incluirse otras funciones dentro del mismo fichero, estas serán *subfunciones* o funciones auxiliares de la 
principal, implicando que sólo resulten "visibles" y utilizables en el ámbito de la función principal. La sintaxis 
más general de una función MATLAB sería:

```matlab
function [out1, out2,...] = nfun(arg1, arg2, ...)
% ...
% ... cuerpo de la función
% ...
end
```

Donde `nfun` es el nombre que se la ha dado a la función; out1 y out2 son valores de retorno de la función; y 
arg1 y arg2 son argumentos de entrada formales de la función `nfun`. Evidentemente los puntos suspensivos indican
que los parámetros de salida y/o entrada podrían ser más o menos que los mostrados como ejemplo.

En Python se pueden definir múltiples funciones en un mismo fichero, lo cual se traduce en una enorme ventaja, y no 
sólo puede definir funciones varias, sino también definiciones de clases, ese es el *plus* de Python: la  gran capacidad 
de modularización y organización del código sin tantas restricciones.

Para definir una función en Python se utiliza la palabra reservada `def` seguida del nombre de la función, tal como 
se indica a continuación:

```python
def nfun(arg1,arg2,...):
    # ...
    # Cuerpo de la función
    # ...
    return out1,out2,...
```

Note que en Python se utiliza la instrucción `return` para indicar los valores de retorno de la función.


## Utilizando funciones

Vamos a poner en práctica la definición de funciones, para ello se creará una función llamada `es_par` que 
identificará si un número es par, se devolverá un valor lógico verdadero en caso de ser así o falso en caso
contrario.

En MATLAB:

```matlab
function r =  es_par(n)
if ~rem(n,2)
	r = true;
else
	r = false;
end
end
```

En Python:

```python
def es_par(n):
    if not(n%2):
        r = True
    else:
        r = False
    return r
```

La forma de llamar la función es exactamente la misma:

```python
val = es_par(7)
```

Donde val se espera sea un valor lógico falso para este caso.

No obstante si los valores de retorno son múltiples, entonces existe una variación en la forma de llamar a la función, 
a saber:

```
>> [a,b,c] = fun(x,y,z) % Para MATLAB

>>> a,b,c = fun(x,y,z) # Para Python
```

## Funciones con argumentos variables

Tanto MATLAB como Python tienen la capacidad de soportar funciones con argumentos de entrada variables. En MATLAB se 
utiliza `varargin` para indicar que una función puede recibir un número indefinido de argumentos, por ejemplo:

```matlab
function [a,b,...] = nfun(varargin)
% ...
% Cuerpo de la función
% ...
end
```

En Python la notación utilizada para ello es anteponer un asterisco (*) al nombre del parámetro formal:

```python
def nfun(*args):
    # ...
    # Cuerpo de la función
    # ...
    return a,b,...
```

El concepto manejado es muy similar: todos los argumentos de entrada se guardan en un arreglo, un cell array en el
caso de MATLAB y una tupla en Python, de modo que el programador definirá en el cuerpo de la función los criterios
que habrán de seguirse para utilizar cada uno de los valores de entrada. Para ejemplificar mejor este proceso vamos 
a crear una función cuyo nombre será `maximo`, y que pueda recibir como argumento un arreglo de valores o bien dos 
números reales cualesquiera.

En MATLAB:

```matlab
function m = maximo(varargin)
if length(varargin)==1
    v = varargin{1};
    m = v(1);
    for i = 2:length(v)
        if v(i)>m
            m = v(i);
        end
    end
elseif length(varargin)==2
    m = varargin{1};
    a = varargin{2};
    if a > m
        m = a;
    end
else
    error('Número de argumentos de entrada inválidos');
end
end
```

En Python:

```python
def maximo(*args):
    if len(args)==1:
        v = args[0]
        m = v[0]
        for i in v:
            if i > m:
                m = i
    elif len(args)==2:
        m = args[0]
        a = args[1]
        if a > m:
            m = a
    else:
        raise SyntaxError
    return m
```

Una diferencia notoria en los ejemplos anteriores es la manera de acceder a los elementos de un arreglo, mientras en MATLAB
se utilizan paréntesis y llaves, en Python se utiliza el corchete. Además, en MATLAB los índices de un arreglo comienzan 
en uno, no así en Python que sigue la convención de la mayoría de los lenguajes y comienza en cero.

## Un plus en Python: keyword arguments

Las funciones en Python permiten el uso de *keyword arguments*. Para mostrar esta característica vamos a definir una 
función `info_contacto` que mostrará en pantalla información de un contacto (nombre, dirección, ...):

```python
def info_contacto(**kwargs):
    nombre = kwargs.get('nombre')
    direccion = kwargs.get('direccion')
    telefono = kwargs.get('telefono')
    email = kwargs.get('email')
    info = """
    Nombre : {}
    Dirección : {}
    Teléfono : {}
    E-mail : {}
    """.format(nombre,direccion,telefono,email)
    print info
```

Revisemos un poco: para indicar que se utilizarán *keyword arguments* es necesario anteceder el nombre del parámetro 
con dos asteriscos (**nombre_parametro), desde luego el nombre del parámetro o argumento puede ser cualquiera (evitando, 
claro, las palabras reservadas del lenguaje). Los parámetros de la función son pasados como se indica a continuación:

```python
funcion(arg1=valor1, arg2=valor2, arg3=valor3, ...)
```

Es decir, el argumento real asignado al formal. Todos los argumentos que se pasan a la función son "almacenados" en 
un diccionario en la forma:

```python
kwargs = {'arg1':valor1, 'arg2':valor2, 'arg3':valor3, ...}
```

Por lo cual para acceder al valor de un determinado argumento puede utilizarse el método `get` del diccionario, por 
ejemplo:

```python
valor1 = kwargs.get('arg1')
valor2 = kwargs.get('arg2')
valor3 = kwargs.get('arg3')
...
```

La función `info_contacto` definida anteriormente podríamos ejecutarla como sigue:

```python
	info_contacto(nombre="Ana", direccion="Av. Siempreviva 742", telefono="1892312333", email="ana@gmail.com")
```

Y obtener en pantalla:

```
Nombre : Ana
Dirección : Av. Siempreviva 742
Teléfono : 1892312333
E-mail : ana@gmail.com
```

Es importante mencionar que los argumentos pasados por clave-valor pueden ir en cualquier orden, de modo que en 
la función anterior pudo haberse colocado primero la dirección o cualquier otro argumento, sin afectar el resultado.

### Valores por defecto de un argumento

Otra posibilidad que brinda Python es colocar un valor por defecto al argumento de una función, esto mediante 
la notación *keyword arguments*. Véase el siguiente ejemplo:

```python
def tri(n, car="*"):
    for x in range(1,n+1):
        print x*car
```

La función `tri` imprime en pantalla un triángulo de caracteres de base **n**, utilizando asteriscos como
caracteres por defecto. Por ejemplo:

```
>>> tri(5)
*
**
***
****
*****
```

Es decir, se puede omitir el segundo argumento y entonces Python tomará el que se le ha indicado en la forma 
clave-valor. Pero si insertamos el segundo argumento se "desechará" el valor por defecto y se tomará el valor 
pasado por el usuario:

```
>>> tri(7, "o")
o
oo
ooo
oooo
ooooo
oooooo
ooooooo
```