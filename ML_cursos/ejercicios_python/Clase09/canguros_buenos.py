# -*- coding: utf-8 -*-
class Canguro:
    """Un Canguro es un marsupial."""
    
    def __init__(self, nombre, contenido=None): # El error era que compartian 'contenido' distintas clases
        """Inicializar los contenidos del marsupio.

        nombre: string
        contenido: contenido inicial del marsupio, lista.
        """
        self.nombre = nombre
        if contenido is None:
            contenido = []
        self.contenido_marsupio = contenido

    def __str__(self):
        """devuelve una representación como cadena de este Canguro.
        """
        t = [ self.nombre + ' tiene en su marsupio:' ]
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)
            t.append(s)
        #print(t)    
        return '\n'.join(t)

    def meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.

        item: objecto a ser agregado
        """
        self.contenido_marsupio.append(item)

#%%
if __name__ == '__main__':
    madre_canguro = Canguro('Madre')
    cangurito = Canguro('gurito')
    madre_canguro.meter_en_marsupio('billetera')
    madre_canguro.meter_en_marsupio('llaves del auto')
    madre_canguro.meter_en_marsupio(cangurito)
    
    print(cangurito)

# Al ejecutar este código todo parece funcionar correctamente.
# Para ver el problema, imprimí el contenido de cangurito. print(cangurito)
# Notamos que tiene lo mismo que madre_canguro

# La explicacion del fenomeno
# https://es.stackoverflow.com/questions/489645/evitar-que-se-modifique-un-atributo-lista-de-un-objeto-al-modificar-el-atributo?noredirect=1#comment870363_489645