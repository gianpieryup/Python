import cobol_funcion as cf

interface = 'employee_data.bin'
archivo_cobol = 'inbound.cob'

cf.read_file(interface)

# Se valida el Formato del archivo cobol
df, dict_structure = cf.extractor_copybook(archivo_cobol)
print(df)

#  format='binary' o 'ascii'
df_final = cf.parser(interface, dict_structure, df, rows=2, format='ascii')
print(df_final)