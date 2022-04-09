import copy

celdas_bombas = ['-*-*-',
                 '--*--',
                 '----*',
                 '*----']


def buscar_esquina_sup_izq(celdas: list, pos_actual:tuple):
    """Devuelve la cantidad de bombas que hay cercanas, a un punto ubicado en la esquina superior izq
    de la matriz
    """
    bombas = 0
    fila = pos_actual[0]
    columna = pos_actual[1]
    # busco en la fila de abajo
    if celdas[fila+1][columna] == '*':
        bombas += 1
    # busco a la derecha
    if celdas[fila][columna+1] == '*':
        bombas += 1
    # busco en diagonal hacia abajo, a la derecha
    if celdas[fila+1][columna+1] == '*':
        bombas += 1
    return bombas


def buscar_esquina_sup_der(celdas: list, pos_actual:tuple):
    """Devuelve la cantidad de bombas que hay cercanas, a un punto ubicado en la esquina superior der
    de la matriz
    """
    bombas = 0
    fila = pos_actual[0]
    columna = pos_actual[1]
    # busco en la fila de abajo
    if celdas[fila+1][columna] == '*':
        bombas += 1
    # busco a la izq
    if celdas[fila][columna-1] == '*':
        bombas += 1
    # busco en diagonal hacia abajo, a la izq
    if celdas[fila+1][columna-1] == '*':
        bombas += 1
    return bombas


def buscar_primera_fila(celdas: list, pos_actual:tuple):
    """Devuelve la cantidad de bombas que hay cercanas, a un punto ubicado en la primera fila
    de la matriz
    """
    bombas = 0
    fila = pos_actual[0]
    columna = pos_actual[1]
    # busco en la fila de abajo
    if celdas[fila+1][columna] == '*':
        bombas += 1
    # busco a la izq
    if celdas[fila][columna-1] == '*':
        bombas += 1
    # busco a la derecha
    if celdas[fila][columna+1] == '*':
        bombas += 1
    # busco en diagonal hacia abajo, a la izq
    if celdas[fila+1][columna-1] == '*':
        bombas += 1
    # busco en diagonal hacia abajo, a la derecha
    if celdas[fila+1][columna+1] == '*':
        bombas += 1
    return bombas


def buscar_esquina_inf_der(celdas: list, pos_actual:tuple):
    """Devuelve la cantidad de bombas que hay cercanas, a un punto ubicado en la esquina inferior der
    de la matriz
    """
    bombas = 0
    fila = pos_actual[0]
    columna = pos_actual[1]
    # busco en la fila de arriba
    if celdas[fila-1][columna] == '*':
        bombas += 1
    # busco a la izq
    if celdas[fila][columna-1] == '*':
        bombas += 1
    # busco en diagonal hacia arriba, a la izq
    if celdas[fila-1][columna-1] == '*':
        bombas += 1
    return bombas


def buscar_ultima_fila(celdas: list, pos_actual:tuple):
    """Devuelve la cantidad de bombas que hay cercanas, a un punto ubicado en la ultima fila
    de la matriz
    """
    bombas = 0
    fila = pos_actual[0]
    columna = pos_actual[1]
    # busco en la fila de arriba
    if celdas[fila-1][columna] == '*':
        bombas += 1
    # busco a la izq
    if celdas[fila][columna-1] == '*':
        bombas += 1
    # busco a la derecha
    if celdas[fila][columna+1] == '*':
        bombas += 1
    # busco en diagonal hacia arriba, a la izq
    if celdas[fila-1][columna-1] == '*':
        bombas += 1
    # busco en diagonal hacia arriba, a la derecha
    if celdas[fila-1][columna+1] == '*':
        bombas += 1
    return bombas


def buscar_esquina_inf_izq(celdas: list, pos_actual:tuple):
    """Devuelve la cantidad de bombas que hay cercanas, a un punto ubicado en la esquina inferior izq
    de la matriz
    """
    bombas = 0
    fila = pos_actual[0]
    columna = pos_actual[1]
    # busco en la fila de arriba
    if celdas[fila-1][columna] == '*':
        bombas += 1
    # busco a la derecha
    if celdas[fila][columna+1] == '*':
        bombas += 1
    # busco en diagonal hacia arriba, a la derecha
    if celdas[fila-1][columna+1] == '*':
        bombas += 1
    return bombas


