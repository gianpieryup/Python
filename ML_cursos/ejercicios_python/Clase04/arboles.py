# Ejercicio 4.15: Lectura de todos los Ã¡rboles
import csv
import sys

def leer_arboles(nombre_archivo):
    f = open(nombre_archivo, 'rt', encoding="utf8")
    rows = csv.reader(f)
    headers = next(rows)
    
    select = headers # Puedes usarlo como SELECT de SQL
    indices = [headers.index(ncolumna) for ncolumna in select]
    
    arboles = [{ ncolumna: row[index] for ncolumna, index in zip(select, indices)} for row in rows]
    return arboles

arboleda = leer_arboles("../Data/arbolado-en-espacios-verdes.csv")

# Ejercicio 4.16: Lista de altos de JacarandÃ¡
H=[float(arbol['altura_tot']) for arbol in arboleda]

# OJO: Jacarandá con tilde en la (a)
h_jacarandas = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com']=="Jacarandá"]


# Ejercicio 4.17: Lista de altos y diámetros de Jacarandá
t_jacarandas = [(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com']=="Jacarandá"]


# Ejercicio 4.18: Diccionario con medidas
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']

def medidas_de_especies(especies,arboleda):
    '''
    d ={}
    # Tuplas de altura y diametro de una determinda especie
    for esp in especies:
        t_arboles = [(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com']==esp]
        d[esp] = t_arboles
    return d    
    '''  
    
    # BONUS: Echo por comprensión de diccionarios
    diccionario = { esp: [(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com']==esp] for esp in especies }    
    return diccionario
    
if __name__=="__main__":
    res = medidas_de_especies(especies,arboleda)
