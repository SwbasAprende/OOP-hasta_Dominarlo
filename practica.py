class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self._salario = salario
    
    def aplicar_aumento(self, porcentaje):
        self.porcentaje = porcentaje
        aumento = self._salario * porcentaje / 100
        self._salario = aumento + self._salario
    
    def __str__(self):
        return f"Nombre:{self.nombre}\nCargo:{self.cargo}\nSalario: ${self._salario:,}"

class Gerente(Empleado):
    def __init__(self, nombre, cargo, salario):
        super().__init__(nombre, cargo, salario)
        self.equipo = []

    
    def agregar_empleado(self, empleado):
        self.equipo.append(empleado)
    
    def total_equipo(self):
        return f"Tiene en su equipo a {len(self.equipo)} trabajador(es)"

# Uso:
emp1 = Empleado("Johan", "Backend", 1800000)
emp1.aplicar_aumento(10)
print("=== EMPLEADO ===")
print(emp1)
print("=== GERENTE ===")
ger1 = Gerente("Paez", "Empresario", 3000000)
ger1.agregar_empleado(emp1)
print(ger1)
print(ger1.total_equipo())
