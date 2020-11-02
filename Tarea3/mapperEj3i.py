# Mapper: solución del TP3.h: Las tres radio bases con mayor tráfico.

# Selecciona campos del archivo CSV: RegQoE
# El formato de cada linea es:
# Fecha hora,IdDisp,TipoDisp,mOS,MNO,IdRadioBase,Lat,Long,GoS,QoE
#
# Este filtro toma una linea de entrada de diez elementos,
# desde stdin, selecciona uno de ellos (IdRbase) y lo entrega en 
# stdout en el formato:
#     <key,value>
# separando cada valor por tab (tabulador).

import sys

for Line in sys.stdin:
    Data = Line.strip().split(",")
    if len(Data) == 10:
        Fecha,IdDisp,tipoDisp,mOS,MNO,IdRbase,Lat,Lon,GoS,QoE = Data
        print (IdRbase, "\t", 1)