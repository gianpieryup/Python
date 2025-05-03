# -*- coding: utf-8 -*-
# Ejercicio 3.18: Lectura de los Ã¡rboles de un parque

import csv
def leer_parque(nombre_archivo,parque):
    f = open(nombre_archivo, 'rt', encoding="utf8")
    filas = csv.reader(f)
    encabezados = next(filas)
    #print(encabezados)
    arboles=[]
    
    for fila in filas:
        arbol = dict(zip(encabezados, fila))
        arbol['altura_tot']=float(arbol['altura_tot'])
        if arbol['espacio_ve']==parque:
            arboles.append(arbol)
    return arboles
    

def especies(lista_arboles):
    especies =set([])
    for arbol in lista_arboles:
        if arbol['nombre_com'] not in especies:
            especies.add(arbol['nombre_com'])
    return especies

from collections import Counter

def contar_ejemplares(lista_arboles):
    ejemplares = Counter()
    for a in lista_arboles:
        ejemplares[a['nombre_com']] += 1
    return ejemplares

def obtener_alturas(lista_arboles, especie):
    lista=[]
    for a in lista_arboles:
        if a['nombre_com'] == especie:
            lista.append(a['altura_tot'])
    return lista

def obtener_inclinaciones(lista_arboles, especie):
    lista=[]
    for a in lista_arboles:
        if a['nombre_com'] == especie:
            lista.append(float(a['inclinacio'])) # d creo
    return lista

def especimen_mas_inclinado(lista_arboles):
    esp = especies(lista_arboles)
    array=[]
    for e in esp:
        inclinaciones = obtener_inclinaciones(lista_arboles, e)
        tupla=(max(inclinaciones),e)        
        array.append(tupla)
        
    return max(array)


def especie_promedio_mas_inclinada(lista_arboles): 
    esp = especies(lista_arboles)
    array=[]
    for e in esp:
        inclinaciones = obtener_inclinaciones(lista_arboles, e)
        tupla=(sum(inclinaciones)/len(inclinaciones),e)        
        array.append(tupla)
    return max(array)    
        
'''
Preguntas extras: Â¿QuÃ© habrÃ­a que cambiar para obtener la especie con un ejemplar 
mÃ¡s inclinado de toda la ciudad y no solo de un parque? Â¿PodrÃ­as dar la latitud y 
longitud de ese ejemplar? Â¿Y dÃ³nde se encuentra (lat,lon) el ejemplar mÃ¡s alto? 
Â¿De quÃ© especie es?
'''
# Cambiaria la funcion: leer_parque() para que lea todos y no filtre por un parque en especifico
def leer_todos_parques(nombre_archivo):
    f = open(nombre_archivo, 'rt', encoding="utf8")
    filas = csv.reader(f)
    encabezados = next(filas)
    arboles=[]
    
    for fila in filas:
        arbol = dict(zip(encabezados, fila))
        arbol['altura_tot']=float(arbol['altura_tot'])
        arboles.append(arbol)
    return arboles

if __name__=="__main__":
    lista_arboles = leer_parque("../Data/arbolado-en-espacios-verdes.csv",'ANDES, LOS')
    es = especie_promedio_mas_inclinada(lista_arboles)
    print("especie_promedio_mas_inclinada",es)



    parques = ["GENERAL PAZ","ANDES, LOS","CENTENARIO"]
    for p in parques:
        lista_arboles = leer_parque("../Data/arbolado-en-espacios-verdes.csv",p)
        ejemplares = contar_ejemplares(lista_arboles).most_common(5)
        h = obtener_alturas(lista_arboles, 'Jacarandá')
        es = especimen_mas_inclinado(lista_arboles)
        print(p)
        print(ejemplares)
        print(f'MAX={max(h)} | promedio={sum(h)/len(h):.2f}')
        print("especimen_mas_inclinado:",es,"\n")


    lista_arboles = leer_todos_parques("../Data/arbolado-en-espacios-verdes.csv")
    arbol_mas_inclinado=lista_arboles[0]
    arbol_mas_alto=lista_arboles[0]
    for a in lista_arboles:
        if a['altura_tot'] > arbol_mas_alto['altura_tot']:
            arbol_mas_alto = a
        if a['inclinacio'] > arbol_mas_inclinado['inclinacio']:
            arbol_mas_inclinado = a
        
    print("El arbol mas inclinado: %s | Inclinacion: %s | Lat: %s | Long: %s "%(arbol_mas_inclinado['nombre_com'],arbol_mas_inclinado['inclinacio'],arbol_mas_inclinado['lat'],arbol_mas_inclinado['long']))       
    print("El arbol mas alto: %s | Altura: %d | Lat: %s | Long: %s "%(arbol_mas_alto['nombre_com'],arbol_mas_alto['altura_tot'],arbol_mas_alto['lat'],arbol_mas_alto['long']))  
