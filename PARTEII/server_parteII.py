import socket
import sys
import threading
import time
import pickle
from check_inicio import inicio

print("Arrancando servidor de juego...")
print("IP servidor de juego: ", socket.gethostbyname(socket.gethostname()))
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(), int(sys.argv[1])))
print("PUERTO servidor de juego: ", sys.argv[1])
server_socket.listen(10)

sala_espera = []

def bienvenida(client_socket, usuario):

    msg1 = f"Bienvenido al juego {usuario}, esta usted en la sala de espera"
    client_socket.send(pickle.dumps(msg1))
    sala_espera.append((client_socket, usuario))
    print(sala_espera)
    if len(sala_espera) >= 2:
        emparejar_clientes()
def emparejar_clientes():


    cliente1, cliente2 = sala_espera[:2]
    print(cliente2)
    print(cliente1)
    # Elimina los clientes emparejados de la lista
    sala_espera.remove(cliente1)
    sala_espera.remove(cliente2)
    print(sala_espera)

    # Lanza la partida con los clientes emparejados
    hilo2 = threading.Thread(target = partida, args = ((cliente1, cliente2)))
    hilo2.start()

def partida(client_socket1, client_socket2):
    usuario1 = client_socket1[1]
    usuario2 = client_socket2[1]
    client_socket1 = client_socket1[0]
    client_socket2 = client_socket2[0]

    msg = f"<---- Jugador encontrado: {usuario2}. Comenzando partida. Cargando...---->"
    msg_2 = f"<---- Jugador encontrado: {usuario1}. Comenzando partida. Cargando...---->"
    msg1 = '<---- Lanzando moneda... su apuesta: CARA ---->'
    msg2 = '<---- Lanzando moneda... su apuesta: CRUZ ---->'

    client_socket1.send(pickle.dumps(msg))
    client_socket2.send(pickle.dumps(msg_2))
    time.sleep(2)
    client_socket1.send(pickle.dumps(msg1))
    client_socket2.send(pickle.dumps(msg2))
    time.sleep(2)


    if inicio() == '1': # GANA CARA

        msg3 = f"<---- ¡Has ganado {usuario1}!. Comienzas la partida... ---->"
        msg4 = f"<---- ¡Has perdido {usuario2}!. Espera tu turno... ---->"

        client_socket1.send(pickle.dumps(msg3))
        client_socket2.send(pickle.dumps(msg4))

        datos = client_socket1.recv(1024)
        if not datos:
            print('NO ENTRA')
        if pickle.loads(datos) == "OK":
            client_socket1.send(pickle.dumps('----> ESPERA TU TURNO <----'))
            client_socket2.send(pickle.dumps('Es tu turno. Posiciona el equipo.'))
            cadena2 = client_socket2.recv(1024)
            if not cadena2:
                print("HOLA")
            hilo2 = threading.Thread(target=manejo_partida, args=(client_socket1, client_socket2))
            hilo2.start()

    else: # GANA CRUZ

        msg3 = f"<---- ¡Has ganado {usuario2}!. Comienzas la partida... ---->"
        msg4 = f"<---- ¡Has perdido {usuario1}!. Espera tu turno... ---->"

        client_socket1.send(pickle.dumps(msg4))
        client_socket2.send(pickle.dumps(msg3))

        datos3 = client_socket2.recv(1024)
        if not datos3:
            print('NO ENTRA')
        if pickle.loads(datos3) == "OK":
            client_socket2.send(pickle.dumps('----> ESPERA TU TURNO <----'))
            client_socket1.send(pickle.dumps('Es tu turno. Posiciona el equipo.'))
            datos2 = client_socket1.recv(1024)
            if not datos2:
                print("HOLA")
            hilo2 = threading.Thread(target=manejo_partida,args=(client_socket2, client_socket1))
            hilo2.start()


def manejo_partida(j1, j2):
    mensaje1 = f"----> COMIENZO DE LA PARTIDA <----"
    mensaje3 = f"----> COMIENZO DE LA PARTIDA. ESPERA TU TURNO <----"
    final = False
    j1.send(pickle.dumps(mensaje1))
    j2.send(pickle.dumps(mensaje3))

    while not final:

        if mensajeria_turno(j1,j2) is False:
            break
        if mensajeria_turno(j2,j1) is False:
            break
def mensajeria_turno(jugador1, j2):
    jugador1.send(pickle.dumps('---> ES SU TURNO <---'))
    datos5 = jugador1.recv(1024)
    print(pickle.loads(datos5))

    if pickle.loads(datos5) == 'FIN':
        jugador1.send(pickle.dumps('---> FIN DE TURNO. ESPERE EL SIGUIENTE <---'))
        return True
    elif pickle.loads(datos5) == 'PERDIDO':
        print("RECIBIDO PERDIDO")
        time.sleep(1)
        j2.send(pickle.dumps('GANADO'))
        return False
    else:
        enviar = pickle.loads(datos5)
        print(enviar)
        j2.send(pickle.dumps(enviar))
        datos6 = j2.recv(1024)
        cadena = pickle.loads(datos6)
        time.sleep(1)
        for i in cadena:
            jugador1.send(pickle.dumps(i))
        time.sleep(1)
        jugador1.send(pickle.dumps('---> FIN DE TURNO. ESPERE EL SIGUIENTE <---'))
        return True

try:
    while True:
        client_socket, addr = server_socket.accept()
        if client_socket:
            print("Client conectado: ", addr)
            datos = client_socket.recv(1024)
            if not datos:
                break
            usuario = pickle.loads(datos)

            print(f"Recibido de: ---> {addr} <--- mensaje: {usuario.upper()}")

            hilo1 = threading.Thread(target=bienvenida,args=(client_socket, usuario))

            hilo1.start()


except KeyboardInterrupt:
    print("Apagando servidor de juego :(")
    server_socket.close()