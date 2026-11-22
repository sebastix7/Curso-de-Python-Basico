print("Ejercicio de la parte 1")

producto = float(input("Digite el precio del producto: "))
unidades = int(input("Cuantas unidades tiene: "))

multiplicar = producto * unidades
print("El resultado de multiplicar es: ", multiplicar)

print("Ejercicio de la parte 2")
base = float(input("Digite la base del triangulo: "))
altura =float(input("Digite la altura del triangulo: "))

area = (base * altura)
print("El resultado del area es: ", area)

print("Ejercicio de la seccion 3")
import getpass
clave = getpass.getpass("Dime tu contraseña: ")

print("Ejercicio de la seccion 4")

temperatura = float(input("Ingresa la temperatura (°C): "))
if temperatura < 15:
    print("Hace frío, llevo un abrigo")
elif temperatura >= 15 and temperatura <= 25:
    print("Clima templado y agradable")
else: 
    print("Hace calor, usar ropa ligera")