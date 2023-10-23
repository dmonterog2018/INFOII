from utils import validar_celda_contigua
from utils import validar_celda
from utils import comprobar_celda_disponible
class Personajes:
    def __init__(self, vida_maxima, vida_actual, dano, posicion,enfriamiento):
        self.vida_maxima = vida_maxima
        self.vida_actual = vida_actual
        self.dano = dano
        self.posicion = posicion
        self.enfriamiento = enfriamiento


    def mover(self, celda_nueva, equipo):

        print('Aqui no entra')



class medico(Personajes):
    def __init__(self, vida_maxima, vida_actual, dano, posicion, enfriamiento):
        super().__init__(vida_maxima,vida_actual,dano,posicion,enfriamiento)

    def habilidad(self,celda_curar, equipo):

        if self.vida_actual > 0:
            if validar_celda(celda_curar,'d',4):
                if comprobar_celda_disponible(celda_curar,equipo) == False:
                    for miembro in equipo:
                        for validar in miembro.values():
                            if validar == celda_curar:
                                if miembro['vida actual'] < miembro['vida maxima'] and miembro['vida actual'] > 0:
                                    miembro['vida actual'] = miembro['vida maxima']
                                    return True
                                else:
                                    print('El miembro que intentas curar esta muerto o tiene su maxima vida')
                                    return False
                            else:
                                pass
                else:
                    print('La celda que has indicado no hay nadie...')
                    return False
        else:
            print('No puedes usar la habilidad porque el medico esta muerto')
            return False




    def mover(self, celda_nueva, equipo):

        if validar_celda(celda_nueva, 'd',4):
            if comprobar_celda_disponible(celda_nueva, equipo):
                if validar_celda_contigua(self.posicion,celda_nueva):
                    self.posicion = celda_nueva
                    equipo[0]['posicion'] = self.posicion
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False



# Personaje inteligencia (no militar)
class inteligencia(Personajes):
    def __init__(self, vida_maxima, vida_actual, dano, posicion, enfriamiento):
        super().__init__(vida_maxima,vida_actual,dano,posicion,enfriamiento)


    def habilidad(self, celda_marcada, equipo):
        if validar_celda(celda_marcada, 'd', 4):
                print(f'La inteligencia esta rastreando en la celda: {celda_marcada}...')
                equipo[3]['enfriamiento'] = 1
                return True
    def mover(self, celda_nueva, equipo):

        if validar_celda(celda_nueva, 'd',4):
            if comprobar_celda_disponible(celda_nueva, equipo):
                if validar_celda_contigua(self.posicion,celda_nueva):
                    self.posicion = celda_nueva
                    equipo[3]['posicion'] = self.posicion
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False


# Personaje artillero (militar)
class artillero(Personajes):

    def __init__(self, vida_maxima, vida_actual, dano, posicion, enfriamiento):
        super().__init__(vida_maxima,vida_actual,dano,posicion,enfriamiento)

    def habilidad(self, celda_marcada, equipo):
        if validar_celda(celda_marcada, 'd', 4):
                print(f'Se ha ejecutado el ataque a la celda: {celda_marcada}')
                equipo[1]['enfriamiento'] = 1
                return True

    def mover(self, celda_nueva, equipo):

        if validar_celda(celda_nueva, 'd',4):
            if comprobar_celda_disponible(celda_nueva, equipo):
                if validar_celda_contigua(self.posicion,celda_nueva):
                    self.posicion = celda_nueva
                    equipo[1]['posicion'] = self.posicion
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False


# Personaje francotirador (militar)
class francotirador(Personajes):

    def __init__(self, vida_maxima, vida_actual, dano, posicion, enfriamiento):
        super().__init__(vida_maxima,vida_actual,dano,posicion,enfriamiento)

    def habilidad(self,celda_atacar, equipo):
        if equipo[2]['vida actual'] > 0:
            if equipo[2]['enfriamiento'] == 0:
                if validar_celda(celda_atacar, 'd', 4):
                    print(f'Se ha ejecutado el ataque a la celda: {celda_atacar}')
                    equipo[2]['enfriamiento'] = 1
                    return True

            else:
                print('Ya usaste esta habilidad')
                return False
        else:
            print('Tu francotirador esta muerto, no puedes hacer eso')


    def mover(self, celda_nueva, equipo):

        if validar_celda(celda_nueva, 'd',4):
            if comprobar_celda_disponible(celda_nueva, equipo):
                if validar_celda_contigua(self.posicion,celda_nueva):
                    self.posicion = celda_nueva
                    equipo[2]['posicion'] = self.posicion
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False