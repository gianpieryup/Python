# -*- coding: utf-8 -*-
import csv
import informe_funciones

def costo_camion(nombre_archivo):
    informe = informe_funciones.leer_camion(nombre_archivo)

    costo_total=0
    for d in informe:
        cajones = d['cajones']
        precio = d['precio']
        costo_total += cajones * precio

    return costo_total

if __name__=="__main__":
    costo = costo_camion('../Data/fecha_camion.csv')
