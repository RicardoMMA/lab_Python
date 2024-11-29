def bienvenida(nombre):
    print(f"¡Bienvenido, {nombre}! Gracias por usar el sistema de facturación.")

def liquidar_producto(nombre_producto, precio, descuento=0.10):
    precio_final = precio * (1 - descuento)
    return {"nombre_producto": nombre_producto, "precio": precio, "descuento": descuento, "precio_final": precio_final}

def mostrar_factura(productos):
    print("\n--- Factura ---")
    for producto in productos:
        print(f"Producto: {producto['nombre_producto']}, Precio: {producto['precio']}, Descuento: {producto['descuento'] * 100}%, Precio Final: {producto['precio_final']}")
    
    producto_mayor_valor = max(productos, key=lambda x: x['precio_final'])
    print(f"\nProducto de mayor valor: {producto_mayor_valor['nombre_producto']} con un precio final de {producto_mayor_valor['precio_final']}")

nombre_usuario = input("Por favor, ingrese su nombre: ")
bienvenida(nombre_usuario)

n = int(input("\n¿Cuántos productos desea ingresar? "))
productos = []

for i in range(n):
    nombre_producto = input(f"\nIngrese el nombre del producto {i + 1}: ")
    precio = float(input(f"Ingrese el precio de {nombre_producto}: "))
    
    descuento = input(f"Ingrese el descuento para {nombre_producto} en porcentaje (deje vacío para aplicar 10% por defecto): ")
    if descuento == "":
        descuento = 0.10
    else:
        descuento = float(descuento) / 100
    
    producto = liquidar_producto(nombre_producto, precio, descuento)
    productos.append(producto)

mostrar_factura(productos)
