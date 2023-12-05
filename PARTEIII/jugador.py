from utils import validar_celda, comprobar_celda_disponible
from personajes import medico, artillero, francotirador, inteligencia

max_col = 'd'  # Columna
max_row = 4  # Fila


# Creamos la clase Jugador (Clase Base)
class Jugador:
    def __init__(self):
        # Inicializamos los valores a los atributos
        self.oponente = None  # Inicializamos el oponente
        self.equipo = []  # Inicializamos una lista vacia para el equipo
        self.turno_end = False  # Inicializamos el turno
        self.turno = []  # Inicializamos una lista vacia para el turno

    # Funcion para crear el equipo con sus caracteristicas
    def crear_equipo(self):
        # Creamos el Medico con sus caracteristicas
        medico_instancia = medico(1, 1, 0, '', 0)  # vida_maxima, vida_actual, dano, posicion, enfriamiento
        # Instanciamos los valores que tiene el Medico al inicializar el juego.
        dicc_medico = {'nombre': 'medico', 'vida maxima': medico_instancia.vida_maxima,
                       'vida actual': medico_instancia.vida_actual, 'dano': medico_instancia.dano,
                       'posicion': medico_instancia.posicion, 'enfriamiento': medico_instancia.enfriamiento}
        self.equipo.append(dicc_medico)  # Guardamos los valores del medico en un diccionario dentro de la lista

        # Creamos el Artillero con sus caracteristicas
        artillero_instancia = artillero(2, 2, 1, '', 0)  # vida_maxima, vida_actual, dano, posicion, enfriamiento
        # Instanciamos los valores que tiene el Artillero al inicializar el juego.
        dicc_artillero = {'nombre': 'artillero', 'vida maxima': artillero_instancia.vida_maxima,
                          'vida actual': artillero_instancia.vida_actual, 'dano': artillero_instancia.dano,
                          'posicion': artillero_instancia.posicion, 'enfriamiento': artillero_instancia.enfriamiento}
        self.equipo.append(dicc_artillero)  # Guardamos los valores del artillero en un diccionario dentro de la lista

        # Creamos el Francotirador con sus caracterisrticas
        francotirador_instancia = francotirador(3, 3, 3, '',
                                                0)  # vida_maxima, vida_actual, dano, posicion, enfriamiento
        # Instanciamos los valores que tiene el Francotirador al inicializar el juego.
        dicc_francotirador = {'nombre': 'francotirador', 'vida maxima': francotirador_instancia.vida_maxima,
                              'vida actual': francotirador_instancia.vida_actual, 'dano': francotirador_instancia.dano,
                              'posicion': francotirador_instancia.posicion,
                              'enfriamiento': francotirador_instancia.enfriamiento}
        self.equipo.append(
            dicc_francotirador)  # Guardamos los valores del francotirador en un diccionario dentro de la lista

        # Creamos Inteligencia con sus caracteristicas
        inteligencia_instancia = inteligencia(2, 2, 0, '', 0)  # vida_maxima, vida_actual, dano, posicion, enfriamiento
        # Instanciamos los valores que tiene Inteligencia al inicializar el juego.
        dicc_inteligencia = {'nombre': 'inteligencia', 'vida maxima': inteligencia_instancia.vida_maxima,
                             'vida actual': inteligencia_instancia.vida_actual, 'dano': inteligencia_instancia.dano,
                             'posicion': inteligencia_instancia.posicion,
                             'enfriamiento': inteligencia_instancia.enfriamiento}
        self.equipo.append(
            dicc_inteligencia)  # Guardamos los valores de inteligencia en un diccionario dentro de la lista

    # Funcion para posicionar cada miembro del equipo en una celda
    def posicionar_equipo(self):
        # Medico
        while True:
            celda_medico = input('Indica la celda (A-D, 1-4. p.ej: B2) en la que posicionar al Medico: ').lower()
            if validar_celda(celda_medico, max_col, max_row) == True:  # Validar que la celda esta dentro del tablero
                if comprobar_celda_disponible(celda_medico,
                                              self.equipo) == True:  # Comprobamos que la celda no esta ocupada
                    self.equipo[0]['posicion'] = celda_medico  # Guardamos la posicion dentro de la lista
                    break

        # Artillero
        while True:
            celda_artillero = input('Indica la celda (A-D, 1-4. p.ej: B2) en la que posicionar al Artillero: ').lower()
            if validar_celda(celda_artillero, max_col, max_row) == True:  # Validar que la celda esta dentro del tablero
                if comprobar_celda_disponible(celda_artillero,
                                              self.equipo) == True:  # Comprobamos que la celda no esta ocupada
                    self.equipo[1]['posicion'] = celda_artillero  # Guardamos la posicion dentro de la lista
                    break

        # Francotirador
        while True:
            celda_francotirador = input(
                'Indica la celda (A-D, 1-4. p.ej: B2) en la que posicionar al Francotirador: ').lower()
            if validar_celda(celda_francotirador, max_col,
                             max_row) == True:  # Validar que la celda esta dentro del tablero
                if comprobar_celda_disponible(celda_francotirador,
                                              self.equipo) == True:  # Comprobamos que la celda no esta ocupada
                    self.equipo[2]['posicion'] = celda_francotirador  # Guardamos la posicion dentro de la lista
                    break

        # Inteligencia
        while True:
            celda_inteligencia = input(
                'Indica la celda (A-D, 1-4. p.ej: B2) en la que posicionar al Inteligencia: ').lower()
            if validar_celda(celda_inteligencia, max_col,
                             max_row) == True:  # Validar que la celda esta dentro del tablero
                if comprobar_celda_disponible(celda_inteligencia,
                                              self.equipo) == True:  # Comprobamos que la celda no esta ocupada
                    self.equipo[3]['posicion'] = celda_inteligencia  # Guardamos la posicion dentro de la lista
                    break

    # Funcion para calcular las celdas en un area
    def calculo_celdas(self, celda_usuario, max_col, max_row):
        col_usuario = ord(celda_usuario[0]) - ord('a')  # Sacar valor numerico de la columna
        row_usuario = int(celda_usuario[1])  # Sacar valor numerico de la fila

        celdas_contiguas = []  # Lista vacia para almacenar las celdas contiguas

        for row in range(row_usuario, min(row_usuario + 2, max_row + 1)):  # Recorremos las filas
            for col in range(col_usuario,
                             min(col_usuario + 2, ord(max_col.lower()) - ord('a') + 1)):  # Recorremos las columnas
                celdas_contiguas.append(chr(col + ord('a')) + str(row))  # Almacenamos en la lista los celdas contiguas
        return celdas_contiguas

    # Funcion que recibe la accion ejecutada por el oponente
    def recibir_accion(self, tipo, celda_afectada):
        print('-----> INFORME <-----')
        self.turno.append(f"-----> RESULTADO DE LA ACCIÓN <-----\n")
        if tipo == 'f':  # Si el tipo es Francotirador
            for miembro in self.equipo:  # Recorremos la lista equipo enemigo
                if miembro[
                    'posicion'] == celda_afectada:  # Comprobamos si en la casilla afectada se encuentra un miembro del equipo
                    miembro['vida actual'] = miembro['vida actual'] - self.equipo[2][
                        'dano']  # Modificamos la vida del personaje con el daño del francotirador
                    print(f"Tu {miembro['nombre']} ha muerto :(")
                    self.turno.append(f"El {miembro['nombre']} ha muerto en la celda: {celda_afectada}")  # Añadimos al informe que el personaje afectado a muerto
                else:
                    pass

        elif tipo == 'a':  # Si el tipo es Artillero

            afectados = self.calculo_celdas(celda_afectada, max_col,
                                            max_row)  # Calculamos el area que va a ser afectada en el tablero
            for miembro in self.equipo:  # Recorremos la lista equipo enemigo
                for i in afectados:  # Recorremos una lista con las casilas afectadas
                    if miembro['posicion'] == i:  # Comprobamos si hay algun personaje en las casillas
                        if miembro['vida actual'] > 0:  # Comprobamos que el personaje este vivo
                            miembro['vida actual'] = miembro['vida actual'] - self.equipo[1][
                                'dano']  # Modificamos la vida del personaje con el daño del artillero
                            print(f"El {miembro['nombre']} ha sido herido en la celda: {miembro['posicion']} ---> VIDAS[{miembro['vida actual']}/{miembro['vida maxima']}]")
                            # Añadimos al informe el personaje afectado con la celda y la vida actual comparada con la vida maxima
                            self.turno.append(f"El {miembro['nombre']} ha sido herido en la celda: {miembro['posicion'].upper()}")
                        else:
                            print(f"El {miembro['nombre']} ya estaba muerto :(")
                    else:
                        pass

        elif tipo == 'i':  # Si el tipo es Inteligencia
            afectados = self.calculo_celdas(celda_afectada, max_col,
                                            max_row)  # Calculamos el area que va a ser afectada en el tablero
            for miembro in self.equipo:  # Recorremos la lista equipo enemigo
                for i in afectados:  # Recorremos una lista con las casilas afectadas
                    if miembro['posicion'] == i:  # Comprobamos si hay algun personaje en las casillas
                        if miembro['vida actual'] > 0:  # Comprobamos que el personaje este vivo
                            print(f"Tu {miembro['nombre']} ha sido avistado en la celda: {miembro['posicion']}")
                            # Añadimos al informe el personaje afectado con la celda en la que se encuentra
                            self.turno.append(
                                f"El {miembro['nombre']} ha sido avistado en la celda: {miembro['posicion'].upper()}")
                        else:
                            print(f"El {miembro['nombre']} ya estaba muerto :(")
                    else:
                        pass

    # Funcion para elegir la accion a realizar
    def realizar_accion(self):
        # Menu con las acciones a realizar
        if self.equipo[0]['vida actual'] > 0:  # Comprueba si el medico esta vivo
            print('-----> 1. Mover (Medico) <-----')
        if self.equipo[1]['vida actual'] > 0:  # Comprueba si el artillero esta vivo
            print('-----> 2. Mover (Artillero) <-----')
        if self.equipo[2]['vida actual'] > 0:  # Comprueba si el francotirador esta vivo
            print('-----> 3. Mover (Francotirador) <-----')
        if self.equipo[3]['vida actual'] > 0:  # Comprueba si inteligencia esta vivo
            print('-----> 4. Mover (Inteligencia) <-----')
        if self.equipo[0]['vida actual'] > 0 and self.equipo[0][
            'enfriamiento'] == 0:  # Comprueba si el medico esta vivo y si se puede utilizar su habilidad
            for miembro in self.equipo:  # Recorremos la lista equipo
                if miembro['vida actual'] < miembro['vida maxima'] and miembro[
                    'vida actual'] != 0:  # Comprueba si se puede curar a alguno de los personajes
                    print('-----> 5. Habilidad (Medico) <-----')
                    break
        if self.equipo[1]['vida actual'] > 0 and self.equipo[1][
            'enfriamiento'] == 0:  # Comprueba si el artillero esta vivo y si se puede utilizar su habilidad
            print('-----> 6. Habilidad (Artillero) <-----')
        if self.equipo[2]['vida actual'] > 0 and self.equipo[2][
            'enfriamiento'] == 0:  # Comprueba si el francotirador esta vivo y si se puede utilizar su habilidad
            print('-----> 7. Habilidad (Francotirador) <-----')
        if self.equipo[3]['vida actual'] > 0 and self.equipo[3][
            'enfriamiento'] == 0:  # Comprueba si inteligencia esta vivo y si se puede utilizar su habilidad
            print('-----> 8. Habilidad (Inteligencia) <-----')

        while True:
            try:
                acc = input('Seleccione una acción: ')
                int(acc)  # Convertir la accion de string a entero
                if int(acc) <= 8:  # Comprobar que la accion es menor/igual a 8 (opciones del menu)
                    if int(acc) == 1:  # Accion 1 elegida (mover medico)
                        while True:
                            celda_nuevo = input('Introduce la celda a la que quiere mover el personaje: ').lower()
                            medico1 = self.equipo[0]  # Guardamos en medico1 el primer valor de la lista equipo
                            # Creamos una instancia con los valores almacenados del diccionario en medico1
                            medico_instancia = medico(medico1['vida maxima'],
                                                      medico1['vida actual'],
                                                      medico1['dano'], medico1['posicion'],
                                                      medico1['enfriamiento'])
                            if medico_instancia.mover(celda_nuevo,
                                                      self.equipo) == True:  # Comprobamos la celda a la que movemos
                                return True

                    elif int(acc) == 2:  # Accion 2 elegida
                        while True:
                            celda_nuevo = input('Introduce la celda a la que quiere mover el personaje: ').lower()
                            artillero1 = self.equipo[1]  # Guardamos en artillero1 el segundo valor de la lista equipo
                            # Creamos una instancia con los valores almacenados del diccionario en artillero1
                            artillero_instancia = artillero(artillero1['vida maxima'],
                                                            artillero1['vida actual'],
                                                            artillero1['dano'], artillero1['posicion'],
                                                            artillero1['enfriamiento'])
                            if artillero_instancia.mover(celda_nuevo,
                                                         self.equipo) == True:  # Comprobamos la celda a la que movemos
                                return True

                    elif int(acc) == 3:  # Accion 3 elegida
                        while True:
                            celda_nuevo = input('Introduce la celda a la que quiere mover el personaje: ').lower()
                            francotirador1 = self.equipo[
                                2]  # Guardamos en francotirador1 el tercer valor de la lista equipo
                            # Creamos una instancia con los valores almacenados del diccionario en francotirador1
                            francotirador_instancia = francotirador(francotirador1['vida maxima'],
                                                                    francotirador1['vida actual'],
                                                                    francotirador1['dano'], francotirador1['posicion'],
                                                                    francotirador1['enfriamiento'])
                            if francotirador_instancia.mover(celda_nuevo,
                                                             self.equipo) == True:  # Comprobamos la celda a la que movemos
                                return True

                    elif int(acc) == 4:  # Accion 4 elegida
                        while True:
                            celda_nuevo = input('Introduce la celda a la que quiere mover el personaje: ').lower()
                            inteligencia1 = self.equipo[
                                3]  # Guardamos en inteligencia1 el cuarto valor de la lista equipo
                            # Creamos una instancia con los valores almacenados del diccionario en inteligencia1
                            inteligencia_instancia = inteligencia(inteligencia1['vida maxima'],
                                                                  inteligencia1['vida actual'],
                                                                  inteligencia1['dano'], inteligencia1['posicion'],
                                                                  inteligencia1['enfriamiento'])
                            if inteligencia_instancia.mover(celda_nuevo,
                                                            self.equipo) == True:  # Comprobamos la celda a la que movemos
                                return True

                    elif int(acc) == 5:  # Accion 5 elegida
                        while True:
                            celda_curar = input(
                                'Introduce la celda donde se encuentre el personaje que quieras curar: ').lower()
                            medico1 = self.equipo[0]  # Guardamos en medico1 el primer valor de la lista equipo
                            # Creamos una instancia con los valores almacenados del diccionario en medico1
                            medico_instancia = medico(medico1['vida maxima'],
                                                      medico1['vida actual'],
                                                      medico1['dano'], medico1['posicion'],
                                                      medico1['enfriamiento'])
                            if medico_instancia.habilidad(celda_curar, self.equipo) == True:
                                print('-----> RESULTADO DE LA ACCIÓN <-----')
                                for elemento in self.equipo:  # Recorremos la lista equipo
                                    if elemento[
                                        'enfriamiento'] == 0:  # Comrpobamos que el valor enfriamiento es igual a 0
                                        if elemento[
                                            'posicion'] == celda_curar:  # Comprobamos que la poscion sea igual a celda_curar
                                            print(f"El {elemento['nombre']} se ha curado en la celda: {celda_curar}")
                                            self.equipo[0][
                                                'enfriamiento'] = 2  # Cambiamos el valor de enfriamiento para que no se pueda utilizar en el siguiente turno
                                            return True
                                    else:
                                        print('El enfriamiento esta activado para este turno, prueba en el sigueinte')
                                        break
                                break

                    elif int(acc) == 6:  # Accion 6 elegida
                        while True:
                            celda_marcada = input('Introduce la celda a atacar en un 2x2 con el artillero: ').lower()
                            artillero1 = self.equipo[1]  # Guardamos en artillero1 el segundo valor de la lista equipo
                            # Creamos una instancia con los valores almacenados del diccionario en artillero1
                            artillero_instancia = artillero(artillero1['vida maxima'],
                                                            artillero1['vida actual'],
                                                            artillero1['dano'], artillero1['posicion'],
                                                            artillero1['enfriamiento'])
                            if artillero_instancia.habilidad(celda_marcada, self.equipo):
                                self.equipo[1][
                                    'enfriamiento'] = 2  # Cambiamos el valor de enfriamiento para que no se pueda utilizar en el siguiente turno
                                return True, ('a', celda_marcada)

                    elif int(acc) == 7:  # Accion 7 elegida
                        while True:
                            celda_atacar = input('Introduce la celda a la que quieres atacar: ').lower()
                            francotirador1 = self.equipo[
                                2]  # Guardamos en francotirador1 el tercer valor de la lista equipo
                            # Creamos una instancia con los valores almacenados del diccionario en francotirador1
                            francotirador_instancia = francotirador(francotirador1['vida maxima'],
                                                                    francotirador1['vida actual'],
                                                                    francotirador1['dano'], francotirador1['posicion'],
                                                                    francotirador1['enfriamiento'])
                            if francotirador_instancia.habilidad(celda_atacar, self.equipo):
                                self.equipo[2][
                                    'enfriamiento'] = 2  # Cambiamos el valor de enfriamiento para que no se pueda utilizar en el siguiente turno
                                return True, ('f', celda_atacar)

                    elif int(acc) == 8:  # Accion 8 elegida
                        celda_marcada = input('Introduce la celda a atacar en un 2x2 con la inteligencia: ').lower()
                        inteligencia1 = self.equipo[3]  # Guardamos en inteligencia1 el cuarto valor de la lista equipo
                        # Creamos una instancia con los valores almacenados del diccionario en inteligencia1
                        inteligencia_instancia = inteligencia(inteligencia1['vida maxima'],
                                                              inteligencia1['vida actual'],
                                                              inteligencia1['dano'], inteligencia1['posicion'],
                                                              inteligencia1['enfriamiento'])
                        if inteligencia_instancia.habilidad(celda_marcada, self.equipo):
                            self.equipo[3][
                                'enfriamiento'] = 2  # Cambiamos el valor de enfriamiento para que no se pueda utilizar en el siguiente turno
                            return True, ('i', celda_marcada)
                else:
                    print('El numero introducido no es correcto')
            except ValueError:
                print('Mal formato')

    # Funcion para mostrar informe
    def informe1(self):
        print('-----> SITUACIÓN DEL EQUIPO <-----')
        for elemento in self.equipo:  # Recorremos la lista equipo
            if elemento[
                'vida actual'] > 0:  # Si el personaje esta vivo lo añadimos al informe con su posicion y la vida restante
                print(
                    f"{elemento['nombre'].upper()} --> Posicion: {elemento['posicion'].upper()} --> [Vidas {elemento['vida actual']}/{elemento['vida maxima']}]")
        print('<------------------------------>')

    # Funcion para manejar el enfriamiento
    def tiempo_enfriamiento(self):
        for miembro in self.equipo:  # Recorremos la lista equipo
            if miembro['enfriamiento'] != 0:  # Si el enfriamiento es distinto a 0
                miembro['enfriamiento'] = miembro['enfriamiento'] - 1  # Restamos 1 al enfriamiento
                if miembro['enfriamiento'] == 0:  # Si el enfriamiento es igual a 0
                    miembro['enfriamiento'] = 0  # Le asignamos el valor 0

    # Funcion que limpia las posiciones de los personajes muertos, permitiendo el movimiento del resto del equipo
    def limpiar_pos(self):
        for miembros in self.equipo:  # Recorremos la lista equipo
            if miembros['vida actual'] <= 0:  # Comprobamos que la vida actual sea menor que 0
                miembros['posicion'] = ''  # Asignamos una posicion vacia

    def turno1(self):
        if self.turno_end == False:  # Comprobamos si el turno ha terminado
            self.tiempo_enfriamiento()  # Llamamos a la funcion
            self.limpiar_pos()  # Llamamos a la funcion
            self.informe1()  # Llamamos a la funcion
            print(self.realizar_accion()) # Llamamos a la funcion
            #self.set_oponente(self.oponente)  # Llamamos a la funcion

    def check_point(self) -> bool:
        if self.equipo[1]['vida actual'] <= 0 and self.equipo[2][
            'vida actual'] <= 0.:  # Comprobamos si el artillero y el francoritador del equipo rival han sido derrotados (personajes militares)
            return True  # Si se cumple la condicion el juego termina
        else:
            return False

    # Funcion para establecer el oponente
    def set_oponente(self, oponente):
        self.oponente = oponente  # Asignamos el oponente desde el main
        return self.oponente  # Devolvemos el valor oponente a cada jugador