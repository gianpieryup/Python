# -*- coding: utf-8 -*-
# formato_tabla.py

class FormatoTabla:
    def encabezado(self, headers):
        '''
        Crea el encabezado de la tabla.
        '''
        raise NotImplementedError()

    def fila(self, rowdata):
        '''
        Crea una única fila de datos de la tabla.
        '''
        raise NotImplementedError()

class FormatoTablaTXT(FormatoTabla):
    '''
    Generar una tabla en formato TXT
    '''
    def encabezado(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def fila(self, data_fila):
        for d in data_fila:
            print(f'{d:>10s}', end=' ')
        print()
            
class FormatoTablaCSV(FormatoTabla):
    '''
    Generar una tabla en formato CSV
    '''
    def encabezado(self, headers):
        print(','.join(headers))

    def fila(self, data_fila):
        print(','.join(data_fila))

class FormatoTablaHTML(FormatoTabla):
    '''
    Generar una tabla en formato HTML
    '''
    def encabezado(self, headers):
        print("<tr><th>",end='')
        print("</th><th>".join(headers),end='')
        print("</th></tr>")
    
    def fila(self, data_fila):
        # No olvidar que para visualizarlo en HTML encapsular el resultado <table></table>
        print("<tr><td>",end='')
        print('</td><td>'.join(data_fila),end='')
        print("</td></tr>")

def crear_formateador(fmt):
    # Elige formato
    if fmt == 'txt':
        return FormatoTablaTXT()
    elif fmt == 'csv':
        return FormatoTablaCSV()
    elif fmt == 'html':
        return FormatoTablaHTML()
    else:
        raise RuntimeError(f'Unknown format {fmt}')        