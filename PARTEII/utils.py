# Funcion para limpiar el terminal
def limpiar_terminal():
    print(chr(27) + "[2J")


# Funcion para validar una celda
def validar_celda(celda, max_col, max_row) -> bool:
    if len(celda) > 2 or len(celda) <= 1:  # Comprobamos el formato de celdas (B2)
        print('No es el formato correcto, intentalo otra vez')
        return False
    else:
        if celda[0] <= max_col and int(celda[1]) <= max_row:  # Si el formato es correcto y esta dentro del rango
            return True
        else:  # Si el rango es mayor al establecido FALSE
            print("Celda fuera de rango, intentalo otra vez")
            return False


# Funcion para comrpobar si la celda esta ocupada
def comprobar_celda_disponible(celda, equipo) -> bool:
    for i in equipo:  # Recorremos la lista equipo
        for t in i.values():  # Recorremos los valores del diccionario de la lista equipo
            if t == celda:  # Comrporbamos si la celda esta ocupada por otro miembro del equipo
                print('La celda elegida ya esta ocupada por otro miembro. Seleccione otra por favor')
                return False
    else:
        return True


# Funcion para validar celdas al mover un personaje
def validar_celda_contigua(celda1, celda2) -> bool:
    max_col = 'd'
    max_row = 4
    if not validar_celda(celda2, max_col,
                         max_row):  # Si la funcion validar_celda no es True, devolver FALSE y volver a validar_celda
        return False
    # Verificar si celda1 y celda2 son adyacentes
    if ((celda1[0] == celda2[0] and abs(int(celda1[1]) - int(celda2[1])) == 1) or (
            celda1[1] == celda2[1] and abs(ord(celda1[0]) - ord(celda2[0])) == 1)):
        # Columna: ((celda1[0] == celda2[0] and abs(int(celda1[1]) - int(celda2[1])) == 1) comprueba que la celda de la columna es la misma y que la diferencia del valor de la fila es 1
        # Fila: (celda1[1] == celda2[1] and abs(ord(celda1[0]) - ord(celda2[0]))== 1)) comprueba que la celda de la fila es la misma y que la diferencia del valor de la columna (ASCII) es 1
        # Si una de las dos condiciones se cumple, significa que la celda es adyacente
        print('Movimiento efectueado')
        return True
    else:  # Si ninguna de las condiciones se cumple, la celda no es adyacente y devolvemos FALSE
        print('La celda a la que intentas moverte no es contigua. Intentalo otra vez')
        return False