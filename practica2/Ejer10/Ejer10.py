'''10. Trabajando con los contenidos de los archivos que pueden acceder en el curso:
• nombres
• eval1
• eval2
Manipule estos archivos para realizar lo siguiente:
• Generar una estructura con los nombres de los estudiantes y la suma de ambas notas.
• Calcular el promedio de las notas totales e informar que alumnos obtuvieron menos que el
promedio.
'''
def borrarCaracteres(lista):
    aux = []
    for char in lista:
        char = char.replace(',',"").replace("'", "").replace("\n", "")
        aux.append(char)
    return aux

def calcularNotas (lista_nombres, eval1, eval2):
    """hago una lista de tuplas, donde cada tupla tenga nombre y nota total de ambas evaluaciones"""
    pos = 0
    lista = []
    for nombre in lista_nombres:
        tupla = (nombre, int(eval1[pos])+int(eval2[pos]))
        lista.append(tupla)
        pos += 1
    return lista

def CalcularProm(notas):
    '''Calculo el promedio de las notas totales y me lo guardo'''
    total=0
    for n in notas:
        total +=n[1]
    prom= total/len(notas)
    return prom

def promediosBajos(notas,prom):
    '''Informo alumnnos con promedio bajos'''
    for n in notas:
        if n[1] < prom:
            print(f"{n[0]}'tiene una nota por debajo del promedio")

'''Abro los archivos y los combierto en lista'''
nombres= list(open(r'pythonPracticas\practica2\Ejer10\nombres_1.txt',mode="r",encoding='utf-8'))
eval1= list(open(r'pythonPracticas\practica2\Ejer10\eval1.txt',mode="r",encoding='utf-8')) 
eval2= list(open(r'pythonPracticas\practica2\Ejer10\eval2.txt',mode="r",encoding='utf-8')) 

'''borro los caracteres todos los caracteres innecesarios'''
nom = borrarCaracteres(nombres)
evaluacion1 = borrarCaracteres(eval1)
evaluacion2 = borrarCaracteres(eval2)

'''Me guardo en una lista el nombre del estudiante y la suma de sus notas y luego lo muestro'''
notaFinal =calcularNotas(nom,evaluacion1,evaluacion2)
'''print(f"Nombres de los estudiantes y la suma de ambas notas:\n{notaFinal}")'''

'''Calculo el promedio de las notas totales e informo
quienes fueron los alumnos con tuvieron notas menor al promedio'''
promedio =CalcularProm(notaFinal)
promediosBajos(notaFinal,promedio)