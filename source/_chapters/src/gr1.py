# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np				

x = np.linspace(0,10)
y = np.sin(x)-np.cos(x)

plt.plot(x,y,color="r",linewidth=3,linestyle='--')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title(u'Mi gráfica')
plt.show()