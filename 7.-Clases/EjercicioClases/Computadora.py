class Computadora():
    contadorComputadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contadorComputadoras += 1
        self._idComputadora = Computadora.contadorComputadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def monitor(self):
        return self.monitor

    @monitor.setter
    def monitor(self, monitor):
        self._monitor = monitor

    @property
    def teclado(self):
        return self._teclado

    @teclado.setter
    def teclado(self, teclado):
        self._teclado = teclado

    @property
    def raton(self):
        return self.raton

    @raton.setter
    def raton(self, raton):
        self._raton = raton

    def __str__(self):
        return f'Computadora \n[idComputadora: {self._idComputadora} nombre: {self._nombre} \nMonitor: {self._monitor.__str__()} \nTeclado: {self._teclado.__str__()} \nRaton: {self._raton.__str__()}]'
