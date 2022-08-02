from DispositivoEntrada import *


class Teclado(DispositivoEntrada):
    ContadorTeclado = 0
    def __init__(self,tipoEntrada,marca):
        Teclado.ContadorTeclado +=1
        super().__init__(tipoEntrada,marca)
        self._idTeclado =Teclado.ContadorTeclado

    def __str__(self):
        return f'Teclado [id: {self._idTeclado} {super().__str__()}]'
