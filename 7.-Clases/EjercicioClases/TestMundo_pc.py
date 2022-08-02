from Teclado import *
from Raton import *
from Monitor import *
from Computadora import *
from Orden import *

if __name__ == '__main__':
    teclado = Teclado('mecanico','razer')
    raton = Raton('precision','razer')
    monitor = Monitor('hp','22 pulgadas')
    computadora1 = Computadora('mamalona',monitor,teclado,raton)

    orden1 = Orden()
    orden1.agregarComputadora(computadora1)
    print(orden1)