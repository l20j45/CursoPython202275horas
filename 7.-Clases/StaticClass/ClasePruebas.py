class MiClase:
    variable_clase = 0

    def __init__(self,variableInstancia):
        self.variableInstancia = variableInstancia
        MiClase.variable_clase += 1

    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)

    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

MiClase.metodo_estatico()
MiClase.metodo_clase()