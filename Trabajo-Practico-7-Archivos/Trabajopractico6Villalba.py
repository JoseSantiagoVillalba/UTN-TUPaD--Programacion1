import os

archivo = "productos.txt"

if not os.path.exists(archivo):
    with open(archivo, "w", encoding="utf-8") as f:
        f.write("Lapicera,120.5,30 \n")
        f.write("Cuaderno,250,50 \n")
        f.write("Mochila,1500,10 \n")


productos = []
with open(archivo, "r", encoding="utf-8") as f:
    for linea in f:
        linea = linea.strip()
        if linea:  # ignorar líneas vacías
            nombre, precio, cantidad = linea.split(",")
            producto = {
                "nombre": nombre,
                "precio": float(precio),
                "cantidad": int(cantidad)
            }
            productos.append(producto)


print("\nListado de productos:")
for p in productos:
    print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")


nuevo_nombre = input("\nIngrese el nombre del nuevo producto: ")
nuevo_precio = float(input("Ingrese el precio del nuevo producto: "))
nueva_cantidad = int(input("Ingrese la cantidad del nuevo producto: "))

nuevo_producto = {
    "nombre": nuevo_nombre,
    "precio": nuevo_precio,
    "cantidad": nueva_cantidad
}

productos.append(nuevo_producto)


buscar = input("\nIngrese el nombre de un producto a buscar: ")
encontrado = False
for p in productos:
    if p["nombre"].lower() == buscar.lower():
        print(f"Producto encontrado: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
        encontrado = True
        break
if not encontrado:
    print("Producto no encontrado.")


with open(archivo, "w", encoding="utf-8") as f:
    for p in productos:
        f.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

print("\nArchivo productos.txt actualizado correctamente.")
