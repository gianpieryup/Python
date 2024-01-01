# Ejercicio 4.6: Propagacion
''' Se podria reducir la funcion con listas por conprension
    [num for x in range(cantidad)]
'''
def bloques(num,cantidad):
    res = []
    for x in range(cantidad):
        res.append(num)
    return res

def propagar(lista):
    print(lista)
    # separamos en listas por el -1
    res_total=[]
    res = []
    for e in lista:
        if e != -1:
            res.append(e)
        else:
            if res != []:
                res_total.append(res)
                res=[]
    res_total.append(res) # La ultima que quedo
    print(res_total)
    
    propagado=[]
    for lista in res_total:
        if 1 in lista:
            propagado = propagado + bloques(1,len(lista))
            
        else:
            propagado = propagado + lista
        propagado.append(-1)
    
    if propagado[-1]== -1 and len(lista) != len(propagado):
        propagado.pop() #En la ultima iteracion se dejo un -1 extra
    
    print(propagado)
    return propagado

if __name__=="__main__":
    p = propagar([0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0])
    