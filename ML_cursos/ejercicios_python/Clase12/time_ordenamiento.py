# -*- coding: utf-8 -*-
import random

# Ordenamiento por selección
def ord_seleccion(lista):
    n = len(lista) - 1
    
    while n > 0:
        # posición del mayor valor del segmento
        p = buscar_max(lista, 0, n)
        lista[p], lista[n] = lista[n], lista[p]
        #print("DEBUG: ", p, n, lista)

        # reducir el segmento en 1
        n = n - 1
    
    return lista

def buscar_max(lista, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""

    pos_max = a
    for i in range(a + 1, b + 1):
        if lista[i] > lista[pos_max]:
            pos_max = i
    return pos_max


# Ordenamiento por inserción
def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    
    for i in range(len(lista) - 1):
        if lista[i + 1] < lista[i]:
            reubicar(lista, i + 1)
        #print("DEBUG: ", lista)
    
    return lista

def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""
        
    v = lista[p]

    j = p
    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1

    lista[j] = v


# Divide y venceras
# Adiferencia de todos los demas su creciemiento es logaritmico
# Mucho menos comparaciones que los exponenciales
def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
       
    # cantidad de comparaciones
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq = merge_sort(lista[:medio])
        der = merge_sort(lista[medio:])
        lista_nueva = merge(izq, der)
    return lista_nueva

def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []
    while(i < len(lista1) and j < len(lista2)):

        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado


# BURBUJEO
def ord_burbujeo(lista):
    esta_ordenado = True
    for i in range(1,len(lista)):
        for j in range(0,len(lista)-i):
            if(lista[j+1] < lista[j]):
                aux=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=aux
                esta_ordenado = False # no porque tube que cambiar uno en este recorrido
                
        if esta_ordenado:
            break # Salimos
        else:
            esta_ordenado = True
    
    return lista

# Ejercicio 12.5: comparar métodos gráficamente
def generar_lista(N):
    tirada=[]
    for i in range(N):
        tirada.append(random.randint(1,1000)) 
    return tirada

# Ejercicio 12.8:
def generar_listas(Nmax):
    listas = []
    for N in range(Nmax):
        listas.append(generar_lista(N))
    return listas


import timeit as tt
import numpy as np
import matplotlib.pyplot as plt


def experimento_timeit(Nmax):
    
    listas = generar_listas(Nmax)
    
    tiempos_seleccion = []
    tiempos_insercion=[]
    tiempos_merge=[]
    tiempos_burbujeo=[]
    
    global lista
    
    for lista in listas:
        
        tiempo_seleccion = tt.timeit('ord_seleccion(lista.copy())', number = 100, globals = globals())
        tiempo_insercion = tt.timeit('ord_insercion(lista.copy())', number = 100, globals = globals())
        tiempo_merge = tt.timeit('merge_sort(lista.copy())', number = 100, globals = globals())
        tiempo_burbujeo = tt.timeit('ord_burbujeo(lista.copy())', number = 100, globals = globals())
        
        # guardo el resultado
        tiempos_seleccion.append(tiempo_seleccion)
        tiempos_insercion.append(tiempo_insercion)
        tiempos_merge.append(tiempo_merge)
        tiempos_burbujeo.append(tiempo_burbujeo)
        
    # paso los tiempos a arrays
    tiempos_seleccion = np.array(tiempos_seleccion)
    tiempos_insercion = np.array(tiempos_insercion)
    tiempos_merge = np.array(tiempos_merge)
    tiempos_burbujeo = np.array(tiempos_burbujeo)
    

    ejex=np.arange(Nmax)
    plt.plot(ejex,tiempos_burbujeo,label = 'Burbuja')
    plt.plot(ejex,tiempos_insercion,label = 'Insercion')
    plt.plot(ejex,tiempos_seleccion,label = 'Seleccion')
    plt.plot(ejex,tiempos_merge,label = 'Merge')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    experimento_timeit(100)