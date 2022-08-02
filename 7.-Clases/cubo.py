class rectangulo:
    def __init__(self,base,altura,profundidad):
        self.base=base
        self.altura=altura
        self.profundidad=profundidad

    def area(self):
        return self.base*self.altura*self.profundidad

area = float(input("Proporciona la base: "))
altura = float(input("Proporciona la altura: "))
profundidad = float(input("Proporciona la profundidad: "))
rectangulo1 = rectangulo(area,altura,profundidad)
print(f'area rectangulo {rectangulo1.area()}')