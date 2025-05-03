# -*- coding: utf-8 -*-
import random

# Ordenamiento por selección
def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""

    # posición final del segmento a tratar
    n = len(lista) - 1

    # cantidad de operaciones
    cp = 0
    
    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p = buscar_max(lista, 0, n)
        cp += n
        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista[p], lista[n] = lista[n], lista[p]
        #print("DEBUG: ", p, n, lista)

        # reducir el segmento en 1
        n = n - 1
    
    return cp #lista

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

    # cantidad de operaciones
    cp = 0
    
    for i in range(len(lista) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista[i + 1] < lista[i]:
            cp +=  reubicar(lista, i + 1)
        #print("DEBUG: ", lista)
    
    return cp #lista

def reubicar(lista, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""
        
    v = lista[p]
    iteraciones=0
    
    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    while j > 0 and v < lista[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista[j] = lista[j - 1]
        j -= 1
        iteraciones += 1

    lista[j] = v
    return iteraciones


# Divide y venceras
# Adiferencia de todos los demas su creciemiento es logaritmico
# Mucho menos comparaciones que los exponenciales
def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
       
    # cantidad de comparaciones
    cp, ci, cd = 0, 0, 0
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq, ci = merge_sort(lista[:medio])
        der, cd = merge_sort(lista[medio:])
        lista_nueva, cp = merge(izq, der)
    return lista_nueva, cp + ci + cd

def merge(lista1, lista2):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []
    iteraciones = 0
    while(i < len(lista1) and j < len(lista2)):
        iteraciones += 1
        if (lista1[i] < lista2[j]):
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar lo que falta de una lista
    resultado += lista1[i:]
    resultado += lista2[j:]

    return resultado, iteraciones


# BURBUJEO
def ord_burbujeo(lista):
    # cantidad de operaciones
    cp = 0
    esta_ordenado = True
    for i in range(1,len(lista)):
        for j in range(0,len(lista)-i):
            if(lista[j+1] < lista[j]):
                aux=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=aux
                esta_ordenado = False # no porque tube que cambiar uno en este recorrido
                
        cp+= len(lista) - i # No cuenta todo el recorrido ya sabe que los ultimos estan ok
        if esta_ordenado:
            break # Salimos
        else:
            esta_ordenado = True
    
    return cp

# Ejercicio 12.5: comparar métodos gráficamente
def generar_lista(N):
    tirada=[]
    for i in range(N):
        tirada.append(random.randint(1,1000)) 
    return tirada


def experimento(N, k):
    burbujeo=0
    insercion=0
    seleccion=0
    merge=0
    
    for i in range(k):
        l1 = generar_lista(N)
        l2 = l1.copy() # pasa que la lista se ordena
        l3 = l1.copy() # pasa que la lista se ordena
        l4 = l1.copy() # pasa que la lista se ordena
        
        burbujeo += ord_burbujeo(l1)
        insercion += ord_insercion(l2)
        seleccion += ord_seleccion(l3)
        merge += merge_sort(l4)
    
    return burbujeo/k, insercion/k, seleccion/k, merge/k


import matplotlib.pyplot as plt
import numpy as np

def experimento_vectores(Nmax):
    comparaciones_seleccion=[]
    comparaciones_insercion=[]
    comparaciones_burbujeo=[]
    comparaciones_merge=[]
    
    for n in range(Nmax):
        l1 = generar_lista(n)
        l2 = l1.copy() # pasa que la lista se ordena
        l3 = l1.copy() # pasa que la lista se ordena
        l4 = l1.copy() # pasa que la lista se ordena
        
        comparaciones_burbujeo.append(ord_burbujeo(l1))
        comparaciones_insercion.append(ord_insercion(l2))
        comparaciones_seleccion.append(ord_seleccion(l3))
        comparaciones_merge.append(merge_sort(l4)[1])
    
    ejex=np.arange(Nmax)
    plt.plot(ejex,comparaciones_burbujeo,label = 'Burbuja')
    plt.plot(ejex,comparaciones_insercion,label = 'Insercion')
    plt.plot(ejex,comparaciones_seleccion,label = 'Seleccion')
    plt.plot(ejex,comparaciones_merge,label = 'Merge')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    experimento_vectores(500)