# Ejercicio 2.2: Lectura de un archivo de datos
f = open('../Data/camion.csv', 'rt')
headers = next(f) # Nos saltamos el header
print("Header:",headers)
costo_total=0
for line in f:
    row = line.split(',')
    costo_total = costo_total + int(row[1])*float(row[2])
    print(row)
    
f.close()
print("Costo total",costo_total)


# Ejercicio 2.3: Precio de la naranja
f = open('../Data/precios.csv', 'rt')
pre_naranja = 0
headers = next(f) # Nos saltamos el header
for line in f:
    row = line.split(',')
    if row[0] == "Naranja":
        pre_naranja = row[1]
    
f.close()
print("El precio de la naranja es:",pre_naranja)


# Ejercicio 2.4: Archivos comprimidos
import gzip
with gzip.open('../Data/camion.csv.gz', 'rt') as f:
    for line in f:
        print(line, end = '')
      
        
      
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

