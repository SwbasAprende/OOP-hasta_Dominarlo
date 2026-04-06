class Libro:
    
    def __init__(self, nombre, autor, año):
        self._nombre = nombre
        self._autor = autor
        self._año = año
        
    def __str__(self):
        return f"El {self._nombre} fue escrito por {self._autor} en el año {self._año}"
    
class Biblioteca:
    def __init__(self, nombre, autor, año):
        self.nombre = nombre
        self.autor = autor
        self.año = año
        self.estanteria = []
        
    def agregar_libro(self, libro):
        self.estanteria.append(libro)
        
    def total_libros(self):
        return f"La estanteria cuenta con {len(self.estanteria)} libro(s)"
    
    def __str__(self):
        return f"El {self.nombre} fue escrito por {self.autor} en el año {self.año}"
        
lib1 = Libro("Principito", "David Beckham", 2002)
print(lib1)
ubi1 = Biblioteca("Jardin", "Profes", 2012)
ubi1.agregar_libro(lib1)
ubi1.agregar_libro(ubi1)
print(ubi1)
print(ubi1.total_libros())