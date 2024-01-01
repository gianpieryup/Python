# -*- coding: utf-8 -*-

# Ejercicio 11.9: Pascal     
def pascal(n,k):
   res = 1
   if k != 0 and k != n:
       res = pascal(n-1, k-1) + pascal(n-1, k) 
   return res

# Ejercicio 11.10: Combinatorios
def combinaciones(lista,k):
    if k==1:
        return lista
    
    resto = combinaciones(lista,k-1)
    res=[]
    for l in resto:
        for n in lista:
            res += [l+n]
                
    return res
        

if __name__ == '__main__':
    print("pascal(5, 2)=",pascal(5, 2))