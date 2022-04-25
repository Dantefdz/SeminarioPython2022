import csv
import os.path
import os
import datetime
from collections import Counter
import datetime


def most_common_week_day(datos):
    '''devuelvo una tupla (dia_de_semana_mayor_registros , cant_registros)'''
    
    formato = "%d/%m/%Y %H:%M"
    dias_semana = ['lunes', 'martes', 'miercoles',
                   'jueves', 'viernes', 'sabado', 'domingo']

    # Paso los datos leidos a string y los junto todos en una unica cadena 
    lista = "".join(list(map(lambda x:  str(
        datetime.datetime.strptime(x[0], formato).weekday()), datos)))

    mas_comun = Counter(lista).most_common(1)
    tupla = (dias_semana[int(mas_comun[0][0])], mas_comun[0][1])
    return tupla


def day_amount(datos):
    """devuelve una varaible TimeDelta, con la cant de tiempo entre el primer y ultimo registro"""
    
    formato = "%d/%m/%Y %H:%M"
    # data_set esta ordenado por fecha, y no hay que iterarlo para saber el maximo y minimo
    primero = datetime.datetime.strptime(datos[0][0], formato)
    ultimo = datetime.datetime.strptime(datos[len(datos)-1][0], formato)
    time_dif = primero - ultimo

    return time_dif

path_files = "pythonPracticas\Practica3"
archivo_net = "BBB_nuevo.csv"

path_arch = os.path.join(os.getcwd(), path_files)
archivo_net = open(os.path.join(path_arch, archivo_net), "r",encoding='utf-8')
data_net = csv.reader(archivo_net, delimiter=',')
header , datos = next(data_net), list(data_net )


print(most_common_week_day(datos))
print(day_amount(datos))