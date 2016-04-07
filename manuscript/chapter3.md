# Estructuras de control

## Sentencia if

En MATLAB la sentencia if múltiple tiene la siguiente estructura:

```python
if cond1
    % ...
elseif cond2
    % ...
    % ...
    % ...
elseif condN
    % ...
else
    % ...
end
``` 

Algo similar ocurre con Python, con la diferencia que se deben colocar dos puntos después de cada instrucción,
que la identación obviamente es obligatoria, el `elseif` se "acorta" a `elif` además que en Python no se 
coloca la instrucción `end` para indicar el final del bloque:

```python
if cond1:
    # ...
elif cond2:
    # ...
    # ...
    # ...
elif condN:
    # ...
else:
    # ...
```

Veamos un ejemplo concreto reproducido en ambos lenguajes:

```matlab
% Ejemplo MATLAB
n = input('Inserte un número: ');
if n > 0
    disp('Positivo');
elseif n < 0
    disp('Negativo');
else
    disp('Cero');
end
```

```python
# Ejemplo python
n = input('Inserte un número: ')
if n > 0:
    print "Positivo"
elif n < 0:
    print "Negativo"
else:
    print "Cero"
```


## Sentencia switch

La sentencia switch de MATLAB, característica de lenguajes inspirados por la sintaxis de C, no tiene un equivalente 
*directo* en Python, pero puede emularse para algunos casos utilizando los diccionarios.

Por ejemplo, suponga que quiere desarrollar un programa en el cual ingrese dos números y enseguida seleccione la 
operación arimética que realizará con ellos, en MATLAB y utilizando switch sería algo como:

```matlab
a = input('a = ');
b = input('b = ');
oper = input('Operación a realizar \n\n1. Suma \n2.Resta \n3.Multiplicación \n4.División\n\n');
switch oper
    case 1
        r = a+b;
    case 2
        r = a-b;
    case 3
        r = a*b;
    case 4
        r = a/b;
end
fprintf('Resultado = %g', r);
```

En Python un código "equivalente" utilizando diccionarios sería:

```python
a = input('a = ')
b = input('b = ')
oper = raw_input('Operación a realizar \n\n1. Suma \n2.Resta \n3.Multiplicación \n4.División\n\n')
opciones = {'1':a+b,'2':a-b,'3':a*b,'4':a/b}
resultado = opciones.get(oper)
if resultado is not None:
    print "Resultado = %g"%(resultado)
else:
    print "Opción incorrecta"
```

## Bucle for

En este bucle MATLAB y Python guardan cierta similitud: ambos recorren un arreglo u objeto iterable, que puede 
ser una lista, tupla (Python) o un array (MATLAB).

En MATLAB es común hacer lo siguiente al utilizar un ciclo for:

```matlab
for i = 1:10
    % ... código útil
    % ... algo más de código
end
```

O bien:

```matlab
for k = 1:0.2:100
    % ...
    % ...
end
```

Pero también es posible hacerlo de cualquiera de las siguientes maneras:


```matlab
str = 'hola';
celda = {1,2,3,4,5,10,2,-2};
mat = rand(4);

for ii = str
    disp(ii); % Imprime cada caracter de str
end

for jj = celda
    disp(jj); % Imprime cada componente de celda
end

for kk = mat
    disp(kk); % Imprime cada elemento de la matriz aleatoria mat
end
```

En Python funciona de manera similar, con una clara variación de sintaxis. Un ejemplo muy básico es:

```python
for x in range(10):
    print x
```

Que imprime lo siguiente:

```
	0
	1
	2
	3
	4
	5
	6
	7
	8
	9
```

Note que en lugar del signo igual (=) de MATLAB, Python utiliza el nexo **in**, y claro, los dos puntos que se muestran al 
finalizar la expresión inicial son obligatorios y necesarios como en el caso de la sentencia `if`, además de que la 
instrucción `end` de MATLAB no se presenta en Python. Es importante mencionar también que la función `range` devuelve 
una lista de enteros en el intervalo semi-abierto [0,N), es decir, desde cero hasta N, excluyendo a este último.

Pero, como se ha mencionado, con el bucle `for` se puede recorrer cualquier objeto iterable de Python. Por ejemplo, 
para recorrer una cadena de caracteres:

```python
for letra in "hola mundo":
    print letra
```

```
	h
	o
	l
	a
	 
	m
	u
	n
	d
	o
```

O incluso imprimir un clásico triángulo de caracteres en pantalla:

```python
car = "*"
for n in xrange(1,11):
    print n*car
```

```
	*
	**
	***
	****
	*****
	******
	*******
	********
	*********
	**********
```

De lo anterior, mención *especial* merece la función `xrange`, que es muy similar a `range` (de hecho la sintaxis es 
la misma), pero que en lugar de devolver una lista de enteros, devuelve un objeto iterable, lo cual le hace más eficiente 
en cuestión de tiempo y memoria. Algo que quizá por ahora no resulte tan crítico, pero que muy posiblemente le sea útil 
posteriormente.


## Bucle while

El bucle `while` sigue una *filosofía* similar en ambos lenguajes, difiriendo simplemente en los dos puntos e 
indentación de Python y la terminación `end` de MATLAB, véase el ejemplo siguiente:

En MATLAB:

```matlab
k = 0;
while k < 10
    disp(k);
    k = k + 1;
end
```

En Python:

```python
k = 0
while k < 10:
    print k
    k += 1
```