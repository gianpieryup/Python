# Introducción a Python

De propósito general, **multiparadigma** ,de **tipado dinámico** , open source

- *Lenguaje compilado* : Es aquel que requiere de un `compilador` ósea transforma mi `.h` a `.exe` el cual mi computadora entiende. Ejemplos `Java, C, C++, C#,..`
- *Lenguaje interpretado* : Toma el archivo y traduce línea por línea a lenguaje maquina. Ejemplos `PHP, Ruby, Python`

`Python` usa ambos , pero eso depende de que procesos

### Ejecutar un programa en Python

1. Si tienes Python instalado, como lo se ? En la terminal poner   `python --version`
   
   Por consola: Escribir  `python`  +  <kbd> Enter </kbd> . Te quedara un símbolo.

   > *>>>*  'Aquí puedes escribir código python'

   Para salir de la consola.

   > *>>>* exit()

2. Si quiero ejecutar un archivo.py , primero estar parado por consola en la ubicación del archivo.

   > *>* python archivo.py



### Buenas Practicas

En Python existe los PEP's, Mejoras de propuestas de Python, de los cuales al momento de codificar nos interesa PEP8.
PEP8 Es una guía de codificación, la cual nos permite escribir código Python de una manera, mucho más legible y de forma consistente, a través de ciertas "reglas" y recomendaciones. Por ejemplo, en la guía podemos encontrar

- utilizar espacios sobre tabs.
- utilizar la nomenclatura de **snake case** para nombrar variables. (**ej:** una_palabra_muy_larga)
- utilizar palabras en mayúsculas para las constantes.
- Para las clases : MiClaseConNombreMuyLargo



## INDICE
<!-- TOC -->

