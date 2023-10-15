#Script para definir la clase jugador

from utils import validar_celda
from utils import comprobar_celda_disponible

max_col = 'd'
max_row = 4

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.equipo = []
        self.turno_end = False

    equipo = ['medico', 'inteligencia', 'artillero', 'francotirador']

    #Metodo para gestionar el turno del juego
    def turno(self) -> bool:
        if self.turno_end:
            return True
        else:
            # Aregar codigo para delimitar que el turno se acaba
            self.turno_end = True #Cuando termine el turno establece turno = TRUE
            return True

    #Metodo para que un jugador realice su accion
    #def realizar_accion() -> str:

    #Metodo para recibir la accion del jugador contrario
    #def recibir_accion(str) -> None / dict():

    #Metodo para crear el equipo de juego (inicio de juego)
    def crear_equipo(self, nombre):
        dicc = {}
        while True:
            celda_medico = input('Indica la celda (A-D, 1-4. p.ej: B2) en la que posicionar al Medico: ')
            if validar_celda(celda_medico, max_col, max_row) == True:
                if comprobar_celda_disponible(celda_medico,self.equipo) == True:
                    dicc = {'medico' : celda_medico}
                    self.equipo.append(dicc)
                    print(self.equipo)
                    break
            else:
                pass

        while True:
            celda_inteligencia = input('Indica la celda (A-D, 1-4. p.ej: B2) en la que posicionar al Inteligencia: ')
            if validar_celda(celda_inteligencia, max_col, max_row) == True:
                if comprobar_celda_disponible(celda_inteligencia, self.equipo) == True:
                    dicc = {'inteligencia' : celda_inteligencia}
                    self.equipo.append(dicc)
                    print(self.equipo)
                break
            else:
                pass

        while True:
            celda_artillero = input('Indica la celda (A-D, 1-4. p.ej: B2) en la que posicionar al Artillero: ')
            if validar_celda(celda_artillero, max_col, max_row) == True:
                if comprobar_celda_disponible(celda_artillero, self.equipo) == True:
                    dicc = {'artillero' : celda_artillero}
                    self.equipo.append(dicc)
                    print(self.equipo)
                    break
            else:
                pass

        while True:
            celda_francotirador = input('Indica la celda (A-D, 1-4. p.ej: B2) en la que posicionar al Francotirador: ')
            if validar_celda(celda_francotirador, max_col, max_row) == True:
                if comprobar_celda_disponible(celda_francotirador, self.equipo) == True:
                    dicc = {'francotirador' : celda_francotirador}
                    self.equipo.append(dicc)
                    print(self.equipo)
                    break
            else:
                pass

    #Metodo para posicionar el equipo (inicio de juego)
    #def posicionar_equipo():

        
jugar = Jugador('nombre')
jugar.crear_equipo('nombre')