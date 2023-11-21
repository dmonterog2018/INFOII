import socket
import sys
import threading
from check_inicio import inicio

print("Arrancando servidor de juego...")
print("IP servidor de juego: ", socket.gethostbyname(socket.gethostname()))
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(), int(sys.argv[1])))
print("PUERTO servidor de juego: ", sys.argv[1])
server_socket.listen()

lock = threading.Lock()

def bienvenida(client_socket, usuario):
    print(client_socket, usuario)
    msg1 = f"Bienvenido al juego {usuario}, esta usted en la sala de espera"
    client_socket.send(msg1.encode())

def handle_client(client_socket, addr):
    try:
        datos = client_socket.recv(1024)
        if not datos:
            return
        usuario = datos.decode()
        print(f"Recibido de: ---> {addr} <--- mensaje: {usuario.upper()}")

        bienvenida(client_socket, usuario)
        # Puedes realizar más operaciones con este cliente si es necesario

    except Exception as e:
        print(f"Error al manejar cliente {addr}: {e}")
    finally:
        client_socket.close()

try:
    while True:
        client_socket, addr = server_socket.accept()
        if client_socket:
            print("Cliente conectado: ", addr)

            # Crea un nuevo hilo para manejar este cliente
            client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
            client_handler.start()

except KeyboardInterrupt:
    server_socket.close()
    print("Apagando servidor de juego :(")
