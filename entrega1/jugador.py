from utils import validar_celda
from utils import comprobar_celda_disponible
max_col = 'd'
max_row = 4

# Creamos las clases jugador y personajes.

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.equipo = []



    def crear_equipo(self, nombre):
        dicc = {}


        while True:
            celda_medico = input('Indica la celda (A-D, 1-4. p.ej: B2) en la que posicionar al Medico: ')
            if validar_celda(celda_medico, max_col, max_row) == True:
                if comprobar_celda_disponible(celda_medico,self.equipo) == True:
                    print('HOLA')
                    dicc = {'medico':celda_medico}
                    self.equipo.append(dicc)
                    break
            else:
                pass
        while True:
            celda_artillero = input('Indica la celda (A-D, 1-4. p.ej: B2) en la que posicionar al Artillero: ')
            if validar_celda(celda_artillero, max_col, max_row) == True:
                if comprobar_celda_disponible(celda_artillero, self.equipo) == True:
                    dicc = {'artillero': celda_artillero}
                    self.equipo.append(dicc)
                    break
            else:
                pass

        while True:
            celda_francotirador = input('Indica la celda (A-D, 1-4. p.ej: B2) en la que posicionar al Francotirador: ')
            if validar_celda(celda_francotirador, max_col, max_row) == True:
                if comprobar_celda_disponible(celda_francotirador, self.equipo) == True:
                    dicc = {'francotirador': celda_francotirador}
                    self.equipo.append(dicc)
                    break
            else:
                pass

        while True:
            celda_inteligencia = input('Indica la celda (A-D, 1-4. p.ej: B2) en la que posicionar al Inteligencia: ')
            if validar_celda(celda_inteligencia, max_col, max_row) == True:
                if comprobar_celda_disponible(celda_inteligencia, self.equipo) == True:
                    dicc = {'inteligencia': celda_inteligencia}
                    self.equipo.append(dicc)
                    print(self.equipo)
                break
            else:
                pass

class Personaje:

    personajes = {
        'nombre': 'Médico',
        'vida_maxima' : 200,
        'vida_actual' : 200,
        'danyo' : 30,
        'posicion': '',
        'enfriamiento_restante' : 0
    }

jugar = Jugador('nombre')
jugar.crear_equipo('nombre')
