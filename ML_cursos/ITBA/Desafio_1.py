''' ACLARACION: Para el HACKERANT
    Notar bien que oupit quiere el programa
    Se toma en cuenta la cantidad de compilaciones (succes rate)
    Se toma en cuenta el tiempo
    NUNCA TOCAR la def o el __init__ (NUNCA)
'''

# La conjetura del Dr. Lothar
def lothar(n):
    pasos=0
    while n != 1:
        if n%2 == 0:
            n = int(n / 2)
        else:
            n = n*3 + 1
        pasos = pasos + 1
    return pasos

n = int(input())

print( lothar(n) )