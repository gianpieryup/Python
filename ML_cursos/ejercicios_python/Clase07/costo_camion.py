# -*- coding: utf-8 -*-
import informe_final

def costo_camion(nombre_archivo):
    informe = informe_final.leer_camion(nombre_archivo)

    costo_total=0
    for d in informe:
        cajones = d['cajones']
        precio = d['precio']
        costo_total += cajones * precio

    return costo_total

if __name__=="__main__":
    costo = costo_camion('../Data/fecha_camion.csv')
    print(costo)
