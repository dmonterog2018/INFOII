#Metodo para limpiar el terminal
def limpiar_terminal():
    print(chr(27) + "[2J")

#Metodo para validar una celda
def validar_celda(celda, max_col,max_row) -> bool:
    if len(celda) > 2 or len(celda) <= 1:
        print('No es el formato correcto, intentalo otra vez')
        return False
    else:
        if celda[0] <= max_col and int(celda[1]) <= max_row:
            print("Celda correcta")
            return True
        else:
            print("Celda fuera de rango, intentalo otra vez")
            return False

#Metodo para comprobar si la celda esta disponible       
def comprobar_celda_disponible(celda,equipo) -> bool:
    for i in equipo:
        for t in i.values():
            if t == celda:
                print('La celda elegida ya esta ocupada por otro miembro. Seleccione una correcta')
                return False
    return True

#Metodo para validar las celdas contiguas
def validar_celda_contigua(celda1,celda2) -> bool:
    max_col = 'd'
    max_row = 4
    if not validar_celda(celda2, max_col,max_row):
        return False

    if ((celda1[0] == celda2[0] and abs(celda1[1] - celda2[1]) == 1) or (celda1[1] == celda2[1] and abs(ord(celda1[0]) - ord(celda2[0]))== 1)):
        print('Movimiento efectueado')
        return True

    else:
        print('La celda a la que intentas moverte no es contigua. Intentalo otra vez')
        return False

#Metodo para validar la accion
def validar_accion(accion) -> bool:
    if accion != 1 and accion != 0:
        print('Accion equivocada. Intentalo otra vez')
        return False
    else:
        return True
#validar_celda_contigua('a2', 'b3')