# -*- coding: utf-8 -*-
from sklearn.datasets import load_iris
import seaborn as sns
import pandas as pd


if __name__ == '__main__':
    # creamos un dataframe de los datos de flores
    iris_dataset = load_iris()
    
    # etiquetamos las columnas usando las cadenas de iris_dataset.feature_names
    iris_dataframe = pd.DataFrame(iris_dataset['data'], columns = iris_dataset.feature_names)

    # Agregamos la columna 'target'
    iris_dataframe['target'] = iris_dataset['target'] 
    
    sns.pairplot(iris_dataframe, hue="target")