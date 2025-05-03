# -*- coding: utf-8 -*-
import csv

def parse_csv(nombre_archivo, select = None, types = None, has_headers = True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    with open(nombre_archivo) as f:
        filas = csv.reader(f)
        
        if has_headers: # La primera linea(del CSV) sera interpretado como parametro
            # Lee los encabezados del archivo
            encabezados = next(filas)
 
            # Si se indicó un selector de columnas,
            #    buscar los índices de las columnas especificadas.
            # Y en ese caso achicar el conjunto de encabezados para diccionarios
    
        if select:
            if has_headers:
                indices = [encabezados.index(nombre_columna) for nombre_columna in select]
                
            # No tenemos nombre
                
            encabezados = select
        else:
            indices = []
        
       
        
        registros = []
        for fila in filas:
            if not fila:    # Saltear filas vacías
                continue
            # Filtrar la fila si se especificaron columnas
            #if has_headers:
            if indices:
                fila = [fila[index] for index in indices]

            # Ejercicio 6.8 : Si se indicó los tipos de datos
            if types:
                fila = [func(val) for func, val in zip(types, fila) ]
            
            if has_headers:    
                # Armar el diccionario
                registro = dict(zip(encabezados, fila))        
                registros.append(registro)
            else:
                # Armar tupla
                registro = tuple(fila)        
                registros.append(registro)

    return registros

