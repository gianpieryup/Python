def ahorcado():
    palabra = input()
    contador = 0
    while len(palabra) != 0:
        letra = input()
        palabra = palabra.replace(letra, "" )
        contador+=1
    return contador

cant = ahorcado()
print("Intentos", cant)    