#Actividades 
#1) Dado el diccionario precios_frutas
#   precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
#   1450}
#   Añadir las siguientes frutas con sus respectivos precios:
#   Naranja = 1200
#   Manzana = 1500
#   Pera = 2300


precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
print(precios_frutas)

print()
print("1) Se agregan frutas")
precios_frutas ["Naranja"] = 1200
precios_frutas ["Manzana"] = 1500
precios_frutas ["Pera"] = 2300
print(precios_frutas)


#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
#   desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
#   Banana = 1330
#   Manzana = 1700
#   Melón = 2800

print()
print("2) Se actualizan precios de las frutas")
precios_frutas ["Banana"] = 1330
precios_frutas ["Manzana"] = 1700
precios_frutas ["Melón"] = 2800
print(precios_frutas)


#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
#   desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
#   precios.

print()
print("3) se muestrasn solo las frutas")
lista_nombres_frutas = [precios_frutas.keys()]
print(lista_nombres_frutas)


#4) Escribí un programa que permita almacenar y consultar números telefónicos.
#   Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#   Luego, pedí un nombre y mostrale el número asociado, si existe.

print()
print("4) Se crean contactos de celu")
contactos = {}
for i in range(0,5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el numero del contacto: ")
    contactos [nombre] = numero

buscado = input("Ingrese el nombre que quiere buscar: ")

if buscado in contactos:
    print(f"el numero de {buscado} es {contactos[buscado]}")
else:
    print("no existe en los contactos")

#5) Solicita al usuario una frase e imprime:
#   Las palabras únicas (usando un set).
#   Un diccionario con la cantidad de veces que aparece cada palabra

print()
print("5) la frase")

frase = input("Ingrese una frase: ")


#6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
#Luego, mostrá el promedio de cada alumno.


print()
print("6) Alumnos y notas")
lista_alumnos = []
notas_alumnos = []
promedio_alumnos = []

for i in range(0,3):
    alumno = input("Ingrese el nombre del alumno: ")
    suma = 0
    tupla_notas = ()
    lista_alumnos.append(alumno)
    for i in range(0,3):
        nota = int(input(f"Ingrese la {i + 1} nota: "))
        suma += nota
        tupla_notas += (nota,)
    notas_alumnos.append(tupla_notas)
    promedio = suma/3
    promedio_alumnos.append(promedio)
    print(tupla_notas)

for i in range (3):
    print(f"Notas de {lista_alumnos[i]}: {notas_alumnos[i]}")
    print(f"Promedio de {lista_alumnos[i]}: {promedio_alumnos[i]}")


#7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 
#   y Parcial 2:
#   Mostrá los que aprobaron ambos parciales.
#   Mostrá los que aprobaron solo uno de los dos.
#   Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

print()
print("7) Parciales aprobados")
parcial_1 = {1, 2, 3, 4, 5, 6}
parcial_2 = {4, 5, 6, 7, 8, 9}

ambos = parcial_1 & parcial_2
solo_uno = parcial_1 ^ parcial_2
al_menos_uno = parcial_1 | parcial_2

print("Aprobaron ambos:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)

#8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. 
#   Permití al usuario:
#   Consultar el stock de un producto ingresado.
#   Agregar unidades al stock si el producto ya existe.
#   Agregar un nuevo producto si no existe.


print()
print("8) Diccionario valores, stock")

dicc_stock = {
    "celulares": 10,
    "notebooks": 5,
    "telefonos": 20,
    "Pcs": 15,
}
print(dicc_stock)

consulta_prod:str = str(input("Indique el producto que desea consultar: "))

if consulta_prod in dicc_stock:
    agregar = input(f"El stock de {consulta_prod} es : {dicc_stock[consulta_prod]} desea agregar mas apretando 'a'?: ")
    if agregar.lower() == 'a':
        agregar_stock = int(input("Indique el stock del producto: "))
        dicc_stock[consulta_prod] = dicc_stock[consulta_prod] + agregar_stock
        print(dicc_stock)
else:
    agregar_prod = input("Indique el nombre del producto que va a agregar: ")
    stock_prod = input("Indique el stock: ")
    dicc_stock[agregar_prod] = stock_prod
print(dicc_stock)

#9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
#   Permití consultar qué actividad hay en cierto día y hora.

print()
print("9) La agenda")


agenda = {
    ("lunes","10:00"): "estudiar",
    ("lunes","12:00"): "gymnasio",
    ("martes","10:00"): "trabajar",
    ("miercoles","10:00"): "siesta",
    ("miercoles","10:00"): "cursar",
    ("jueves","10:00"): "lavar",
    ("viernes","10:00"): "ordenar",
    ("sabado","10:00"): "cursar",

}


agenda_consulta_dia:str = input("Indique el dia que quiere consultar: ")
agenda_consulta_hora:str = input("Indique la hora que quiere consultar: ")

agenda_consulta = (agenda_consulta_dia, agenda_consulta_hora)

if agenda_consulta in agenda:
    print (agenda[agenda_consulta])
else:
    print("Hay un error o no se encuentra el evento")


#10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo 
#   diccionario donde:
#   Las capitales sean las claves.
#   Los países sean los valores.


print()
print("10) Paises y capitales")

dicc_paises = {
    "Argentina":"Buenos Aires",
    "Chile":"Santiago",
    "Uruguay":"Montevideo",
    "Peru":"Lima",
}
print(dicc_paises)

dicc_capitales = {}

for pais, cap in dicc_paises.items():
    dicc_capitales[cap] = pais


print(dicc_capitales)