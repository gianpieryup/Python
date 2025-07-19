## 20 - Módulo pandas

Un modulo con funciones para el tratamiento de `Series`

#### Series

¿Que es esto? . Un objeto **"Series"** es un vector con datos indexados. Como una lista o array solo que puedes definir los **"índices"**

````python
import pandas as pd

#Si no se especifican indices, se asigna una secuencia de indices por defecto.
serie1 = pd.Series((3,5,7))
serie1
	0  ->  3
	1  ->  5
	2  ->  7
	dtype: int64
    
#Ahora asignando indices.
asignaturas = ["mate","historia","fisica","literatura"]
notas = [8,7,6,9]
# Una serie de notas, indexado por asignaturas
serie_notas_daniel = pd.Series(notas,index=asignaturas)  
    
serie_notas_daniel
    mate          8
	historia      7
	fisica        6
	literatura    9
	dtype: int64

#Ejemplo
serie_notas_daniel["fisica"]
6

# Acceder a los Datos(values) de una "Serie", sin los indices
serie_notas_daniel.values
array([8, 7, 6, 9], dtype=int64)

# Acceder a los indices de una "Serie"
serie_notas_daniel.index
Index(['mate', 'historia', 'fisica', 'literatura'], dtype='object', name='Asignatura')
-----------------------


# Los elementos cuyo valor sea >= 8
serie_notas_daniel[serie_notas_daniel >= 8]
    mate          8
	literatura    9
	dtype: int64
    
# Dandole un nombre a la serie    
serie_notas_daniel.name = "Notas de Daniel"
serie_notas_daniel
    mate          8
	historia      7
	fisica        6
	literatura    9
	Name: Notas de Daniel, dtype: int64
        
# Ponerle nombre al campo de los index
serie_notas_daniel.index.name = "Asignatura"

serie_notas_daniel
	Asignatura
	mate          8
	historia      7
	fisica        6
	literatura    9
	Name: Notas de Daniel, dtype: int64
        
# Serie a diccionario
diccionario = serie_notas_daniel.to_dict()
diccionario
{'mate': 8, 'historia': 7, 'fisica': 6, 'literatura': 9}

# Diccionario a serie
# Pierde los nombres, porque en el diccionario no se guarda
serie = pd.Series(diccionario)
serie
	mate          8
	historia      7
	fisica        6
	literatura    9
	dtype: int64
    
#Promediar series
asignaturas = ["mate","historia","fisica","literatura"]
notas_ana = [7,8,5,9]
serie_notas_ana = pd.Series(notas_ana,index=asignaturas)
serie_notas_ana
	mate          7
	historia      8
	fisica        5
	literatura    9
	dtype: int64
        
serie_notas_clase = ( serie_notas_daniel + serie_notas_ana) / 2
serie_notas_clase
    Asignatura
	mate          7.5
	historia      7.5
	fisica        5.5
	literatura    9.0
	dtype: float64
````

### DataFrames

Es como un tabla de **Excel** , con filas y columnas. <span style="background:yellow;">La primera fila que tiene el nombre de las columnas</span>, no se cuenta como fila del DataFrame



````python
import pandas as pd
import webbrowser #Funcionalidades con internet

website = "https://es.wikipedia.org/wiki/Anexo:Campeones_de_la_NBA"
webbrowser.open(website) #Al ejecutarse, habre la pagina web

#Vamos a buscar una tabla y la vamos a seleccionar,IMPORTANTE:
#La copiamos, ponele las primeras 10 filas. Ahora estan copiadas en el portapapeles

# CREAR UN DATAFRAME del portapeles
dataframe_nba = pd.read_clipboard()
dataframe_nba

#Los nombres de las columnas
dataframe_nba.columns

#Datos de la columna
dataframe_nba['Campeón del Oeste']

#Devolver la fila 5
dataframe_nba.loc[5]  # dataset[5:6] pero lo anterior queda mejor

#Las primeras 3 filas
dataframe_nba.head(3)

#Las ultimas 2 filas
dataframe_nba.tail(2)


