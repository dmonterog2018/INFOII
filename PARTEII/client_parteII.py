import socket
import sys
import pickle
import time

from jugador import Jugador

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((sys.argv[1], int(sys.argv[2])))

while True:
    usuario = input("Introduce el nombre de usuario en partida: ")
    if len(usuario) != 0:
        print("Enviando usuario al servidor...")
        c.send(pickle.dumps(usuario))
        break
    else:
        print("Introduce un usuario por favor")

j1 = Jugador()

while True:
    datos = c.recv(1024)
    if not isinstance(pickle.loads(datos), tuple):
        print(pickle.loads(datos))
    if pickle.loads(datos) == (f"<---- ¡Has ganado {usuario}!. Comienzas la partida... ---->") or pickle.loads(datos) == ('Es tu turno. Posiciona el equipo.'):

        j1.crear_equipo()
        j1.posicionar_equipo()
        c.send(pickle.dumps('OK'))
    elif pickle.loads(datos) == 'GANADO':
        print(f"***** HAS GANADO LA PARTIDA {usuario}, ENHORABUENA *****")
        break
    elif pickle.loads(datos) =='---> ES SU TURNO <---':
        if j1.check_point():
            c.send(pickle.dumps('PERDIDO'))
            print(f'***** HAS PERDIDO LA PARTIDA {usuario}, BIEN JUGADO *****')
            break
        j1.tiempo_enfriamiento()  # Llamamos a la funcion
        j1.limpiar_pos()  # Llamamos a la funcion
        j1.informe1()  # Llamamos a la funcion

        resultado = j1.realizar_accion()

        if isinstance(resultado, bool) and resultado:
            c.send(pickle.dumps('FIN'))

        elif isinstance(resultado, tuple) and len(resultado) == 2:
            letra, celda = resultado
            c.send(pickle.dumps(resultado))
            # Haz lo que necesites con letra y celda
    elif isinstance(pickle.loads(datos), tuple):
        lanzamiento = pickle.loads(datos)
        verificacion = lanzamiento[0]
        tupla = lanzamiento[1]
        tipo, celda = tupla
        j1.recibir_accion(tipo,celda)
        time.sleep(3)
        c.send(pickle.dumps(j1.turno))

print('---> DESCONECTANDO DEL SERVIDOR <---')
c.close()








