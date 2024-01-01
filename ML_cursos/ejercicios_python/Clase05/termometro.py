import random
import numpy as np

def normalvariate():
    mu=0
    sigma=0.2
    variacion = random.normalvariate(mu ,sigma)
    return 37.5 + variacion

def medir_temp(n):    
    res = []
    for i in range(n):
        valor = normalvariate()
        res.append(valor)
        # print(f'{valor:.2f}', end=', ')
    
    # Ejercicio 5.8: Guardar temperaturas
    np.save('../Data/temperaturas', res)
    return res

def resumen_temp(n):
    res = medir_temp(n)
    maximo = max(res)
    minimo = min(res)
    promedio = sum(res)/n
    
    res.sort()
    if n%2==0: #PAR
        media = res[n//2] + res[(n//2) + 1]
    else:
        media = res[(n - 1)//2]
    
    return (maximo,minimo,promedio,media)

if __name__=="__main__":
    tem = resumen_temp(999)

'''
type(4/2)
<class 'float'>
x=4/2
lista[x] : list indices must be integers or slices, not float
'''