# CREAR UN DATAFRAME a partir de un diccionario
lista_asignaturas = ["mate","historia","fisica"]
lista_notas = [7,8,9]
dicc = {'Asignaturas':lista_asignaturas,'Notas':lista_notas}

dataframe_notas = pd.DataFrame(dicc)
dataframe_notas
````

#### Índices

````python
#Indices
import pandas as pd
lista_valores = [1,2,3]
lista_indices = ['a','b','c']
serie = pd.Series(lista_valores,lista_indices)

# Acceder a los indices de una "Serie"
serie.index
Index(['a', 'b', 'c'], dtype='object')

serie.index[1]
'b'

# Los indices son inmutables/ los valores no
# serie.index[0] = 'z' /ERROR!!
# serie['a'] = 9 /OK!!

#Crear indices en un Dataframe
lista_valores = [[6,7,8],[8,9,5],[6,9,7]]
lista_indices = ["Matematica","Historia","Fisica"]
lista_nombres = ["Antonio","Maria", "Pedro"]#Las columnas

dataframe = pd.DataFrame(lista_valores, index=lista_indices,columns=lista_nombres)

#dataframe
			Antonio	  Maria	  Pedro
Matematica		6		7		8
Historia		8		9		5
Fisica			6		9		7


dataframe.index
Index(['Matematica', 'Historia', 'Fisica'], dtype='object')

dataframe.index[0]
'Matematica'
````

#### Eliminar elementos

````python
# Eliminar elementos en series y Dataframes
import pandas as pd
import numpy as np

#Tiene que haber (=) cantidad de elementos que indices
serie = pd.Series(np.arange(4),index=['a','b','c','d'])

#eliminar un elemento,es mediante su indice
serie.drop('c')

#Ojo no presiste. guardar el nuevo resultado en una variable

np.arange(9).reshape(3,3).
array([[0, 1, 2],
       [3, 4, 5],
       [6, 7, 8]])

lista_valores = np.arange(9).reshape(3,3)
lista_indices = ['a','b','c']
lista_columnas = ['c1','c2','c3']
dataFrame = pd.DataFrame(lista_valores, index=lista_indices, columns=lista_columnas)

# borrar fila
dataFrame.drop('b')

# borrar columna
# axis :1 el eje
dataFrame.drop('c2',axis=1)

#no olvidar que, los cambios no persisten
#una solucion: dataFrame = dataFrame.drop('c2',axis=1)
````

#### Seleccionar datos en series

````python
import pandas as pd
import numpy as np

lista_valores = np.arange(3)
lista_indices = ['i1','i2','i3']
serie = pd.Series(lista_valores, index=lista_indices)

#Podemos multiplicar a todo por 2
serie = serie*2

#Buscar valor por indice
serie['i2']
#Alternativamente se puede buscar por indice numerico convencional
serie[1]

#SubSeries
#desde 0 hasta 1
serie[0:2]

#desde el indice 'i1' hasta el 'i2'
serie['i1':'i2']

# Condicionales : Toma los datos para comparar
serie[serie > 3]

# En una Serie : Los indices son inmutables/ los valores no
serie[serie > 3] = 6
````

### Seleccionar datos en dataframes

Como selecciono las filas y columnas que quiero

````python
import pandas as pd
import numpy as np
lista_valores = np.arange(25).reshape(5,5)
lista_valores

# Tenemos 5 filas .Por tanto nesecitamos 5 INDICES
lista_indices = ['i1','i2','i3',"i4","i5"]

#Entonces, nesecitamos 5 nombres de columnas
lista_columnas = ['c1','c2','c3','c4','c5']
dataframe = pd.DataFrame(lista_valores,index=lista_indices,columns=lista_columnas)

dataframe
		 c1  c2  c3  c4  c5
    i1    0   1   2   3   4
    i2    5   6   7   8   9
    i3   10  11  12  13  14
    i4   15  16  17  18  19
    i5   20  21  22  23  24

/*--------- Elejir columnas --------*/
#Tomar datos de una columna.OBS no son las filas como en las matrices
dataframe['c2']  # Agregando .values quita los indices quedando un array
    i1     1
    i2     6
    i3    11
    i4    16
    i5    21
