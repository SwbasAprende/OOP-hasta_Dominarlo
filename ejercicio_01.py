# Sistema simple de Empleados.

class Empleados:    

    def aumento_salario(self):
        nombre = input("Nombre: ")
        cargo = input("Cargo: ")
        _salario = float(input("Salario: "))
        porcentaje = int(input("%: "))
        aumento = _salario * porcentaje / 100        
        total = _salario + aumento
        print(f"{nombre} es {cargo} y su sueldo es de {total:,}")

empleado = Empleados()
empleado.aumento_salario()

class Gerente(Empleados):
    nombre = input("Nombre: ")
    num_empleados = int(input("N°Empleados: "))
    
    def agregar_empleado(self):
        nombre = input("Nombre: ")
        cargo = input("Cargo: ")
        _salario = float(input("Salario: "))
        equipo = []
        equipo.append(empleado)
        if empleado:
            self.num_empleados += 1
            print("✅ Empleado agregado correctamente")
        print(f"{nombre} {cargo} es parte del equipo del gerente {self.nombre} y con el son {self.num_empleados} a su cargo")
grupo = Gerente()
grupo.agregar_empleado()