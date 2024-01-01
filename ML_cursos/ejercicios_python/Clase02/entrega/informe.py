import csv

def leer_camion(nombre_archivo):

    camion = []
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        next(rows)
        for row in rows:
            d={}
            d['nombre']=row[0]
            d['cajones']=int(row[1])
            d['precio']=float(row[2])
            camion.append(d)

    return camion

camion=leer_camion("../Data/camion.csv")
print(camion)

costo_camion = 0.0
for s in camion:
    costo_camion += s['cajones']*s['precio']



def leer_precios(nombre_archivo):
    f = open(nombre_archivo, 'r')
    rows = csv.reader(f)
    d={}
    
    for row in rows:
        try:
            fruta = row[0]
            precio = float(row[1])
            d[fruta]=precio
        except:
            print("Invalido",row)
    return d

precios = leer_precios('../Data/precios.csv')
print(precios)    

recaudacion_venta = 0.0
for k,v in precios.items():
    recaudacion_venta += v

diferencia = recaudacion_venta - costo_camion
print("Balance : recaudacion_venta=",recaudacion_venta,"| costo_camion=",costo_camion)
print("Balance :","Perdida" if diferencia < 0 else "Ganancia")



