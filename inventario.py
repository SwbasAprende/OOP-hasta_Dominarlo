class Inventario:
    def __init__(self):
        self.productos = []
        
    def agregar_producto(self, nombre, precio, cantidad):
        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        }
        self.productos.append(producto)
        print(f"{producto['nombre']}, Agregado correctamente ✅")
        
    def vender_producto(self, nombre, venta):
        for producto in self.productos:
            if producto['nombre'].lower() == nombre.lower():
                if venta > producto['cantidad']:
                    print("⚠️  verifique la cantidad a comprar")
                    break
                else:
                    producto['cantidad'] -= venta
                    print("Su compra fue exitosa!")
                    break
        else:
            print("error: este producto no existe!")
    def reporte(self):
        total = 0
        for producto in self.productos:
            totalRep = producto['cantidad'] * producto['precio']
            total += totalRep 
            print(f"{producto['nombre']}: {producto['precio']:,} x {producto['cantidad']} = {totalRep:,}\n----------------")
        print(f"TOTAL INVENTARIO: ${total:,}")
        
cl1 = Inventario()
while True:
    print("----- Menú del inventario -----")
    print("1. Agregar producto")
    print("2. Vender producto")
    print("3. Ver reporte")
    print("4. Salir")
    
    opcion = input("Ingrese una opcion: ")
    
    if opcion == "1":
        cl1.agregar_producto(input("Nombre: "), int(input("Precio: ")), int(input("Cantidad: ")))
        print("===" * 10)
    elif opcion == "2":
        cl1.vender_producto(input("Nombre del producto a vender: "), int(input("Cantidad?: ")))
    elif opcion == "3":
        print("=== TABLA DE REPORTE ===")
        cl1.reporte()
    elif opcion == "4":
        print(" ⌛ Saliendo...")
        break
    else:
        print("error: esta opcion no existe")