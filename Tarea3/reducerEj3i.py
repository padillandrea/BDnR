#!/usr/local/bin/python3

# Reducer: solución del TP3.h: Los tres dispositivos que más llamadas hacen. 

# Toma datos, desde stdin, con formato: <key,value> y los procesa.
# Como value solo es "1" para la ocurrencia de un tipoDisp,
# el procesamiento simplemente va contando las ocurrencias.
# 
# Los datos llegan ordenados por IdRbase, por lo que
# al detectar el cambio de IdRbase, se despliega el resultado.

import sys

#Valores iniciales.
acumulados = 0
IdRbaseAnt = None
reducer = {}

print ("id", "\t", "num")

#Lee cada línea de datos.
for line in sys.stdin:
    dataIn = line.strip().split("\t")
    if len(dataIn) != 2:
        # Hay algo raro, ignora esta linea.
        continue
        
    IdRbase, valor  = dataIn
    
    if IdRbaseAnt != IdRbase:
        if IdRbaseAnt != None:
            reducer[IdRbaseAnt] = acumulados
        IdRbaseAnt = IdRbase
        acumulados = 0
        
    IdRbaseAnt = IdRbase
    acumulados += 1

if IdRbaseAnt != None:
    reducer[IdRbaseAnt] = acumulados
    
i = 0
for key, value in sorted(reducer.items(), key = lambda item: (item[1], item[0]), reverse = True):
    i += 1
    if i > 3:
        break
    print ("%s \t %s" % (key, value))