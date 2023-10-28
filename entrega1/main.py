# Importamos las funciones necesarias de los otros archivos.

from utils import limpiar_terminal
from jugador import Jugador




def main():
    print('Bienvenidos a Tactical Battle. Iniciemos tu aventura en el juego!\n')
    input('Turno del Jugador 1. Pulsa intro para comenzar el juego...')
    j1 = Jugador()
    j1.crear_equipo()
    j1.posicionar_equipo()
    input('Jugador 1, ha terminado su turno')
    limpiar_terminal()

    input('Turno del Jugador 2. Pulsa intro para comenzar su turno...')
    j2 = Jugador()
    j2.crear_equipo()
    j2.posicionar_equipo()
    input('Jugador 2, ha terminado su turno. Pulse intro.')
    limpiar_terminal()

    j1.set_oponente(j2)
    j2.set_oponente(j1)
    final = False
    while not final:
        input('Turno del Jugador 1. Pulsa intro para comenzar')
        final = j1.turno1()

        if final:
            print('****** EL JUGADOR 1 HA GANADO LA PARTIDA! ********')
            return 0
        input('Jugador 1, pulse intro para terminar su turno')
        limpiar_terminal()

        input('Turno del Jugador 2. Pulsa intro para comenzar')
        final = j2.turno1()
        if final:
            print('****** EL JUGADOR 2 HA GANADO LA PARTIDA! ********')
            return 0
        input('Jugador 2, pulse intro para terminar su turno')
        limpiar_terminal()



if __name__ == '__main__':
    main()