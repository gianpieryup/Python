# -*- coding: utf-8 -*-
votos = int(input())
dic={}
for i in range(votos):
    candidato = input()
    if candidato in dic:
        dic[candidato]+= 1
    else:
        dic[candidato] = 1

ganador="Anonimus"
cant = 0
for k,c in dic.items():
    if c > cant:
        cant=c
        ganador=k
        
print(ganador)