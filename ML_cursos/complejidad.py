
¿Por qué los tests l[i+1]==0 y l[i-1]==0 de la función propagar_al_vecino no causan un IndexError 
en los bordes de la lista?

Facil : Lo agrega como condicion en el if para controlarlo ahi
if e==1 and i<n-1 and l[i+1]==0:



¿Por qué propagar([0,0,0,0,1]) y propagar([1,0,0,0,0]), siendo entradas perfectamente simétricas, 
no generan la misma cantidad de repeticiones de llamadas a la función propagar_al_vecino?


Por que recorren de izuierda a derecha
[0,0,0,0,1] 
[0,0,0,1,1] -- despues de 1° iteracion
[0,0,1,1,1] -- despues de 2° iteracion
[0,1,1,1,1] -- despues de 3° iteracion
[1,1,1,1,1] -- despues de 4° iteracion

Si NO existe un 1 termina todo en la primera iteracion
Si existe un 1 en el centro aumenta de a 2
Si existe un 1 a la izquierda termina todo en la primera iteracion
Si existe un 1 a la derecha aumenta de a 1 (el peor caso)
# Complejidad O(n)

