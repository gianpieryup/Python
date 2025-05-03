# -*- coding: utf-8 -*-
# Ejercicio 11.13: Hojas ISO y recursión
def medidas_hoja_A(N):
   if N==0: return (841,1189)
   ancho_ant = medidas_hoja_A(N-1)[0]
   alto_ant = medidas_hoja_A(N-1)[1]
   return (alto_ant//2,ancho_ant)