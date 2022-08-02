class Persona:
    def __init__(self,nombre,edad):
        self._nombre=nombre
        self._edad=edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self.edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def __str__(self):
        return f'Persona: [nombre: {self._nombre} edad: {self._edad}]'

class Empleado(Persona):
    def __init__(self,nombre,edad,sueldo):
        super().__init__(nombre,edad)
        self._sueldo = sueldo

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo

    def __str__(self):
        return f'Empleado: [sueldo: {self.sueldo}] {super().__str__()} '

if __name__ == '__main__':
    empleado1 = Empleado('Juan',28,5000)
    print(empleado1.nombre)
    print(empleado1.sueldo)
