# -*- coding: utf-8 -*-
# ticker.py

from vigilante import vigilar
import csv

def elegir_columnas(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def cambiar_tipo(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def hace_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    rows = cambiar_tipo(rows, [str, float, int])
    rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    return rows


def filtrar_datos(rows, nombres):
    # for row in rows:
    #     if row['nombre'] in nombres:
    #         yield row
    filas = (fila for fila in rows if fila['nombre'] in nombres)
    return filas

def ticker(camion_file, log_file, fmt):
    return True
            
# productor → procesamiento → procesamiento → consumidor
if __name__ == '__main__':
    lines = vigilar('../Data/mercadolog.csv')
    rows = parsear_datos(lines)
    for row in rows:
        print(row)
