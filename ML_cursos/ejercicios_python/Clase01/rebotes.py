'''
    Ejercicio 1.5: La pelota que rebota
    Una pelota de goma es arrojada desde una altura de 100 metros y 
    cada vez que toca el piso salta 3/5 de la altura desde la que cayó. 
    Escribí un programa rebotes.py que imprima una tabla mostrando las alturas 
    que alcanza en cada uno de sus primeros diez rebotes.
'''

altura =100
for i in range(10):
    altura =3*altura/5
    print(round(altura,4))