## Sección 9 : Módulos

Es un fichero que tiene funciones que luego las importo en mi archivo original.

````python
# Archivo: modulo.py
def saludar(nombre):
    """Documentación de nuestra funcion"""
	print("Hola " + nombre)

class Persona:
    """Documentación de nuestra clase"""
    def __init__(self,nombre):
        """Documentación de nuestro método"""
        self.nombre = nombre
----------------------------

# Importar todas las funciones y clases del fichero 'modulo'
import modulo
modulo.saludar("Jorge")
usuarioP = modulo.Persona("Pedro")


# Importar solo una funcion o clase del fichero 'modulo'
from modulo import saludar
saludar("Jorge")
#Puedo simplificar, si quiero multiples
from modulo import (suma,resta,mul)

#Puedo importar todos con la misma forma
from modulo import *

#opcional renombrar la funcion
from modulo import saludar as quehay
````

### PIP

Gestor de paquetes y módulos para python, `en node era npm`

````shell
Para ver si lo tenemos
$ pip --version

Paquetes y modulos instalados
$ pip list
````

Como importar un modulo nuevo

````shell
$ pip install camelcase
````

````python
import camelcase
came1 = camelcase.CamelCase() #Objeto de la clase, una instancia
texto = "mi nombre es antonio"
print(came1.jump(texto))
````

Podemos desinstalarlo si ya no queremos el modulo

````shell
$ pip uninstall camelcase
````

Como en `NodeJS` en la carpeta : Se encuentran todos los módulos que están disponibles a usar en cualquier ubicación desde consola
> C:\Users\HP\AppData\Local\Programs\Python\Python38-32\Lib\site-packages

#### Archivos py

Cuando importamos un modulo en otro archivo se creara una carpeta llamada `__pycahe__`  que seria el modulo compilado a código binario. Esto facilita ya que no estará compilando a código maquina a cada rato, si no leera el archivo ejecutable

Este archivo se crea cuando ha sido importado por primera vez o cuando el modulo a sido modificado.

#### Atributo `__name__`

A diferencia de `C` no tenemos una función principal `main` ,podemos reconocer cual es el archivo que se esta ejecutando

````python
if __name__ == '__main__':
    print("Yo soy el archivo principal")
else:
    print("Esto como modulo")
````

#### Paquetes

Es un folder o carpeta que tiene muchos módulos. Empecemos, debemos crear un archivo llamado `__init.py` junto con todos los módulos(`aves.py` e `felinos.py`) en la misma ubicación. Todos estos archivos los guardo en una carpeta ,ejem `animales`

En el archivo principal importo la carpeta animales

````python
# from elPaquete.elarchivo
from animales.aves import Pinguino
pinguino = Pinguino()
````

Y que pasa con el archivo `__init.py` esta en blanco?? . Lo podemos rellenar

````python
# En __init.py
print("Este es un mensaje de init")
#Osea esto siempre se ejecutara siempre que se importe el `paquete` animales
# Podemos poner todos los imports en este archivo 
# Podemos poner la conexion a la base de datos asi no tengo que hacerlo en cada modulo
# Podemos definir funciones
````

#### Anotaciones

Las anotaciones son **únicamente de carácter informativo**

````python
def saludo(nombre : str )-> None:
	print("Hola" + nombre)
    
#Informamos que es 'str' un string
#Podemos especificar los siguientes: str,int,float y bool
#Informamos el tipo de dato que retorna (->)
#None : como void
def suma(num1 : int,num2 : int = 100)-> int:
    return num1+num2
print(suma(56.8)) #Puede recibir cualquier tipo
````

#### comprehension

````python
lista = []

for x in range(0,101):
    lista.append(x)
print(lista)

#PODEMOS obtener el mismo resultado en menos lineas
# Dependiendo puede ser [],() o {}
# ['valor a almacenar' | 'ciclo']
estructura = [x for x in range(0,101)]
print(estructura)

# Tuplas
# ['valor'|'ciclo' |'condicion']
estructura = tuple((x for x in range(0,101) if x % 2 == 0 ))
print(estructura)

#Utiliza esta forma cuando es simple el algoritmo
# Diccionario
dic = {indice:valor for indice,valor in enumerate(estructura)}
````





## Sección 10 : Ficheros de texto

````python
# (rt : r lectura, t : texto)
fichero = open("nobreDelArchivo.txt","rt")
datos_fichero = fichero.read()
print(datos_fichero)