# Cuando tomas un columna, tienes una SERIE    
dataframe['c2']['i2']
6    
#Podemos elegir las columnas
dataframe[['c3','c1']]


#Selecionar por valor
#Del dataFrame los valores(filas) que cumplan una condicion, en este caso que el valor de cuya pocicion en la columna 'c2' sea mayor a 15
dataframe[dataframe['c2'] > 15]

#Para condicionales: Devuelve una tabla de 'true'/ 'false'
dataframe > 20

/*--------- Elejir Filas --------*/
En los DataFrames de Pandas existen diferentes formas de seleccionar los registros de las filas y columnas. Siendo dos de las más importantes iloc y loc. La primera permite seleccionar los elementos en base a la posición, mientras que la segunda permite seleccionar mediante etiquetas o declaraciones condicionales. Esta entrada en un tutorial en el que se explicaran los fundamentos para seleccionar filas y columnas en Pandas con iloc y loc

dataframe.loc['i3'] # Agregando .values quita los indices quedando un array
    c1    10
    c2    11
    c3    12
    c4    13
    c5    14
dataframe.loc['i3']['c4']

# La ventaja de iloc es que puedo usar numeros, para identificar los indices. Como los indices pueden ser alfanumericos, facilita la escritura de codigo

# CON ILOC encaso que el dataframe
df.iloc[0] # Primera fila
df.iloc[1] # Segunda fila
df.iloc[-1] # Última fila
````

#### Operaciones

````python
# Operaciones sobre series y dataframes
import pandas as pd
import numpy as np

serie1=pd.Series([0,1,2],index=['a','b','c'])
serie2=pd.Series([3,4,5,6],index=['a','b','c','d'])

#Suma y tiene criterios de no coincidencia, los rellena con NaN
serie1 +serie2


lista_valores = np.arange(4).reshape(2,2)
lista_indices = list('ab') #Forma de construir una lista
lista_columnas = list('12')
dataframe = pd.DataFrame(lista_valores,index=lista_indices, columns=lista_columnas)

lista_valores_2 = np.arange(9).reshape(3,3)
lista_indices_2 = list('abc') #Forma de construir una lista

lista_columnas_2 = list('123')
dataframe_2 = pd.DataFrame(lista_valores_2,index=lista_indices_2, columns=lista_columnas_2)

#Los lugares donde hay datos faltantes , se asigna NaN
dataframe_3 = dataframe + dataframe_2

#Mi dataframe_3 tiene valores NaN , al sumar puedo reemplazarlos por 0 asi no hay perdida de datos
dataframe_3.add(dataframe_2,fill_value=0)
````

#### Ordenación y clasificación

````python
import pandas as pd
import numpy as np

lista_valores = range(4)
lista_indices = list('CABD')

serie = pd.Series(lista_valores,index=lista_indices)

#Ordenar por indices
serie.sort_index()

#Ordenar por valores
serie.sort_values()

# Cambia el valor por: Su Lugar, si estubiera ordenado por valor(No cambia la posicion)
serie.rank()
````

#### Estadísticas

````python
# Estadisticas en dataframes
import pandas as pd
import numpy as np

array = np.array([[1,8,3],[5,6,7]])
dataframe = pd.DataFrame(array, index=['a','b'], columns=list('123'))
dataframe
	1	2	3
a	1	8	3
b	5	6	7

#Suma por columnas
dataframe.sum()
#Suma por filas
dataframe.sum(axis=1)#Osea por el otro eje

#El minimo valor, de cada columna
dataframe.min()

#El maximo valor, de cada columna
dataframe.max()
#El otro sentido es 'axis=1' como argumento

dataframe.idxmin()
#Primero haya el valor minimo de la columna y lo cambia por su indice

#Breve Descripcion de toda la tabla, por columnas
dataframe.describe()
````

#### Valores nulos

````python
# Valores nulos - NaN
import pandas as pd
import numpy as np

lista_valores = ['1','2',np.nan,'4']
serie = pd.Series(lista_valores, index=list('abcd'))

# Me sale 'True' si el elemento es nulo
serie.isnull()

#Borrar valores nulos, no persiste en el original
serie.dropna() #Para que persista: serie = serie.dropna()

