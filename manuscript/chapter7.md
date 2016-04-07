# Gráficas

Las gráficas en MATLAB son parte de su enorme popularidad, puesto que dispone de un amplio catálogo de
posibilidades, y una flexibilidad importante.

La librería Matplotlib de Python no es menos interesante, puede que sea menos *madura*, pero mantiene 
una coherencia y simplicidad extraordinaria. Además que permite la manipulación de los entes gráficos 
como objetos de una determinada clase, lo cual le convierte en la mayoría de los casos en una poderosa
herramienta.

Matplotlib dispone también de un módulo llamado `pylab`, el cual es prácticamente un mini-MATLAB, en 
cuestiones de gráficas, claro. Pero para nuestros propósitos omitiremos este módulo, y en su lugar
utilizaremos el módulo `pyplot` que tiene una estructura más *pythonica*.

## Gráficas en dos dimensiones

En MATLAB haríamos algo como lo siguiente:

```matlab
x = linspace(0,10);
y = cos(x);
plot(x,y);
```

Con Matplotlib:

```
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10)
y = np.cos(x)

plt.plot(x,y)
plt.show()
```

Ahora lo importante: con las primeras dos líneas importamos los módulos que utilizaremos, `matplotlib.pyplot` y
`numpy` en este caso, además de usar un pseudónimo para cada uno. El resto de lineas es prácticamente similar, 
con la necesidad de anteponer el pseudónimo del módulo correspondiente para cada una de las funciones. La
instrucción `plt.show()` sirve para mostrar la gráfica que hemos creado, si no colocamos esto el programa no
mostraría ningún resultado. Esa es una de las principales diferencias respecto a MATLAB.

### Modificando etiquetas y título

Vamos a hacer unas pequeñas modificaciones para colocar un título y etiquetas a la gráfica anterior.

Para MATLAB:

```matlab
x = linspace(0,10);
y = cos(x);
plot(x,y);
xlabel('Eje X');
ylabel('Eje Y');
title('Mi gráfica');
```

En Python / Matplotlib:

```python
import matplotlib.pyplot as plt
import numpy as np				

x = np.linspace(0,10)
y = np.cos(x)

plt.plot(x,y)
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title(u'Mi gráfica')
plt.show()
```

![IMG01](images/ch7/img_01.PNG)


### Modificando el color, ancho y estilo de linea

En MATLAB existe la posibilidad de pasar un tercer argumento a la función `plot` en forma de string, el cual
indica un color y estilo de linea, por ejemplo:

```matlab
>> plot(x,y,'r--');
```

La linea anterior traza una gráfica de color rojo y "punteada" o discontinua.

Matplotlib funciona exactamente igual, puede especificar de esa forma un color y estilo de linea, por ejemplo:

```python
import matplotlib.pyplot as plt
import numpy as np				

x = np.linspace(0,10)
y = np.sin(x)-np.cos(x)

plt.plot(x,y,'r--')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title(u'Mi gráfica')
plt.show()
```

![IMG02](images/ch7/img_02.PNG)

En MATLAB se utilizan los argumentos *pareados* para modificar las características de un objeto gráfico, por 
ejemplo para modificar el ancho de línea de una gráfica:

```matlab
plot(x,y,'r','linewidth',3);
```

En Python existe el concepto de *keyword argument* (vea la sección correspondiente a funciones) que permite pasar 
argumentos como se muestra enseguida:

```python
plt.plot(x,y,'r',linewidth=3)
```

Con lo anterior se estaría modificando el ancho de línea.

Para modificar el color y estilo de línea también es posible hacerlo mediante *keyword arguments*, vea el ejemplo 
mostrado a continuación:

```python
import matplotlib.pyplot as plt
import numpy as np				

x = np.linspace(0,10)
y = np.sin(x)-np.cos(x)

plt.plot(x,y,color=(0,1,0),linewidth=3,linestyle='--')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title(u'Mi gráfica')
plt.show()
```

Puede notar que el color puede especificarse mediante una tupla de tres elementos, cuyos valores corresponden al 
modelo de color RGB, en un intervalo de 0 a 1. Pero Matplotlib presenta además una flexibilidad extraordinaria, 
permitiendo especificar el color mediante valores hexadecimales (muy común en la programación web), es decir, para 
indicar que se requiere un color rojo puede hacerlo de las siguientes formas equivalentes entre sí:

```python
plt.plot(x,y,color="r")
plt.plot(x,y,color=(1,0,0))
plt.plot(x,y,color="#ff0000")
```
