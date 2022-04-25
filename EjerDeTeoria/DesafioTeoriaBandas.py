import json
import csv
archivo = open("bandas.txt", "w")
datos = [
{"nombre": "William Campbell", "ciudad": "La Plata", "ref": "www.instagram.com/williamcampbellok"},
{"nombre": "Buendia", "ciudad": "La Plata", "ref":"https://buendia.bandcamp.↪com/"},
{"nombre": "Lúmine", "ciudad": "La Plata", "ref": "https://www.instagram.↪com/luminelp/"}]
json.dump(datos, archivo)
archivo.close()
archivo = open("bandas.txt", "r")
datos = json.load(archivo)
print(datos)
#datos_a_mostrar = json.dumps(datos, indent=4)
#print(datos_a_mostrar)
archivo.close()

print("ahora")
archivo_cvs = open("bandas.csv", "r")
csvreader = csv.DictReader(archivo_cvs, delimiter=',')
for linea in csvreader:
  print(linea["Nombre"])

archivo_cvs.close()
