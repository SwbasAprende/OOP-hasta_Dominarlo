class Vehiculo:
    def __init__(self, marca, modelo, velocidad):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        
    def acelerar(self, cantidad):
        self.velocidad += cantidad
        print(f"Su velocidad ahora es de {self.velocidad} kms/h ⏱️")
    
    def frenar(self, cantidad):
        if cantidad > self.velocidad:
            print("❌error: no se puede cumplir")
        elif cantidad >= self.velocidad:
            self.velocidad = 0
            print(f"El vehiculo se detuvo por completo 🚗")
        else:
            self.velocidad -= cantidad
            print(f"Su velocidad ahora es de {self.velocidad} kms/h ⏱️")   
# Prueba
cond1 = Vehiculo("Susuki", 86, 58)
# cond1.acelerar(int(input("Cuantos kms quiere acelerar: ")))
cond1.frenar(58)
cond2 = Vehiculo("Ferrari", 91, 158)
cond2.frenar(int(input("Cuantos kms quiere frenar: ")))