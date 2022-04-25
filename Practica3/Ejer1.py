import csv
from tkinter import N
from traceback import print_tb
from collections import defaultdict
import os.path
import os


# def shows_De_Pais(pais,archivo): esto era sin aplicar lambdas lo dejo por las dudas
#     shows = set()
#     for elem in archivo:
#         if pais in elem[5]:
#             shows.add(elem[1])
#     return shows

def filtrar(lista):
    '''Recibe una lista, la limpia, saca vacios y saca espacios al principio/final'''
    lista = list(map(lambda x: x.split(','), lista))
    aux = []
    for listado in lista:        
        for l in listado:
            aux.append(l.strip())
    return list(filter(bool, set(aux)))

def Todos_Los_Paises(datos):
    '''Devuelve todos los paises del csv'''
    return filtrar(list(map(lambda x: x[5], datos)))

def Buscar_Por_Tipo(pais,datos):
    '''Devuelve una lista con los tipos de shows que tiene un pais, si no esta el pais devuelve falso'''
    paises = Todos_Los_Paises(datos)

    if pais in paises:                
        generos_del_pais = list(filter(bool,set(map(lambda linea: linea[10] if pais in linea[5] else False, datos))))  
        return filtrar(generos_del_pais)
    else:
        return False

    
def Buscar_Por_Pais(pais, show, datos):
    '''Devuelve si el pais tiene el show (si el pais no esta devulve False)'''
    paises  = Todos_Los_Paises(datos)
    if pais in paises:         
        lista = list(( map(lambda x : True if (show == x[2] and pais in list(x[5].split(', '))) else False ,datos)))
        if True in lista:
            return 'Esta'
        else:
            return 'No esta'
    else:
        return False

def Ordenar_Paises(datos):
    '''Ordena alfabeticamete la lista de paises'''
    paises = Todos_Los_Paises(datos)
    paises.sort()
    return paises
         
def Buscar_Por_Año(año,datos):
    '''Devuelve una lista con las pelis estrenadas en ese año'''
    lista = list(filter(bool, set(map(lambda x: x[2] if x[7] == año else False , datos))))
    return lista
    

# Abrimos el archivo .csv
path_files = "pythonPracticas\Practica3"
archivo_net = "netflix_titles.csv"

path_arch = os.path.join(os.getcwd(), path_files)
archivo_net = open(os.path.join(path_arch, archivo_net), "r",encoding='utf-8')
data_net = csv.reader(archivo_net, delimiter=',')
header , datos = next(data_net), list(data_net )



#result = set(show[1] for show in (list(filter(lambda n: x in n, datos))))    
#print(result)

print(f"Todos los paises con shows son : {Todos_Los_Paises(datos)}")   
print("================================") 
x = input('ingrese pais: ').title()           
print(Buscar_Por_Tipo(x,datos))
print("================================")  
print(Buscar_Por_Pais('Argentina', 'The Kingdom', datos))
print("================================")  
print(Ordenar_Paises(datos))
print("================================")  
print(Buscar_Por_Año('1999',datos))