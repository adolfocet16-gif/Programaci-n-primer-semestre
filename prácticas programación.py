# Enunciado: Crea una clase Perro con atributos nombre y edad.
# Agrega un método ladrar() que imprima "¡Guau!".
# Instancia un objeto y muestra sus atributos.
# SOLUCIÓN:

class Perro:
    # Corrección: Se agregaron los dobles guiones bajos a __init__
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def ladrar(self):
        # Corrección: Sintaxis limpia de la cadena de texto
        print("¡Guau!")

# Prueba
mi_perro = Perro("Rex", 3)
print(f"{mi_perro.nombre} tiene {mi_perro.edad} años")
mi_perro.ladrar()
