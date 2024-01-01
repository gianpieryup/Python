# -*- coding: utf-8 -*-
import os
def archivos_png(directorio):
    archivos_png = []
    for nombre_directorio, dirs, ficheros in os.walk(directorio):
        #print(nombre_directorio)
        for nombre_fichero in ficheros:
            if nombre_fichero.endswith('.png'):
                #print(nombre_fichero)
                archivos_png.append(nombre_fichero)
    return archivos_png



if __name__ == '__main__':
     import sys
     # archivos_png('../Data/ordenar') para la consola interativa
     
     # Consola Formal
     # python3 listar_imgs.py ../Data/ordenar
     # sys.argv = ['listar_imgs.py','../Data/ordenar']
     ruta = sys.argv[-1]
     print(archivos_png(ruta))
     