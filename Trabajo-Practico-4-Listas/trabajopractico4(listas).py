#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
#range.
listaA:list = ["A", 5, 8]
listaB:list = [1, 5, "PATO"]

listaC:list = listaA + listaB
print(listaC)

print("----------------------------------------")

print("punto 1")

lista:list = list(range(4,101,4))

print(lista)


#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
#penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
#indexing con números negativos!
print("----------------------------------------")

print("punto 2")

lista2: list = ["A", 2, 5, "hola", False]
print(lista2)
lista_penultimo:list = lista2[-2]

print(lista_penultimo)


#3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
#pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por
#ejemplo:
#lista_vacia = []
print("----------------------------------------")
print("punto 3")
lista_vacia: list = []

lista_vacia.append("pato")
lista_vacia.append("leon")
lista_vacia.append("serpiente")

print(lista_vacia)

#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
#respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
#en los videos o bien investigar cómo funciona el indexing con números negativos!
#animales = ["perro", "gato", "conejo", "pez"]"""
print("----------------------------------------")
print("punto 4")

animales: list = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[3] = "oso"

print(animales)

#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
print("----------------------------------------")
print("punto 5")
numeros: list = [8,15,3,22,7]
numeros.remove(max(numeros))
print(numeros)
print("El programa remueve el elemento con mayor valor de la lista")


#6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
#pantalla los dos primeros.
print("----------------------------------------")
print("punto 6")
lista3:list = []

for i in range (10, 31):
    if i%5 == 0:
        lista3.append(i)

rango_lista: list = lista3 [0:2]
print(rango_lista)

#7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
#cualesquiera.
#autos = ["sedan", "polo", "suran", "gol"]
print("----------------------------------------")
print("punto 7")

autos:list = ["sedan", "polo", "suran", "gol"]
autos[1] = "corsa"
autos[2] = "yaris"

print(autos)


#8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
#directamente. Imprimir la lista resultante por pantalla."""
print("----------------------------------------")
print("punto 8")

lista_dobles: list = []
for i in range (5,16):
    if i%5 == 0:
        lista_dobles.append(i*2)
print(lista_dobles)



#9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
#diferentes clientes:
#compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
#["agua"]]
#a) Agregar "jugo" a la lista del tercer cliente usando append.
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
#c) Eliminar "pan" de la lista del primer cliente.
#d) Imprimir la lista resultante por pantalla"""
print("----------------------------------------")
print("punto 9")
compras:list = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)


#10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
#● Posición lista_anidada[0]: 15
#● Posición lista_anidada[1]: True
#● Posición lista_anidada[2][0]: 25.5
#● Posición lista_anidada[2][1]: 57.9
#● Posición lista_anidada[2][2]: 30.6
#● Posición lista_anidada[3]: False
#Imprimir la lista resultante por pantalla."""
print("----------------------------------------")
print("punto 10")
lista_anidada:list = []
lista_anidada.append([]) 
lista_anidada[0].append(15)
lista_anidada.append(True)     
lista_anidada.append([25.5, 57.9, 30.6])  
lista_anidada.append(False)
print(lista_anidada)
