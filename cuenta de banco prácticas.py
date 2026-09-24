# SOLUCIÓN:
class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.__saldo = saldo_inicial  # Atributo privado corregido

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito exitoso. Nuevo saldo: ${self.__saldo}")
        else:
            print("La cantidad a depositar debe ser mayor a cero.")

    def retirar(self, cantidad):
        if cantidad <= 0:
            print("La cantidad a retirar debe ser mayor a cero.")
        elif cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Retiro exitoso. Nuevo saldo: ${self.__saldo}")
        else:
            print("Saldo insuficiente")

# Prueba
cuenta = CuentaBancaria(1000)
cuenta.depositar(500)
cuenta.retirar(300)
