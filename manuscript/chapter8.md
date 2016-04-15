# Programación orientada a objetos

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

I> Extraño que no se utilice la palabra `class` en MATLAB para definir una clase, pero recuerde que 
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




## Herencia


## Métodos estáticos
