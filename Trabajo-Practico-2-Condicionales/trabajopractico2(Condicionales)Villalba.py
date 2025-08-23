from statistics import mode, median, mean
import random


edad: int = int(input("Ingrese su edad: "))
if edad >= 18 and edad < 120:
    print("Es mayor de edad") 
elif edad < 18 and edad > 0:
    print("No es mayor de edad")
else: 
    print("Entrada invalida")



nota: float = float(input("Ingrese su nota: "))
if nota >=  6 and nota <= 10:
    print("Aprobado") 
elif nota < 6 and nota > 0:
    print("Desaprobado")
else: 
    print("Entrada invalida")


numero: int = int(input("Ingrese un numero par: "))
resultado: int = numero % 2 
if resultado == 0:
    print("Ha ingresado un número par") 
else: 
    print("Por favor, ingrese un número par")



edad2: int = int(input("Ingrese su edad: "))
if edad2 < 12 and edad2 >= 0:
    print("Es un niño") 
elif edad2 >= 12 and edad2 < 18:
    print("Es Adolescente")
elif edad2 >= 18 and edad2 < 30:
    print("Es un adulto/a joven")
elif edad2 > 30: 
    print("Adulto/a")
else:
    print("No se haceptan numeros negativos")



contraseña: str = str(input("Indique su contraseña de entre 8 y 14 caracteres: "))
if len(str(contraseña)) > 8 and len(str(contraseña)) < 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")



numeros_aleatorios: float = [random.randint(1,100) for i in range(50)]
print("Lista de números aleatorios:", numeros_aleatorios)
moda: float =  mode(numeros_aleatorios)
mediana: float = median(numeros_aleatorios)
media: float = mean(numeros_aleatorios)
if media > mediana:
    print("Sesgo positivo")
elif media < mediana and mediana > moda:
    print("Sesgo negativo")
else: 
    print("Sin sesgo")



texto_a_escribir: str = str(input("Ingrese una frase o una palabra: "))
if texto_a_escribir.endswith(("a", "A", "e", "E", "i", "I", "o", "O", "u", "U")):
    print(f"{texto_a_escribir}!")
else:
    print(f"{texto_a_escribir}")



nombre: str = str(input("Ingrese su nombre: "))
numero_nombre: int = int(input("Si desea pasarlo a mayusculas oprima 1, si desea pasarlo a minusculas oprima 2, si desea que solo la primera sea ayuscula oprima 3: "))

if numero_nombre == 1: 
    print(f"{nombre.upper()}")
elif numero_nombre == 2:
    print(f"{nombre.lower()}")
elif numero_nombre == 3:
    print(f"{nombre.title()}")
else:
    print("Error, indique el 1, 2 o 3")



magnitud: float = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3 and magnitud > 0:
    print("Muy leve")
elif magnitud == 3 and magnitud < 4:
    print("Leve")
elif magnitud == 4 and magnitud < 5:
    print ("Moderado") 
elif magnitud == 5 and magnitud < 6:
    print ("Fuerte")
elif magnitud == 6 and magnitud < 7:
    print("Muy fuerte")
elif magnitud >= 7 and magnitud <= 10:
    print("Extremo")
else:
    print ("ERROR")



hemisferio: str = str(input("Indique en que hemisferio se encunetra N(norte), S(sur)"))
mes: int = int(input("Indique en que numero de mes esta"))
dia: int = int(input("Indique que dia(fecha) es hoy"))

if hemisferio == "N":
    if (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        print("Primavera")
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 22):
        print("Verano")
    elif (mes == 9 and dia >= 23) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
        print("Otoño")
    else:
        print("Invierno")
elif hemisferio == "S":
    if (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        print("Otoño")
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 22):
        print("Invierno")
    elif (mes == 9 and dia >= 23) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
        print("Primavera")
    else:
        print("Verano")
