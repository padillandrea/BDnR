# Mapper: solución del TP3.e: Identifica las cinco radio bases que ofrecen, respectivamente, la mejor y la peor calidad de experiencia.

# Selecciona campos del archivo CSV: RegQoE
# El formato de cada linea es:
# Fecha hora,IdDisp,TipoDisp,mOS,MNO,IdRadioBase,Lat,Long,GoS,QoE
#
# Este filtro toma una linea de entrada de diez elementos,
# desde stdin, selecciona uno de ellos (QoE) y lo entrega en 
# stdout en el formato:
#     <key,value> (agrega ceros a la izquierda si es necesario)
# separando cada valor por tab (tabulador).

import sys

for Line in sys.stdin:
    Data = Line.strip().split(",")
    if len(Data) == 10:
        Fecha,IdDisp,tipoDisp,mOS,MNO,IdRbase,Lat,Lon,GoS,QoE = Data
        if int(QoE) < 10:
            print(IdRbase+"\t"+"00"+str(QoE))
        elif int(QoE) < 100:
            print(IdRbase+"\t"+"0"+str(QoE))
        else:
            print(MNO+"\t"+str(QoE))