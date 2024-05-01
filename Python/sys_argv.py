#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
 
print("Número de parámetros: ", len(sys.argv))
print("Lista de argumentos: ", sys.argv)

# ----------------------------------------
# > python kwargs.py ui 77
# ----------------------------------------
# Número de parámetros:  3
# Lista de argumentos:  ['kwargs.py', 'ui', '77']