#-----------------
#Ahora con DataFrame
lista_valores = [[1,2,3],[4,np.nan,5],[6,7,np.nan]]
lista_indices = list('123')
lista_columnas = list('abc')
dataframe = pd.DataFrame(lista_valores, index=lista_indices, columns=lista_columnas)

#Hay nulos en el DataFrame?
dataframe.isnull()

#borrar nulos, vasta que aparesca un nulo en la fila y se borra tola la fila
dataframe.dropna()

#reemplazar NaN por otro valor
dataframe.fillna(0)
````

#### Jerarquía de índices

````python
import pandas as pd
import numpy as np

lista_valores = np.random.rand(6)
lista_indices = [[1,1,1,2,2,2],['a','b','c','a','b','c']]
series = pd.Series(lista_valores, index=lista_indices)

# Tenemos doble indice
# El indice de primer nivel es:  1 y 2
# El indice de segundo nivel es:  a , b yc
series
    1  a    0.742062
       b    0.419324
       c    0.544580
    2  a    0.049094
       b    0.802933
       c    0.486000
    
series[1]
    a    0.742062
    b    0.419324
    c    0.544580
    
series[1]['b']    
0.41932362004918

#Podemos aprovechar el 'doble indice' para crear un DataFrame
# El indice principal o de primer nivel => El indice del DataFrame
# El indice de segundo nivel => Los nombre de las columnas del DataFrame
dataframe = series.unstack()

#DataFrame => serie con doble indice
dataframe.stack()
````

<span style="background:yellow;">**BONUS** : Numeros random enteros </span>

````python
# randint(num_minimo,num_max,cantidad_numeros)
np.random.randint(1,10,3)
array([6, 3, 7])
````

## 21 - HTML y EXCEL

#### HTML

````python
import pandas as pd
url = 'https://es.wikipedia.org/wiki/Anexo:Finales_de_la_Copa_Mundial_de_F%C3%BAtbol'

# ME devuleve una lista de todos los DataFrames que hay en la pagina
dataframes = pd.io.html.read_html(url)

# Elegimos el que nesecitamos
dataframes_futbol = dataframes[0]

# En el video original los nombres de las columnas eran 0 1 2 3 .. Y la primera fila tenia los verdaderos nombres de las columnas para arreglar esto se hicieron los siguientes pasos 

#La primera fila
dataframes_futbol.loc[0]

# Se convierten a diccionario
dict(dataframes_futbol.loc[0])

#Renombrar las columnas
#dataframes_futbol = dataframes_futbol.rename(dict(dataframes_futbol.loc[0]))

#Tendriamos duplicado con la primera fila
# Borrar una fila
#dataframes_futbol = dataframes_futbol.drop(0)

# Borrar una columna
dataframes_futbol = dataframes_futbol.drop('Notas',axis=1)
````

#### EXCEL

````python
# Leer un Excel (.xlsx)
import pandas as pd

# En Terminal,me salia un error que no tenia la libreria 'xldr'
# pip install xlrd
# Y todo ok
dataset = pd.read_excel("data.xlsx")

print(dataset)
````

## 22 - Tratamiento de datos

#### Unión de dataframes

````python
import pandas as pd

dataframe1 = pd.DataFrame({'c1': ['1','2','3'] ,'clave':['a','b','c'] })

dataframe2 = pd.DataFrame({'c2': ['4','5','6'] ,'clave':['c','b','e'] })

# Es como un INNER JOIN de dos tablas,con la condicion de que tengan el mismo valor en la columna (*), 'on = (*)'
dataframe3 = pd.DataFrame.merge(dataframe1,dataframe2,on='clave')

# LEFT JOIN, how :left
dataframe4 = pd.DataFrame.merge(dataframe1,dataframe2,on='clave',how='left')
# how [left/rigth/outer] cuando no hay coincidencias lo rellena con NaN
````

#### Concatenación de datos

Como en las listas con `+`

````python
import pandas as pd
import numpy as np

array1 = np.arange(9).reshape(3,3)
np.concatenate([array1,array1])