# crear y/o guardar informacion en un archivo
# (wt : w escritura, t : texto)
fichero = open("fichero_para_grabar.txt","wt")
cadena_texto = "Hay que bonito soy"
fichero.write(cadena_texto)
fichero.close() #cerramos el fichero, para que mas adelante se pueda abrir

# Agregar info al archivo
# (at : a append, t : texto)
fichero = open("fichero_para_grabar.txt","at")
cadena_texto = "\n nueva linea"
fichero.write(cadena_texto) # lo agrega al final
fichero.close()

# Borrar un fichero de texto
import os
os.remove("fichero.txt")
````

## Sección 11 : Ficheros binarios

````python
import pickle	#Modulo para manejar ficheros binarios
lista = ["rojo", "axul"]
fichero = open("archivo.pckl","wb")
pickle.dump(lista,fichero)
fichero.close()

# Leer datos de un fichero binario
fichero = open("archivo.pckl","rb")
lista_leida = pickle.load(fichero)
print(lista_leida)

#Que onda con este guardado, Fijate que se guarda como un diccionario osea que cuando lo vuelva a leer sera un array y no una cadena de texto '[1,2,3]' 
````

## Sección 12 : Gestión de errores

````python
# try ... except ... else .... finally

# Si se produce algun error en el bloque 'try' se ejecuta el bloque 'except'
try:
	n1 = 5
    n2 = 0
    div = 5 /0
    print(div)
except:
	print("Ha habido un error")

    
#Podemos especificar que 'except' puede ser
try:
	n1 = 5
    n2 = 0
    div = 5 /0
    print(div)
except ZeroDivisionError:	#Si coincide con este tipo de error
    print("Error, division entre cero")
except:    #Si es otro error distinto al de arriba
	print("Ha habido un error")
   

#En case de que no haya error en el bloque 'try' se ejecuta 'else'
try:
    #...
except:
    #...
else:
    print("la division funciono correctamente")
    

# finally  : Permite ejecutar un codigo independiente del 'try' y del 'except' 
try:
    #...
except:
    #...
else:
    #...
finally:
    print("Esta prueba try se ha acabado")
````

## Sección 13: Expr Reg, JSON, fecha y hora

### Expresiones Regulares

Como en JavaScript con la librería 're', ``ver apunte de E.R. en javascript`

````python
import re
texto = "Hola , mi nombre es antonio"
resultado = re.search("nombre",texto)
# 'resultado' es un objeto con informacion de la busqueda
# resultado.start() / resultado.end()
if (resultado):
    print("cadena encontrada")
else
	print("cadena no encontrada")
    
# ---
re.search("antonio%",texto)
re.search("^Hola",texto)

# el caracter (.) es cualquiera, el (*) es una o mas repeticiones
re.search("mi.*es",texto)

----
# findall : busca todas las ocurrencias que halla, y las muestra en un array
texto = """
El coche de Luis es rojo,
el coche de antonio es blanco,
y el coche de maria es rojo
"""

re.findall("coche.*rojo",texto)

# split: cortar bajo un separador
re.split("\n",texto)

# sub : sustituye todas las coincidencias
re.sub("la palabra que queremos cambiar","el nuevo valor",texto)
````

### JSON

Convertir datos de un diccionario a JSON

````python
# Diccionario
products = { "nombre" : "silla" , "color" : "rojo" , "precio" : 80}

# comvierte un diccionario en formato JSON
import json
estructura_JSON = json.dump(products)
estructura_JSON[0]

# JSON => Diccionario
products2 = json.loads(estructura_json)
products2["nombre"]
````

### fecha y hora

````python
from datetime import datetime
fechaHoy = datetime.now()
print(fechaHoy)

# Los metodos
.year		.hour
.month		.minute
.day		.second			.microsecond
````

## Sección 14: Base de datos

````python
# SQlite : sistema de gestion de base de datos
import sqlite3
# Nombre de la base de datos si existe de lo contrario lo crea
conexion = sqlite3.connect("mydatabase.db")

#Para ejecutar sentencias sql con `execute`: SELECT, INSERT,UPDATE,DELETE, WHERE , ORDERBY
cursor = conexion.cursor()
cursor.execute("CREATE TABLE personas(nombre TEXT,apellido TEXT,edad INTEGER)")

#Para comitear los cambios
conexion.commit()
conexion.close()
````

#### Insertar varias filas a la vez

````python
cursor = conexion.cursor()
lista = [('Pedro','Rodrigez',26),('Maria','Lopez',45)]

cursor.executemany("INSERT INTO PERSONAS VALUES (?,?,?,?)",lista)
conexion.commit()
conexion.close()
````

Algunos ejemplos

````python
import sqlite3
conexion = sqlite3.connect("mydatabase.db")
cursor = conexion.cursor()
cursor.execute("SELECT * FROM PERSONAS")
personas = cursor.fetchall()

for pe in personas:
    print(pe)

# No hay commit pues estoy seleccionando, si fuera delete/Insert/update y quiero persistir los cambios, nesesariamete nesecitamos el "commit"
conexion.close()
````



## Sección 15: Interfaz gráfica con el módulo tkinter

Vendría a ser como el `Windos form de C#`

