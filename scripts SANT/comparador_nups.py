import pandas as pd
import numpy as np
# Si dejamos el scrip en la misma carpeta que los csv's solo debemos poner los nombres y no la ruta
name_oracle='oracle.csv'
name_hive='hive.csv'
header_nup_oracle = 'NUP'
header_nup_hive = 'cod_per_nup'


archivo_oracle=pd.read_csv(name_oracle)
archivo_hive=pd.read_csv(name_hive)

# Las cabeceras, para solo quedarnos con los nups
nup_oracle=archivo_oracle[header_nup_oracle]
nup_hive=archivo_hive[header_nup_hive]


print('-'*10,"HIVE",'-'*10)
archivo_hive["en_oracle"]=nup_hive.isin(nup_oracle)
print(archivo_hive.groupby(["en_oracle"]).count()[header_nup_hive],'\n')
en_hive_pero_no_en_oracle = np.setdiff1d(nup_hive, nup_oracle)
print("Algunos NUPS \n",en_hive_pero_no_en_oracle[:25],'\n')



print('-'*10,"ORACLE",'-'*10)
archivo_oracle["en_hive"]=nup_oracle.isin(nup_hive)
print(archivo_oracle.groupby(["en_hive"]).count()[header_nup_oracle],'\n')
en_oracle_pero_no_en_hive = np.setdiff1d(nup_oracle, nup_hive)
print("Algunos NUPS \n",en_oracle_pero_no_en_hive[:25])



'''
AUTOR: Gianpier Yupanqui
LAST MODIFICATION: 29/04/2022

NOTES
No hace falta quitar los 0 de la izquierda al leerlos con pandas ya se los quita

#crea y guarda en un archivo .csv con los resultados
archivo_hive.to_csv(r"add_columns.csv") 
'''