# Concatenacion en el eje x
np.concatenate([array1,array1], axis=1)

serie1 = pd.Series([1,2,3],index=['a','b','c'])
serie2 = pd.Series([4,5,6],index=['d','e','f'])
pd.concat([serie1,serie2])

#Podemos añadir una clave de mayor nivel
pd.concat([serie1,serie2], keys=['serie1','serie2'])

#Dataframes
dataframe1 = pd.DataFrame(np.random.rand(3,3),columns=['a','b','c'])
dataframe2 = pd.DataFrame(np.random.rand(2,3),columns=['a','b','c'])

dataframe_concat = pd.concat([dataframe1,dataframe2])

# Podemos ignorar los indices de los elementos iniciales y solo enumerar el nuevo dataframe
dataframe_concat_i = pd.concat([dataframe1,dataframe2], ignore_index=True)
````

#### Combinar Series y DataFrames

````python
import pandas as pd
import numpy as np

serie1 = pd.Series([1,2,np.nan])
serie2 = pd.Series([4,5,6])

# a una serie la concatenas con otra , Si tiene coincidencias en los indices se queda con la primera(obio es un metodo que se le hace ala primera serie), si tiene valores 'NaN' los reemplaza por el segundo
serie3 = serie1.combine_first(serie2)

# Con dataFrames
lista_valores = [1,2,np.nan]
dataframe1 = pd.DataFrame(lista_valores)
lista_valores_2 = [4,5,6]
dataframe2 = pd.DataFrame(lista_valores_2)

# Convinar el primero con el segundo(importa el orden)
condataframe = dataframe1.combine_first(dataframe2)
````



#### Duplicados en DataFrames

````python
import pandas as pd
lista_valores = [[1,2],[1,2],[5,6],[5,8]]

lista_indices = list('mnop')
lista_columnas = ['valor1','valor2']
dataframe = pd.DataFrame(lista_valores,index=lista_indices,columns= lista_columnas)

#eliminar las filas que tengan valores duplicados, dejando solo una
dataframe.drop_duplicates()

# Si no quiero repetidos en la columna 'valor1', Borra las filas cuyo valor en la 'column1' se repita.Se queda con el primer elemento en no repetirse
dataframe.drop_duplicates(['valor1'])

# Si queremos mantener no el primero si no el ultimo
dataframe.drop_duplicates(['valor1'],keep='last')
````

#### Reemplazar datos en Series

````python
import pandas as pd
serie = pd.Series([1,2,3,4,5],index=list('abcde'))

# Reeemplaza el elemento 1 por el 6
# No persiste en el original
serie.replace(1,6)

# Podemos reemplazar multiples valores de la lista,con un diccionario
serie.replace({2:8,3:9})
````

#### Renombrar índices

````python
import pandas as pd
import numpy as np

lista_valores = np.arange(9).reshape(3,3)
lista_indices = list('abc')

dataframe = pd.DataFrame(lista_valores,index=lista_indices)

#1forma, los cambios en los indices persisten
nuevos_indices = dataframe.index.map(str.upper)
dataframe.index = nuevos_indices

#2 forma con la funcion rename
dataframe = dataframe.rename(index=str.lower)

# pero y valores distintos??, atraves de un diccionario se definira la relacion de los cambios, No persiste los cambios
nuevos_indices = {'a':'f','b':'g','c':'h'}
dataframe = dataframe.rename(index = nuevos_indices)

# solo uno con el diccionario
# SI persiste el cambio
nuevos_indices = {'f':'j'}
dataframe.rename(index=nuevos_indices, inplace=True)
````

#### Agrupar datos en categorías

````python
import pandas as pd
import numpy as np

precios = [42,55,48,23,5,21,88,34,26]
rango = [0,10,20,30,40,50,60,70,80,90,100]

# Nos dice en que rango esta cada elemento
precios_con_rango = pd.cut(precios, rango)

#Informacion de la cantidad de elementos que hay en cada RANGO
pd.value_counts(precios_con_rango)
````

#### Filtrar datos en DataFrames

````python
import pandas as pd
import numpy as np

# crea una lista de numeros aleatorios en (0,1] , con 10 filas y 3 columnas 
lista_valores = np.random.rand(10,3)

