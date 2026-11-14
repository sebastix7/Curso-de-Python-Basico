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
print("Primeros 6 caracteres:", completo[:6]) # cada letra asume un numero y se completa [2:4]... etc

# 4. Métodos útiles de cadenas
print("En mayúsculas:", completo.upper()) #convierte a mayus o minus
print("Veces que aparece 'a':", completo.count("a")) #cuantas "a" hay
print("¿Es alfanumérico?:", "Python123".isalnum()) #verifica si solo hay letras y numeros 

# Metodos/atributos de una variable de tipo str
texto = "   Python es facil y Python es genial   "

# 1. Limpieza de espacios en los extremos (.strip)
print("Texto limpio:", texto.strip())

# 2. Mayúsculas y Minúsculas (.upper / .lower)
print("Mayúsculas:", "python".upper())
print("Minúsculas:", "PYTHON".lower())

# 3. Conteo de subcadenas (.count)
print("Veces que aparece 'Python':", texto.count("Python"))

# 4. Reemplazar partes del texto (.replace)
print("Texto reemplazado:", texto.replace("facil", "increible"))

# 5. Buscar posición (.find)
print("Posición de 'facil':", texto.find("facil"))

# 6. Validaciones (.isalnum / .isdigit)
print("¿'Sebas123' es alfanumérico?:", "Sebas123".isalnum())
print("¿'98765' son solo números?:", "98765".isdigit())

# Variables booleanas

# SEXTO PROGRAMA: Variables Booleanas (bool)

# 1. Definición directa y tipo
b1 = True
b2 = False
print("Tipo:", type(b1))  # <class 'bool'>

# 2. Comparaciones (<, >, <=, >=, ==, !=)
b3 = 13 <= 18             # True
b4 = 12 == 11             # False
print("¿13 <= 18?:", b3)

# 3. Operadores Lógicos (and, or, not)
print("b1 and b2:", b1 and b2)  # False (ambos verdaderos)
print("b1 or b2:", b1 or b2)    # True (al menos uno verdadero)
print("not b1:", not b1)        # False (invierte el valor)