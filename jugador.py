class Jugador:
    def __init__(self, nombre, nivel, rango):
        self.nombre = nombre
        self.nivel = nivel
        self.rango = rango
    
    def subir_nivel(self):
        self.nivel += 1
        return f"{self.nombre} Nivel actualizado correctamente ✅\nNivel: {self.nivel}"

    def __str__(self):
        return f"Nombre: {self.nombre}\nNivel: {self.nivel}\nRango: {self.rango}"
    
class JugadorVIP(Jugador):
    def __init__(self, nombre, nivel, rango, beneficios):
        super().__init__(nombre, nivel, rango)
        self.beneficios = beneficios
        
    def __str__(self):
        return f"Nombre: {self.nombre}\nNivel: {self.nivel}\nRango: {self.rango}\nBeneficio: {self.beneficios}"
    
        
# Prueba
id1 = Jugador("Paaez", 17, "Diamante")
id2 = Jugador("jota", 22, "Heroico")
id3 = JugadorVIP("Julian", 45, "Gran maestro", "skin exclusiva")
print(id1)
print(id2)
print(id1.subir_nivel())
print(id3)
print(id3.subir_nivel())
