#!/usr/local/bin/python3

# Reducer: solución del TP3.e: Identifica las cinco radio bases que ofrecen, respectivamente, la mejor y la peor calidad de experiencia.

# Toma datos, desde stdin, con formato: <key,value> y los procesa.
# el procesamiento simplemente es ir acumulando la suma de val por IdRBase
# y al final, calcular e imprimir los porcentajes.
# 
# Los datos deben llegar ordenados por tipoDisp.

import sys
import heapq

#Preparación de variables.
scoreAcumulado = 0
totElem = 0
IdRbaseAnt = None
maxIdQoE = []
minIdQoE = []

#Lee cada línea de datos.
for line in sys.stdin:
    dataIn = line.strip().split("\t")
    if len(dataIn) != 2:
        # Hay algo raro, ignora esta linea.
        continue

    IdRbaseActual, QoEActual  = dataIn
    QoEActual = int(QoEActual)

    #Cuando cambia el IdRbase, guarda los 5 QoE mejores y peores.
    if IdRbaseAnt and IdRbaseAnt != IdRbaseActual:
        scorePromedio = scoreAcumulado/totElem
        heapq.heappush(maxIdQoE, (scorePromedio, IdRbaseAnt)) # min Heap para almacenar los primeros cinco
        heapq.heappush(minIdQoE, (-scorePromedio, IdRbaseAnt)) # max Heap para almacenar los últimos cinco

        # Eliminamos elementos de los heaps si exceden su capacidad
        if len(maxIdQoE) > 5:
            heapq.heappop(maxIdQoE)
        if len(minIdQoE) > 5:
            heapq.heappop(minIdQoE)

        scoreAcumulado = 0
        totElem = 0

    IdRbaseAnt = IdRbaseActual
    totElem += 1
    scoreAcumulado += QoEActual			#Va acumulando para el tipoDisp actual.

#Guarda el acumulado del último IdRbase.
if IdRbaseAnt:
    scorePromedio = scoreAcumulado/totElem
    heapq.heappush(maxIdQoE, (scorePromedio, IdRbaseAnt))
    heapq.heappush(minIdQoE, (-scorePromedio, IdRbaseAnt))

    if len(maxIdQoE) > 5:
        heapq.heappop(maxIdQoE)
    if len(minIdQoE) > 5:
        heapq.heappop(minIdQoE)

# Imprimimos los resultados
print("top 5", "\t","QoE Promedio")
while maxIdQoE:
    QoE, IdRbase = heapq.heappop(maxIdQoE)
    print(IdRbase, "\t", QoE)
print()

print("bot 5", "\t","QoE Promedio")
while minIdQoE:
    QoE, IdRbase = heapq.heappop(minIdQoE)
    print(IdRbase, "\t", -QoE)