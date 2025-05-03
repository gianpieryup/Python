# Terminated due to timeout

def dis_rara(p1, p2):
    x = abs(p1[0] - p2[0])
    y = abs(p1[1] - p2[1])
    
    return min(x,y)


string = input() 
string_splt = string.strip().split(" ")
N = int(string_splt[0])
K = int(string_splt[1])


lista_puntos = []
for s in range(N):
    string = input() 
    string_splt = string.strip().split(" ")
    x = int(string_splt[0])
    y = int(string_splt[1])
    lista_puntos.append((x,y))

    
from itertools import combinations
        
lista_distancias = []

for x,y in combinations(range(N),2):
    d = dis_rara(lista_puntos[x],lista_puntos[y])
    lista_distancias.append(d)

lista_distancias.sort()
print(lista_distancias[K-1])

