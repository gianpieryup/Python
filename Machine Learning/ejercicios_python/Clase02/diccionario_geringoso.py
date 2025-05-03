def traducir_a_gerundio(palabra):
    gerundio=''
    for c in palabra:
        gerundio = gerundio + c
        if c == 'a':
            gerundio = gerundio + "pa"
        if c == 'e':
            gerundio = gerundio + "pe"
        if c == 'i':
            gerundio = gerundio + "pi"    
        if c == 'o':
            gerundio = gerundio + "po"
        if c == 'u':
            gerundio = gerundio + "pu"    
    return gerundio


def dicc_gerundio(lista):
    d = {}
    for elem in lista:
        d[elem] = traducir_a_gerundio(elem)
    return d

d = dicc_gerundio(['banana', 'manzana', 'mandarina']) 
print(d)