import csv
from typing import Counter


def generate_file(nombre):
    """
    genera un archivo ".txt" a partir de un nombre otorgado por parametro "input"
    devolviendo el arhcivo generado con la funcion writer creada.
    """
    na = open(nombre+".txt", "w", encoding='utf-8')
    return csv.writer(na)


# Abrimos el archivo .csv
archivo = open(r'pythonPracticas\TOTAL_nuevo.csv',mode="r",encoding='utf-8')

# utlizamos un "lector" para .csv, delimitado por ","
csvreader = csv.DictReader(archivo, delimiter=',')

#writer = csv.writer(generate_file(nombrea=input("ingrese nombre de archivo: ")))
writer = generate_file("Nocturno")#nombre=input("ingrese nombre de archivo: "))

new = list(csvreader)
for elem in csvreader:
    if ((elem["Hora"]> 7) and (elem["Hora"] < 19)):
        writer.writerow([elem["Hora"], elem["Nombre completo del usuario"], elem["Usuario afectado"], elem["Nombre evento"], elem["Descripción"],  elem["Dirección IP"]])
        new.append(new[elem])
archivo.close()
#no se como hacer para sacar la fecha...