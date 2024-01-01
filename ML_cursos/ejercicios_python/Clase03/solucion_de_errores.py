#Ejercicios de errores en el código

#%%
#   Ejercicio 3.1. Función tiene_a()
#   Comentario: 
#   El error era de SEMANTICO, y estaba ubicado en los returns
#   Basicamente la funcion determinaba si la primera letra era 'a' o no
#   No revisando las demas leras

#   Lo corregí cambiando la ubicacion del return False

#   A continuación va el código corregido
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    
    return False

#%%
#Ejercicio 3.2. Función tiene_a(), nuevamente
#Comentario: El error era de tipo SINTACTICO

'''
def tiene_a(expresion) -> Se olvido el (:)
while i<n -> Se olvido el (:)
if expresion[i] = 'a' -> es (==)
return Falso -> es False
'''

#%%
#   Ejercicio 3.3. Función tiene_uno()
#   Comentario: El error era en TIEMPO DE EJECUCION y estaba ubicado en 
#   n = len(expresion)
#   No valida si la expresion es un int

#%%
#   Ejercicio 3.4: Alcances
#   La siguiente suma no da lo que debería:
'''
def suma(a,b):
    c = a + b   # Variable Local 'c' indefinida
'''

#%%
#   Ejercicio 3.5: Pisando memoria
''' RESPUESTA
    La razon es que se guarda 'registro' en cada posicion de la lista 'camion'
    por lo que todos los elementos de la lista seran iguales
    CORREGIREMOS ESTO CON un nuevo 'registro' por cada linea 
'''

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro={} # Aqui lo pongo
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion



if __name__=="__main__":
    #tiene_a('UNSAM 2020')
    #tiene_a('abracadabra')
    #tiene_a('La novela 1984 de George Orwell')

    camion = leer_camion('../Data/camion.csv')
    pprint(camion)