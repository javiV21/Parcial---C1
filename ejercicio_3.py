class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Proveedor:
    def __init__(self, nombre, producto, cantidad, precio_sugerido):
        self.nombre = nombre
        self.producto = producto
        self.cantidad = cantidad
        self.precio_sugerido = precio_sugerido

class Venta:
    def __init__(self, productos_vendidos, total_dolares, dinero_entregado, vuelto_dolares):
        self.productos_vendidos = productos_vendidos
        self.total_dolares = total_dolares
        self.dinero_entregado = dinero_entregado
        self.vuelto_dolares = vuelto_dolares

class Tienda:
    def __init__(self):
        self.productos = {}
        self.proveedores = []
        self.ventas = []

    def atender_proveedor(self):
        nombre = input("Ingrese el nombre del proveedor: ")
        producto = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad del producto: "))
        precio_sugerido = float(input("Ingrese el precio sugerido: "))
        
        # Registrar o actualizar producto
        if producto in self.productos:
            self.productos[producto].precio = precio_sugerido
            print(f"El precio del producto '{producto}' ha sido actualizado a ${precio_sugerido:.2f}.")
        else:
            self.productos[producto] = Producto(producto, precio_sugerido)
            print(f"Producto '{producto}' registrado con precio sugerido ${precio_sugerido:.2f}.")
        
        proveedor = Proveedor(nombre, producto, cantidad, precio_sugerido)
        self.proveedores.append(proveedor)
        print(f"Proveedor '{nombre}' atendido y producto '{producto}' registrado con cantidad {cantidad}.")

    def registrar_venta(self):
        productos_vendidos = []
        total_compra = 0
        print("Ingrese los productos vendidos (escriba 'fin' para terminar):")
        
        while True:
            producto = input("Nombre del producto: ")
            if producto.lower() == 'fin':
                break
            precio = float(input(f"Ingrese el precio de {producto}: "))
            cantidad = int(input(f"Cantidad de {producto}: "))
            total_compra += precio * cantidad
            productos_vendidos.append((producto, cantidad, precio))
        
        if total_compra > 0:
            print(f"Total de la venta en dólares: ${total_compra:.2f}")
            
            dinero_entregado = float(input("Ingrese el dinero entregado por el cliente en dólares: "))
            vuelto_dolares = dinero_entregado - total_compra
            
            if vuelto_dolares >= 0:
                venta = Venta(productos_vendidos, total_compra, dinero_entregado, vuelto_dolares)
                self.ventas.append(venta)
                print(f"Vuelto en dólares: ${vuelto_dolares:.2f}")
            else:
                print("El dinero entregado no es suficiente para cubrir la venta.")
        else:
            print("No se realizó ninguna venta.")

    def mostrar_ventas(self):
        if not self.ventas:
            print("No se han registrado ventas.")
            return
        
        print("Ventas realizadas:")
        for i, venta in enumerate(self.ventas, start=1):
            print(f"\nVenta #{i}")
            print("Productos vendidos:")
            for producto, cantidad, precio in venta.productos_vendidos:
                print(f"- {producto}, Cantidad: {cantidad}, Precio unitario: ${precio:.2f}")
            print(f"Total en dólares: ${venta.total_dolares:.2f}")
            print(f"Dinero entregado: ${venta.dinero_entregado:.2f}")
            print(f"Vuelto en dólares: ${venta.vuelto_dolares:.2f}")

def menu():
    tienda = Tienda()
    
    while True:
        print("\n--- Menú de Tienda ---")
        print("1. Atender proveedor")
        print("2. Registrar venta")
        print("3. Mostrar ventas realizadas")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            tienda.atender_proveedor()
        elif opcion == "2":
            tienda.registrar_venta()
        elif opcion == "3":
            tienda.mostrar_ventas()
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Iniciar el menú
menu()
