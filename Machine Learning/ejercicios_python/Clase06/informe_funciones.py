# -*- coding: utf-8 -*-
import fileparse as fp
import csv

def leer_camion(nombre_archivo):
    '''
    Computa el precio total del camion (cajones * precio) de un archivo
    '''
    # has_headers = True
    camion = fp.parse_csv(nombre_archivo, select = ['nombre','cajones','precio'], types = [str,int,float])
    return camion

def leer_precios(nombre_archivo):

    lista_precios = fp.parse_csv(nombre_archivo,types = [str,float],has_headers=False)
    # Como son tuplas se nesecita esto
    precios = dict(lista_precios)
    return precios

def hacer_informe(camion, precios):
    lista = []
    for lote in camion:
        precio_venta = precios[lote['nombre']]
        cambio = precio_venta - lote['precio']
        t = (lote['nombre'], lote['cajones'], precio_venta, cambio)
        lista.append(t)
    return lista

def imprimir_informe(informe):
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    print('%10s %10s %10s %10s'  % headers)
    print(('-' * 10 + ' ') * len(headers))
    for row in informe:
        print('%10s %10d %10.2f %10.2f' % row)

def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    '''
    Basicamente esta funcion emula una secuencia de funciones (script)
    '''
    camion = leer_camion(nombre_archivo_camion)
    precios = leer_precios(nombre_archivo_precios)
    informe = hacer_informe(camion, precios)
    imprimir_informe(informe)

if __name__=="__main__":
    informe_camion('../Data/camion.csv','../Data/precios.csv')
   
