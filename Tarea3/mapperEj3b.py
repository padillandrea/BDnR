# Mapper: solución del TP3.b: Porcentaje del tipo de dispositivo por operador.

# Selecciona campos del archivo CSV: RegQoE
# El formato de cada linea es:
# Fecha hora,IdDisp,TipoDisp,mOS,MNO,IdRadioBase,Lat,Long,GoS,QoE
#
# Este filtro toma una linea de entrada de diez elementos,
# desde stdin, selecciona dos de ellos (MNO y tipoDisp) y lo entrega en 
# stdout en el formato:
#     <key1,key2,value>
# separando cada valor por tab (tabulador).

import sys

for Line in sys.stdin:
    Data = Line.strip().split(",")
    if len(Data) == 10:
        Fecha,IdDisp,tipoDisp,mOS,MNO,IdRbase,Lat,Lon,GoS,QoE = Data

    if int(tipoDisp)<10:
        print(MNO+"\t"+"0"+str(tipoDisp)+"\t"+"1")
    else:
        print(MNO+"\t"+str(tipoDisp)+"\t"+"1")