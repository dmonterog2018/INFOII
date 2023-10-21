from utils import validar_celda
from utils import comprobar_celda_disponible
from personajes import medico
from personajes import artillero
from personajes import francotirador
from personajes import inteligencia


max_col = 'd'
max_row = 4

# Creamos las clases jugador y personajes.

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.oponente = None
        self.equipo = []
        self.turno_end = False
        self.informe = []
        self.medico_instancia = None   #   PREGUNTAR AL PROFE PORQUE LA ISNTANCIA ASI NO FUNCIONA
        self.turno = []

    def crear_equipo(self,nombre):

        # CREAMOS EL MEDICO CON SUS CARACTERISTICAS
        medico_instancia = medico(1,1, 0,'',0)  #Instanciamos los valores que tiene el medico al inicializar el juego.
        dicc_medico = {'nombre': 'medico', 'vida maxima': medico_instancia.vida_maxima, 'vida actual': medico_instancia.vida_actual, 'dano': medico_instancia.dano,
                       'posicion': medico_instancia.posicion, 'enfriamiento': medico_instancia.enfriamiento}
        self.equipo.append(dicc_medico)   #  Guardamos todos los  valores en un diccionario dentro de la lista

        # CREAMOS EL ARTILLERO CON SUS CARACTERISTICAS

        artillero_instancia = artillero(2, 2, 1, '', 0)
        dicc_artillero = {'nombre': 'artillero', 'vida maxima': artillero_instancia.vida_maxima,
                       'vida actual': artillero_instancia.vida_actual, 'dano': artillero_instancia.dano,
                       'posicion': artillero_instancia.posicion, 'enfriamiento': artillero_instancia.enfriamiento}
        self.equipo.append(dicc_artillero)

        # CREAMOS EL FRANCOTIRADOR CON SUS CARACTERISTICAS

        francotirador_instancia = francotirador(3, 3, 3, '', 0)
        dicc_francotirador = {'nombre': 'francotirador', 'vida maxima': francotirador_instancia.vida_maxima,
                          'vida actual': francotirador_instancia.vida_actual, 'dano': francotirador_instancia.dano,
                          'posicion': francotirador_instancia.posicion, 'enfriamiento': francotirador_instancia.enfriamiento}
        self.equipo.append(dicc_francotirador)

        # CREAMOS EL INTELIGENCIA CON SUS CARACTERISTICAS

        inteligencia_instancia = inteligencia(2, 2, 0, '', 0)
        dicc_inteligencia = {'nombre': 'inteligencia', 'vida maxima': inteligencia_instancia.vida_maxima,
                              'vida actual': inteligencia_instancia.vida_actual, 'dano': inteligencia_instancia.dano,
                              'posicion': inteligencia_instancia.posicion,
                              'enfriamiento': inteligencia_instancia.enfriamiento}
        self.equipo.append(dicc_inteligencia)

    def posicionar_equipo(self, nombre):

        while True:
            celda_medico = input('Indica la celda (A-D, 1-4. p.ej: B2) en la que posicionar al Medico: ')
            if validar_celda(celda_medico, max_col, max_row) == True:
                if comprobar_celda_disponible(celda_medico,self.equipo) == True:
                    self.equipo[0]['posicion'] = celda_medico
                    break

        while True:
            celda_artillero = input('Indica la celda (A-D, 1-4. p.ej: B2) en la que posicionar al Artillero: ')
            if validar_celda(celda_artillero, max_col, max_row) == True:
                if comprobar_celda_disponible(celda_artillero, self.equipo) == True:
                    self.equipo[1]['posicion'] = celda_artillero
                    break

        while True:
            celda_francotirador = input('Indica la celda (A-D, 1-4. p.ej: B2) en la que posicionar al Francotirador: ')
            if validar_celda(celda_francotirador, max_col, max_row) == True:
                if comprobar_celda_disponible(celda_francotirador, self.equipo) == True:
                    self.equipo[2]['posicion'] = celda_francotirador
                    break

        while True:
            celda_inteligencia = input('Indica la celda (A-D, 1-4. p.ej: B2) en la que posicionar al Inteligencia: ')
            if validar_celda(celda_inteligencia, max_col, max_row) == True:
                if comprobar_celda_disponible(celda_inteligencia, self.equipo) == True:
                    self.equipo[3]['posicion'] = celda_inteligencia
                    print(self.equipo)
                    break

    def recibir_accion(self, tipo,celda_afectada):

        if tipo == 'f':
            print(self.oponente.equipo)
            for miembro in self.oponente.equipo:
                if miembro['posicion'] == celda_afectada:
                    miembro['vida actual'] = 0
                    print('-----> RESULTADO DE LA ACCIÓN <-----')
                    print(f"El {miembro['nombre']} ha muerto en la celda: {celda_afectada}")
                    self.oponente.turno.append(f"Tu {miembro['nombre']} ha muerto :(")
                else:
                    pass
    def realizar_accion(self):

        print('-----> 1. Mover (Medico) <-----')
        print('-----> 2. Mover (Artillero) <-----')
        print('-----> 3. Mover (Francotirador) <-----')
        print('-----> 4. Mover (Inteligencia) <-----')
        print('-----> 5. Habilidad (Medico) <-----')
        print('-----> 6. Habilidad (Artillero) <-----')
        print('-----> 7. Habilidad (Francotirador) <-----')
        print('-----> 8. Habilidad (Inteligencia) <-----')

        while True:
            try:
                acc = input('Seleccione una acción: ')
                int(acc)
                if int(acc) <= 8:
                    if int(acc) == 1:
                        while True:
                            celda_nuevo = input('Introduce la celda a la que quiere mover el personaje: ')
                            medico1 = self.equipo[0]
                            medico_instancia = medico(medico1['vida maxima'], medico1['vida actual'], medico1['dano'],
                                                      medico1['posicion'],medico1['enfriamiento'])
                            if medico_instancia.mover(celda_nuevo, self.equipo) == True:
                                return True

                    elif int(acc) == 2:
                        while True:
                            celda_nuevo = input('Introduce la celda a la que quiere mover el personaje: ')
                            artillero1 = self.equipo[1]
                            artillero_instancia = artillero(artillero1['vida maxima'], artillero1['vida actual'],
                                                            artillero1['dano'], artillero1['posicion'], artillero1['enfriamiento'])
                            if artillero_instancia.mover(celda_nuevo, self.equipo) == True:
                                return True

                    elif int(acc) == 3:
                        while True:
                            celda_nuevo = input('Introduce la celda a la que quiere mover el personaje: ')
                            francotirador1 = self.equipo[2]
                            francotirador_instancia = francotirador(francotirador1['vida maxima'], francotirador1['vida actual'],
                                                                    francotirador1['dano'], francotirador1['posicion'], francotirador1['enfriamiento'])
                            if francotirador_instancia.mover(celda_nuevo, self.equipo) == True:
                                return True
                    elif int(acc) == 4:
                        while True:
                            celda_nuevo = input('Introduce la celda a la que quiere mover el personaje: ')
                            inteligencia1 = self.equipo[3]
                            inteligencia_instancia = inteligencia(inteligencia1['vida maxima'], inteligencia1['vida actual'],
                                                                    inteligencia1['dano'], inteligencia1['posicion'], inteligencia1['enfriamiento'])
                            if inteligencia_instancia.mover(celda_nuevo, self.equipo) == True:
                                return True

                    elif int(acc) == 5:
                        while True:
                            celda_curar = input('Introduce la celda donde se encuentre el personaje que quieras curar: ')
                            medico1 = self.equipo[0]
                            medico_instancia = medico(medico1['vida maxima'], medico1['vida actual'], medico1['dano'],
                                                      medico1['posicion'], medico1['enfriamiento'])
                            if medico_instancia.habilidad(celda_curar, self.equipo) == True:
                                for elemento in self.equipo:
                                    if elemento['enfriamiento'] == 0:
                                        if elemento['posicion'] == celda_curar:
                                            personaje_a_curar = elemento['nombre']
                                            self.turno.append(f'Se ha curado el {personaje_a_curar} de la celda: {celda_curar}')
                                            return True
                                    else:
                                        print('El enfriamiento esta activado para este turno, prueba en el sigueinte')
                                        break
                                break
                    elif int(acc) == 6:
                        while True:
                            celda_atacar = input('Introduce la celda a la que quieres atacar: ')
                            francotirador1 = self.equipo[2]
                            francotirador_instancia = francotirador(francotirador1['vida maxima'],francotirador1['vida actual'],francotirador1['dano'], francotirador1['posicion'],
                                                                    francotirador1['enfriamiento'])
                            if francotirador_instancia.habilidad(celda_atacar, self.equipo):
                                self.recibir_accion('f',celda_atacar)
                                return True

                    elif int(acc) == 7:
                        pass
                    elif int(acc) == 8:
                        pass
                else:
                    print('El numero introducido no es correcto')
            except ValueError:
                print('Mal formato')


    def informe1(self):

        print('-----> INFORME <-----')
        for p in self.turno:
            print(p)
        self.turno.clear()
        print('<------------------------------>')

        print('-----> SITUACIÓN DEL EQUIPO <-----')
        for elemento in self.equipo:
            if elemento['vida actual'] > 0:
                print(f"{elemento['nombre'].upper()} --> Posicion: {elemento['posicion'].upper()} --> [Vidas {elemento['vida actual']}/{elemento['vida maxima']}]")
        print('<------------------------------>')

    def turno(self) -> bool:
        if self.turno_end:
            return True
        else:

            return False
    def set_oponente(self,oponente):
        self.oponente = oponente
        return self.oponente

'''jugar = Jugador('Nombre')
jugar.crear_equipo(jugar)
jugar.posicionar_equipo(jugar)
jugar.realizar_accion()
jugar.informe1()'''

