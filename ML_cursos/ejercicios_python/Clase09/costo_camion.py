# costo_camion.py
import informe_final
#%%
def costo_camion(filename):
    '''
    Calcula el costo total (cajones*precio) de un camión
    '''
    camion = informe_final.leer_camion(filename)
    return sum([c.costo() for c in camion])
#%%
def main(args):
    if len(args) != 2:
        raise SystemExit('Usoe: %s archivo_camion' % args[0])
    filename = args[1]
    print('Costo total:', costo_camion(filename))
#%%
if __name__ == '__main__':
    import sys
    main(sys.argv)
