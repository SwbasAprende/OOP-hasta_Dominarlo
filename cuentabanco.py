class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Su deposito fue exitoso ✅\nUsted deposito ${cantidad:,} C0P")
    
    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("❌error: Fondos insuficientes")
        elif self.saldo >= 0:
            self.saldo -= cantidad
            print(f"Su retiro fue exitoso ✅\nUsted retiro ${cantidad:,}C0P")
    
    def __str__(self):
        return f"=== TITULAR DE LA CUENTA ===\nTitular: {self.titular}\nTu cuenta tiene ${self.saldo:,} C0P"

class CuentaPremium(CuentaBancaria):
    def __init__(self, titular, saldo, limite_sobregiro):
        super().__init__(titular, saldo)
        self.limite_sobregiro = limite_sobregiro
        
    def retirar(self, cantidad):
        if cantidad > self.limite_sobregiro + self.saldo:
            print("❌error: Fondos insuficientes")
        else:
            self.saldo -= cantidad
            print(f"Su retiro fue exitoso ✅\nUsted retiro ${cantidad:,} C0P")
    
    def __str__(self):
        return f"=== TITULAR DE LA CUENTA ===\nTitular: {self.titular}\nTu cuenta tiene ${self.saldo:,} C0P\nTu limite de sobregiro es de ${self.limite_sobregiro:,} C0P"
# Prueba
# per1 = CuentaBancaria("Sebas", 2000000)
# print(per1)
# per1.depositar(int(input("Cantidad a depositar: ")))
# print(per1)
# per1.retirar(int(input("Cantidad a retirar: ")))
per2 = CuentaPremium("Lic. Armando", -500000, 1000000)
print(per2)
per2.retirar(int(input("Cantidad a retirar: ")))
print(per2)

