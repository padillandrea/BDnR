#!/usr/local/bin/python3

# Reducer: solución del TP3.d: Calidad de experiencia: Promedio general y por operador. 

# Toma datos, desde stdin, con formato: <MNO, QoE> y los procesa.
# Como value solo es "1" para la ocurrencia de un tipoDisp,
# el procesamiento simplemente va contando las ocurrencias.
# 
# Los datos llegan ordenados por tipoDisp, por lo que
# al detectar el cambio de tipoDisp, se despliega el resultado.

import sys

#Valores iniciales.
x = {'33401':'Nextel', '33402':'Telcel', '33403':'Movistar', '33405':'Iusacell/Unefon'}
MNOAnt = None
acumulados = 0
suma = 0
print("Inciso d) Calidad de experiencia: Promedio general y por operador. ")

for line in sys.stdin:
    line, val = line.strip().split(",")
    
    if MNOAnt != line:
        if MNOAnt != None:
            print(x[MNOAnt], ",", suma/acumulados)
        acumulados = 0
        suma = 0
        MNOAnt = line
        
    acumulados += 1
    suma += float(val)
    MNOAnt = line
    
if MNOAnt != None:
    print(x[MNOAnt], ",", suma/acumulados)
