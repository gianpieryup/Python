# -*- coding: utf-8 -*-
import csv
def leer_arboles(nombre_archivo):
    f = open(nombre_archivo, 'rt', encoding="utf8")
    rows = csv.reader(f)
    headers = next(rows)
    
    select = headers # Puedes usarlo como SELECT de SQL
    indices = [headers.index(ncolumna) for ncolumna in select]
    
    arboles = [{ ncolumna: row[index] for ncolumna, index in zip(select, indices)} for row in rows]
    return arboles


import os
import matplotlib.pyplot as plt
import numpy as np

'''
Te recomendamos generarlas en una ventana nueva. 
Luego, con plt.clf() podés borrar la figura actual y con 
plt.figure() generás una nueva figura por si querés dejar varias abiertas a la vez.
'''

#Ejercicio 5.26: Scatterplot (diámetro vs alto) de Jacarandás
def scatter_hd(lista_de_pares):
    
    # Con NUMPY puedo escoger una columna 
    # print(arr[:,3])
    l = np.array(lista_de_pares)
    d = l[:,1] 
    h = l[:,0]
    # d = [ t[1] for t in lista_de_pares]
    # h = [ t[0] for t in lista_de_pares]
    plt.figure()
    plt.scatter(d,h)
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.title("Relación diámetro-alto para Jacarandás")




# Ejercicio 5.27
def medidas_de_especies(especies,arboleda):
    diccionario = { esp: [(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com']==esp] for esp in especies }    
    return diccionario

def plot_especies(arboleda):
    especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    medidas = medidas_de_especies(especies, arboleda)
    plt.figure()
    for m in medidas:
        l = medidas[m]
        d = [ t[1] for t in l]
        h = [ t[0] for t in l]
        plt.scatter(d,h,label=m)
    
    plt.xlim(0,30) 
    plt.ylim(0,100) 
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.legend()

if __name__=="__main__":
    
    # Ejercicio 5.25: Histograma de altos de Jacarandás
    nombre_archivo = os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
    arboleda = leer_arboles(nombre_archivo)
    altos = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com']=="Jacarandá"]
    plt.figure()
    plt.hist(altos,bins=25)
        
    # Ejercicio 5.26: Scatterplot (diámetro vs alto) de Jacarandás
    t_jacarandas = [(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com']=="Jacarandá"]
    scatter_hd(t_jacarandas)
    
    # Ejercicio 5.27
    plot_especies(arboleda)
    