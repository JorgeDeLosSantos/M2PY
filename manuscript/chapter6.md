# Vectores y matrices {#vectores-y-matrices}

En este capítulo abordaremos el uso del módulo NumPy para el manejo de arreglos numéricos 
(matrices y vectores), de modo que aún cuando no se especifique de forma explícita, 
se asumirá que se ha importado la librería NumPy utilizando el alias `np` , 
tal como se indica enseguida:

```python	
>>> import numpy as np
```


## Definiendo un vector

Tomaremos el vector **v=<3,-1,8>** como ejemplo; en MATLAB para crear dicho vector sería:

```matlab
>> v = [3,-1,8];
```

Para Python utilizaremos la función `array` del módulo NumPy, pasando como argumentos una lista con los elementos que
conforman el vector:

```python
>>> v = np.array([3,-1,8])
>>> type(v)
<type 'numpy.ndarray'>
```

Para crear un vector equiespaciado puede utilizarse la función `range`:

```
>>> v=np.array((range(10)))
>>> v
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
```

Incluso puede definir un vector utilizando listas por comprensión.

```python
>>> lista=[k**2 for k in range(10)]
>>> v=np.array(lista)
>>> print v
[ 0  1  4  9 16 25 36 49 64 81]
```

En resumen, para crear un vector se debe pasar una lista como argumento a la función `np.array`.

### Algunos vectores predefinidos

Al igual que MATLAB, en Python/NumPy se tienen funciones que generan vectores numéricos predefinidos y que resultan 
muy útiles. Ejemplo de ello es `linspace`, que genera un arreglo de puntos linealmente equiespaciados en un intervalo,
la cantidad de puntos es modificable, siendo 50 por defecto, por ejemplo, para generar un arreglo numérico de 0 a 10 con 
50 puntos sería:

```python
>>> v = np.linspace(0,10)
>>> print v
[  0.           0.20408163   0.40816327   0.6122449    0.81632653
   1.02040816   1.2244898    1.42857143   1.63265306   1.83673469
   2.04081633   2.24489796   2.44897959   2.65306122   2.85714286
   3.06122449   3.26530612   3.46938776   3.67346939   3.87755102
   4.08163265   4.28571429   4.48979592   4.69387755   4.89795918
   5.10204082   5.30612245   5.51020408   5.71428571   5.91836735
   6.12244898   6.32653061   6.53061224   6.73469388   6.93877551
   7.14285714   7.34693878   7.55102041   7.75510204   7.95918367
   8.16326531   8.36734694   8.57142857   8.7755102    8.97959184
   9.18367347   9.3877551    9.59183673   9.79591837  10.        ]
```

O si requiere una cantidad más reducida de puntos:

```python
>>> v = np.linspace(1,5,5)
>>> print v
[ 1.  2.  3.  4.  5.]
```

Incluso puede crear un vector en orden decreciente:

```python
>>> v = np.linspace(10,0,11)
>>> print v
[ 10.   9.   8.   7.   6.   5.   4.   3.   2.   1.   0.]
```

Otra de esas funciones es `logspace`, la cual crea un vector logarítmicamente espaciado, siendo la sintaxis:

```python
>>> np.logspace(A,B,N)
```

Lo anterior define un vector de N puntos en el intervalo `10eA` a `10eB`.

Por ejemplo:

```python
>>> v = np.logspace(1,10,10)
>>> print v
[  1.00000000e+01   1.00000000e+02   1.00000000e+03   1.00000000e+04
   1.00000000e+05   1.00000000e+06   1.00000000e+07   1.00000000e+08
   1.00000000e+09   1.00000000e+10]
```

Además de las anteriores, también existe la función `arange` que trabaja de forma similar a `linspace`, 
excepto que en vez de especificarse el número de puntos, se especifica el "paso" entre cada elemento, 
siendo la sintaxis:

```python
>>> np.arange(a,b,paso)
```

Por ejemplo:

```python
	>>> v = np.arange(1,2,0.25)
	>>> print v
	[ 1.    1.25  1.5   1.75]
```

## Definiendo una matriz

Suponga que requiere crear la matriz:

{$$}
A= \begin{pmatrix} 
  1 & 5 & 2 \\ 
  -3 & 1 & 7  \\ 
  0 & 4 & 8 
\end{pmatrix}
{/$$}

Utilizando MATLAB:

```matlab
>> A = [1,5,2;-3,1,7;0,4,8];
```

Para Python usaremos la función `np.array`, que deberá recibir como argumento una lista de listas, 
donde cada sub-lista es una fila de la matriz.

```python
>>> A=np.array([[1,5,2],[-3,1,7],[0,4,8]])
>>> A
array([[ 1,  5,  2],
       [-3,  1,  7],
       [ 0,  4,  8]])
```

Además de la forma anterior, es posible definir matrices "especiales" utilizando funciones predefinidas 
del módulo NumPy, por ejemplo una matriz aleatoria:

```python
	>>> np.random.random((3,3))
	array([[ 0.02477974,  0.21974255,  0.25890696],
	       [ 0.13803954,  0.6985599 ,  0.55097814],
	       [ 0.0294198 ,  0.80517378,  0.688599  ]])
```

Una matriz conformada por *unos*:

```python
>>> np.ones((4,3))
array([[ 1.,  1.,  1.],
       [ 1.,  1.,  1.],
       [ 1.,  1.,  1.],
       [ 1.,  1.,  1.]])
```

O una conformada por ceros:

```python
>>> np.zeros((5,5))
array([[ 0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.,  0.]])
```

En todos los casos anteriores habrá notado que el argumento de entrada es una tupla de dos elementos que indica 
el número de filas y columnas que tendrá la matriz. Adicionalmente podría especificar el tipo de dato mediante el 
*keyword argument* dtype.

Note que en NumPy las matrices de ceros y unos se crean de manera similar que en MATLAB, con la diferencia que 
el número de filas y columnas se especifica mediante una tupla y en MATLAB con dos argumentos separados. 

Otra diferencia notoria es que por ejemplo en el caso de MATLAB si quiere definir una matriz cuadrada de ceros 
entonces sólo debe indicar un argumento:

```matlab
>> MZ = zeros(5);
```

En Python, no obstante, se deben indicar tanto filas y columnas en la tupla que indica la forma:

```python
>>> MZ=np.zeros((5,5))
>>> print MZ
[[ 0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.]
 [ 0.  0.  0.  0.  0.]]
```

## Operaciones básicas con matrices

### Suma y resta

Definimos dos matrices A y B de 3x3:

```python
>>> A=np.array([[1,-1,2],[8,3,0],[-5,7,4]])
>>> B=np.array([[3,2,0],[11,-4,1],[6,1,2]])
>>> print A
[[ 1 -1  2]
 [ 8  3  0]
 [-5  7  4]]
>>> print B
[[ 3  2  0]
 [11 -4  1]
 [ 6  1  2]]
```

Por definición es necesario que las matrices a sumar o restar tengan las mismas dimensiones, puesto que son 
operaciones realizadas elemento a elemento. Para llevar a cabo las operaciones simplemente debe hacerse como 
lo haría con valores escalares (al igual que en MATLAB):

```python
>>> A+B
array([[ 4,  1,  2],
       [19, -1,  1],
       [ 1,  8,  6]])
>>> A-B
array([[ -2,  -3,   2],
       [ -3,   7,  -1],
       [-11,   6,   2]])
>>> B-A
array([[ 2,  3, -2],
       [ 3, -7,  1],
       [11, -6, -2]])
```

