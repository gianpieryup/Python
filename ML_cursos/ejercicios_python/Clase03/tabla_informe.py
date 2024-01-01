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
            print("Linea invalida:",row)
    return d

# Ejercicio 3.14: Imprimir una tabla con formato
def hacer_informe(camion, precios):
    
    res=[]
    for c in camion:
        nombre = c['nombre']
        cajones = c['cajones']
        precio_cajon = c['precio']
        precio_venta = precios[nombre]
        cambio =  precio_venta - precio_cajon
        res.append((nombre,cajones,precio_cajon,cambio))
        
    return res

if __name__=="__main__":
    camion = leer_camion('../Data/camion.csv')
    precios = leer_precios('../Data/precios.csv')
    informe = hacer_informe(camion, precios)
    
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    print('%10s %10s %10s %10s' % headers)
    # Que horrible era la otra forma (Amo las tuplas ahora que puedo usarla asi)
    # print(f'{headers[0]:>10s} {headers[1]:>10s} {headers[2]:>10s} {headers[3]:>10s}')
    print('---------- ---------- ---------- ----------')
    for r in informe:
        print('%10s %10d %10.2f %10.2f' % r) # r es una tupla
    
    # la del dolar te la debo quiero creer que se logra solo adecuando el (f')
