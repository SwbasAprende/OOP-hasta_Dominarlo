class Cafe:
    
    def __init__(self, mesa, sillas, empleados):
        self.mesa = mesa
        self.sillas = sillas
        self.empleados = empleados
    
    def agregar_mesas(self, agregar):
        disponibles = []    
        if self.mesa == 0:
            self.mesa += agregar    
            disponibles.append(agregar)
            print(f"{agregar} mesa(s) agregada(s)\nTotal mesas: {self.mesa}")
        elif self.mesa >= 1:    
            print("Mesas suficientes")
            
    def agregar_sillas(self, cantidad):
        self.sillas += cantidad
        print(f"{cantidad}, sillas agregadas\nTotal: {self.sillas}")
        
    def agregar_empleados(self, contrato):
        self.empleados += contrato
        print(f"{contrato} Empleado(s) agregado(s) correctamente ✅")

    def __str__(self):
        return f"Su local cuenta con:\nMesas: {self.mesa}\nSillas: {self.sillas}\nEmpleados: {self.empleados}"
print("--- Bienvenido a Café ---")
print("Le haremos una breve encuesta para saber que tan grande es su local.\nUsted cuenta con")
cliente1 = Cafe(int(input("Cuantas mesas: ")), int(input("Cuantas sillas: ")), int(input("Cuantos empleados: ")))
print("==" * 20)
while True:
    print("------- BIENVENIDO JEFE --------")
    print("¿Que vamos hacer hoy?")
    print("0. Ver mi local")
    print("1. Agregar mesas")
    print("2. Agregar sillas")
    print("3. Agregar empleados")
    print("4. Salir")
    
    opcion = input("En que te ayudo?:")
    if opcion == "1":
        cliente1.agregar_mesas(int(input("Cuantas?:")))
        print("=" * 20)
    elif opcion == "2":
        cliente1.agregar_sillas(int(input("Cuantas?:")))
        print("=" * 20)
    elif opcion == "3":
        cliente1.agregar_empleados(int(input("Cuantos?:")))
        print("=" * 20)
    elif opcion == "4":
        print("⌛ Saliendo...")
        break
    elif opcion == "0":
        print(cliente1)
        print("=" * 20)
    else:
        print("Esta opcion no existe!")