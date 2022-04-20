import os
ext = input("Extension nueva ?: ")
lista_archivos = os.listdir()
for a in lista_archivos:
    name,extension = a.split('.')
    if extension != 'py':
        new_name = name + '.' + ext
        #print(name,extension,new_name)
        os.rename(a,new_name)