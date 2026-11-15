# RESUMEN - SESIÓN 3

# 1. FUNCIÓN DE ENTRADA: input()
# Detiene el programa y espera que el usuario escriba algo por teclado.
nombre = input("Ingresa tu nombre: ")


# 2. CONVERSIÓN DE TIPOS (Type Casting)
# Sirve para transformar el texto (str) del input() en número para poder calcular.
edad = int(input("Ingresa tu edad (entero): "))    
estatura = float(input("Ingresa tu estatura en m: ")) 

# Ejemplo práctico (Cálculo de IMC visto en clase)
peso = float(input("Ingresa tu peso en kg: "))
imc = peso / (estatura ** 2)


# 3. MÓDULO getpass
# Sirve para pedir contraseñas o datos sensibles sin que se vean en pantalla al escribir
import getpass
clave = getpass.getpass("Ingresa tu clave secreta: ")


# 4. FUNCIÓN DE SALIDA: print()
# Ejemplo 1: Con f-strings (la más limpia y moderna, :.2f limita a 2 decimales)
print(f"Hola {nombre}, tu IMC es {imc:.2f}")

# Ejemplo 2: Con operador % y comillas triples (docstring) visto en clase
print("""
REPORTE
Edad: %d años
IMC: %.2f
""" % (edad, imc))


# 5. ESTRUCTURA DE CONTROL: if / elif / else
# Permite tomar decisiones según se cumpla o no una condición (True/False)

# Ejemplo 1: Clasificación por rangos
if edad >= 0 and edad < 18:
    print("Eres menor de edad.")
elif edad >= 18 and edad < 65:
    print("Eres adulto.")
else:
    print("Edad fuera de rango o adulto mayor.")

# Ejemplo 2: Validación con .isdigit() antes de convertir a int()
dato = input("Ingresa un número entero: ")
if dato.isdigit():
    numero = int(dato)
    print(f"Número válido: {numero}")
else:
    print("Ingreso ERRÓNEO: no escribiste solo números.")