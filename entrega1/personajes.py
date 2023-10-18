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
    def __init__(self, vida_maxima, vida_actual, dano, posicion, enfriamiento):
        super().__init__(vida_maxima,vida_actual,dano,posicion,enfriamiento)

    def habilidad(self,celda_curar, equipo):
        if self.vida_actual > 0:
            if validar_celda(celda_curar,'d',4):
                pass


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


    def habilidad(self):
        return
    def mover(self, celda_nueva, equipo):

        if validar_celda(celda_nueva, 'd',4):
            if comprobar_celda_disponible(celda_nueva, equipo):
                if validar_celda_contigua(self.posicion,celda_nueva):
                    self.posicion = celda_nueva
                    equipo[3]['inteligencia'] = self.posicion
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

    def habilidad(self):
        return

    def mover(self, celda_nueva, equipo):

        if validar_celda(celda_nueva, 'd',4):
            if comprobar_celda_disponible(celda_nueva, equipo):
                if validar_celda_contigua(self.posicion,celda_nueva):
                    self.posicion = celda_nueva
                    equipo[1]['artillero'] = self.posicion
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

    def habilidad(self):
        return

    def mover(self, celda_nueva, equipo):

        if validar_celda(celda_nueva, 'd',4):
            if comprobar_celda_disponible(celda_nueva, equipo):
                if validar_celda_contigua(self.posicion,celda_nueva):
                    self.posicion = celda_nueva
                    equipo[2]['francotirador'] = self.posicion
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False