#Script para definir los personajes

#Personaje medico (no militar)
class medico:
    vida_maxima = 1
    vida_actual = 1
    dano = 0
    posicion = '' #Posicion que ocupa en el tablero
    enfriamiento_restante = 0
    #equipo = list[] Comentado porque no sabemos como utilizarlo de momento

    #Este metodo se utiliza para mover el personaje durante el turno
    def mover():
        return
    
    #Este metodo se utiliza para ejecutrar la habilidad de un personaje
    def habilidad():
        return

#Personaje inteligencia (no militar)
class inteligencia:
    vida_maxima = 2
    vida_actual = 2
    dano = 0
    posicion = '' #Posicion que ocupa en el tablero
    enfriamiento_restante = 0
    #equipo = list[] Comentado porque no sabemos como utilizarlo de momento

    #Este metodo se utiliza para mover el personaje durante el turno
    def mover():
        return
    
    #Este metodo se utiliza para ejecutrar la habilidad de un personaje
    def habilidad():
        return

#Personaje artillero (militar)
class artillero:
    vida_maxima = 2
    vida_actual = 2
    dano = 1
    posicion = '' #Posicion que ocupa en el tablero
    enfriamiento_restante = 0
    #equipo = list[] Comentado porque no sabemos como utilizarlo de momento

    #Este metodo se utiliza para mover el personaje durante el turno
    def mover():
        return
    
    #Este metodo se utiliza para ejecutrar la habilidad de un personaje
    def habilidad():
        return

#Personaje francotirador (militar)
class francotirador:
    vida_maxima = 3
    vida_actual = 3
    dano = 3
    posicion = '' #Posicion que ocupa en el tablero
    enfriamiento_restante = 0
    #equipo = list[] Comentado porque no sabemos como utilizarlo de momento

    #Este metodo se utiliza para mover el personaje durante el turno
    def mover():
        return
    
    #Este metodo se utiliza para ejecutrar la habilidad de un personaje
    def habilidad():
        return