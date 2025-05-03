def busqueda_lineal(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
    return pos

''' Complejidad = n
El algoritmo de búsqueda lineal tiene un comportamiento proporcional a la longitud 
de la lista involucrada, o que es un algoritmo lineal.
'''

# Ejercicio 4.3: Búsquedas de un elemento
def buscar_u_elemento(lista,e):
    res = busqueda_lineal(lista[::-1],e)
    if res != -1:
        res = len(lista) - res -1
    return res

def buscar_n_elemento(lista,e):
    cant = 0
    for i, z in enumerate(lista): # recorremos la lista
        if z == e:   # si encontramos a e
            cant += 1
    return cant

# Ejercicio 4.4: Búsqueda de máximo y mínimo
def maximo(lista):
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía y de números positivos.
    '''
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    m = lista[0]
    for e in lista: # Recorro la lista y voy guardando el mayor
        if e > m:
            m = e
    return m