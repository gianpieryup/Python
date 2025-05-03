import random

# Ejercicio 5.5: Calcular pi
# Con random.random() generamos valores aleatorios entre 0 y 1 con una "distribución uniforme"
def generar_punto():
    x = random.random()
    y = random.random()      
    
    return x,y

N = 100000  # puntos con una distribución uniforme en el cuadrado unitario
M = 0 # puntos_dentro_circulo
for i in range(N):
    x,y = generar_punto()
    
    if x**2 + y**2 < 1:
        M += 1

# M = pi/4 * N 
pi = 4*M/N


# Ejercicio 5.6: Gaussiana
# Distribucion normal o Gaussiana.
# La distribución normal tiene dos parámetros, denominados 
# media : letras griegas mu
# desvío estándar : letras griegas sigma
# random.normalvariate(mu,sigma)

for i in range(6):
    print(f'{random.normalvariate(0,1):.2f}', end=', ')
