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


#Segunda parte "El Modulo Random"
import random as r 
dado = r.randint(1,6)
print("Resultado: ", dado) #para simular un dado

opciones = ["Piedra","papel", "tijera"]
eleccion = r.choice(opciones) #sirve para elegir 1 elemento al azar de una lista de opc
print("La com eligió: ", eleccion)

probabilidad = r.random() #sirve para generar un decimal entre 0.0 y 1.0
print("Porcentaje/Probabilidad: ", probabilidad)