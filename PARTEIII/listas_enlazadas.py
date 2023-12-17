
class Nodo:

    def __init__(self, dato,puntuacion, siguiente=None, anterior = None):
        self.dato = dato
        self.puntuacion = puntuacion
        self.siguiente = siguiente  # Inicializado en None
        self.anterior = anterior

class ListaEnlazada:

    def __init__(self):
        self.cabeza = None
        self.size = 0


    def insertarEn(self, dato,puntuacion):

        nuevo = Nodo(dato, puntuacion)

        if self.cabeza is None or puntuacion > self.cabeza.puntuacion:
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo

        else:

            actual = self.cabeza
            while actual.siguiente and puntuacion <= actual.siguiente.puntuacion:
                actual = actual.siguiente

            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo
            self.size += 1



    def estaVacia(self):
        return self.cabeza is None

    def calcular_size(self):
        return self.size

    def peek(self):
        return self.cabeza.dato


    def mostrar(self):
        actual = self.cabeza
        salida = ''

        while actual is not None:
            salida += str(actual.dato) +" : " + str(actual.puntuacion) + "\n"
            actual = actual.siguiente

        return salida[:-2]

