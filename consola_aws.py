from time import sleep
import datetime

print('*'*15)
print('* CONSOLA AWS *')
print('*'*15)

for i in range(8):
    x = datetime.datetime.now()
    print ("Fecha y hora =", x)
    sleep(3600) # espera en seg