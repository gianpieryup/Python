# -*- coding: utf-8 -*-
def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    return pos, medio

'''
    Si:  len(lista)= 2^k. 
    aproximadamente log2(len(lista)) comparaciones.
'''

def donde_insertar(lista, x):
    '''
    reciba una lista ordenada y un elemento
    '''
    pos,medio = busqueda_binaria(lista, x)
    if pos == -1: # No lo encontro
        return medio # donde podria insertarlo
    else: # Si lo encontro
        return pos

# Ejercicio 6.15: Insertar un elemento en una lista
def insertar(lista, x):
    #lista = lista[:pos] + x + lista[pos:] # Estoy redefiniendo(esto no persiste en listas)
    pos,medio = busqueda_binaria(lista, x)
    if pos == -1: # No lo encontro
        lista.insert(medio, x)
        return medio
    else: # Si lo encontro
        return pos
    
if __name__=="__main__":
    lista = [0,2,4,6]
    d1 = donde_insertar(lista, 3)
    l2 = insertar(lista, 3)
