numero: float = int(input("Ingresa un numero: "))

valorMinimo: float = 0
valorMaximo: float = 5

if valorMinimo <= numero <= valorMaximo:
    print(f"el {numero} esta en el rango")
else:
    print(f"{numero} no esta en el rango")
