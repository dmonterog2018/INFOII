import socket
import pickle

name = input('Introduzca su nombre de usuario: ') #Introducir un nombre de usuario

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creo el socket TCP/IP
client.connect((socket.gethostname(), 5555)) #Conecto el cliente con el sevidor

try:
    while True:
        #Enviar datos
        msg = name
        msg_codif = pickle.dumps(msg) #Codificamos el mensaje
        client.sendall(msg_codif) #Enviamos el mensaje
        
        #Recibir datos
        msg_recv = client.recv(1024) #Recibimos hasta 1024 bytes
        msg_decod = pickle.loads(msg_recv) #Decodificar el mensaje

except KeyboardInterrupt:
    client.close()

client.close()
print("Conexión cerrada")