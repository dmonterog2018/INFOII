from utils import validar_celda_contigua
from utils import validar_celda
from utils import comprobar_celda_disponible
class Personajes:
    def __init__(self, vida_maxima, vida_actual, dano, posicion,enfriamiento, equipo):
        self.vida_maxima = vida_maxima
        self.vida_actual = vida_actual
        self.dano = dano
        self.posicion = posicion  # Posicion que ocupa en el tablero
        self.enfriamiento = enfriamiento
        self.equipo = equipo

    def mover(self, celda_nueva, equipo):
        print('Aqui no entra')


        '''for i in equipo:
            for b in i.values():
                print(i.values())
                if celda not in b:
                    if validar_celda_contigua(b, celda):
                        print(f'Te moviste a la celda{celda}')
                        return True
                    else:
                        print(f'La celda{celda} no es contigua.')
                        return False
                else:
                    print('¡La celda que has introducido es la misma!')
                    return False'''



class medico(Personajes):
    vida_maxima = 1
    vida_actual = 1
    dano = 0
    posicion = ''  # Posicion que ocupa en el tablero
    enfriamiento_restante = 0
    equipo = []

    # Este metodo se utiliza para mover el personaje durante el turno

    # Este metodo se utiliza para ejecutrar la habilidad de un personaje
    def habilidad(self,nombre, equipo):
        for i in equipo:
            for v in i.values():
                if v == nombre:
                    pass
        return

    def mover(self, celda_nueva, equipo):

        if validar_celda(celda_nueva, 'd',4):
            if comprobar_celda_disponible(celda_nueva, equipo):
                if validar_celda_contigua(self.posicion,celda_nueva):
                    self.posicion = celda_nueva
                    equipo[0]['medico'] = self.posicion


# Personaje inteligencia (no militar)
class inteligencia(Personajes):
    vida_maxima = 2
    vida_actual = 2
    dano = 0
    posicion = ''  # Posicion que ocupa en el tablero
    enfriamiento_restante = 0

    # equipo = list[] Comentado porque no sabemos como utilizarlo de momento
    # Este metodo se utiliza para ejecutrar la habilidad de un personaje
    def habilidad(self):
        return

    def mover(self, celda_nueva, equipo):

        if validar_celda(celda_nueva, 'd',4):
            if comprobar_celda_disponible(celda_nueva, equipo):
                if validar_celda_contigua(self.posicion,celda_nueva):
                    self.posicion = celda_nueva
                    equipo[0]['inteligencia'] = self.posicion


# Personaje artillero (militar)
class artillero(Personajes):
    vida_maxima = 2
    vida_actual = 2
    dano = 1
    posicion = ''  # Posicion que ocupa en el tablero
    enfriamiento_restante = 0

    # equipo = list[] Comentado porque no sabemos como utilizarlo de momento

    # Este metodo se utiliza para ejecutrar la habilidad de un personaje
    def habilidad(self):
        return

    def mover(self, celda_nueva, equipo):

        if validar_celda(celda_nueva, 'd',4):
            if comprobar_celda_disponible(celda_nueva, equipo):
                if validar_celda_contigua(self.posicion,celda_nueva):
                    self.posicion = celda_nueva
                    equipo[0]['artillero'] = self.posicion


# Personaje francotirador (militar)
class francotirador(Personajes):
    vida_maxima = 3
    vida_actual = 3
    dano = 3
    posicion = ''  # Posicion que ocupa en el tablero
    enfriamiento_restante = 0

    # equipo = list[] Comentado porque no sabemos como utilizarlo de momento

    # Este metodo se utiliza para ejecutrar la habilidad de un personaje
    def habilidad(self):
        return

    def mover(self, celda_nueva, equipo):

        if validar_celda(celda_nueva, 'd',4):
            if comprobar_celda_disponible(celda_nueva, equipo):
                if validar_celda_contigua(self.posicion,celda_nueva):
                    self.posicion = celda_nueva
                    equipo[0]['francotirador'] = self.posicion