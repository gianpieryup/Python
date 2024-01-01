# Ejercicio 3.9: La función zip()
import csv

def costo_camion(nombre_archivo):
    
    f = open(nombre_archivo, 'rt')
    filas = csv.reader(f)
    encabezados = next(filas)
    costo_total=0
    
    for n_fila, fila in enumerate(filas, start=1):
        record = dict(zip(encabezados, fila))
        try:
            ncajones = int(record['cajones'])
            precio = float(record['precio'])
            costo_total += ncajones * precio
        except:
            print(f'Fila {n_fila}: No pude interpretar: {fila}')
    return costo_total

#  Se pude especificar el tipo de error que quieres capturar
#  except [tipo_error]:
#  ValueError : hay un problema con el contenido del objeto al que intentó asignar el valor
#  KeyError : No existe el indice
        
if __name__=="__main__":
    costo = costo_camion('../Data/fecha_camion.csv')
    print('Costo total:', costo) 
    # Costo total: 47671.15        

    # PRUEBA ARBOLES
    # f = open('../Data/arbolado-en-espacios-verdes.csv', 'rt', encoding='utf8')
    # encabezados = next(f).strip("\n").split(',')
    # arboles = []
    # for line in f:
    #     fila = line.strip("\n").split(',')
    #     arbol = {}
    #     for e,d in zip(encabezados,fila):
    #         arbol[e]=d
    #     arboles.append(arbol)           
