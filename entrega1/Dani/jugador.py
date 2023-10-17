#Script para definir la clase jugador

from utils import validar_celda, comprobar_celda_disponible, validar_celda_contigua, validar_accion

max_col = 'd'
max_row = 4

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.equipo = []
        self.turno_end = False

    #Metodo para gestionar el turno del juego
    def turno(self) -> bool:
        if self.turno_end:
            return True
        else:
            # Aregar codigo para delimitar que el turno se acaba
            self.turno_end = True #Cuando termine el turno establece turno = TRUE
            return True

    #Metodo para que un jugador realice su accion
    def realizar_accion(self) -> str:
        while True:
            #Decidir si mover o utilizar habilidad
            try:
                accion = int(input('Escribe 1 (Mover el personaje) o 0 (Utilizar habilidad): '))
            except ValueError:
                print('Error. Debe ser 1 o 0')
                accion = int(input('Escribe 1 (Mover el personaje) o 0 (Utilizar habilidad): '))
            if validar_accion(accion) == True:
                if accion == 1:
                    print('mover')
                    #Mover personaje
                    break
                elif accion == 0:
                    #Utilizar la habilidad del personaje
                    print('habilidad')
                    break

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

#Clase Personaje
class Personaje():
    def __init__(self, nombre, vida, dano, enfriamiento):
        self.nombre = nombre
        self.vida = vida
        self.enfriamiento = enfriamiento

#Subclase Medico
class Medico(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, vida = 1, enfriamiento = 0)

#Subclase Inteligencia
class Inteligencia(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, vida = 2, enfriamiento = 0)
#Subclase Artillero
class Artillero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, vida = 2, enfriamiento = 0)
        self.dano = 1

    #Metodo para ejecutar la habilidad del artillero
    def disparar(self):
        vida = vida - dano

#Subclase Francotirador
class Francotirador(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, vida = 3, enfriamiento = 0)
        self.dano = 3

    #Metodo para ejecutar la habilidad del francotirador
    def disparar(self):
        vida = vida - dano

'''        
jugar = Jugador('nombre')
jugar.crear_equipo('nombre')
jugar.realizar_accion()
'''