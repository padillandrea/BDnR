# Mapper: solución del TP3.g: Porcentaje de llamadas por tipo de operador.

# Selecciona campos del archivo CSV: RegQoE
# El formato de cada linea es:
# Fecha hora,IdDisp,TipoDisp,mOS,MNO,IdRadioBase,Lat,Long,GoS,QoE
#
# Este filtro toma una linea de entrada de diez elementos,
# desde stdin, selecciona uno de ellos (MNO) y lo entrega en 
# stdout en el formato:
#     <MNO>

import sys

for Line in sys.stdin:
    Data = Line.strip().split(",")
    res = Data[4]
    print(res)