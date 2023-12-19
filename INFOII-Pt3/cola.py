class Nodo:
    def __init__(self, dato, next=None):
        self.dato = dato
        self.next = next


class Cola:
    def __init__(self):
        self.frente = None
        self.final = None
        self.size = 0

    def vacia(self):
        if self.frente is None and self.final is None:
            return True
        else:
            return False

    def encolar(self, dato):
        nodo = Nodo(dato)

        if self.vacia():  # Frente y final apuntan al nuevo
            self.frente = nodo
            self.final = nodo
        else:
            self.final.next = nodo  # Conecto el último de la fila con el nodo nuevo
            self.final = nodo  # Actualizo la referencia al último de la fila

        self.size += 1

    def get_size(self):  # Cambié el nombre del método
        longitud = self.size
        return longitud

    def desencolar(self):
        devolver = self.frente
        if self.vacia():
            return devolver  # "devolver" es None
        elif self.size == 1:  # Se queda vacía
            self.frente = None
            self.final = None
        else:  # Frente apunta al segundo (el primero sale de la cola)
            self.frente = self.frente.next

        self.size -= 1  # Disminuyo el tamaño
        return devolver.dato  # Devuelvo el valor

    def peek(self):
        # Si no hay elementos, devuelvo None
        if self.frente is None:
            return None
        # Si hay algo, devuelvo el valor del primer elemento
        return self.frente.dato

    def mostrar(self):
        # Uso actual para ir moviéndome entre nodos
        actual = self.frente  # Empiezo en el primer elemento
        while actual is not None:  # Recorro hasta el final
            print(actual.dato, end=" => ")
            actual = actual.next  # paso al siguiente
        print()

    def buscar(self, dato):
        # Uso actual para ir moviéndome entre nodos
        actual = self.frente  # Empiezo en la cima
        while actual is not None:  # Recorro hasta el final
            if actual.dato == dato:  # Si encuentro, devuelvo True
                return True
            actual = actual.next
        # Si llego al final sin encontrarlo, devuelvo False
        return False