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




### Tipos de Datos

En un DataFrame de pandas, el tipo de dato `object` generalmente se refiere a datos que son cadenas de texto (strings). Sin embargo, también puede usarse para representar cualquier tipo de dato que no tenga un tipo nativo específico en pandas (por ejemplo, listas, diccionarios o combinaciones de tipos).
Cuando pandas no puede determinar un tipo más específico (como `int`, `float`, `datetime`, etc.), asigna el tipo `object` como una categoría general. Esto ocurre más frecuentemente con columnas que contienen texto, pero también puede suceder si una columna tiene datos mixtos (por ejemplo, una combinación de números y cadenas).

Si deseas verificar el tipo de datos específico contenido en una columna de tipo `object`, puedes usar el método `pd.Series.apply(type).value_counts()` para ver qué tipos están presentes:

```python
df['columna'].apply(type).value_counts()
```

O, si deseas asegurarte de que una columna específica sea de un tipo particular (por ejemplo, convertir una columna de `object` a `str`), puedes hacer la conversión utilizando `.astype(str)`:

```python
df['columna'] = df['columna'].astype(str)
```

Lo puedes definir en la creacion del dataframe, en el import, etc. con el campo `dtypes: {”campo1”: str, “campo2”: int, … }`