````python
import tkinter
raiz = tkinter.Tk()
raiz.title("Mi programa") #Como en html
#Esto de arriba siempre debe estar
-----------------------

# creamos el componente FRAME [body en HTML]
frame = tkinter.Frame(raiz)
frame.config(bg="blue",width=400,height=300)#Fondo y tamaño
frame.pack() #mostrar por pantalla
#Es como una caja centrada de color azul,

# creamos el componente LABEL (etiqueta) [span en HTML]
texto = "Hola Mundo"
etiqueta = tkinter.Label(raiz,text=texto) #texto
#Color/fondo/tipografia,tamaño
etiqueta.config(fg="green",bg="lightgrey",font=("Cortana",30))
etiqueta.pack() #mostrar por pantalla

# creamos el componente ENTRY [input en HTML]
# Entrada de datos por teclado
entrada = tkinter.Entry(raiz)
#justificacion/tipo(show:"*")
entrada.config(justify="center",show="*")
entrada.pack()

# creamos un componente TEXT [texArea en HTML]
entrada = tkinter.Text(raiz)
# Ancho/Alto/padx y pady : Padding/selectbackdroom: color al seleccionar
entrada.config(width=20, heigth=10,font=("Verdana",15),padx=10,pady=10, selectbackground="lightgrey")
entrada.pack()

# Componente Butom [Butom en HTML]
def accion():
    print("Hola mundo")
# command: funcion que se ejecutara
botom = tkinter.Button(raiz,text="Ejecutar",command=accion)
botom.config(fg="green")
botom.pack()

# Componente RadioButom[igual que HTML]
def seleccionar():
    print(opcion.get())
#Se guarda en la variable 'opcion'
opcion = tkinter.IntVar()

radiobutton1 = tkinter.Radiobutton(raiz,text="Opcion 1",variable=opcion,value=1,command=seleccionar)
radiobutton1.pack()

radiobutton2 = tkinter.Radiobutton(raiz,text="Opcion 2",variable=opcion,value=2,command=seleccionar)
radiobutton2.pack()

# Componente ChekButton[igual que HTML]
def verificar():
    valor = check1.get()
    if (valor == 1):
        print("El check esta activado")
    else:
        print("El check esta desactivado")

check1 = tkinter.IntVar()
# onvalue: valor si esta asignado /offvalue : lo contrario
boton1 = tkinter.Checkbutton(raiz, text="Opcion 1",variable=check1,onvalue=1,offvalue=0,command=verificar)
boton1.pack() #empaqueta el tag en un div, ponele!!

# Componente MessageBox[igual que HTML]
from tkinter import messagebox
def avisar():
    tkinter.messagebox.showinfo("Titulo","Mensaje con la info")

boton = tkinter.Button(raiz,text="Pulsar para aviso",command=avisar)
boton.pack() #empaqueta el tag en un div, ponele!!

# Componente MessageBox para una desicion[igual que HTML]
from tkinter import messagebox
def avisar():
    #Se crea el Messagebox
    resultado = tkinter.messagebox.askquestion("Advertencia PAPU","¿Quieres borrar este fichero?")
    if resultado == "yes":
        print("Se, borro ")
    else:
        print("No, no quiero borrar")

#Botom ya echo anteriormente    
boton = tkinter.Button(raiz,text="Pulsar para aviso",command=avisar)
boton.pack() #empaqueta el tag en un div, ponele!!


# Componente Filedialog para abrir un fichero [input=file]
from tkinter import filedialog
def abrirfichero:
    rutafichero = filedialog.askopenfilename(title="Abrir un fichero")
    print(rutafichero)
