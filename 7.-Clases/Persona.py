class Persona:
    def __init__(self,nombre,apellido,edad,*args):
        self._nombre=nombre
        self._apellido=apellido
        self._edad=edad
        self._valores=args

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return _apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    @property
    def valores(self):
        return self._valores

    @valores.setter
    def valores(self, valores):
        self._valores = valores

    def mostrar_detalle(self):
        print(f'edad:{self._edad} nombre: {self._nombre} apellido: {self._apellido} {self._valores} ')

    def __del__(self):
        print(f'Persona: {self._nombre} Apellido: {self._apellido}')
if __name__ == '__main__':
    persona1 = Persona("daniel","Rojas",28,455585,2,3,5 )
    persona1.mostrar_detalle()
    print(persona1.nombre)
    persona1.nombre = "luis"
    print(persona1.nombre)