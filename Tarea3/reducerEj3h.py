#!/usr/local/bin/python3

# Reducer: solución del TP3.h: Los tres dispositivos que más llamadas hacen. 

# Toma datos, desde stdin, con formato: <key,value> y los procesa.
# Como value solo es "1" para la ocurrencia de un tipoDisp,
# el procesamiento simplemente va contando las ocurrencias.
# 
# Los datos llegan ordenados por tipoDisp, por lo que
# al detectar el cambio de tipoDisp, se despliega el resultado.

import sys

#Valores iniciales.
acumulados = 0
tipoDispAnt = None
reducer = {}

print ("disp", "\t", "num")

#Lee cada línea de datos.
for line in sys.stdin:
    dataIn = line.strip().split("\t")
    if len(dataIn) != 2:
        # Hay algo raro, ignora esta linea.
        continue
        
    tipo, valor  = dataIn
    
    if tipoDispAnt != tipo:
        if tipoDispAnt != None:
            reducer[tipoDispAnt] = acumulados
        tipoDispAnt = tipo
        acumulados = 0
        
    tipoDispAnt = tipo
    acumulados += 1

if tipoDispAnt != None:
    reducer[tipoDispAnt] = acumulados
    
i = 0
for key, value in sorted(reducer.items(), key = lambda item: (item[1], item[0]), reverse = True):
    i += 1
    if i > 3:
        break
    print ("%s \t %s" % (key, value))