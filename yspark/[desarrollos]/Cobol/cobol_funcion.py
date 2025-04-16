import json
from coboljsonifier.copybookextractor import CopybookExtractor
from coboljsonifier.parser import Parser
from coboljsonifier.config.parser_type_enum import ParseType
import pandas as pd
import ast
from colorama import init, Fore

def read_file(interface, size=1024):
    with open(interface, 'rb') as f:
        chunk = f.read(size)
        print(chunk)
    

def extractor_copybook(archivo_cobol):
    dict_structure = CopybookExtractor(archivo_cobol).dict_book_structure
    df = pd.DataFrame([key for key in dict_structure.keys()], columns=['Name'])
    df['type'] = [value['type'] for value in dict_structure.values()]
    df['format'] = [value['format'] for value in dict_structure.values()]
    df['size'] = [value['size'] for value in dict_structure.values()]
    df['decimals'] = [value['decimals'] for value in dict_structure.values()]
    
    return df, dict_structure

def parser(interface, dict_structure, df, rows, format):

    if format == 'ascii':
        parser = Parser(dict_structure, ParseType.FLAT_ASCII).build()
    if format == 'binary':
        parser = Parser(dict_structure, ParseType.BINARY_EBCDIC).build()
    
    size = parser.size
    print(Fore.GREEN + "Registry calculated lenght: ", size)

    with open(interface, 'rb') as f2:
        for x in range(rows):
            # EBCDIC
            data = f2.read(size)

            parser.parse(data)
            dictvalue = parser.value

            pretty = json.dumps(dictvalue, indent=4,default=str)
            val_convert = ast.literal_eval(pretty.replace("null", "None"))
            col = 'col' + str(x)
            df[col] = [value for value in val_convert.values()]

    return df
