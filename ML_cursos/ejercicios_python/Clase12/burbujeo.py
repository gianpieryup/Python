# -*- coding: utf-8 -*-
def ord_burbujeo(lista):
    for i in range(1,len(lista)):
        for j in range(0,len(lista)-i):
            if(lista[j+1] < lista[j]):
                aux=lista[j];
                lista[j]=lista[j+1];
                lista[j+1]=aux;
    return lista

# Pendiente lo de recursivo
