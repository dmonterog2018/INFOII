import socket
import pickle

lobby = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creamos el socket TCP/IP
server_socket.bind((socket.gethostname(), 5555)) #Conectamos servido a una direccion IP y puerto
server_socket.listen(1) #Lo ponemos en escucha

try:
    while True: #Esperamos a que se conecte un cliente
        client_socket, addr = server_socket.accept() 
        if client_socket:
            print('Cliente conectado: ', addr)
            lobby.append(addr)
            while True:
                #Recibir datos
                msg = client_socket.recv(1024) #Recibimos hasta 1024 bytes
                msg_decod = pickle.loads(msg) #Decodificar el mensaje
                print(msg_decod)

                #Enviar datos
                msg_env = 'datos'
                msg_codif = pickle.dumps(msg_env) #Codificamos el mensaje
                client_socket.sendall(msg_codif) #Enviamos el mensaje

except KeyboardInterrupt:
    server_socket.close()