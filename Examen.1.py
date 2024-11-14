# Datos iniciales del almacén
productos_almacen = {
    "Estantería A": [{"nombre": "Chocolate Amargo", "cantidad": 20, "precio": 2.5},
                     {"nombre": "Mermelada de Fresa", "cantidad": 15, "precio": 3.0}],
    "Estantería B": [{"nombre": "Aceitunas Verdes", "cantidad": 50, "precio": 1.5},
                     {"nombre": "Aceite de Oliva Extra", "cantidad": 10, "precio": 6.0}],
    "Estantería C": [{"nombre": "Café Molido", "cantidad": 25, "precio": 5.0},
                     {"nombre": "Té Verde", "cantidad": 40, "precio": 2.0}],
    "Estantería D": [{"nombre": "Pasta Integral", "cantidad": 30, "precio": 1.8},
                     {"nombre": "Arroz Basmati", "cantidad": 20, "precio": 1.7}]
}

# Función para agregar nuevos productos al almacén
def agregar_producto(almacen, estanteria, nombre, cantidad):
    if estanteria not in almacen:
        return f"Esa estantería no existe. Por favor, elija una de las siguientes: {', '.join(almacen.keys())}"
    
    for producto in almacen[estanteria]:
        if producto["nombre"] == nombre:
            producto["cantidad"] += cantidad
            return f"Producto '{nombre}' ya existe. Cantidad actualizada. Precio: {producto['precio']}"

    # Si el producto no existe, se añade con el precio proporcionado
    precio = float(input(f"Introduce el precio para el nuevo producto '{nombre}': "))
    producto = {"nombre": nombre, "cantidad": cantidad, "precio": precio}
    almacen[estanteria].append(producto)
    return f"Producto '{nombre}' agregado correctamente a {estanteria}"

# Función para retirar productos del almacén
def retirar_producto(almacen, nombre, cantidad):
    for estanteria, productos in almacen.items():
        for producto in productos:
            if producto["nombre"] == nombre:
                if producto["cantidad"] >= cantidad:
                    producto["cantidad"] -= cantidad
                    return f"Producto '{nombre}' retirado correctamente"
                else:
                    return f"Error: no hay suficiente cantidad de '{nombre}'"
    return f"Error: producto '{nombre}' no encontrado"

# Función para verificar disponibilidad de un producto
def verificar_disponibilidad(almacen, nombre):
    for estanteria, productos in almacen.items():
        for producto in productos:
            if producto["nombre"] == nombre:
                return f"Producto '{nombre}' está en {estanteria} con {producto['cantidad']} unidades"
    return f"Producto '{nombre}' no encontrado"

# Función para verificar el estado del almacén
def estado_almacen(almacen):
    estado = ""
    total_valor = 0
    valores_estanterias = {}
    for estanteria, productos in almacen.items():
        valor_estanteria = 0
        estado += f"\n{estanteria}:\n"
        for producto in productos:
            estado += f"  - {producto['nombre']}: {producto['cantidad']} unidades a {producto['precio']} cada una\n"
            valor_estanteria += producto['cantidad'] * producto['precio']
        valores_estanterias[estanteria] = valor_estanteria
        total_valor += valor_estanteria
    for estanteria, valor in valores_estanterias.items():
        estado += f"\nValor de {estanteria}: {valor}"
    estado += f"\n\nValor total del almacén: {total_valor}"
    return estado

# Función para transferir productos entre estanterías
def transferir_producto(almacen, nombre, cantidad, origen, destino):
    if origen not in almacen or destino not in almacen:
        return "Error: una o ambas estanterías no existen"
    for producto in almacen[origen]:
        if producto["nombre"] == nombre:
            if producto["cantidad"] >= cantidad:
                producto["cantidad"] -= cantidad
                for prod_dest in almacen[destino]:
                    if prod_dest["nombre"] == nombre:
                        prod_dest["cantidad"] += cantidad
                        return f"Producto '{nombre}' transferido de {origen} a {destino}"
                else:
                    almacen[destino].append({"nombre": nombre, "cantidad": cantidad, "precio": producto["precio"]})
                    return f"Producto '{nombre}' transferido de {origen} a {destino}"
            else:
                return f"Error: cantidad insuficiente de '{nombre}' en {origen}"
    return f"Error: producto '{nombre}' no encontrado en {origen}"

# Función para encontrar la estantería con mayor valor y la con menos productos
def analizar_estanterias(almacen):
    mayor_valor = ("", 0)
    menor_productos = ("", float('inf'))
    for estanteria, productos in almacen.items():
        valor = sum(p["cantidad"] * p["precio"] for p in productos)
        cantidad_productos = sum(p["cantidad"] for p in productos)
        if valor > mayor_valor[1]:
            mayor_valor = (estanteria, valor)
        if cantidad_productos < menor_productos[1]:
            menor_productos = (estanteria, cantidad_productos)
    return f"Estantería con mayor valor acumulado: {mayor_valor[0]}, Estantería con menos productos: {menor_productos[0]}"

# Menú de opciones para gestionar el almacén
def menu():
    while True:
        print("\nGestión de Almacén")
        print("1. Agregar Producto")
        print("2. Retirar Producto")
        print("3. Verificar Disponibilidad")
        print("4. Verificar Estado del Almacén")
        print("5. Transferir Producto")
        print("6. Analizar Estanterías")
        print("0. Salir")
        
        opcion = input("Elige una opción: ")

        if opcion == "1":
            estanteria = input("Estantería (A, B, C, D): ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            print(agregar_producto(productos_almacen, estanteria, nombre, cantidad))

        elif opcion == "2":
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            print(retirar_producto(productos_almacen, nombre, cantidad))

        elif opcion == "3":
            nombre = input("Nombre del producto: ")
            print(verificar_disponibilidad(productos_almacen, nombre))

        elif opcion == "4":
            print(estado_almacen(productos_almacen))

        elif opcion == "5":
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            origen = input("Estantería de origen: ")
            destino = input("Estantería de destino: ")
            print(transferir_producto(productos_almacen, nombre, cantidad, origen, destino))

        elif opcion == "6":
            print(analizar_estanterias(productos_almacen))

        elif opcion == "0":
            break

        else:
            print("Opción no válida, por favor elige de nuevo.")

# Ejecutar el menú
menu()