# -*- coding: utf-8 -*-
import csv

# Lancar y Atrapar excepciones son 2 cosas distintas

def parse_csv(iterable, select = None, types = None, has_headers = True, silence_errors = False):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    # Ejercicio 7.6: De archivos a "objetos cual archivos"
    filas = csv.reader(iterable)
        
            
    if has_headers: # La primera linea(del CSV) sera interpretado como parametro
        # Lee los encabezados del archivo
        encabezados = next(filas)
 
        # Si se indicó un selector de columnas,
        #    buscar los índices de las columnas especificadas.
        # Y en ese caso achicar el conjunto de encabezados para diccionarios
    
    if select:
        try: 
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]            
        except:  # Ejercicio 7.1: Lancemos excepciones
            raise RuntimeError("Para seleccionar, necesito encabezados.")
                
        encabezados = select
    else:
        indices = []
        
         
    registros = []
    for i,fila in enumerate(filas,1): # Para que empieze a enumerar en 1
        if not fila:    # Saltear filas vacías
            continue
        # Filtrar la fila si se especificaron columnas
        #if has_headers:
        if indices:
            fila = [fila[index] for index in indices]

        if types:
            try: # Ejercicio 7.2: Atrapemos excepciones
                fila = [func(val) for func, val in zip(types, fila) ]
            except ValueError as e:
                if not silence_errors:
                    print(f'Fila {i}: No pude convertir {fila}')
                    print(f'Fila {i}: Motivo: {e}')

        if has_headers:    
            # Armar el diccionario
            registro = dict(zip(encabezados, fila))        
            registros.append(registro)
        else:
            # Armar tupla
            registro = tuple(fila)        
            registros.append(registro)

    return registros