import csv
import sys

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

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'
    
costo = costo_camion(nombre_archivo)
print('Costo total:', costo)

"""
python camion_commandline.py ../Data/missing.csv
python3 camion_commandline.py ../Data/missing.csv
"""