- [Cadenas Variables y Números](#cadenas-variables-y-n%C3%BAmeros)
    - [Conversión de Tipo de dato](#conversi%C3%B3n-de-tipo-de-dato)
    - [Cadena de Texto](#cadena-de-texto)
    - [Funciones de cadenas](#funciones-de-cadenas)
    - [Imprimir variables de cadena de texto](#imprimir-variables-de-cadena-de-texto)
    - [Entrada texto por teclado](#entrada-texto-por-teclado)
    - [Operadores](#operadores)
    - [Fechas](#fechas)
- [Colección de datos](#colecci%C3%B3n-de-datos)
    - [Listas:](#listas)
    - [Matriz](#matriz)
    - [Pilas](#pilas)
    - [Tuplas](#tuplas)
    - [Conjuntos](#conjuntos)
    - [Diccionario](#diccionario)
- [Bucles y Condiciones](#bucles-y-condiciones)
    - [None](#none)
    - [if-else](#if-else)
    - [No podía faltar el if ternario](#no-pod%C3%ADa-faltar-el-if-ternario)
    - [Bucles](#bucles)
        - [BONUS](#bonus)
- [Clases objetos y Funciones](#clases-objetos-y-funciones)
    - [Clases](#clases)
        - [Herencia](#herencia)
        - [Sobre escritura de métodos](#sobre-escritura-de-m%C3%A9todos)
        - [La clase Object](#la-clase-object)
    - [Funciones](#funciones)
         - [Cantidad indefinida de Parámetros](#cantidad-indefinida-de-par%C3%A1metros)
        - [Como terminar una función](#como-terminar-una-funci%C3%B3n)
            - [Alcance de las variables](#alcance-de-las-variables)
            - [Función Lambda](#funci%C3%B3n-lambda)
        - [Funciones Anidadas](#funciones-anidadas)
        - [Closures](#closures)
        - [Decoradores](#decoradores)
    - [Generadores](#generadores)
<!-- /TOC -->

## Cadenas Variables y Números

Sensible a mayúsculas para declarar variables.

````python
var1 = "Hola "
var2 = "Mundo"
conca = var1 + var2
> conca
"Hola Mundo"
````

```python
a = 3
> type(a)  # hallar el tipo de dato de la variable
int

b = 3.7
> type(b)
float

> a + b  # Como en C# convierte implicitamente (a) de (int -> float)
float

#ASIGNACION MULTIPLE
a , b, c = 10, "Juan", "Pedro"
```


## Conversión de Tipo de dato

````python
num = 5
cadena = str(num) # Coversion a cadena
> cadena
'5'
> "Hola" + num //error => str(num) ok

cadena = '25'
num = int(cadena) # Conversion a entero
> num
25

cadena = '25.7'  # Ojo aca la variable no es int, recordar
num = float(cadena) # Conversion a decimal
> num
25.7
````


## Cadena de Texto

````python
cadena = "Hola Mundo"
> cadena[0] # 0 -> H / 1 -> o / ...
'H'
> cadena[-1] # -1 -> o / -2 -> d /... (Es un recorrido inverso)
'o'
> cadena[2:7] # Desde la pos 2 (inclusive) hasta la 7 (no se incluye la 7)
'la Mu'
> cadena[2:] # Todo a partir de la posicion 2
'la Mundo'
> cadena[:5] # Todos los elementos hasta la posicion 5 no inclusive
'Hola'
````

### Funciones de cadenas

````python
cadena = "Hola Mundo"
longitud: len(cadena)
    
mayusculas: cadena.upper() # solo muestra
cadena = cadena.upper() # si quiero modificar

minusculas : cadena.lower()
    
cadena.split()
["Hola","Mundo"]

cadena2 = "hola,mundo"
cadena2.split(',')


# Si bien los strings son casi como listas, son inmutables
# Osea no se pueden alterar
nombre = "Marianito"
nombre[8] = 'x'
#para modificar habria que setear el valor la variable 'nombre'

# Esto no funciona, para arreglarlo transformarlo a 'list'
nombre = "Marianito"
milista = list(nombre)
milista[8] = 'x'

#  Cómo formatear la moneda en Python
amount = 123456.78
currency = "${:,.2f}".format(amount)

print(currency)
OUTPUT> $123,456.78
````

### Imprimir variables de cadena de texto

````python
nombre = 'Julio'
print("hola" + nombre)

print("Hola {}, feliz {}".format(nombre,"cumple"))


# Por defecto {} se justifica hacia la "izquierda" desde el lugar inicial
print("Jus izq : {r}".format(r=10))
print("Jus izq : {r}".format(r=200))
print("Jus izq : {r}".format(r=3000))

# Jus izq : 10
# Jus izq : 200
# Jus izq : 3000



# Si agregamos los : -> {0:4} se justifica hacia la "derecha" empezando 3 espacios
print("Jus der : {r:4}".format(r=10))
print("Jus der : {r:4}".format(r=200))
print("Jus der : {r:4}".format(r=3000))

# Jus der :   10
# Jus der :  200
# Jus der : 3000

#Un entero y 3 numeros decimales
print("acotado : {r:1.3f}",format(r=res)) 

#python > 3.6 se puede embeber las variables:
print(f"Hola {nombre} como esta la familia")

In [1]: txt1 = "izquierda"
In [2]: txt2 = "centrado"
In [3]: txt3 = "derecha"
In [4]: print("||{:<15}||{:^15}||{:>15}||".format(txt1, txt2, txt3))
               ||izquierda      ||   centrado    ||        derecha||

````

### Entrada texto por teclado

````python
print("Introduce tu nombre")
entrada = input()
print(entrada)

# Forma mas culera
nombre = input("Nombre: ")
edad = int(input("Edad: "))
print(nombre, "tiene",edad,"años")
````

### Operadores

Diferencia importante entre el operador `(== y is)`

````python
resto(%), potencia(**) , cociente (//)

#a = a + b   // a += b
(*=,/=,**=,//=)

(==,!=,<,>,>=,<=)

(and, or, not)

----------------------------
a = [1,2,3]
b = [1,2,3]

a == b  # True

a is b  # False

# En este casa obtenemos False; Esto se debe a que con == compararemos que dos valores sean iguales y con is compareremos que dos objetos sean iguales, cosas completamente diferentes

# Si imprimimos el id de cada objeto, observaremos que son valores completamente diferentes, con lo cual concluimos que son dos objetos diferentes

>>> id(a)
2459807112128
>>> id(b)
2459807129024
````

### Fechas

````python
#Es necesario importar las depencendias necesarias
from datetime import date, datetime, timedelta

# Día actual: 2023-11-06
today = date.today()
# Fecha actual: 2023-11-06 01:27:45.918486
now = datetime.now()
# Definir mi fecha
my_date = datetime(2023, 10, 28, 9)

# OPERACIONES CON FECHAS
# Sumar dos días a la fecha actual: 2023-11-08 01:29:41.098619
new_date = now + timedelta(days=2)

# Castear con un formato a tipo string
format = now.strftime('Día :%d, Mes: %m, Año: %Y, Hora: %H')
````

### Colección de datos

#### Listas: 

Es *mutable* (puedo agregar y quitar elementos)

````python
x = ["hola",2020]
x[0]
"hola"

"""
MUTABLE:
		x[0] = 7
		x
		[7,2020]
"""

#LONGITUD
len(x)    # Rpta 2

#LIST : como palabra reservada
numberlist = list((1,2,3,4)) #list() solo recibe un argumento

"""
TIP: En python, cuando asignamos una lista a una variable, esta variable hace referencia      al lugar de la memoria en la que se encuentra la lista, y no a su contenido.

	 l = [1,2,3]
	 w = l  #Se igualaron los punteros,estos apuntan a la misma direccion en memoria
	 l[0] = 666
	 print(w)
     [666,2,3]
"""
x.append("naranja") 
> ["hola",2020,"naranja"]

x.remove("hola")
> [2020,"naranja"]

x = list(range(1,10)) => x = [1,2,3,4,5,6,7,8,9]

#Recorrer una lista con (for in)
for color in colores
	print(color)
    
#Borrar todos los elementos
x.clear()

#Existen mas funciones
#  Pertenece (in)
>>> elemento in conjunto
true

# quitar el ultimo, esto altera la lista original
.pop() #devuelve el ultimo

# SUBLISTAS
cursos = ["a","b","c","d","e"]
sub = cursos[0:3] # "abc" no incluye la posicion cursos[3]
sub = cursos[:7] # equivale a cursos[0:7]
sub = cursos[1:7:2] # desde / hasta / saltos
sub = cursos[::-1] # INVERTIR LISTA

# BONUS
x = [3, 4, 7, 11]
y = [1, 5, 6]
[x,y]
[[3, 4, 7, 11], [1, 5, 6]]

#Concatenar
x+y
[3, 4, 7, 11, 1, 5, 6]

#Multiplicar
y*2      # Sera distinto con un array, lista != array
[1, 5, 6, 1, 5, 6]

#El ultimo elemento
x[-1] #Igual que las cadenas de cadenas de texto
11

# "Persistencia" al pasar por parametro (Modificar elementos [SI], Reasignar [NO])
````

#### Matriz

Mas adelante en *Matemáticas* usaremos el modulo `numpy`

````python
fila1 = [10,20]
fila2 = [30,40]
matriz = [fila1, fila2]
matriz[1][0] == 30
````



#### Pilas

````python
Como una estructura de datos una Pila - LIFO
.append() # añadir al final de pila
.pop() # quitar el ultimo que fue añadido
````

#### Tuplas

Una colección de elementos *inmutables* (<span style="background:yellow;">**no se pueden alterar**</span>).

Son mas rápidas para la búsqueda de elementos

````python
x = (1,2,3,4,5,6,7,8,9)
x[0] == 1
sub = x[:9:2] #los primeros 9 elementos de a 2 por 2

#TIP
tupla = (1,2,3,4)
# Para que esta asignacion funcione deben tener igual cantidad de variables
a, b, c, d = tupla # la tupla tiene 4 elementos
# O bien si solo te importa ciertas posiciones
a, b, _, _ = tupla

tupla = (1,2,3,4,5,6)
a, b, c, *d = tupla
# a=1,b=2,c=3,d=[4,5,6]

a, *b, c, d = tupla
# a=1,b=[2,3,4],c=5,d=6 /python es inteligente


- tuple() convierte una lista de elementos en una tupla
tupla = tuple([1,2,3])
# tupla == (1,2,3)

- list() convierete una tupla a una nueva lista

# BONUS
Los strings pueden convertirse tanto en tuplas como en listas
- zip(arr1,arr2) #devuelve una concatenacion, cortando la de mayor longitud
````

#### Conjuntos

Una colección de elementos desordenados (sin índices) y <span style="background:yellow;">sin elementos repetidos</span> .La palabra “**set**” significa “**conjunto**” en inglés. Es **mutable** como *las listas y los diccionarios* que permite agregar y quitar elementos cumpliendo los requisitos de unicidad y <span style="background:yellow;">búsqueda en tiempo constante.</span>

````python
conj_color = {"rojo","verde","azul"}
conj_color[0] #Error
conj_color.add("negro")#ADD
conj_color.remove("rojo")#DELETE

#Además es posible hacer operaciones entre sets como unión, intersección y diferencia
s1.union(s2)
s1.intersection(s2)
s1.difference(s2)
````

**NO OLVIDAR**

Notar que la **sintaxis para crear un conjunto** es muy similar a la de creación de diccionarios.
El caso especial es cuando queremos crear un conjunto vacío: la sintaxis {} no funcionará, ya
que eso crea un diccionario vacío. Podemos crear un conjunto vacío con: `set()`



#### Diccionario

Una estructura de datos distinta a tuplas o listas (dado que no esta indexado por números) sino (llave: valor) . Básicamente es un objeto JSON

````python
# Si quiero declarar una variable vacio del tipo diccionario
dicc = {}

#como un json (clave:valor)
dic = {'color':'rojo', 'tipo':'toyotas'}
#dic['color'] == 'rojo'

#Agregar elementos, si no existe la key la agrega
dic['black'] = 'negro'

dic.pop['tipo'] #Borra este elemento y devuelve su valor 'toyotas'
del dic['tipo'] #Alternativa de borrado
dic.clear() ó dic = {} # Borrar todo el diccionario
----

diccionario = {"a":1,"b":2,"a":3}
# NO hay error pero no pueden haber llaves duplicadas, en caso yo defina esto, automaticamente queda el ultimo valor

"z" in diccionario #Toma como buscador las claves, en este caso la res='false'

res = diccionario["z"] #Error, usar el de abajo
#Igual al anteiror pero si hay error nos devuelve 'None'
res = diccionario.get("z")
#Ademas tiene un parametro opcional a devolver si no lo encuentra
res = diccionario.get("z",0)

# Si existe la clave 'z' cambia su valor. Si no lo agrega
res = diccionario.setdefault("z",{})
---


# Keys
dic.keys()

# Values
dic.values()

# Items
res = list(dic.items())
res == [('a',1),('b',2),('c',3)]

# Recorrer un diccionario, por clave
for clave in dic:
	print(clave)

# Recorrer de cada elemento (key:values) 
for clave,valor in dic.items():
	print(clave,valor)

------------
# Si ya no quiero trabajar con esta estructura pueso convertirla en lista o en tupla, Osea primero saco las keys o bien los values y apartir de ai
````

### Bucles y Condiciones

#### None

````python
variable = None
print(variable)
#Python lo toma como un valor falso {None,0,[]}
if(None):
else
	print("aca")
````



#### if-else

````python
if(3 > 4):
    print("3 es mayor que 4")

if (a > b) and (b < d):
    print("hola")
    
if 'condicion' :
    |#codigo
else
	print("en el else")
    
if 'condicion' :			|	if (){
    #codigo					|	#cofigo
elif (a == b)				|	}else{
	print("son iguales")	|		if(a == b){
else						|		print("son iguales") 
	print("ninguna")		|		}else{
    						|		print("ninguna")
							|		}
							|	}	
````

#### No podía faltar el if ternario

````python
resultado = valor_si if condicion else valor_no
````



#### Bucles

````python
# FOR
for elemento in lista:
    print(elemento)

# Aca el 'num' seria un numero entero = 0, en cada iteracion aumenta en 1, automaticamente, podemos especificar num
for num , letra in enumerate ( palabra ):
	print (num , letra )

#Especificar el valor inicial de 'num' aca empieza en '7'
for num , letra in enumerate ( palabra,7 ):
	print (num , letra )
    
# Funcionan el break y el continue  

# WHILE
while (condicion):
    print("aun estoy en el while")
````

#### BONUS

````python
# La funcion 'range'
range(10) # == range(0,10,1)
range(valorinicial,valorfinal,intervalo?opcional)
range(3,8,2)
3
5
7
````

## Clases objetos y Funciones

### Clases

````python
class Clasesilla:
	color = 'blanco' #es una variable de clase y pueden ser usada por cualquier instancia
	precio = 100
    
obj = Clasesilla() #instanciar un objeto
obj.color #funciona como 'get' y 'set'

--------------------------------------------
--#Aca los atributos son estaticos,creo
print(Clasesilla.color) # devuelve 'blanco'


#METODOS ESTATICOS
# TIP: no podemos usar variables creadas en la instancia
# Si podemos utilizar variables de clase(Por que es estatico,crep)
# Fijate que no uso 'self', osea es una metodo de la clase
numero = 2
@staticmethod
def area(base,altura)
	return (base - altura)/Triangulo.numero

#METODOS de CLASE
# [cls: hace referencia a la clase
# [self: hace referencia a la instancia]
class Circulo:
    pi = 3.14159265
    @classmethod
    def area(cls,radio):
        return cls.pi * radio**2


--------------------------------------------
#OBLIFATORIO:Todos los metodos deben recibir el paramtero self
#Notar que no debo declarar como atributos 'nombre' ó 'edad'
class Persona:
    #Constructor
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    #Metodo
    def saludar(self):	#NO OLVIDAR el 'self'
        print("Hola me llamo",self.nombre)
        
persona1 = Persona('Juan',37)  
persona1.saludar()#Notar que no se le pasa parametros

-----#Algunas funcionalidades
print(type(persona1))

#Se puede generar atributos fuera de la clase como en PHP :v
class Usuario:
    def saludar(self):
        print("Hola")
	def mostrar_nombre(self):
        print(self.nombre)
        
codi = Usuario()
codi.nombre = 'codi'
codi.mostrar_nombre()

----
#Constructor con valores por default
    def __init__(self,nombre='',edad=''):
        self.nombre = nombre
        self.edad = edad
````

#### Herencia

````python
class Animal:

class Perro(Animal): #Poner entre parentesis la "clase Padre"
    
#HERENCIA MULTIPLE
class Animal:
class Mascota:

class Perro(Animal,Mascota):
# SUPERTIP : Las clases padres deben ser definidas antes que Perro
# TIP2 : Si ambas clases padres tienen el mismo metodo, busca de izquierda a derecha. Pero si la define Perro se queda aca
````

#### Sobre escritura de métodos

````python
class Animal:
	def dormir(self):
        print("Dormir Animal")

#Se trata como metodos estaticos cuando estan heredando     
class Perro(Animal):
	def dormir(self):
        Animal.dormir(self)#Si hay parametros ,,,,
        print("que eres un Perro")
````

> El verdadero constructor no es `__init__` tenerlo en cuenta

#### La clase Object

Cuando defines una clase esta se hereda de una clase común llamada 'Object'

````python
class Gato:
    def ...
    def __str__(self):
        return self.nombre
    
#El str te mostraba el lugar en la memoria donde esta almacenado
En este caso lo seteamos por el nombre
    
#Existe una segunda forma para crear clases
class Pato(object): #Basicamente hereda de 'object'
	def ...
    
# dict
pato = Pato("Lucas")
print(pato.__dict__) #Me muestra los atributos
````



### Funciones

````python
def saludar():
	print('BUenas dias')
    
def saludar(nombre):
	print('BUenas dias' + nombre)   
#No admiten Sobrecarga admitida, se toma la ultima definicion

#USO del Return
def sumar(num1, num2):
    suma = num1 + num2
    return suma
print("Operacion 4 + 5 = ",sumar(4,5))
-------
#Parametros Opcionales con valores por defecto
def crear(nom,apell='Ninguno',edad=10):
    return nom + apell + str(edad)
crear("Codi","Facilito ")
"CodiFacilito 10"
#El orden es de derecha a izquierda

#OJO : Se puede especificar que paramatro llevara valor
crear(edad=7,nombre="Codi")

------------------------------------
#Paso por valor , Paso por referencia
colores = ["rojo", "verde", "azul"]
def incluir_color(colores,color):
    colores.append(color)
    
color = "negro"
incluir_color(colores,color)
colores
#Se modifico la lista
````

> TIP : Como en la guía de C# los objetos y los Arrays siempre se pasan por referencia OJO

#### Cantidad indefinida de Parámetros

````python
#El asterisco agrupara todos los parametros en una tupla
def suma(*args)
	print(args)
	total = 0
	for valor in args:
		total+=valor
	return total
	
resultado = suma(10,20,30,40)
print(resultado)

# El uso de los asteristicos no me restringe tener solo un parametro, solamente debe cumplir que este al final
def suma(param_req,*args):
    return ...
resultado = suma("algo",10,20,30)

#Como Convencion en Python usar la palabra (args)

# Convencion (**kwargs) podemos pasar un diccionario
def users(**kwargs):
    print(kwargs)
users(cod=True,facilito=False)
# {'cod': True, 'facilito':False}

# TAmbien podemos combinar el (*) con el (**)
````

#### Como terminar una función

Obviamente la identacion es las llaves ,pero veamos algunas excepciones

````python
def f():
    print('hola')

res = f() # Por defecto si la funcion 'f' no tiene return,se le asigna 'None'
print(res)

#Todo lo que va despues del return no se mira
````

##### Alcance de las variables

````python
animal = "Leon" #Variable global

def f():
	print(animal) #valor de halla arriba
	animal = 'Ballena' #Variable loval
    print(animal)
    
-----
#Si quiero modificar el dato usamos la palabra 'global'
animal = "Leon"

def f():
    global animal
	animal = 'Ballena' 
    print(animal)

print(animal)
def()
````

##### Función Lambda

````python
# lambda losParametros : 'valor del return'
resultado = lambda numero : numero + 30
resultado(10)

resultado2 = lambda nume1, num2 : num1 + num2
resultado2(10,20)
````

#### Funciones Anidadas

````python
def comenzar(lista):
    
    def reproducir():
        """
        Si quiero modificar lista uso la palabra clave nonlocal
        nonlocal lista
        lista = [1,2,3]
        
        """
        for val in lista:
            print(val)
    print(lista)        
    reproducir() #NO olvidar esta linea si no no se muestra nada        
            
lista = ['a','b','ooo']
comenzar(lista)
````

#### Closures

Cuando una función retorne otra función

````python
def f(mesaje):
    mesaje = mensaje.title() #Imprime variable local
    def m()
    	print(mesaje)
    return m

#Como aprendimos anteriormente podemos guardar una funcion en una variable
nf = f("Hola")
nf()
````

#### Decoradores

Sirve para reutilizar código

````python
#a, b, c
#a(b) -> c

def decorador(f):
    def nuevaf():
        print("Podemos agragar codigo antes")
    	f()
        print("Podemos agragar codigo despues")
	return nuevaf

@decorador #Ojo aca el nombre es igual a la otra funcion
def funcion_a_decorar():
    print("Esta es una funcion a decorar")
    
funcion_a_decorar()

#Vamos por partes Gianpier me mareo , okey yo tambien estoy mareado
1. Se ejecuta funcion_a_decorar() es un funcion que esta decorada por otra funcion pero esta es la principal
2. Entonces como sera decorada, se ejecutara el decorador y se pasara como argumeto la funcion. Asi que basicamente miralo como que solo se ejecuta el decorador y que el parametro f es la funcion a decorar
````

### Generadores

````python
def tabla(numero,maximo=10):
    for posicion in range(1,maximo+1)
    	yield numero * posicion
# yield seria como un return pero sin terminar la funcion, es como retornar una lista de elementos
"""
Equivale a:
def tabla(numero,maximo=10):
	res = []
    for posicion in range(1,maximo+1)
    	res = res.append(numero * posicion)
    return res	
"""
 
    
for resultado in tabla(9):
    print(resultado)
    
---
#Osea como retornan una lista
def gen_basico():
    yield "uno"   
    yield "dos"
    yield "tres"
   
for valor in gen_basico():
    print(valor)  # uno, dos, tres
    
````

Bonus

````python
Podemos trabajar con la documentación a través de su atributo __doc__

print(mi_funcion.__doc__)
````

