import random

ganador = ''
def inicio():
    ganador = random.randint(1,2)
    return str(ganador)

print(inicio())