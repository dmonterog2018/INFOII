import socket
import sys
import pickle
from jugador import Jugador

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((sys.argv[1], int(sys.argv[2])))

usuario = input("Introduce el nombre de usuario en partida: ")
if len(usuario) != 0:
    print("Enviando usuario al servidor...")
    c.send(pickle.dumps(usuario))
elif len(usuario) == 0:
    print("Introduce un usuario por favor")

j1 = Jugador()

while True:
    datos = c.recv(1024)
    print(pickle.loads(datos))
    if pickle.loads(datos).startswith('<---- ¡Has ganado') or pickle.loads(datos).startswith('Es tu turno'):

        j1.crear_equipo()
        j1.posicionar_equipo()
        c.send(pickle.dumps('OK'))

    elif pickle.loads(datos) =='---> ES SU TURNO <---':
        j1.tiempo_enfriamiento()  # Llamamos a la funcion
        j1.limpiar_pos()  # Llamamos a la funcion
        j1.informe1()  # Llamamos a la funcion

        resultado = j1.realizar_accion()

        if isinstance(resultado, bool) and resultado:
            print("Éxito: Solo contiene True")
            c.send(pickle.dumps('FIN'))

        elif isinstance(resultado, tuple) and len(resultado) == 2:
            print("Éxito: Contiene datos adicionales")
            letra, celda = resultado
            c.send(pickle.dumps(resultado))
            # Haz lo que necesites con letra y celda











