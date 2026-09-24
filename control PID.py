# Nombre: Adolfo Contreras
# Sección: SII-S06
# CI: 32145626
# Carrera: Robótica y automatización

class Controlador:
    def __init__(self, nombre, setpoint):
        self.__nombre = nombre
        self._setpoint = setpoint

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def controlar(self):
        print("El controlador ajusta el sistema.")

class ControladorPID(Controlador):
    def __init__(self, nombre, setpoint):
        super().__init__(nombre, setpoint)

    def controlar(self):
        print("Aplicando control PID.")

class ControladorOnOff(Controlador):
    def __init__(self, nombre, setpoint):
        super().__init__(nombre, setpoint)

    def controlar(self):
        print("Aplicando control On/Off.")

if __name__ == "__main__":
    controlador_pid = ControladorPID("PID Temperatura", 150.5)
    controlador_onoff = ControladorOnOff("Termostato Básico", 24.0)

    controlador_pid.controlar()
    controlador_onoff.controlar()