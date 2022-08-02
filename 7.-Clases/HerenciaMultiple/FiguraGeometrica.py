# ABC= ABSTRACT BASE CLASS
from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self,ancho,alto):
        self._ancho = ancho
        self._alto = alto

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        self._alto = alto

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho

    @abstractmethod
    def calcularArea(self):
        pass

    def __str__(self):
        return f'Figura Geometrica: [alto: {self._alto} ancho: {self._ancho}]'


