# Ejercicio 4.5: Invertir una lista
def invertir_lista(lista):
    invertida = []
    for e in lista: # Recorro la lista
        invertida = [e] + invertida #agrego el elemento e al principio de la lista invertida
    return invertida

if __name__=="__main__":
    print(invertir_lista([1, 2, 3, 4, 5]))
    print(invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']))