dataframe = pd.DataFrame(lista_valores)

#Seleccionar una columnas del dataframe
columna = dataframe[0] 

# Filtrar los valores de la columna(seria como una serie)
columna[columna > 0.70]

# tambien a nivel de datframe, los que no cumplan seran reemplazadas por 'NaN'
dataframe[dataframe > 0.70]
````

#### Combinación de elementos

````python
import pandas as pd
import numpy as np

# crea una lista de numeros aleatorios en (0,1] , con 10 filas y 3 columnas 
lista_valores = np.arange(25).reshape(5,5)

dataframe = pd.DataFrame(lista_valores)

# Una permutacio aleatoria de la lista [0,1,2,3,4]
combinacion_aleatoria = np.random.permutation(5)

# Reordenar segun una permutacion de indices las filas del dataframe
dataframe.take(combinacion_aleatoria)
````

#### Agrupación en DataFrames

````python
#Agrupacion o en SQL (GROUP BY)
import pandas as pd
import numpy as np

lista_valores = {'clave1':['x','x','y','y','z'], 
                 'clave2':['a','b','a','b','a'],
                'datos1':np.random.rand(5),
                'datos2':np.random.rand(5)}

# Podemos crear un Dataframe a partir de un diccionario
dataframe = pd.DataFrame(lista_valores)
# Los indices se asignan por defecto 0,1,2

# Esto seria en SQL: "SELECT datos1 GROUP BY clave1"
grupo1 = dataframe['datos1'].groupby(dataframe['clave1'])

# Como a lo de arriba le falta una funcion de agregacion, en el SELECT se corrige asi:
# SELECT AVG(datos1) GROUP BY clave1
grupo1.mean()
````



#### Agregación en DataFrames

````python
# Osea como un group by de cada columna, no como el anterior que habia que especificar el SELECT
import pandas as pd
import numpy as np

lista_valores = [[1,2,3],[4,5,6],[7,8,9],[np.nan,np.nan,np.nan]]
lista_columnas = list('abc')
dataframe = pd.DataFrame(lista_valores,columns=lista_columnas)

# Agrupa por columnas con una funcion de agregacion,(obvia los valores nulos)
dataframe.agg(['sum','min'])

# Agrupa por filas,(los valores nulos,los entiende como 0)
dataframe.agg('sum',axis=1)
````



## 23 - Módulos seaborn y matplotlib

**seaborn** : Es una librería o un modulo python para hacer gráficos estadísticos en python. Esta construida sobre el modulo de `matplotlib` y esta integrada con la estructura de datos `Pandas` 

#### Instalaciones de seaborn y matplotlib

````shell
En mi compu en consola
$ pip install seaborn

Para usarlo en anaconda
$ conda install seborn
````

#### Histogramas

Un histograma es una representación grafica de una variable o de unos datos en forma de barra, donde la superficie de cada barra es proporcional a la frecuencia de los valores representados

````python
import pandas as pd
import numpy as np

import matplotlib as mpl
import seaborn as sns

#Para ver los graficos, esto es en notbook
%matplotlib inline

datos1 = np.random.randn(100)

# Ver el 'histograma' del array 'datos1'
# El eje y : es la cantidad de valores
# El eje x : valores
mpl.pyplot.hist(datos1)

# Con sns
sns.distplot(datos1)
# Podemos especificar el color
sns.distplot(datos1, color="green")
# alpha varia de 0 a 1 es el brillo
mpl.pyplot.hist(datos1, color ="grey",alpha=0.5)

datos2 = np.random.randn(80)
mpl.pyplot.hist(datos2,color="yellow",alpha=0.4)

# Poner los dos graficos superpuestas
# bins : la cantidad de barras
mpl.pyplot.hist(datos1, color="green",alpha=0.3, bins=20)
mpl.pyplot.hist(datos2, color="blue",alpha=0.3, bins=20)

# Con 'seaborn'
datos3 = np.random.randn(1000)
datos4 = np.random.randn(1000)
# Datos 3 arriba
# Datos 4 deracha
# los puntos azules son las coincidencias
sns.jointplot(datos3,datos4)

