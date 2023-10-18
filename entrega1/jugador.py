from utils import validar_celda
from utils import comprobar_celda_disponible
#from personajes import Personajes


max_col = 'd'
max_row = 4

# Creamos las clases jugador y personajes.

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.equipo = []
        self.turno_end = False



    def crear_equipo(self, nombre):
        dicc = {}


        while True:
            celda_medico = input('Indica la celda (A-D, 1-4. p.ej: B2) en la que posicionar al Medico: ')
            if validar_celda(celda_medico, max_col, max_row) == True:
                if comprobar_celda_disponible(celda_medico,self.equipo) == True:
                    dicc = {'medico':celda_medico}
                    self.equipo.append(dicc)
                    break


        while True:
            celda_artillero = input('Indica la celda (A-D, 1-4. p.ej: B2) en la que posicionar al Artillero: ')
            if validar_celda(celda_artillero, max_col, max_row) == True:
                if comprobar_celda_disponible(celda_artillero, self.equipo) == True:
                    dicc = {'artillero': celda_artillero}
                    self.equipo.append(dicc)
                    break


        while True:
            celda_francotirador = input('Indica la celda (A-D, 1-4. p.ej: B2) en la que posicionar al Francotirador: ')
            if validar_celda(celda_francotirador, max_col, max_row) == True:
                if comprobar_celda_disponible(celda_francotirador, self.equipo) == True:
                    dicc = {'francotirador': celda_francotirador}
                    self.equipo.append(dicc)
                    break


        while True:
            celda_inteligencia = input('Indica la celda (A-D, 1-4. p.ej: B2) en la que posicionar al Inteligencia: ')
            if validar_celda(celda_inteligencia, max_col, max_row) == True:
                if comprobar_celda_disponible(celda_inteligencia, self.equipo) == True:
                    dicc = {'inteligencia': celda_inteligencia}
                    self.equipo.append(dicc)
                    print(self.equipo)
                    break

    def realizar_accion(self):

        print('-----> 1. Mover (Medico) <-----')
        print('-----> 2. Mover (Artillero) <-----')
        print('-----> 3. Mover (Francotirador) <-----')
        print('-----> 4. Mover (Inteligencia) <-----')
        print('-----> 5. Habilidad (Medico) <-----')
        print('-----> 6. Habilidad (Artillero) <-----')
        print('-----> 7. Habilidad (Francotirador) <-----')
        print('-----> 8. Habilidad (Inteligencia) <-----')

        acc = input('Seleccione una acción: ')

        try:
            int(acc)
            if int(acc) <= 8:
                print('ENTRA')
            else:
                print('El numero introducido no es correcto')
        except ValueError:
            print('CACA')
            pass




    def turno(self) -> bool:
        if self.turno_end:
            return True
        else:

            return False


jugar = Jugador('Nombre')
#jugar.crear_equipo(jugar)
jugar.realizar_accion()