# Mapper: solución del TP3.d: Calidad de experiencia: Promedio general y por operador.

# Selecciona campos del archivo CSV: RegQoE
# El formato de cada linea es:
# Fecha hora,IdDisp,TipoDisp,mOS,MNO,IdRadioBase,Lat,Long,GoS,QoE
#
# Este filtro toma una linea de entrada de diez elementos,
# desde stdin, selecciona dos de ellos (MNO y QoE) y lo entrega en 
# stdout en el formato:
#     <MNO , QoE>
# separando cada valor por una coma.

import sys

for Line in sys.stdin:
    Data = Line.strip().split(",")
    res = Data[4] + "," + Data[9]
    print(res)