edad: int = int(input("Ingrese su edad: "))
if edad >= 18 and edad < 70:
    print("Es mayor de edad") 
elif edad < 18 and edad > 0:
    print("No es mayor de edad")
elif edad >= 200: 
    print("Es un fosil")
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






