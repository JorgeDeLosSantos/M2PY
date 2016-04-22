﻿# Programación orientada a objetos

En MATLAB la cuestión de la programación orientada a objetos (POO) está un poco más limitada respecto a Python, sobre 
todo porque MATLAB en un principio no fue concebido como un lenguaje para soportar POO, sin embargo en Python 
el panorama es diferente, los objetos son el alma del lenguaje.

Primeramente, *aclarar* que no entraremos en detalles de definiciones sobre conceptos fundamentales como 
objetos, clases y esas cosas. El propósito es puramente mostrar la manera de portar un código escrito con 
orientación a objetos en MATLAB a su equivalente en Python.

## Definiendo clases

En MATLAB las clases se definen utilizando la palabra reserva `classdef`:

```matlab
classdef MiClase
    %
    % Cuerpo de la clase
    %
end
```

I> Es un poco *extraño* que no se utilice la palabra `class` en MATLAB para definir una clase, pero recuerde que 
I> esta se usa para identificar el tipo de una variable.

En Python una clase se define utilizando la palabra reservada `class` seguido por el nombre de la clase: 

```python
class MiClase:
    # ...
    # Cuerpo de la clase
    # ...
```

Desde luego en Python, nuevamente, la indentación juega un papel muy importante.

### El constructor de la clase

En MATLAB el constructor de la clase es una función con el mismo nombre de la clase, ubicada dentro 
de un bloque de métodos:

```matlab
classdef MiClase
    methods
        function obj = MiClase(args)
            % Cuerpo del constructor
        end
    end
end
``` 

En Python, se utiliza el método `__init__` que actúa como un *pseudoconstructor*:

```python
class MiClase:
    def __init__(self,args)
        # Cuerpo del constructor
``` 

Con las dos estructuras anteriores podemos establecer lo siguiente:

En MATLAB es necesario que el constructor retorne un valor asignado a la variable `obj`, el cual 
será el objeto mismo. No así en Python, cuyo constructor no necesariamente debe retornar un valor.

Sin embargo habrá notado que en Python, además de los argumentos ordinarios de inicialización que 
pudiera requerir nuestra clase, se necesita pasar como primer argumento un parámetro (por convención 
y tómelo como una *obligación*, este parámetro se llamará `self`) que hace referencia a la clase misma, 
y mediante el cual se *pasan* los atributos entre los métodos de la clase.


## Herencia

En MATLAB para heredar de una clase debe utilizarse el signo < después del nombre de la clase y enseguida 
indicar el nombre de la superclase:

```matlab
classdef MiClase < SuperClase

% Cuerpo de la clase

end
```

En Python para heredar de una clase, la superclase se debe colocar entre paréntesis después del nombre de la 
clase, como si fuera un argumento de función:

```python
class MiClase(SuperClase):
    # Cuerpo de la clase
```

Llamando a la superclase:

```matlab
classdef MiClase < SuperClase

% Cuerpo de la clase

end
```

```python
class MiClase(SuperClase):
    def __init__(self,args):
        # Cuerpo de la clase
        SuperClase.__init__(self,args)
```

o

```python
class MiClase(SuperClase):
    def __init__(self,args):
        # Cuerpo de la clase
        super(MiClase,self).__init__(args)
```


### Herencia múltiple

```matlab
classdef MiClase < SuperClase1 & SuperClase2
% 
% Cuerpo de la clase
% 
end
```


```python
class MiClase(SuperClase1, SuperClase2):
    # Cuerpo de la clase
```
