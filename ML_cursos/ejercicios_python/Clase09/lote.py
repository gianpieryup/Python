# -*- coding: utf-8 -*-
class Lote:
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio
        
    # Ahora los objectos no se veran como <x.14541679411> si no como f'strings
    def __repr__(self):
        return f'Lote({self.nombre}, {self.cajones}, {self.precio})'
    
    
    def costo(self):
        return  self.cajones * self.precio
    
    def vender(self,ncajones):
        self.cajones -= ncajones

class MiLote(Lote):
    def rematar(self):
        self.vender(self.cajones)        

if __name__ == '__main__':
    s = Lote('Pera', 100, 490.10)
    print(s.costo())
    
    s.vender(25)
    print(s.cajones)
    print(s.precio) # los geter son sin () no son metodos con parametros
    
    c = MiLote('Pera', 100, 490.1)
    print("Heredo el metodo vendo 25 de 100", c.vender(25))
    print("Me queda",c.cajones)

    c.rematar()
    print("Remato todos mis cajones\nMe quedan",c.cajones) 
    