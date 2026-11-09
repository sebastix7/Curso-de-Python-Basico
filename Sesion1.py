import math as m # Sirve para funciones y operaciones avanzadas

# Primer programa
precio_original = 100 
descuento = 0.15
impuesto = 0.18

precio_con_descuento = precio_original * (1.0 - descuento)
precio_final = precio_con_descuento * (1.0 + impuesto)
porcentaje_del_original = (precio_final / precio_original) * 100.0

print("Precio final:", precio_final)
print("Porcentaje del original:", porcentaje_del_original)

# Segundo programa
print("Segundo programa")
print("Resultado:", m.pow(3, 3))

# Tercer programa
print("Tercer programa")
print("Resultado_1: ", m.acos(0.5))


# Segunda parte "El Modulo Random"
import random as r 
dado = r.randint(1,6)
print("Resultado: ", dado) #para simular un dado

opciones = ["Piedra","papel", "tijera"]
eleccion = r.choice(opciones) #sirve para elegir 1 elemento al azar de una lista de opc
print("La com eligió: ", eleccion)

probabilidad = r.random() #sirve para generar un decimal entre 0.0 y 1.0
print("Porcentaje/Probabilidad: ", probabilidad)

# Tercera parte "Variable de tipo cadena de caracter (str)"

curso = "Python Basico"
sesion = "Segunda Sesion"
completo = curso + " - " + sesion # Concatenación
print("Texto unido:", completo)

# 2. Acceso a caracteres (Índices)
print("Primer caracter:", completo[0])     # Muestra la 'P'
print("Ultimo caracter:", completo[-1])    # Muestra la 'n'

# 3. Subcadenas (Slicing)
print("Primeros 6 caracteres:", completo[:6])

# 4. Métodos útiles de cadenas
print("En mayúsculas:", completo.upper()) #convierte a mayus o minus
print("Veces que aparece 'a':", completo.count("a")) #cuantas "a" hay
print("¿Es alfanumérico?:", "Python123".isalnum()) #verifica si solo hay letras y numeros 