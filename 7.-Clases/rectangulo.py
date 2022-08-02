class rectangulo:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura

    def area(self):
        return self.base*self.altura

area = float(input("Proporciona la base: "))
altura = float(input("Proporciona la altura: "))
rectangulo1 = rectangulo(area,altura)
print(f'area rectangulo {rectangulo1.area()}')