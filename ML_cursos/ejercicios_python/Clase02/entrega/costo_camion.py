# Ejercicio 2.9: Funciones de la biblioteca
import csv

def costo_camion(nombre_archivo):
    f = open(nombre_archivo, 'rt')
    rows = csv.reader(f)
    next(rows) # Nos saltamos el header
    costo=0
    
    for row in rows:
        # row = line.split(',') no es necesario con import csv
        try:
            ncajones = int(row[1])
            costo = costo + ncajones*float(row[2])
        except:
            print("[warning] Linea invalida:",row)    
            
    f.close()
    return costo

costo = costo_camion('../Data/missing.csv')
print('Costo total:', costo)        







        