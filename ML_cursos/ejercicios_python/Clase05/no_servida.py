# -*- coding: utf-8 -*-
import random

def tirar():
    tirada=[]
    for i in range(5):
        tirada.append(random.randint(1,6)) 
    return tirada

def es_generala(tirada):
    
    e = tirada[0]
    for t in tirada:
        if e!= t:
            return False
    return True

def tirar_g(cant):
    tirada=[]
    for i in range(cant):
        tirada.append(random.randint(1,cant+1)) 
    return tirada

def estadistica(tirada): 
    dic={}
    for num in tirada:
        if num in dic:
            dic[num]+= 1
        else:
            dic[num] = 1
    mayor = max([(dic[x],x) for x in dic])
    valor_max = mayor[1]
    repeticiones = mayor[0]
    return valor_max, repeticiones


def no_nesecariamente_servida():
    tirada = tirar()
    print("TIRADA 1:",tirada)
    num_mas_repetido , cant_repeticiones = estadistica(tirada)
    
    repet_pendientes = 5 - cant_repeticiones
    # print("Se repitieron:",cant_repeticiones,"veces el",num_mas_repetido)
    if repet_pendientes == 0 : #
        return True
    

    tirada = tirar_g(repet_pendientes) #
    print("TIRADA 2:",tirada)
    
    rep_num_seg_iter = tirada.count(num_mas_repetido)
    repet_pendientes -= rep_num_seg_iter
    if repet_pendientes <= 0 : #
        return True
    
    
    tirada = tirar_g(repet_pendientes) #
    print("TIRADA 3:",tirada)
    
    rep_num_ter_iter = tirada.count(num_mas_repetido)
    repet_pendientes -= rep_num_ter_iter
    return repet_pendientes <= 0
    tirada = tirar()
    print("TIRADA 1:",tirada)
    num_mas_repetido , cant_repeticiones = estadistica(tirada)
    
    repet_pendientes = 5 - cant_repeticiones
    print("Se repitieron:",cant_repeticiones,"veces el",num_mas_repetido)
    if repet_pendientes == 0 :
        return True
    

    tirada = tirar()
    print("TIRADA 2:",tirada)
    
    rep_num_seg_iter = tirada.count(num_mas_repetido)
    repet_pendientes -= rep_num_seg_iter
    if repet_pendientes <= 0 :
        return True
    
    
    tirada = tirar()
    print("TIRADA 3:",tirada)
    rep_num_seg_iter = tirada.count(num_mas_repetido)
    repet_pendientes -= rep_num_seg_iter
    
    return repet_pendientes <= 0
