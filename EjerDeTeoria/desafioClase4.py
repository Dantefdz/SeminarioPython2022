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
archivo = open(r'pythonPracticas\EjerDeTeoria\netflix_titles.csv',mode="r",encoding='utf-8')

# utlizamos un "lector" para .csv, delimitado por ","
csvreader = csv.DictReader(archivo, delimiter=',')

#writer = csv.writer(generate_file(nombrea=input("ingrese nombre de archivo: ")))
writer = generate_file("nuevo_archivo")#nombre=input("ingrese nombre de archivo: "))

# 1- guardar en otro archivo las peliculas agregadas en el año 2021.sad

for elem in csvreader:
    if "2021" in elem["release_year"]:
        writer.writerow([elem["show_id"], elem["release_year"], elem["description"]])
archivo.close()

# 2- los cinco (5) países con más producciones en Netflix. (x country)
archivo = open(r'pythonPracticas\EjerDeTeoria\netflix_titles.csv',mode="r",encoding='utf-8')
csvreader2 = csv.reader(archivo, delimiter=',')
new = list(csvreader2)
new2 = list()

for x in range(len(new)):
  if new[x][5] != "":
    new2.append(new[x][5])

c = Counter(new2)

print(c.most_common(5))
archivo.close()