<div align="center">
	<code><img width="100" src="https://user-images.githubusercontent.com/25181517/183423507-c056a6f9-1ba8-4312-a350-19bcbc5a8697.png" alt="Python" title="Python"/></code>
</div>

## Configuraciones

Para saber la ubicacion de la ruta de instalacion de tu python

```python
import os
import sys

print(os.path.dirname(sys.executable))
```

## INDICE
<!-- TOC -->

- [Python 01](Python%2001.md)
- [Python 02](Python%2002.md)
- [Python 03](Python%2003.md)
- [entornos_virtuales](entornos_virtuales.md)



### ASCII-UNICODE

```python
''' 
En Python existen las funciones 'ord' y 'chr' que sirven para trabajar 
con caracteres y su representación en Unicode
Podes ver la tabla para constatar los caracteres
'''

# Letra Mayusculas (65-90)
for num in range(65,91):
    print("Num",num,"-> caracter:",chr(num)) 


# Letras Minusculas (97-122)
for num in range(97,123):
    print("Num",num,"-> caracter:",chr(num))
    
# Cambiar a mayusculas o minusculas
palabra = "Yo TE conoZco"
print(palabra.lower())
print(palabra.upper())
```
