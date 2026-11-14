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

# Ejercicio: Generador de Código de Usuario
# Crea dos variables: carrera = "ingenieria" y sede = "lima".Extrae las primeras 3 letras de carrera 
# ([:3]) y las primeras 3 letras de sede ([:3]), y únelas en mayúsculas con un número aleatorio de 3 cifras (r.randint(100, 999) convertido a 
# texto con str(...)).   Imprime el código resultante (ej: INGLIM482) y verifica con .isalnum() si el código generado es válido (alfanumérico).

carrera = "Ingeniería"
sede = "lima"
tres_carrera = carrera[:3] 
tres_sede = sede[:3] 

numero = str(r.randint(100,999))
codigo_usuario = (tres_carrera + tres_sede + numero).upper()

print("Código generado:", codigo_usuario)
print("¿Es alfanumérico?:", codigo_usuario.isalnum()) 

# Slicing 
lenguaje = "Programacion en Python"
print("Primeros 12 caracteres", lenguaje[0:12])

# Metodos de cadenas 
usuario = "sebastian2026"
print("En mayúsculas sería: ", usuario.upper())
print("Hay tantas a", usuario.count("a"))
print("Esto es alfanumerico?", usuario.isalnum())

# Metodo de una variable de tipo str

correo = " SEBASTIAN.ILLANES@GMAIL.COM "
print("texto limpio", correo.strip())
print("minusculas: ", "SEBASTIAN.ILLANES@GMAIL.COM".lower())

mensaje = "hola mundo, hola python, hola codigo"
print("Hay", mensaje.count("hola"), "palabras holas")
print("mayusculas", "hola mundo, hola python, hola codigo".upper())

# Seguimos con lo que resta
frase = "Aprender Java es divertido"
print("La palabra Java esta en la posicion: ", frase.find("Java"))
print("Frase reemplazada: ", frase.replace("Java", "Python"))

# Series booleanas 

nota = 15
asistencia = 80

print("¿Aprobado?:", nota >= 11) 
print("¿Asistencia perfecta?:", asistencia == 100)  
print("¿No sacó nota máxima?:", nota != 20) 

tiene_entrada = True
es_vip = False

print("Entrada y VIP:", tiene_entrada and es_vip) 
print("Entrada o VIP:", tiene_entrada or es_vip)   
print("No es VIP:", not es_vip)                    