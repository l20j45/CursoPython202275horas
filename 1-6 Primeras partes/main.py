Numero = input("Ingresa el numero")

print(f'Numero: {Numero}')

print(f'numero al reves: {"".join(reversed(Numero))}')
if Numero == "".join(reversed(Numero)):
    print("capicua pa")
else:
    print("no es capicua pa")