boton = tkinter.Button(raiz,text="Seleccionar",command=abrirfichero)
boton.pack()

raiz.mainloop()
````

## Sección 16: Generar documentación automáticamente

#### Docstrings

````python
def saludar(nombre):
    """
    Este texto de ayuda aparecera si ejecuto(**)
    """
    print("Hola", nombre)

(**) help(saludar)

class Saludos:
    """
    Texto sobre la clase
    """
    def m(self,nombre):
        """Sobre la funcion"""
        print(nombre)
        
(**) help(Saludos)        
````

#### pydoc

Generar documentación automática desde la consola o terminal

````shell
Sale en la terminal
$ pydoc ruta_del_fichero

Se genera un archivo .html con la documentacion
$ pydoc -w ruta_del_fichero

Para salir Crtl + z  ó q
````

## Sección 17 - Pruebas Automáticas

#### Doctest

Generar pruebas dentro de la documentación, se ponen en el operador `>>>`

````python
def sumar(num1,num2):
	"""
	Esta es la documentacion de la funcion
	Recibe dos parametros y devuelve la suma
	
	>>> sumar(4,3)
	7
	
	>>> sumar(5,4)
	9
	
	>>> sumar(1,3)
	7
	
	"""
    return num1+num2

resultado = sumar(2,4)
print(resultado)

#Para que se ejecute las pruebas
import doctest
doctest.testmod()

-----------------------------------------
#En la terminal, no olvidar (-v) para ejecutar las pruebas
$ python sumar.py -v
````

#### Unittest

Sirve para crear pruebas dentro del propio código

````python
def multiplicar(num1,num2):
	return num1*num2

import unittest
class pruebas(unittest,TestCase):
    def test(self):
        self.assertEqual(sumar(2,4,8))
        
if __name__ == '__main__':
    unittest.main()
````



## 18 - Funciones Avanzadas

#### Funciones Generadoras

````
range(4) //empieza de 0

range(0,4) //de 0 a 4

ramge(0,9,2) // de 0 a 9 , saltando de a 2s
````

#### Filter

````python
# La 'funcion' retorna un booleano
lista_filtrada = filter(funcion,lista)
resultado = list(lista_filtrada)
````

#### Map

````python
# La 'fucion' debe retornar algo
lista_mapeada = map(funcion,lista)
resultado = list(lista_mapeada)
````

> TIP : Al contrario de crear una `def funcion: ...`  Usamos una función lambda

````python
lista_res = list(map(lambda num : num *2),lista)
````

## 19 - Módulo numpy

Modulo de `arrays/matrices` , nada más :slightly_smiling_face: :slightly_smiling_face:

#### Creando arrays

Los <span style="background:yellow;">Arrays </span> que traducido al español seria <span style="background:yellow;">Matrices</span> ,muchas veces se trata a los `arrays` de `1xn` igual que una `lista` pero ten presente que es una <span style="background:yellow;">Matriz de  1xn</span>  , solo eso :smiley:

````python
import numpy as np
np.zeros(4) 	  # Un array de 4 ceros,ojo es decimal
np.ones(4) 		  # Un array de 4 1'nos
np.ones((2,2))    # matriz de 2x2 llena de unos
np.full((2,2),value)  # funciona igual a np.ones pero llena la matriz con el valor value.

np.arange(5)      # [0..4]
np.arange(2,20,3) # [2,5,8,11,14,17]
np.arange(8,1,-1) # [8,7,6,5,4,3,2]

#APA la PAPA un 'ARRAY' != !LISTA
lista1 = [1,2,3,4]
array1 = np.array(lista1)
print(type(lista1))
print(type(array1))

#Array doble
lista1 = [1,2,3,4]
lista2 = [5,6,7,8]
lista_doble = (lista1,lista2)
array_doble = np.array(lista_doble)
print(array_doble)

#Informacion del array
print(array_doble.shape)
(2,4) #info: 2 filas y 4 columnas

#Tipo de dato que contiene el array
array_doble.dtype
````

#### Operaciones

````python
# Operaciones con arrays
import numpy as np
#Ya estaras contento transformaste mi lista en un array de 1x4
array1 = np.array([1,2,3,4])

#Que ganamos con esto? Pues trata de duplicar si un for
array1*2 #Multiplica a cada elemento por 2
#TOMALA mas intuitivo y mejor

