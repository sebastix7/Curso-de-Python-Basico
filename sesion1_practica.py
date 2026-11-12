# Ejercicios con el módulo random

# Crea una lista con 4 nombres de amigos y elige a uno al azar como ganador. Luego, asígnale un puntaje aleatorio 
# entre 50 y 100 puntos, imprime el resultado.

import random as r 
amigos = ["Sebastian", "Matias", "Luis", "Javier"]
ganador = r.choice(amigos)
puntaje = r.randint(50,100)
print("El ganador es", ganador, "y su puntaje es", puntaje)

# Genera una probabilidad de lluvia (un número decimal entre 0.0 y 1.0), multiplícalo por 100 para convertirlo en porcentaje, y muéstralo en 
# pantalla redondeado a 2 decimales.

import random as r
probabilidad = r.random()
porcentaje = round(probabilidad * 100, 2)

print("La probabilidad es", probabilidad, "y en porcentaje es:", porcentaje, "%")

# Ejercicios de Variable de tipo cadena de caracter (str)

# Crea dos variables: nombre (con tu primer nombre) y apellido (con tu apellido). Únelas con un espacio en medio y guarda el resultado en una 
# variable nombre_completo. Luego, imprime el texto unido y muestra por separado la primera letra de tu nombre y la primera letra de tu apellido 
# usando índices positivos ([0]).

nombre = "Sebastian"
apellido = "Illanes"
nombre_completo = nombre + "-" + apellido
print("Mi nombre es: ", nombre_completo)

print("Primera letra de mi nombre: ", nombre_completo[0])
print("Primera letra de mi apellido: ",nombre_completo[-7])

# Crea una variable codigo = "UNI-2026-PERU". Imprime la primera letra ([0]), el guion que está en la posición 3 ([3]) y la última letra usando 
# el índice positivo [12] o [-1] 

codigo = "UNI-2026-PERU"

print("Primera letra es: ", codigo[0])
print("Guion en pos 3:", codigo[3]) 
print(" Ultima letra es: ", codigo[-1])