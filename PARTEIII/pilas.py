

class Nodo:
    def __init__(self, dato, siguiente = None):
        self.dato = dato
        self.siguiente = siguiente


class Pila:
    def __init__(self):
        self.cima = None
        self.tamano = 0

    def apilar(self,dato):
        # Crear el nodo con el nuevo dato
        nuevo = Nodo(dato)
        # Hacer que el nodo apunte a la cima de la pila
        nuevo.siguiente = self.cima
        # Cambiar la cima para que apunte a dato nuevo
        self.cima = nuevo

    def desapilar(self):

        dato = self.cima.dato # Apunto al dato que desapilo
        self.cima = self.cima.siguiente # Apunto la cima al siguiente dato
        self.tamano -= 1 # Resto el tamaño en 1
        return dato # Devuelvo el dato

    def vacia(self):
        if self.tamano == 0:
            return True
        else:
            return False

    def size(self):
        return self.tamano

    def pick(self):
        return self.cima

    def mostrar(self):
        actual = self.cima
        while actual is not None:
            print(actual.dato, end=" => ")
            actual = actual.siguiente
    def buscar(self,dato):
        actual = self.cima
        while actual is not None:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        return False


