from DispositivoEntrada import *


class Raton(DispositivoEntrada):
    ContadorRaton = 0

    def __init__(self, tipoEntrada, marca):
        Raton.ContadorRaton += 1
        super().__init__(tipoEntrada, marca)
        self._idRaton = Raton.ContadorRaton

    def __str__(self):
        return f'Raton [id: {self._idRaton} {super().__str__()}]'
