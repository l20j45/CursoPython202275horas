class aritmetica :
    """
    Clase arimetica para sumar restar y etc.
    """
    def __init__(self,operandoA,operandoB):
        self.operandoA=operandoA
        self.operandoB=operandoB

    def sumar(self):
        return self.operandoA+self.operandoB
    def multiplicar(self):
        return self.operandoA-self.operandoB
    def restar(self):
        return self.operandoA*self.operandoB
    def dividir(self):
        return self.operandoA/self.operandoB

arimetica1 =aritmetica(5,6)
print(arimetica1.sumar())
print(arimetica1.restar())
print(arimetica1.multiplicar())
print(arimetica1.dividir())