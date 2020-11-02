#!/usr/local/bin/python3

# Reducer: solución del TP3.b: Porcentaje del tipo de dispositivo por operador.

# Toma datos, desde stdin, con formato: <key1,key2,value> y los procesa.
# Como val solo es "1" para la ocurrencia de un operador y tipoDisp,
# el procesamiento simplemente es ir acumulando por operador y tipoDisp
# y al final, calcular e imprimir los porcentajes.
# 
# Los datos deben llegar ordenados por operador y tipoDisp.

import sys

#Preparación de variables.
acumulados = 0
total = 0
dispAnt = None
MNOAnt = None
totalDisp = []
i = 1

#Lee cada línea de datos.
for line in sys.stdin:
    dataIn = line.strip().split("\t")
    if len(dataIn) != 3:
        # Hay algo raro, ignora esta linea.
        continue

    MNOActual, dispActual, valorActual  = dataIn

    #Cuando cambia el tipoDisp, guarda los acumulados del tipoDisp actual.
    if dispAnt and dispAnt != dispActual:
        totalDisp.append((dispAnt, acumulados))
        total += acumulados
        dispAnt = dispActual
        acumulados = 0

    #Cuando cambia el MNO, guarda los acumulados del tipoDisp actual.
    if MNOAnt and MNOAnt != MNOActual:
        # Imprimimos todos los dispositivos y porcentajes del MNOAnt
        for disp, dispTotal in totalDisp:
            dispPorc = round(dispTotal/total * 100, 2)
            print(MNOAnt, "\t", disp, "\t", dispPorc,"%")
        totalDisp = []
        total = 0

    dispAnt = dispActual
    MNOAnt = MNOActual
    acumulados += 1			#Va acumulando para el MNO, tipoDisp actual.

#Guarda e imprime acumulado del último MNO.
if MNOAnt:
  for disp, dispTotal in totalDisp:
            dispPorc = round(dispTotal/total * 100, 2)
            print(MNOAnt, "\t", disp, "\t", dispPorc,"%")