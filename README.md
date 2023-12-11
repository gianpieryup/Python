# Python

Todos mis scripts ya sea python o pyspark

- [CARBON](https://carbon.now.sh/) : Codigo para presentaciones
- [MONGO](https://mongoplayground.net/) : Para hacer querys de mongo de forma online:

#### Adicionales

Como crear ejecutables en Python 🐍 [AQUI](https://omes-va.com/como-crear-ejecutables-en-python-pyinstaller-parte-1/)

Object Detection and Recognition: Advancements in Computer Vision [AQUI](https://medium.com/@naveenpandey2706/lesson-4-object-detection-and-recognition-advancements-in-computer-vision-349e61162726)

Template Machine: Es una tecnica para detectar objetos, pero debe ser exactamente el mismo tamaño y posicion. 
Por lo cual tiene un caso de uso limitado.


**pickle** : Para guardar un json(una lista, etc) en un archivo y luego poder levantarlo en cualquier momento 

<br>

> [!TIP]
> Como saber donde tenemos Python instalado.
```python
import os
import sys

print(os.path.dirname(sys.executable))
```
<br>
<br>
<br>
<br>
<br>


#### Pyspark

Para usar pyspark local debes instalar esta dependencia,

> [!NOTE]
> pip install findspark


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

The background color is `#ffffff` for light mode and `#000000` for dark mode.