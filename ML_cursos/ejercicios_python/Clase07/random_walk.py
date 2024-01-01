# -*- coding: utf-8 -*-
# Ejercicio 7.11: Subplots fuera de una grilla
import matplotlib.pyplot as plt
import numpy as np

def randomwalk(largo):
    pasos=np.random.randint(-1,2,largo)
    return pasos.cumsum() # -1,-1,0,1,2,3,2,1,2,3,4,5,4,3,2,1,0,-1,-2



if __name__=="__main__":
    N = 100000
    fig = plt.figure()
    plt.subplot(2, 1, 1) # define la figura de arriba
    
    res = []
    for x in range(12):
        rd = randomwalk(N)
        res.append(rd)
        plt.plot(randomwalk(N))
    plt.title("12 caminos al azar")
    plt.xticks([])
    
    
    res_max_abs = [max([abs(num) for num in e])for e in res]
    ind_max = res_max_abs.index(max(res_max_abs))
    ind_min = res_max_abs.index(min(res_max_abs))
 
    
    plt.subplot(2, 2, 3) # define la primera de abajo, que sería la tercera si fuera una grilla regular de 2x2
    plt.plot(res[ind_max])
    plt.xticks([])
    plt.title("La caminata que mas se aleja")
    
    plt.subplot(2, 2, 4) # define la segunda de abajo, que sería la cuarta figura si fuera una grilla regular de 2x2
    plt.plot(res[ind_min])
    plt.xticks([])
    plt.title("La caminata que menos se aleja")
    plt.show()
        