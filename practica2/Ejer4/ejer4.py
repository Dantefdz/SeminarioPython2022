from collections import Counter


evaluar = """ título: Experiences in Developing a Distributed Agent-based Modeling Toolkit
with Python
resumen: Distributed agent-based modeling (ABM) on high-performance computing resources
provides the promise of capturing unprecedented details of large-scale complex systems.
However, the specialized knowledge required for developing such ABMs creates barriers to
wider adoption and utilization. Here we present our experiences in developing an initial
implementation of Repast4Py, a Python-based distributed ABM toolkit. We build on our
experiences in developing ABM toolkits, including Repast for High Performance Computing
(Repast HPC), to identify the key elements of a useful distributed ABM toolkit. We leverage
the Numba, NumPy, and PyTorch packages and the Python C-API to create a scalable modeling
system that can exploit the largest HPC resources and emerging computing architectures.
"""
def analizar_texto(texto):
    titulo, resumen = texto.replace('\n',' ').split('resumen:')
    match titulo.split():
        case ['título:',*objetcs]:
            titulo = objetcs
    lista_resumen = resumen.split('.')[:-1]
    lista_longitudes = [len(titulo),[]]
    for l in lista_resumen:
        lista_longitudes[1].append(len(l.split()))

    return lista_longitudes


resultado = analizar_texto(evaluar)
calificacion = {
    'facil':0,
    'aceptable':0,
    'dificil':0,
    'muy_dificil':0
}

for i in range(len(resultado[1])):
    if resultado[1][i]<=12:
        calificacion['facil'] += 1
    elif resultado[1][i] <= 17:
        calificacion['aceptable'] +=1
    elif resultado[1][i] <=25:
        calificacion['dificil'] +=1
    else:
        calificacion['muy_dificil'] +=1

print(f"El titulo cumple condiciones: {resultado[0]<=10}.\nCantidad de oraciones: {calificacion['facil']} oraciones faciles de leer,"
      f"{calificacion['aceptable']} oraciones aceptables de leer, {calificacion['dificil']} oraciones dificiles de leer y "
      f"{calificacion['muy_dificil']} oraciones muy dificiles de leer")