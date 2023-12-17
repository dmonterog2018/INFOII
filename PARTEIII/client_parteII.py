import socket
import sys
import pickle
import time

from jugador import Jugador

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((sys.argv[1], int(sys.argv[2])))



while True:
    usuario = input("Introduce el nombre de usuario en partida: ") # Pedimos el usuario
    if len(usuario) != 0:
        print("Enviando usuario al servidor...")
        c.send(pickle.dumps(usuario)) # Enviamos al servidor
        break
    else:
        print("Introduce un usuario por favor") # Sino introducimos nada lo volvemos a pedir

j1 = Jugador() # Instanciamos la clase jugador


def puntuaciong(contador,dead):
    totalg = 0
    puntuacion1 = 1000
    puntuacion2 = max(0, (20 - contador)) * 20
    puntuacion3 = 0
    puntuacion4 = 100 * int(dead)
    for p in j1.equipo:
        if p['vida actual'] > 0:
            puntuacion3 = puntuacion3 + 100
    totalg = totalg + puntuacion1 + puntuacion2 + puntuacion3 + puntuacion4
    return totalg

def puntuacionp(contador, dead, puntuaciong):
        totalp = 0
        puntuacion4 = 0
        puntuacion5 = 0
        puntuacion6 = 100 * int(dead)

        if contador > 10:
            puntuacion4 += (contador - 10) * 20
        for p in j1.equipo:
            if p['vida actual'] > 0:
                puntuacion5 = puntuacion5 + 100
        totalp = totalp + puntuacion4 + puntuacion5 + puntuacion6
        if totalp > puntuaciong:
            totalp += 900
        return totalp



while True:
    datos = c.recv(1024)
    if not isinstance(pickle.loads(datos), tuple):
        print(pickle.loads(datos))
    if pickle.loads(datos) == (f"<---- ¡Has ganado {usuario}!. Comienzas la partida... ---->") or pickle.loads(datos) == ('Es tu turno. Posiciona el equipo.'): # Si ganamos o es el turno de poscionar, creamos le equipo

        j1.crear_equipo()
        j1.posicionar_equipo()
        c.send(pickle.dumps('OK'))
    elif pickle.loads(datos)[0] == 'GANADO': # Si nrecibimos que hemos ganado del servidor lo imprimimos y salimos del bucle
        print(f"***** HAS GANADO LA PARTIDA {usuario}, ENHORABUENA *****")
        cont = pickle.loads(datos)[1]
        total = puntuaciong(cont, pickle.loads(datos)[2])
        print(f"***** PUNTUACIÓN TOTAL: {total} *****")
        gan = ('PERDIDO', j1.muertos(), total, usuario)
        c.send(pickle.dumps(gan))
        print("ENVIADO")
        datos = c.recv(1024)
        print("-----> RANKING <------" + "\n" + pickle.loads(datos))
        time.sleep(3)
        break
    elif pickle.loads(datos) =='---> ES SU TURNO <---':
        j1.turno = [] # Limpiuamos el turno
        if j1.check_point(): # Nos devuelve si el artillero y el franco estan muertos, en ese caso, se envia el mensaje perdido
            pierde = ('PERDIDO', j1.muertos())
            c.send(pickle.dumps(pierde))
            print(f'***** HAS PERDIDO LA PARTIDA {usuario}, BIEN JUGADO *****')
            datos = c.recv(1024)
            cont = pickle.loads(datos)[1]
            total = puntuacionp(cont, pickle.loads(datos)[2], pickle.loads(datos)[3])
            print(f"***** PUNTUACIÓN TOTAL: {total} *****")
            enviar = usuario, str(total)
            c.send(pickle.dumps(enviar))
            datos = c.recv(1024)
            print("-----> RANKING <------" + "\n" + pickle.loads(datos))
            time.sleep(3)
            break
        j1.tiempo_enfriamiento()  # Llamamos a la funcion
        j1.limpiar_pos()  # Llamamos a la funcion
        j1.informe1()  # Llamamos a la funcion

        resultado = j1.realizar_accion()

        if isinstance(resultado, bool) and resultado: # Si el resultado de la acción es simplemente un booleano(SOLO HA MOVIDO), mandamos FIN
            c.send(pickle.dumps('FIN'))

        elif isinstance(resultado, tuple) and len(resultado) == 2: # Si recibimos una tupla ,la mandamos al servidor
            letra, celda = resultado
            c.send(pickle.dumps(resultado))
            # Haz lo que necesites con letra y celda
    elif isinstance(pickle.loads(datos), tuple): # Si recibimos una tupla llamamos a recibir accion y la lanzamos sobre nuestro equipo y mandamos el resultado
        lanzamiento = pickle.loads(datos)
        verificacion = lanzamiento[0]
        tupla = lanzamiento[1]
        tipo, celda = tupla
        j1.recibir_accion(tipo,celda)
        time.sleep(1)
        c.send(pickle.dumps(j1.turno))

print('---> DESCONECTANDO DEL SERVIDOR <---')
c.close()








