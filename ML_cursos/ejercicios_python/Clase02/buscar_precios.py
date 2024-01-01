
def buscar_precio(fruta):
    f = open('../Data/precios.csv', 'rt')
    pre_fruta = 0
    next(f) # Nos saltamos el header
    for line in f:
        row = line.split(',')
        if row[0] == fruta:
            pre_fruta = row[1]
        
    f.close()
    if pre_fruta !=0:
        print("El precio de un cajón de",fruta,"es:",pre_fruta)
    else:
        print(fruta,"no figura en el listado de precios.")
       
buscar_precio('Frambuesa')
buscar_precio('Kale')