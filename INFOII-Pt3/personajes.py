from utils import validar_celda_contigua, comprobar_celda_disponible, validar_celda

# Creamos la clase personaje (Clase Base)
class Personajes:
    def __init__(self, vida_maxima, vida_actual, dano, posicion, enfriamiento):
        # Asignamos los valores a los atributos
        self.vida_maxima = vida_maxima  # Inicializamos la vida maxima de los personajes
        self.vida_actual = vida_actual  # Inicializamos la vida actual de los personajes
        self.dano = dano  # Inicializamos el daño a los personajes (militares)
        self.posicion = posicion  ##Inicializamos la posicion
        self.enfriamiento = enfriamiento  # Inicializamos el enfriamiento de las habilidades


# Personaje Medico (no militar) (Subclase)
class medico(Personajes):
    def __init__(self, vida_maxima, vida_actual, dano, posicion, enfriamiento):
        super().__init__(vida_maxima, vida_actual, dano, posicion,
                         enfriamiento)  # Inicializar los parametros de la Clase Base

    # Habilidad del medico, curar a un personaje de tu equipo
    def habilidad(self, celda_curar, equipo):
        if self.vida_actual > 0:  # Comprobar que el medico esta vivo
            if validar_celda(celda_curar, 'd', 4):  # Validar que la celda que intentamos curar esta dentro del tablero
                if comprobar_celda_disponible(celda_curar,
                                              equipo) == False:  # Comprobamos que la celda esta ocupada por un miembre de nuestro equipo
                    for miembro in equipo:  # Recorremos la lista equipo
                        for validar in miembro.values():  # Recorremos los valores del diccionario de la lista equipo
                            if validar == celda_curar:  # Comprobamos si el valor actual de validar es igual a celda_curar
                                if miembro['vida actual'] < miembro['vida maxima'] and miembro[
                                    'vida actual'] > 0:  # Comprobamos que el personaje que queremos curar esta vivo y su vida es menor a su vida maxima
                                    miembro['vida actual'] = miembro[
                                        'vida maxima']  # Si la condicion se cumple, igualamos su vida actual al valor de vida_maxima
                                    return True
                                else:  # Si la condicion no se cumple, el personaje esta muerto o tiene su vida maxima
                                    print('El miembro que intentas curar esta muerto o tiene su maxima vida')
                                    return False
                            else:
                                pass
                else:  # Si la celda no esta ocupada por nadie
                    print('La celda que has indicado no hay nadie...')
                    return False
        else:  # La vida del medico es inferior a 1
            print('No puedes usar la habilidad porque el medico esta muerto')
            return False

    # Mover la posicion del medico
    def mover(self, celda_nueva, equipo):
        if validar_celda(celda_nueva, 'd',
                         4):  # Validar que la celda a la que intentamos movernos esta dentro del tablero
            if comprobar_celda_disponible(celda_nueva, equipo):  # Comprobamos que la celda no esta ocupada
                if validar_celda_contigua(self.posicion,
                                          celda_nueva):  # Comprobamosque la celda a la que intentamos movernos es adyacente
                    self.posicion = celda_nueva  # Guardamos el valor de la nueva celda
                    equipo[0]['posicion'] = self.posicion  # Actualizamos la posicion dentro de la lista
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False


# Personaje Inteligencia (no militar) (Subclase)
class inteligencia(Personajes):
    def __init__(self, vida_maxima, vida_actual, dano, posicion, enfriamiento):
        super().__init__(vida_maxima, vida_actual, dano, posicion,
                         enfriamiento)  # Inicializar los parametros de la Clase Base

    # Habilidad de inteligencia, descubrir un area del tablero enemigo
    def habilidad(self, celda_marcada, equipo):
        if validar_celda(celda_marcada, 'd', 4):  # Validar que la celda que intentamos ver esta dentro del tablero
            print(f'La inteligencia esta rastreando en la celda: {celda_marcada}...')
            return True

    # Mover la posicion de inteligencia
    def mover(self, celda_nueva, equipo):
        if validar_celda(celda_nueva, 'd',
                         4):  # Validar que la celda a la que intentamos movernos esta dentro del tablero
            if comprobar_celda_disponible(celda_nueva, equipo):  # Comprobamos que la celda no esta ocupada
                if validar_celda_contigua(self.posicion,
                                          celda_nueva):  # Comprobamosque la celda a la que intentamos movernos es adyacente
                    self.posicion = celda_nueva  # Guardamos el valor de la nueva celda
                    equipo[3]['posicion'] = self.posicion  # Actualizamos la posicion dentro de la lista
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False


# Personaje Artillero (militar) (Subclase)
class artillero(Personajes):
    def __init__(self, vida_maxima, vida_actual, dano, posicion, enfriamiento):
        super().__init__(vida_maxima, vida_actual, dano, posicion,
                         enfriamiento)  # Inicializar los parametros de la Clase Base

    # Habilidad de artillero, inflingir un daño en un area al tablero enemigo
    def habilidad(self, celda_marcada, equipo):
        if validar_celda(celda_marcada, 'd', 4):  # Validar que la celda que intentamos atacar esta dentro del tablero
            print(f'Se ha ejecutado el ataque a la celda: {celda_marcada}')
            return True

    # Mover la posicion del artillero
    def mover(self, celda_nueva, equipo):
        if validar_celda(celda_nueva, 'd',
                         4):  # Validar que la celda a la que intentamos movernos esta dentro del tablero
            if comprobar_celda_disponible(celda_nueva, equipo):  # Comprobamos que la celda no esta ocupada
                if validar_celda_contigua(self.posicion,
                                          celda_nueva):  # Comprobamosque la celda a la que intentamos movernos es adyacente
                    self.posicion = celda_nueva  # Guardamos el valor de la nueva celda
                    equipo[1]['posicion'] = self.posicion  # Actualizamos la posicion dentro de la lista
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False


# Personaje Francotirador (militar) (Subclase)
class francotirador(Personajes):
    def __init__(self, vida_maxima, vida_actual, dano, posicion, enfriamiento):
        super().__init__(vida_maxima, vida_actual, dano, posicion,
                         enfriamiento)  # Inicializar los parametros de la Clase Base

    # Habilidad del francotiraodr, matar a un personaje del tablero enemigo
    def habilidad(self, celda_atacar, equipo):
        if equipo[2]['vida actual'] > 0:  # Comprobar que el personaje esta vivo
            if equipo[2]['enfriamiento'] == 0:  # Comrpobar que la habilidad no esta en enfriamiento
                if validar_celda(celda_atacar, 'd',
                                 4):  # Validar que la celda que intentamos atacar esta dentro del tablero
                    print(f'Se ha ejecutado el ataque a la celda: {celda_atacar}')
                    return True
            else:  # La habilidad esta en enfriamiento
                print('Ya usaste esta habilidad')
                return False
        else:  # El francotirador esta muerto
            print('Tu francotirador esta muerto, no puedes hacer eso')

    # Mover la posicion del francotirador
    def mover(self, celda_nueva, equipo):
        if validar_celda(celda_nueva, 'd',
                         4):  # Validar que la celda a la que intentamos movernos esta dentro del tablero
            if comprobar_celda_disponible(celda_nueva, equipo):  # Comprobamos que la celda no esta ocupada
                if validar_celda_contigua(self.posicion,
                                          celda_nueva):  # Comprobamosque la celda a la que intentamos movernos es adyacente
                    self.posicion = celda_nueva  # Guardamos el valor de la nueva celda
                    equipo[2]['posicion'] = self.posicion  # Actualizamos la posicion dentro de la lista
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False