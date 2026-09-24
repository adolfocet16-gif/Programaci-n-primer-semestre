class Actuador:
    def __init__(self, nombre):
        # Atributo privado
        self.__nombre = nombre
        # Atributo protegido (inicia en False)
        self._estado = False
        
    # Encapsulamiento del nombre con @property
    @property
    def nombre(self):
        return self.__nombre
        
    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def activar(self):
        self._estado = True
        print("Actuador activado.")

    def estado(self):
        if self._estado:
            print(f"El actuador {self.nombre} está activo.")
        else:
            print(f"El actuador {self.nombre} está inactivo.")

class Motor(Actuador):
    def __init__(self, nombre):
        super().__init__(nombre)
        
    def girar(self):
        print("Motor girando a 100 RPM.")

class Servo(Actuador):
    def __init__(self, nombre):
        super().__init__(nombre)
        
    def mover_angulo(self, angulo):
        print(f"Servo movido a {angulo}º.")

# --- Requisitos de ejecución ---

# Crea un objeto de cada clase
motor_principal = Motor("Motor A")
servo_brazo = Servo("Servo B")

# Comprobación de estado inicial (opcional, para verificar)
motor_principal.estado()

# Actívalos
motor_principal.activar()
servo_brazo.activar()

# Vuelve a comprobar el estado para ver el cambio
motor_principal.estado()

# Usa su método extra
motor_principal.girar()
servo_brazo.mover_angulo(45)
