from HerenciaMultiple.Color import Color
from HerenciaMultiple.FiguraGeometrica import FiguraGeometrica


class Rectangulo(FiguraGeometrica,Color):
    def __init__(self,base,altura,color):
        FiguraGeometrica.__init__(self,base,altura)
        Color.__init__(self,color)

    def calcularArea(self):
        return self._alto * self._ancho

    def __str__(self):
        return f'Area : [area : {self.calcularArea()}] {FiguraGeometrica.__str__(self)} {Color.__str__(self)}'
