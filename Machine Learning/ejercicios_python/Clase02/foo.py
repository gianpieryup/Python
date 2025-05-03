numero_valido=False
while not numero_valido:
    try:
        a = input('Ingresá un número entero: ')
        n = int(a)
        numero_valido = True
    except ValueError:
        print('No es válido. Intentá de nuevo.')
print(f'Ingresaste {n}.')

'''
Probá también qué ocurre si querés salir sin ingresar nada generando 
una excepción presionando las teclas Ctrl+C. Leé el mensaje que 
describe lo ocurrido: Ctrl+C genera una excepción de 
tipo KeyboardInterrupt que no es atrapada.

Si no especificamos el tipo de excepción que queremos atrapar, 
vamos a terminar atrapando todas la excepciones. 
Probá lo mismo que antes pero con este código.

except ValueError: -> except:
'''
