# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_csv('../Data/OBS_SHN_SF-BA.csv', index_col=['Time'], parse_dates=True)


# df['1-18-2014 9:00':'1-18-2014 18:00'] versatilidad
# df['2-19-2014'] todas las horas |  df['12-25-2014':] de esa fecha para arriba



