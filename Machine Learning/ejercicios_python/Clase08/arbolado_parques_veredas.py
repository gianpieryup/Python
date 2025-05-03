# -*- coding: utf-8 -*-
import pandas as pd
import os

def df(archivo):
    directorio = '../Data'
    fname = os.path.join(directorio,archivo)
    return pd.read_csv(fname)
        
if __name__ == '__main__':
    # dataframe
    df_veredas =  df('arbolado-publico-lineal-2017-2018.csv')
    df_parques = df('arbolado-en-espacios-verdes.csv')
    
    # Ejercicio 8.7: Lectura y selección
    cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']
    df_lineal  = df_veredas[cols_sel]
    
    especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']
    df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico'].isin(especies_seleccionadas)]


    print("Las 10 Especies mas frecuentes son:")
    res = df_lineal['nombre_cientifico'].value_counts()
    print(res.head(10))
    

    
    # SELECT: diametro a la altura del pecho y altura
    df_tipas_veredas = df_veredas[['diametro_altura_pecho', 'altura_arbol']].copy()
    df_tipas_parques = df_parques[['diametro','altura_tot']].copy()
    
    df_tipas_parques = df_tipas_parques.rename(columns={'diametro': "diametro_altura_pecho", 'altura_tot': "altura_arbol"})
    
    df_tipas_veredas['ambiente']='vereda'
    df_tipas_parques['ambiente']='parque'
    
    df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])
    df_tipas.boxplot('diametro_altura_pecho',by = 'ambiente')
    df_tipas.boxplot('altura_arbol',by = 'ambiente')