'''
# Lectura para arhcivos simples y cortos
with open('../Data/camion.csv', 'rt') as f:
        for line in f:
            print(line, end = '')
'''



f = open('../Data/camion.csv', 'rt')
headers = next(f) # puedo saltar una iteracion
print(headers)
#'nombre,cajones,precio\n'
for line in f:
    row = line.split(',')
    print(row)
    
f.close()

