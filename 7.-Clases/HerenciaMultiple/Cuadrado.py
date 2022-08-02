from HerenciaMultiple.Color import Color
from HerenciaMultiple.FiguraGeometrica import FiguraGeometrica


class Cuadrado (FiguraGeometrica,Color):
    def __init__(self,lado,color):
        FiguraGeometrica.__init__(self,lado,lado)
        Color.__init__(self,color)

    def calcularArea(self):
        return self._alto * self.ancho

    def __str__(self):
        return f'Cuadrado : [area : {self.calcularArea()}] {FiguraGeometrica.__str__(self)} {Color.__str__(self)}'
