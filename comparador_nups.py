import pandas as pd
import numpy as np
# Si dejamos el scrip en la misma carpeta que los csv's solo debemos poner los nombres y no la ruta
archivo_oracle=pd.read_csv('oracle.csv')
archivo_hive=pd.read_csv('hive.csv')

# Las cabeceras, para solo quedarnos con los nups
nup_oracle=archivo_oracle["NUP"]
nup_hive=archivo_hive["NUP"]


print('-'*10,"HIVE",'-'*10)
archivo_hive["en_oracle"]=nup_hive.isin(nup_oracle)
print(archivo_hive.groupby(["en_oracle"]).count()['NUP'],'\n')
en_hive_pero_no_en_oracle = np.setdiff1d(nup_hive, nup_oracle)
print("Algunos NUPS \n",en_hive_pero_no_en_oracle[:25],'\n')




print('-'*10,"ORACLE",'-'*10)
archivo_oracle["en_hive"]=nup_oracle.isin(nup_hive)
print(archivo_oracle.groupby(["en_hive"]).count()['NUP'],'\n')
en_oracle_pero_no_en_hive = np.setdiff1d(nup_oracle, nup_hive)
print("Algunos NUPS \n",en_oracle_pero_no_en_hive[:25])







#crea y guarda en un archivo .csv con los resultados
#archivo_hive.to_csv(r"add_columns.csv") 
'''
No hace falta quitar los 0 de la izquierda al leerlos con pandas
ya se los quita
'''