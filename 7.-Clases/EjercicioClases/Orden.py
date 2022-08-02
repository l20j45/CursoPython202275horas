class Orden():
    contadorOrdenes = 0
    def __init__(self):
        Orden.contadorOrdenes+=1
        self._idOrden = Orden.contadorOrdenes
        self._computadoras = []

    def agregarComputadora(self,computadora):
        self._computadoras.append(computadora)

    def __str__(self):
        computadorastr = ''
        for computadora in self._computadoras:
            computadorastr +='\n' + computadora.__str__()
        return f'Orden [numero de orden: {self._idOrden} Computadoras{computadorastr}]'