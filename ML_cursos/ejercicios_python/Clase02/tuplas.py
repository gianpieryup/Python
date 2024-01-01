# Empaquetar tuplas
s = ('Manzanas', 100, 490.1) 
# Desempaquetar tuplas
fruta, cajones, precio = s      # nombre, cajones = s     # ERROR
print('Costo:', cajones * precio)

'''
Tuplas vs. Listas
Las tuplas parecieran ser listas de solo-lectura. 
(Aunque no podés cambiar al tupla, sí podés reemplazar la tupla por una nueva.)
Sin embargo, las tuplas suelen usarse para un solo ítem que consiste 
de múltiples partes mientras que las listas suelen usarse para una 
colección de diferentes elementos, típicamente del mismo tipo.

¿Por qué diccionarios?
Los diccionarios son útiles cuando hay muchos valores diferentes y esos valores 
pueden ser modificados o manipulados. Dado que el acceso a los elementos 
se hace por clave, no es necesario recordar una posición para cierto dato, 
lo que muchas veces cumple un objetivo fundamental: hacer que el código sea más legible

Podés verificar si una clave existe:
if key in d:
'''
fila=['Lima', '100', '32.2']
d = {
        'nombre' : fila[0],
        'cajones' : int(fila[1]),
        'precio'  : float(fila[2])
    }

# Agregar elementos
d['fecha'] = (14, 8, 2020)
d['cuenta'] = 12345

for k in d:
    print(k, '=', d[k])


"FORMA ELEGANTE DE TRABAJAR CON DICCIONARIOS"
items = d.items()
print(items)

for k, v in d.items():
    print(k, '=', v)

'''
# Se puede obtener sus claves con list(d) o con el  método d.keys():

# Podés verificar si una clave existe:
# if key in d:

    
add('Banana')        # Agregar un elemento
remove('Limon')    # Eliminar un elemento
s1 | s2                 # Unión de conjuntos s1 y s2
s1 & s2                 # Intersección de conjuntos
s1 - s2                 # Diferencia de conjuntos
'''
