from math import pi
#1. Crear una función llamada imprimir_hola_mundo que imprima por
#pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#programa principal.

def imprimir_hola_mundo():
    print("Hola Mundo")

imprimir_hola_mundo()

#2. Crear una función llamada saludar_usuario(nombre) que reciba
#como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver:
# “Hola Marcos!”. Llamar a esta función desde el programa
#principal solicitando el nombre al usuario.

nombre: str = input("Ingrese su nombre: ")

def saludar_usuario(nombre):
    print(f"Hola {nombre}")
saludar_usuario(nombre)


#3.Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Ped
# ir los datos al usuario y llamar a esta función con los valores ingresados.

nombre: str = input("Ingrese su nombre: ")
apellido: str = input("Ingrese su apellido: ")
edad: int = int(input("Ingrese su edad: "))
residencia: str = input("Ingrese su residencia: ")

def informacion_personal(nombre, apellido,edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
informacion_personal(nombre, apellido,edad, residencia)

#4. Crear dos funciones:calcular_area_circulo(radio) que reciba el radio como p arámetro y
#devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro 
#y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar
#ambas funciones para mostrar los resultados.

radio: float = float(input("Ingrese el radio del circulo: "))

def calcular_area_circulo(radio):
    area = 2 * pi * radio
    print(f"El area del circulo es {area}")
def calcular_perimetro_circulo(radio):
    perimetro = pi * (radio**2)
    print(f"El perimetro del circulo es {perimetro}")

calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)

#5. Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

segundos:float = float(input("Ingrese la cantidad de segundos: "))
def segundos_a_horas(segundos):
    horas = (segundos / 60) / 60
    print(f"{segundos} segundos son {horas} horas")
segundos_a_horas(segundos)


#6. Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la función.

numero:int = int(input("Ingrese un numero entero: "))
def tabla_multiplicar(numero):
    for i in range (11):
        print(f"{numero} X {i} = {i * numero}")

tabla_multiplicar(numero)


#7. Crear una función llamada operaciones_basicas(a, b) que reciba
#dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
#Mostrar los resultados de forma clara.

a:int = int(input("Define A: "))
b:int = int(input("Define B: "))

def operaciones_basicas(a, b):
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} X {b} = {a * b}")
    print(f"{a} / {b} = {a / b}")

operaciones_basicas(a,b)

#8. Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    print(f"Tu IMC es: {imc}")
    if imc < 18.5:
        print("Categoría: Bajo peso")
    elif 18.5 <= imc < 24.9:
        print("Categoría: Peso normal")
    elif 25 <= imc < 29.9:
        print("Categoría: Sobrepeso")
    else:
        print("Categoría: Obesidad")
calcular_imc(peso, altura)

#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#resultado usando la función.

celsius:float = float(input("Ingrese los grados Celsius: "))

def celsius_a_fahrenheit(celsius):
    fahrenheit:float = (celsius * 1.8) + 32
    print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit")
celsius_a_fahrenheit(celsius)


#10.Crear una función llamada calcular_promedio(a, b, c) que reciba
#tres números como parámetros y devuelva el promedio de ellos.
#Solicitar los números al usuario y mostrar el resultado usando esta
#función.

numero1:float = float(input("Ingrese el primer numero: "))
numero2:float = float(input("Ingrese el segundo numero: "))
numero3:float = float(input("Ingrese el tercer numero: "))

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    print(f"El promedio entre {a}, {b} y {c} es {promedio}")

calcular_promedio(numero1, numero2, numero3)
