# -*- coding: utf-8 -*-
# Ejercicio 7.10: Funciones y documentación

def valor_absoluto(n):
    '''Calcula el valor absoluto de un numero.

    Pre: n es un número
    Pos: Se devuelve el valor positivo del numero
    '''
    if n >= 0:
        return n
    else:
        return -n


def suma_pares(l):
    '''Calcula la suma de elementos pares en una lista.

    Pre: l es una lista de numeros enteros
    Pos: Se devuelve la suma de los elementos que son pares(incluye negativos)
    '''
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0

    return res

def veces(a, b):
    '''Suma a, b veces. Si b es 0 devuelve 0

    Pre: a es numero y b es un entero positivo
    Pos: a multiplicado por b
    '''
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res


def collatz(n):
    '''Calcula la cantidad de iteraciones que nesecita para que atraves del
    Algoritmo de collatz n llegue a 1
    Por cada iteracion:
        si es par -> divide por 2
        si es impar -> se multiplica por 3 y se suma 1
    
    Pre: n es un entero postivo
    Pos: la cantidad de iteraciones usando collatz para que que llegue a 1
    '''
    res = 1

    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1

    return res
