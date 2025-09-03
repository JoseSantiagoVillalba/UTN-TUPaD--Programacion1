#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(0,101):
    print(i)


#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
#dígitos que contiene.

numero:int = int(input("Ingrese un número entero para averiguar sus digitos: "))
n = abs(numero)
contador = 0


if n == 0:
    contador = 1
else:
    while n > 0:
        n = n // 10 
        contador += 1
print(f"El número {numero} tiene {contador} dígitos.")


#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
#dados por el usuario, excluyendo esos dos valores."""



numero5 = int(input("Ingrese un número para sumar: "))
numero6 = int(input("Ingrese un número para sumar: "))
suma2 = 0

if numero5 > numero6:
    for i7 in range(numero6, numero5 + 1):  # desde 1 hasta numero inclusive
        suma2 = suma2 + i7
    print("La suma es:", suma2)
elif numero6 > numero5:
    for i7 in range(numero5, numero6 + 1):  # desde 1 hasta numero inclusive
        suma2 = suma2 + i7
    print("La suma es:", suma2)





#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
#un 0.

bandera: bool = True
contador2: int = 0
while bandera == True:
    numero2:int = int(input("Ingrese un numero entero para sumar. Finaliza con 0: "))
    if numero2 == 0:
        bandera = False
    else:
        contador2 = contador2 + numero2
print(f"El valor total es de {contador2}")


#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número."""
import random

numero: int = random.randint(1,9)

bandera: bool = True
contador3: int = 1
contador4 = 0

while bandera == True:
    adivino: int = int(input("Ingrese un numero: "))
    contador3 += 1
    if adivino == numero:
        print("--------------")
        print("MUY BIEN!!!!!")
        print(f"Arcertaste en {contador3} intentos")
        bandera = False
        print("--------------")
    else:
        print("Intentalo de nuevo, tú puedes")


#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
#entre 0 y 100, en orden decreciente.

for i2 in range(100, -1,-2):
    print(f"{i2}")



#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
#número entero positivo indicado por el usuario."""

numero3 = int(input("Ingrese un número para sumar: "))
suma = 0
for i3 in range(1, numero3 + 1):  # desde 1 hasta numero inclusive
    suma = suma + i3
print("La suma es:", suma)


#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

bandera2: bool = True
cont_par: int = 0
cont_impar: int = 0
cont_pos: int = 0
cont_neg: int = 0


for i5 in range (0, 1, 1):
    numero:int = int(input("Ingrese un numero para saber su estado: "))

    if numero%2 == 0 :
        cont_par += 1
    elif numero%2 == 1 :
        cont_impar += 1
    if numero > 0 :
        cont_pos += 1
    elif numero < 0 :
        cont_neg += 1


print(f"Hay {cont_par} numeros pares, {cont_impar} impares, {cont_pos} positivos y {cont_neg} negativos")




#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
#poder procesar 100 números cambiando solo un valor)."""

contador5: int = 0
media: float = 0
for i6 in range (0, 5, 1):
    numero4: int = int(input("Ingrese un numero entero para ver la media:"))
    contador5 = contador5 + numero4
media = contador5 / 5

print(media)

"""10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745."""

