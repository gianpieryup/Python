# -*- coding: utf-8 -*-
class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0


# Usando un par de objetos de la clase Cola, escribí una nueva clase 
# llamada TorreDeControl que modele el trabajo de una torre de control 
# de un aeropuerto con una pista de aterrizaje. Los aviones que están esperando
#  para aterrizar tienen prioridad sobre los que están esperando para despegar. 
#  La clase debe funcionar conforme al siguiente ejemplo:
    
     
class TorreDeControl:
    def __init__(self):
        '''Crea una cola vacia.'''
        self.cola_arribos = Cola()
        self.cola_partidas = Cola()
        
    def nuevo_arribo(self,na):
        self.cola_arribos.encolar(na)
        
    def nueva_partida(self,na):
        self.cola_partidas.encolar(na)   
    
    def ver_estado(self):
        print("Vuelos esperando para aterrizar: ",end='')
        for a in self.cola_arribos.items:
            print(f'{a} ' ,end='')
        print()
        print("Vuelos esperando para despegar: ",end='')
        for p in self.cola_partidas.items:
            print(p,end='')
        print()
        
    def asignar_pista(self):
        if self.cola_arribos.esta_vacia():  # == []: es un objeto no puedo hacer eso
            if self.cola_partidas.esta_vacia(): 
                print("No hay vuelos en espera")
            else:
                v_arribo = self.cola_partidas.desencolar()
                print(f'El vuelo {v_arribo} aterrizó con éxito.')
        else:
            v_partida = self.cola_arribos.desencolar()
            print(f'El vuelo {v_partida} despegó con éxito.')

                
        
if __name__ == '__main__':
    torre = TorreDeControl()
    
    torre.nuevo_arribo('AR156')
    torre.nueva_partida('KLM1267')
    torre.nuevo_arribo('AR32')
    torre.ver_estado()
    
    torre.asignar_pista()
    torre.asignar_pista()
    torre.asignar_pista()
    torre.asignar_pista()
    