def buscar_primera_col(celdas: list, pos_actual:tuple):
    """Devuelve la cantidad de bombas que hay cercanas, a un punto ubicado en la primera columna
    de la matriz
    """
    bombas = 0
    fila = pos_actual[0]
    columna = pos_actual[1]
    # reutilizo el modulo para buscar bombas hacia abajo
    bombas += buscar_esquina_sup_izq(celdas, pos_actual)
    # busco ahora las que estan hacia arriba
    bombas += buscar_esquina_inf_izq(celdas, pos_actual)
    # le resto las comunes a la derecha
    if celdas[fila][columna + 1] == '*':
        bombas -= 1
    return bombas


def buscar_ultima_col(celdas: list, pos_actual:tuple):
    """Devuelve la cantidad de bombas que hay cercanas, a un punto ubicado en la ultima columna
    de la matriz
    """
    bombas = 0
    fila = pos_actual[0]
    columna = pos_actual[1]
    # uso el modulo para buscar bombas hacia abajo
    bombas += buscar_esquina_sup_der(celdas, pos_actual)
    # busco ahora las que estan hacia arriba
    bombas += buscar_esquina_inf_der(celdas, pos_actual)
    # le resto las comunes a la derecha
    if celdas[fila][columna - 1] == '*':
        bombas -= 1
    return bombas


def buscar_intermedio(celdas: list, pos_actual:tuple):
    """Devuelve la cantidad de bombas que hay cercanas, a un punto ubicado en la ultima columna
    de la matriz
    """
    bombas = 0
    fila = pos_actual[0]
    columna = pos_actual[1]
    # reutilizo el modulo para buscar bombas hacia la izq
    bombas += buscar_primera_col(celdas, pos_actual)
    # busco ahora las que estan hacia la derecha
    bombas += buscar_ultima_col(celdas, pos_actual)
    # le resto las comunes a ambos metodos
    if celdas[fila + 1][columna] == '*':
        bombas -= 1
    if celdas[fila - 1][columna] == '*':
        bombas -= 1
    return bombas


def buscar_bombas(celdas: list, pos_actual: tuple):
    """ Recibe la celda con bombas y una tupla que indica en que posicion estoy actualmente
        Devuelve una lista con el resultado de cantidad de bombas cercanas en cada casillero libre.
    """
    resultado = 0
    if celdas[pos_actual[0]][pos_actual[1]] != '*':
    # Comparaciones si estoy en la primera fila de la matriz
        if pos_actual[0] == 0:
            # Comparo si estoy en la esquina izq
            if pos_actual[1] == 0:
                resultado += buscar_esquina_sup_izq(celdas, pos_actual)
                # Comparo si estoy en la esquina derecha
            elif pos_actual[1] == len(celdas[1])-1:
                resultado += buscar_esquina_sup_der(celdas, pos_actual)
            else:
                resultado += buscar_primera_fila(celdas, pos_actual)

        # comparo si estoy en la ultima fila
        elif pos_actual[0] == len(celdas) - 1:
            if pos_actual[1] == 0:
                resultado += buscar_esquina_inf_izq(celdas, pos_actual)
            elif pos_actual[1] == len(celdas[1]) - 1:
                resultado += buscar_esquina_inf_der(celdas, pos_actual)
            else:
                resultado += buscar_ultima_fila(celdas, pos_actual)

        # curso de acción si estoy en filas intermedias
        else:
            if pos_actual[1] == 0:
                # si estoy en la primera columna
                resultado += buscar_primera_col(celdas, pos_actual)
            elif pos_actual[1] == len(celdas[1]) - 1:
                # si estoy en la ultima columna
                resultado += buscar_ultima_col(celdas, pos_actual)
            else:
                resultado += buscar_intermedio(celdas, pos_actual)
    else:
        resultado = -1
    return resultado


def generar_matriz(celdas_bombas):
    celdas_pistas = []
    for i in range(len(celdas_bombas)):
        fila = []
        for j in range(len(celdas_bombas[1])):
            tupla = i, j
            bombas = buscar_bombas(celdas_bombas, tupla)
            if bombas != -1:
                fila.append(str(bombas))
            else:
                fila.append('*')
        celdas_pistas.append(fila)
    return celdas_pistas

resultado = generar_matriz(celdas_bombas)

print('Matriz de resultados')
for fila in resultado:
    print(fila)