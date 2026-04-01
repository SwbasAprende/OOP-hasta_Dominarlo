class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self._salario = salario
    
    def aplicar_aumento(self, porcentaje):
        self.porcentaje = porcentaje
        aumento = self._salario * porcentaje / 100
        total = aumento + self._salario
        return f"$:{total:,}"
    
    def __str__(self):
        return f"Nombre:{self.nombre}\nCargo:{self.cargo}\nSalario: ${self._salario}"

class Gerente(Empleado):
    def __init__(self, nombre, cargo, salario):
        super().__init__(nombre, cargo, salario)
        self.equipo = []

    
    def agregar_empleado(self, empleado):
            if empleado:
                self.equipo.append(empleado)
    
    def total_equipo(self):
        return f"en el equipo hay {len(self.equipo)} trabajadores."

# Uso:
emp1 = Empleado("Johan", "Backend", 1750000)
emp1.aplicar_aumento(10)
print(emp1)