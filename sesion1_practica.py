# Ejercicios con el módulo random

# Crea una lista con 4 nombres de amigos y elige a uno al azar como ganador. Luego, asígnale un puntaje aleatorio 
# entre 50 y 100 puntos, imprime el resultado.

import random as r 
amigos = ["Sebastian", "Matias", "Luis", "Javier"]
ganador = r.choice(amigos)
print("El ganador es: ", ganador)

puntaje = r.randint(50,100)
print("El puntaje es: ", puntaje)