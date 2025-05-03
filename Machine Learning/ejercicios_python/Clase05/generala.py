# Ejercicio 5.1: Generala servida
import random
def tirar():
    tirada=[]
    for i in range(5):
        tirada.append(random.randint(1,6)) 
    return tirada

def tirar_g(cant):
    tirada=[]
    for i in range(cant):
        tirada.append(random.randint(1,cant+1)) 
    return tirada

# generala servida (cinco dados iguales)
def es_generala(tirada):
    
    e = tirada[0]
    for t in tirada:
        if e!= t:
            return False
    return True

'''
¿Por qué varían más los resultados obtenidos con N = 100000 que con N = 1000000?
Entre mas datos, mas se van hacia la normal

¿Cada cuántas tiradas en promedio podrías decir que sale una generala servida? 
A partir de 500000 estaria dano un intervalo de (720-820)

¿Cómo se puede calcular la probabilidad de forma exacta?
Casos a Favor/Casos Totales = 0.2
Casos a Favor = 6 : Cuando salen todos iguales a (1|2|..|6)
Casos Totales = 6*5 (dados distintos)
'''

# Ejercicio 5.2: Generala no necesariamente servida

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
    # print("TIRADA 1:",tirada)
    num_mas_repetido , cant_repeticiones = estadistica(tirada)
    
    repet_pendientes = 5 - cant_repeticiones
    # print("Se repitieron:",cant_repeticiones,"veces el",num_mas_repetido)
    if repet_pendientes == 0 : #
        return True
    

    tirada = tirar_g(repet_pendientes) #
    # print("TIRADA 2:",tirada)
    
    rep_num_seg_iter = tirada.count(num_mas_repetido)
    repet_pendientes -= rep_num_seg_iter
    if repet_pendientes <= 0 : #
        return True
    
    
    tirada = tirar_g(repet_pendientes) #
    # print("TIRADA 3:",tirada)
    
    rep_num_ter_iter = tirada.count(num_mas_repetido)
    repet_pendientes -= rep_num_ter_iter
    return repet_pendientes <= 0
  


def prob_generala(N):
    G=0
    for i in range(N):
        if no_nesecariamente_servida():
            G+=1
    prob = G/N
    print(f'Tiré {N} veces, de las cuales {G} saqué generala no nesecariamente servida.')
    print("Probabilidad=",prob)



if __name__=="__main__":
    # N = 100000
    # G = sum([es_generala(tirar()) for i in range(N)])
    # prob = G/N
    # print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
    # print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')          

    L = prob_generala(100000)
    
    # ALT = prob_generala_alt(100000)


# Semillas
# Generar números (pseudo-)aleatorios
# Osea que se repitan despues de ciertos intentos

# COMANDO
# random.seed(31415)
# La secuencia de números aleatorios que obtengamos será reproducible utilizando la misma semilla.

'''  VEREMOS que siempre devuelve el mismo resultado
random.seed(31415)
tirada=[]
for i in range(5):
    tirada.append(random.randint(1,6)) 
print(tirada)
'''


    
    
    
'''
#%%    
# Elecciones con reposición (**)
# Elije uno , pero ese uno se repone de la lista original (o sea que no se quita)
caras = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis']
print(random.choice(caras))

# Si queremos realizar múltiples elecciones aleatorias de la lista
print(random.choices(caras,k=5))

#%%
# Ejercicio 5.3: Cocumpleaños
Haciendo miles de experimentos numéricos, estimá la probabilidad de que en un grupo de 30 personas elegidas al azar, dos cumplan años el mismo día. 
Escribí un programita que permita calcular esa probabilidad asumiendo que el año tiene 365 días.

dias = list(range(1,366))
list_cumples = random.choices(dias,k=30)
# ISSUE PARA resolver as un experimento de acuerdo ese espacio muestral
# Calcula la probabilidad


#%%
# Elecciones sin reposición (**)
valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [(valor,palo) for valor in valores for palo in palos]

random.sample(naipes,k=3) # El sample es para que sea sin reposicion(**)   
# donde k < len(naipes)


'''