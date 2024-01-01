def invertir_lista(lista):
    '''Recibe una lista L y la develve invertida.'''
    invertida = []
    i = len(lista)
    while i > 0:    # tomo el último elemento 
        i = i-1
        invertida.append (lista.pop(i))  #
    return invertida


# este IF solo se cumple si este es el modulo principal,
# como cuando ejecutamos "python ejemplos.py" desde una terminal
if __name__=="__main__":
    l = [1, 2, 3, 4, 5]
    m = invertir_lista(l)
    print(f'Entrada {l}, Salida: {m}')
