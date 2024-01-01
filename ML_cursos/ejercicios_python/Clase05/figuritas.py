# -*- coding: utf-8 -*-
import random
import numpy as np

# Ejercicio 5.10: Crear
def crear_album(figus_total):
    return np.zeros(figus_total)

# Ejercicio 5.11: Incompleto
def album_incompleto(A):
    if 0 in A:
        return True
    return False

# Ejercicio 5.12: Comprar
def comprar_figu(figus_total):
    return random.randint(0,figus_total-1)

# Ejercicio 5.13: Cantidad de compras
def cuantas_figus(figus_total):
    intentos = 0
    album = crear_album(figus_total)
    while album_incompleto(album):
        figurita = comprar_figu(figus_total)
        album[figurita] += 1
        intentos += 1
    return  intentos

# Ejercicio 5.15:
def experimento_figus(n_repeticiones, figus_total):
    resultados =[]
    for i in range(n_repeticiones):
        c = cuantas_figus(figus_total)
        resultados.append(c)
    
    promedio = np.mean(resultados) 
    return promedio


# --------------  Ejercicios con paquetes  -------------------
# Ejercicio 5.17:
def comprar_paquete(figus_total, figus_paquete):
    album = np.arange(figus_total)
    return random.choices(album,k=figus_paquete)

# Ejercicio 5.18:
def cuantos_paquetes(figus_total, figus_paquete):
    intentos = 0
    album = crear_album(figus_total)
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        for f in paquete:
            album[f] += 1
        
        intentos += 1
    return  intentos


# Ejercicio 5.23
def comprar_paquete_sin_reposicion(figus_total, figus_paquete):
    album = np.arange(figus_total)
    return random.sample(list(album),k=figus_paquete)

def cuantos_paquetes_sr(figus_total, figus_paquete):
    intentos = 0
    album = crear_album(figus_total)
    while album_incompleto(album):
        paquete = comprar_paquete_sin_reposicion(figus_total, figus_paquete)
        for f in paquete:
            album[f] += 1
        
        intentos += 1
    return  intentos


# -------------- Graficar el llenado del álbum  -------------
def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas

if __name__=="__main__":
    
    # Ejercicio 5.14:
    n_repeticiones = 1000
    figus_total = 6
    resultados =[]
    for i in range(n_repeticiones):
        c = cuantas_figus(figus_total)
        resultados.append(c)
    
    promedio = np.mean(resultados)
    
    exp = experimento_figus(n_repeticiones, figus_total)
    
    
    # Ejercicio 5.16:
    figus_total = np.arange(670)
    r = random.choices(figus_total,k=5)
    
    # Ejercicio 5.19:
    n_repeticiones = 100 # Con 1000 dio 957.621
    figus_total = 670
    figus_paquete = 5
    resultados =[]
    
    for i in range(n_repeticiones):
        c = cuantos_paquetes(figus_total, figus_paquete)
        resultados.append(c)
    
    promedio = np.mean(resultados) 

    
    # Graficar el llenado del álbum
    # figus_total = 670
    # figus_paquete = 5
    
    import matplotlib.pyplot as plt
    plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
    plt.xlabel("Cantidad de paquetes comprados.")
    plt.ylabel("Cantidad de figuritas pegadas.")
    plt.title("La curva de llenado se desacelera al final")
    plt.show()


    # -----------  Ejercicios un toque más estadísticos  ------------
    # Ejercicio 5.20:
    # Trabajar con vectores tiene ventajas
    n_paquetes_hasta_llenar=np.array(resultados)
    
    # Para un experimento, resultados = espacio muestral
    casos_favor = (n_paquetes_hasta_llenar <= 850).sum()
    probabilidad  = casos_favor / len(resultados) # APROX=0.27
    print("Prob llenar CON repeticion", probabilidad)
    
    # Ejercicio 5.21: Plotear el histograma
    import matplotlib.pyplot as plt
    plt.hist(resultados,bins=25)
    plt.show()
    
    # Ejercicio 5.22:
    # Viendo el grafico anterior me iria por 1200
    casos_favor = (n_paquetes_hasta_llenar <= 1200).sum()
    probabilidad  = casos_favor / len(resultados) # APROX=0.9


    # Ejercicio 5.24: Cooperar vs competir
    n_repeticiones = 100 
    # figus_total = 670
    # figus_paquete = 5
    resultados =[]
    
    for i in range(n_repeticiones):
        c = cuantos_paquetes_sr(figus_total, figus_paquete)
        resultados.append(c)
        
    n_paquetes_hasta_llenar=np.array(resultados)
    casos_favor = (n_paquetes_hasta_llenar <= 850).sum()
    probabilidad  = casos_favor / len(resultados)    # 0.32
    print("Prob llenar SIN repeticion", probabilidad)
    ''' COCLUSION: Si no hay figuritas repetidas en un paquete
        La probabilidad deberia aumentar que teniendo repetidas en un paquete
        Tambien es lo logico
    '''
