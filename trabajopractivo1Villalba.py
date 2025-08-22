from math import pi

print(pi)

print("Hola Mundo")



nombre: str = input("Por favor ingrese su nombre: ")
print(f"Hola {nombre}")



nombre2: str = str(input("Por favor ingrese nuevamente su nombre: "))
apellido: str = str(input("Por favor ingrese su apellido: "))
edad: int = int(input("Ingrese su edad: "))
recidencia: str = str(input("Donde vives?: "))
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {recidencia}.")



radio: float = float(input("Indique el radio de un círculo: "))
area: float = pi * (radio ** 2)
perimetro: float = 2 * pi * radio
print(f"El área es: {area}, el perímetro es {perimetro}")



segund: int = int(input("Indique la cantidad de segundos que desea calcular: "))
hora: float = (segund / 60) / 60
print(f"{segund} es igual a {hora} horas")



numero_tabla: int = int(input("Indique un numero para ver su tabla de multiplicar: "))
resultado = numero_tabla * 1
print(f"{numero_tabla} * 1 es igual a {resultado}")
resultado = numero_tabla * 2
print(f"{numero_tabla} * 2 es igual a {resultado}")
resultado = numero_tabla * 3
print(f"{numero_tabla} * 3 es igual a {resultado}")
resultado = numero_tabla * 4
print(f"{numero_tabla} * 4 es igual a {resultado}")
resultado = numero_tabla * 5
print(f"{numero_tabla} * 5 es igual a {resultado}")
resultado = numero_tabla * 6
print(f"{numero_tabla} * 6 es igual a {resultado}")
resultado = numero_tabla * 7
print(f"{numero_tabla} * 7 es igual a {resultado}")
resultado = numero_tabla * 8
print(f"{numero_tabla} * 8 es igual a {resultado}")
resultado = numero_tabla * 9
print(f"{numero_tabla} * 9 es igual a {resultado}")
resultado = numero_tabla * 10
print(f"{numero_tabla} * 10 es igual a {resultado}")



numero_op: float = float(input("Indique un numero distinto de cero para las operaciones: "))
numero_op2: float = float(input("Indique otro numero distinto de cero para las operaciones: "))
suma: int = numero_op + numero_op2
print(f"{numero_op} + {numero_op2} = {suma}")
resta = numero_op - numero_op2
print(f"{numero_op} - {numero_op2} = {resta}")
multiplicacion = numero_op * numero_op2
print(f"{numero_op} x {numero_op2} = {multiplicacion}")
division = numero_op / numero_op2
print(f"{numero_op} / {numero_op2} = {division}")



peso: int = int(input("Indique su peso en kg: "))
altura: float = float(input("Indique su peso en metros: "))
icm: float = peso / (altura**2)
print(f"su índice de masa corporal es igual a {icm}")



grados_celcius: float = float(input("Indique la temperatura en grados Celcius: "))
grados_fahrenheit: float = 9/5 * grados_celcius + 32
print(f"La temperatura en Fahrenheit es de {grados_fahrenheit}")



numero1: float = float(input("Para sacar el promedio, indique el primer numero: "))
numero2: float = float(input("Indique el segundo numero: "))
numero3: float = float(input("Indique el tercero: "))
promedio: float = (numero1 + numero2 + numero3) / 3

print(f"El promedio entre {numero1}, {numero2} y {numero3} es: {promedio}")
