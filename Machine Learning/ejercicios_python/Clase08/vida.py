# -*- coding: utf-8 -*-
from datetime import datetime

def vida_en_segundos(fecha_nac):
    t1 = datetime.strptime(fecha_nac, '%d/%m/%Y')  
    t2 = datetime.now()
    t3 = t2 - t1
    dif_sec = t3.total_seconds()
    return dif_sec

if __name__=="__main__":
   print(vida_en_segundos('21/09/2022'))
    
    
    