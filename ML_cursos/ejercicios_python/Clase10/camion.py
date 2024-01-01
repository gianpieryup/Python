# -*- coding: utf-8 -*-
# camion.py

class Camion:

    def __init__(self, lotes):
        self.lotes = lotes

    def __iter__(self):
        return self.lotes.__iter__()
    
    def __len__(self):
        return len(self.lotes)
    
    def __getitem__(self,indice):
        return self.lotes[indice]
    
    # Resultado de: print(camion)
    def __str__(self):
        res = f'Camion con {len(self)} lotes:\n'
        for l in self.lotes:
            res += f'Lote de {l.cajones} cajones de {l.nombre}, pagados a ${l.precio} cada uno.\n'
        return res
    
    # Resultado de: camion
    def __repr__(self):
        res = "Camion(["
        for l in self.lotes:
            res += f'{l}, '
        res = res[:-2]
        res += "])"  
        return res
    
    def __contains__(self, nombre):
        return any([lote.nombre == nombre for lote in self.lotes])

    def precio_total(self):
        return sum(l.costo() for l in self.lotes)

    def contar_cajones(self):
        from collections import Counter
        cantidad_total = Counter()
        for lote in self.lotes:
            cantidad_total[lote.nombre] += lote.cajones
        return cantidad_total
    
if __name__ == '__main__':
    from lote import Lote
    lista_lotes = [Lote("l1",5,10),Lote("l2",10,20)]
    c = Camion(lista_lotes)