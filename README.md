<div align="center">
	<img width="100" src="https://user-images.githubusercontent.com/25181517/183423507-c056a6f9-1ba8-4312-a350-19bcbc5a8697.png" alt="Python" title="Python"/>
</div>

# Python

Todos los apuntes y scripts :smile:

> [!TIP]
> Como saber donde tenemos Python instalado.
```python
import os
import sys

print(os.path.dirname(sys.executable))
```

Esto nos sirve en caso en caso quisieramos tener python desde cualquier ruta en el cmd.


> [!TIP]
> Versiones de python, existen generalmente dos versiones la 2.7 y la 3.* , como aun pueden haber codigos que corran en la version 2.7 se puede especificar que tipo de version correr nuestro script, generalmente la convencion es:
```console
compu> python script.py            -- corre python 2.7
compu> python3 script.py           -- corre python 3.*
```


#### Enlaces Interesantes

- [CARBON](https://carbon.now.sh/) : Codigo para presentaciones
- [MONGO](https://mongoplayground.net/) : Para hacer querys de mongo de forma online:
- [UNIX](https://www.epochconverter.com/) : Fecha Unix
- [ASCII](https://bytetool.web.app/en/ascii/) : Tabla ascii
- [cmd](https://rctorr.wordpress.com/2014/01/16/procesando-parametros-en-la-linea-de-comando-en-python/) : procesando parametros por linea de comando

#### Adicionales

- Como crear ejecutables en Python 🐍 [AQUI](https://omes-va.com/como-crear-ejecutables-en-python-pyinstaller-parte-1/)
- **pickle** : Para guardar un json(una lista, etc) en un archivo y luego poder levantarlo en cualquier momento 

#### Pyspark

Para usar pyspark local debes instalar esta dependencia,

> [!NOTE]
> pip install findspark