array1+4 #+4 a cada elemento
#TIP: estas operaciones no persisten en el array
array1 = array1 +4 #SOl

lista1 = [1,2,3,4]
lista2 = [5,6,7,8]
lista_doble = (lista1,lista2)
array_doble = np.array(lista_doble)

array_doble + 5 # (+5) a todos los elementos de la matriz
array_doble ** 2 # al cuadrado todos
````

#### Indexación

````python
import numpy as np
array = np.arange(0,11)

#cortar arrays
array[0:3] # [0,1,2]
array[:] # ==array

array_copia = array.copy() # Sin el copy es igual
#TIP : la copia no guarda ninguna relacion con el original, osea que los cambios de la copia no persisten en el original

array2 = np.array(([1,2,3],[4,5,6],[7,8,9]))
array2[1] # [4,5,6]
array2[1][2] # 6
````

#### Matrices

````python
array = np.arange(15).reshape((3,5))
"""
Del [0..14] ordenalos en 3:filas y 5:columnas
array==	[[ 0  1  2  3  4]
 		 [ 5  6  7  8  9]
 		 [10 11 12 13 14]]
"""
array_tras = array.T #La transpuesta


#SUTIL DIFERENCIA
[[1,2][2,5]] # esto es una lista(esto queda plano)
np.array([[1,2][2,5]])  #Esto un array(lo dota de dimension)
	[[1,2],
     [2,5]]

````

#### Entrada y salida con arrays

````python
array1 = np.arange(6) 

np.save('array1s',array1)
np.load('array1s.npy') #recuperar el valor del array

array1 = np.arange(6) 
array2 = np.arange(8)
np.savez('arrays',x=array1,y=array2) #Guardamos 2 arrays

array_recuperado = np.load('arrays.npz') #Recuperamos los arrays
print(array_recuperado['x'])

#Tambien podemos guardarlo en un fichero de texto
np.savetxt('mificheroarray.txt',array2,delimiter=',')
res = np.loadtxt('mificheroarray.txt',delimiter=',')
print(res)
````

#### Funciones con arrays

````python
import numpy as np
array = np.arange(5)
res = np.sqrt(array)#Raiz cuadrada a cada elemento
print(res)

# rand(d) d: la dimension del array
ran = np.random.rand(5)#5 Numeros random entre [0, 1)
print(ran)

lista = [5,6,7,8,9]
array2 = np.array(lista)

#Suma cada elemento de ambos arrays por posicion
suma = np.add(array,array2)
print(suma)

#El maximo entre dos, toma cada elemento para compararlos
maximo = np.maximum(array,array2)
print(maximo)
````

## Matemática

````python
#Algunas cuestiones
5e-10    #Esto equivale 5*10^-3 == 0.005
````



#### Arrays en mate

````python
import numpy as np

np.log(x)		#Logaritmo natural
np.cos(np.pi)	#Coseno
np.sin(np.pi/2)	#Seno
np.sqrt(4)		#2.0
np.e            #2.718281828459045

# La ventaja de trabajar con arrays son las funciones a cada elemento que se hacen
array_l = [2,4,6]
np.log(array_l)

# POSICION DEL ELEMENTO MAXIMO de un array(Si hay muchas, la primera)
v = [7,8,9,3]
np.argmax(v)
2

# ELEMENTO MAXIMO de un array de cualquier dimension
M = np.array([[1,2,3],[4,5,6],[9,0,7]])
V = [4,5,6]
np.max(M)
np.max(V)  

# Producto interno
x = np.array([1,2,0])
y = np.array([0,4,5])
np.dot(x,y)

#MATRICES
A = np.array([1,0,0]) #array de 1x3
B = np.array([[1,2,0],[0,1,0],[1,0,0]]) #array de 3x3
        [[1 2 0]
         [0 1 0]
         [1 0 0]]

#Acceder a los valores matriz
B[0][1] ó B[(0,1)]  # fila 0 , columna 1

#debe respetar el orden de las dimensiones    
np.dot(A,B)      #Producto de Matrices
np.shape(B)      #Informacion de la matriz (#filas,#columnas)
A*B			     #Multiplica cada elemento de igual posicion	
A.T              #Transpuesta ó np.transpose(A)
np.identity(n)   #Matriz identidad de tama~no n.

# Intervalos
np.linspace(1,8,10) # Devuelve un array de 10 elementos equispaciados
````

