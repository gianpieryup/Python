# ML_cursos

Curso de udemy

Machine Learning de A a la Z: R y Python para Data Sciencie



### ejercicios_python

Es del curso de Python 2021C2 UNSAM

https://github.com/python-unsam/Programacion_en_Python_UNSAM/tree/master/Notas



### ML de la A la Z

Link de alguien que anoto todo el curso en una pagina para leer, muy bueno si no entendiste algo

https://daneriaureo.wordpress.com/




- Object Detection and Recognition: Advancements in Computer Vision [AQUI](https://medium.com/@naveenpandey2706/lesson-4-object-detection-and-recognition-advancements-in-computer-vision-349e61162726)

- Template Machine: Es una tecnica para detectar objetos, pero debe ser exactamente el mismo tamaño y posicion. 


## Extrass

`%pylab` un atajo para escribir todos los comandos siguientes; en esencia, **agrega numpy y matplotlib a su sesión**. Esto se incorporó en iPython como herramienta de transición y la recomendación actual es que **no se debe utilizar** . La razón principal es que los siguientes conjuntos de comandos importan demasiado al espacio de nombres global

When the %pylab magic function is entered at the IPython prompt, it triggers the import of various modules within Matplotlib.

Usandolo
```
from pylab import *

x, y = arange(10), cos(x/2)
plot(x, y)
show()
```


Tradicionalmente se tendria que
```
from matplotlib import pyplot as PLT
import numpy as NP

x, y = NP.arange(10), NP.cos(x/2)
fig = PLT.figure()
ax1 = fig.add_subplot(111)
ax1.plot(x, y)
PLT.show()
```

Porque lo menciono? Porque hay codigo antiguo que lo usa, mas que nada para entenderlo.