# Las coincidencias se ven mejor con colores
sns.jointplot(datos3,datos4,kind='hex')
````

#### Distribuciones

````python
# combincacion de estilos
import pandas as pd
import numpy as np
import matplotlib as mpl
import seaborn as sns
%matplotlib inline

datos = np.random.randn(100)
#Curva con los limites maximos de cada area
sns.distplot(datos)

# Quitar las barras y dejar la curva
sns.distplot(datos,rug=False, hist=False)

# barras y curva de distinto color yh mas propiedades
argumentos_curva = {'color':'black', 'label':'Curva'}
argumentos_histograma = {'color':'grey', 'label':'Histograma'}
sns.distplot(datos, bins=25,kde_kws=argumentos_curva,hist_kws=argumentos_histograma)

# Con series es igual
serie = pd.Series(datos)
sns.distplot(serie, bins=25, color="green")
````

#### Gráficos de caja

**Diagrama de caja**: Sirve para representar gráficamente una serie de datos numéricos a través de sus cuartiles

````python
import pandas as pd
import numpy as np
import matplotlib as mpl
import seaborn as sns
%matplotlib inline

datos = np.random.randn(100)
sns.boxplot(datos)

# Mirar en wikipedia 
# La caja azul representa el 50% de los datos y la linea negra del medio donde esta la "media"
# Vemos entonces rapidamente el 25% - 50% - 75% -100% de los datos , Entre que valores estan
````

#### Regresiones lineales :fire: :fire: 

 En estadística el análisis de regresión es un proceso estadístico  para estimar las relaciones entre variables

 Es decir : entender como varia el valor de una variable en función del valor de otras variables

````python
#Regresion lineal o Ajuste lineal
import pandas as pd
import numpy as np
import matplotlib as mpl
import seaborn as sns
%matplotlib inline

#Este es un dataset que viene precargado en el modulo
propinas = sns.load_dataset('tips')
propinas.head()

# EJe X, Eje Y , DataSet
sns.lmplot('total_bill','tip',propinas)

# Podemos coloresar la recta y/o los puntos
# Con diccionarios , como en la seccion anterior
sns.lmplot('total_bill','tip',propinas,scatter_kws={'marker':'o','color':'green'}, line_kws= {'color':'blue'})

# Quitar la linea, solo los puntos
sns.lmplot('total_bill','tip',propinas,fit_reg=False)

# creamos una nueva columna con los porcentajes
# Seria el porcentaje de la propina con respecto a la compra realizada
propinas['porcentaje'] = 100 * propinas['tip']/ propinas['total_bill']
propinas.head()

sns.lmplot('size','porcentaje',propinas)

# Los datos los separa por 'sex' => x y o
sns.lmplot('total_bill','porcentaje',propinas,hue='sex',markers=['x','o'])

# Por dia de la semana
sns.lmplot('total_bill','porcentaje',propinas,hue='day')
````

#### Mapas de calor

Mapa de calor (en ingles : heatmap). Es una representación grafica de datos, por colores específicamente

````python
import pandas as pd
import numpy as np
import matplotlib as mpl
import seaborn as sns
%matplotlib inline

vuelos = sns.load_dataset('flights')
vuelos.head()

# Para hacer el mapa de calor nesecitamos una matriz
# La tabla ordenado de esta forma , solo con numeros, me sirve
vuelos = vuelos.pivot('month','year','passengers')

sns.heatmap(vuelos)

# Podemos ver los valores en el mapa de calor
sns.heatmap(vuelos,annot=True,fmt='d')

# Podemos definir el valor central del mapa de calor
valor_central = vuelos.loc['May'][1956]

sns.heatmap(vuelos,center=valor_central,annot=True,fmt='d')

# Podemos cambiar el sentidon de la barra de colores que esta pegada a la deracha
sns.heatmap(vuelos,center=valor_central,annot=True,fmt='d',cbar_kws={'orientation':'horizontal'})
````

> BONUS : Consultar la documentación en **seaborn.heatmap**

`np.random.randn(1000)` : Significa 1000 valores que sigan una distribución normal