{mainmatter}

# Los primeros pasos

## ¿Qué con MATLAB?

Para comenzar, este texto no tiene la finalidad de *arremeter* contra nadie, así que vamos 
a ser un poco *sensibles* con los *pros* y *contras* de cada lenguaje. MATLAB es un lenguaje de programación 
de alto nivel, interpretado, multiparadigma*, multiplataforma, de tipado dinámico, entre otras 
características, que le han convertido con el paso de los años en un estándar para aplicaciones 
de ingeniería y del ámbito científico, y más aún en el aspecto académico.

Pero ha existido desde siempre cierta disyuntiva en lo que respecta a los costos de las licencias, 
que generalmente suelen ser altos. Y claro, no sólo eso, sino también cuestiones relacionadas con la 
distribución de aplicaciones para usuarios finales, que a más de uno le ha representado complicaciones. 
Además suele ser poco recomendable para el desarrollo de grandes proyectos. En cuanto a la rapidez de 
ejecución, MATLAB dada su condición de lenguaje interpretado suele ser considerado como "un poco lento", 
pero no obstante, para muchas situaciones puede arreglarse mediante la capacidad de agregar librerías 
externas escritas en lenguajes compilados como C y Fortran.


## ¿Por qué Python?

Python es un lenguaje desarrollado a finales de los ochenta y cuyas primeras versiones aparecieron al principio de los
noventa. Es un lenguaje interpretado, de tipado dinámico, multiplataforma, multiparadigma, con una sintaxis sencilla y
distribuido gratuitamente, siendo además de código abierto, lo cual ha permitido que detrás del proyecto exista una
comunidad enorme y muy sólida de usuarios que contribuyen con el mismo.

La diferencia y ventaja más marcada de Python respecto a MATLAB es su condición de lenguaje de propósito general, lo que permite una flexibilidad considerable en el desarrollo de proyectos amplios.

Python se distribuye con una librería estándar, que por sí misma no proporciona las herramientas para el desarrollo de 
aplicaciones en el ámbito cientifico / ingeniería. Por lo cual es necesario instalar de forma independiente dichas 
librerías, y de las cuales se hablará en la siguiente sección.

## ¿Qué necesitamos?

Desde luego tener Python instalado, para ello puede dirigirse a la página de [descargas](https://www.python.org/downloads/)
y seguir los procedimientos que ahí se indican de acuerdo al sistema operativo que disponga.

El tema de las versiones 2.x y 3.x de Python es un punto de "discusión" muy común, lo cierto es que sería más recomendable 
utilizar una versión 3.x, pero en este texto se usará la versión 2.7. Pero claro, la elección es solamente del lector. 
Remarcando el hecho que deberá utilizar las librerías compatibles con la versión de Python instalada.

Ahora, existen múltiples librerías para Python destinadas al computo científico, especializadas en menor o mayor grado, 
pero para comenzar la transición MATLAB-Python existen, a criterio del autor, tres librerías esenciales, a saber:

* NumPy
* SciPy
* Matplotlib

Enseguida una breve descripción de las librerías listadas.

**NumPy**

Pagina del proyecto: [http://www.numpy.org](http://www.numpy.org)

NumPy es una biblioteca extensa que provee los objetos numéricos bases para trabajar con vectores y matrices 
de forma eficiente. 

**SciPy**

Página del proyecto: [http://www.scipy.org](http://www.scipy.org)

SciPy es una biblioteca que contiene múltiples algoritmos para aplicaciones en ingeniería, matemáticas y todo 
el ámbito científico. Utiliza NumPy como base.

**Matplotlib**

Página del proyecto: [http://matplotlib.org](http://matplotlib.org)

Matplotlib es una librería que proporciona herramientas de visualización gráfica en 2D de gran calidad, y una 
capacidad, hasta cierto punto aceptable, para 3D. Es muy notorio también que en cierta medida está inspirada en MATLAB, 
teniendo una sintaxis muy similar, lo cual ayudará mucho en esta *transición*.


Para instalar las librerías puede acceder a las páginas de cada proyecto y proceder conforme se especifica
en la sección de descarga correspondiente. O bien utilizar herramientas de instalación para módulos de Python
como `pip` o `easy_install`.