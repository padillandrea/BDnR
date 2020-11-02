#!/usr/local/bin/python3

# Reducer: solución del TP3.c: Grado de Servicio: Distribución (histograma) del grado de servicio general.

# Toma datos, desde stdin, con formato: <key,value> y los procesa.
# Como value solo es "1" para la ocurrencia de un mOS,
# el procesamiento simplemente va contando las ocurrencias para hacer un histograma.
# 
# Los datos llegan ordenados ascendentemente por clave de mOS, por lo que
# al detectar el cambio de mOS, se despliega el resultado.

import sys

acumulados = 0				#Valores iniciales.
GoSAnt = None
print ("GoS", "\t", "Hist")

for line in sys.stdin:
    dataIn = line.strip().split("\t")	#Lee una línea: clave_mOS "\t" 1
    if len(dataIn) != 2:
        # Hay algo raro, ignora esta linea.
        continue

    esteGoS, esteValor  = dataIn	#Toma el par: Gos, Valor

    if GoSAnt and GoSAnt != esteGoS:		#Si hay cambio de GoS:
        hist = "".join(["*" for _ in range(acumulados//2)]) # Crea el histograma
        print (GoSAnt, "\t", hist)	#imprime el GoS y el  hist.
        GoSAnt = esteGoS		#Valores iniciales del nuevo GoS.
        acumulados = 0

    GoSAnt = esteGoS	#Incrementa la cuenta del mOS actual.
    acumulados += 1

if GoSAnt != None:
    hist = "".join(["*" for _ in range(acumulados//2)])
    print (GoSAnt, "\t", hist) #Último GoS y cuenta.


