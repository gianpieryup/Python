# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 13:04:43 2021

@author: GIANPIER
"""

# -*- coding: utf-8 -*-
# Ejercicio 1.7: La hipoteca de David

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0

while saldo > 0:
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual

print('Total pagado', round(total_pagado, 2))


# Ejercicio 1.8: Adelantos

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
adelanto_mensual = 1000
i = 1
meses = 0
while saldo > 0:
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual
    
    if i <= 12:
        saldo = saldo - adelanto_mensual
        total_pagado = total_pagado + adelanto_mensual
        i = i + 1
           
    meses=meses+1
    
print('Total pagado', round(total_pagado, 2),"en",meses,"meses")


# Ejercicio 1.9: Calculadora de adelantos

pago_extra_mes_comienzo = 61
pago_extra_mes_fin = 108
pago_extra = 1000

saldo = 500000.0
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0.0
mes = 1
while saldo > 0:
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual
    
    if pago_extra_mes_comienzo <= mes and mes <= pago_extra_mes_fin:
        saldo = saldo - pago_extra
        total_pagado = total_pagado + pago_extra
    
    # Ejercicio 1.11: Bonus
    if saldo <0:
        saldo=0
        
    print(f'{mes:3} {total_pagado:10.2f} {saldo:10.2f}')
    # print(mes, round(total_pagado, 2),round(saldo, 2))    
    mes=mes+1
print("Total pagado:",round(total_pagado, 2))
print("Meses:",mes-1)

# Ejercicio 1.12: Un misterio
''' Los caracteres ("",0,[]) representan false
    Todo lo demas es True
'''