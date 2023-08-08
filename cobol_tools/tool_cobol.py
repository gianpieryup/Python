import json
from coboljsonifier.copybookextractor import CopybookExtractor
from coboljsonifier.parser import Parser
from coboljsonifier.config.parser_type_enum import ParseType
import pandas as pd
import ast

pd.options.display.max_rows = 4000

def parse_ascii(dict_structure,interface,df,rows):
    parser = Parser(dict_structure, ParseType.FLAT_ASCII).build()

    with open(interface) as archivo:
        i = 1
        for linea in archivo:
            
            data= linea
            parser.parse(data)
            dictvalue = parser.value
            pretty = json.dumps(dictvalue, indent=4,default=str)
            val_convert = ast.literal_eval(pretty.replace("null", "None"))

            col = 'col' + str(i)
            df[col] = [value for value in val_convert.values()]

            if i==rows:
                break
            
            i = i + 1

def parse_bin(dict_structure,interface, df, rows):
    parser = Parser(dict_structure, ParseType.BINARY_EBCDIC).build()
    size = parser.size
    print("// Registry calculated lenght:", size)

    with open(interface, 'rb') as f2:
        for x in range(rows):

            # EBCDIC
            data = f2.read(size)
            if not data:
                break
           
            if data[0:2] == b'\xF0\xF0':    # ====> El nuestro es este formato
                parser.parse(data)
                dictvalue = parser.value

                pretty = json.dumps(dictvalue, indent=4,default=str)
                val_convert = ast.literal_eval(pretty.replace("null", "None"))
                col = 'col' + str(x)
                df[col] = [value for value in val_convert.values()]

            else:
                print(f'// Registry type {data[0:2]} not processed')

if __name__:
    bookfname = input('FileName del copybook: ')
    interface = input('FileName de la interface: ')
    mode = input('Formato de la interface (bin/ascii): ')
    rows = int(input('Cantidad de rows a leer: '))


    dict_structure = CopybookExtractor(bookfname).dict_book_structure

    df = pd.DataFrame([key for key in dict_structure.keys()], columns=['Name'])
    df['type'] = [value['type'] for value in dict_structure.values()]
    df['format'] = [value['format'] for value in dict_structure.values()]
    df['size'] = [value['size'] for value in dict_structure.values()]
    df['decimals'] = [value['decimals'] for value in dict_structure.values()]

    if mode=='bin':
        parse_bin(dict_structure,interface, df, rows)
    else:
        parse_ascii(dict_structure,interface,df,rows)

    print(df)