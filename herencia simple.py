# EJERCICIO 4: Herencia Simple
# Enunciado: Crea una clase Vehiculo con atributo marca y método arrancar().
# Crea una clase Coche que herede de Vehiculo y agregue el atributo num_puertas.

# SOLUCIÓN:
class Vehiculo:
    def __init__(self, marca):
        self.marca = marca
        
    def arrancar(self):
        print("El vehículo arranca")

class Coche(Vehiculo):
    def __init__(self, marca, num_puertas):
        # Llama al constructor de la clase padre (Vehiculo) para asignar la marca
        super().__init__(marca)
        self.num_puertas = num_puertas

# Prueba
coche = Coche("Toyota", 4)
print(f"Marca: {coche.marca}, Puertas: {coche.num_puertas}")
coche.arrancar()
