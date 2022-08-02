edad: int = int(input("Ingresa tu edad: "))

if 20 <= edad < 30 or 30 <= edad < 40:
    if 20 <= edad < 30:
        print('edad dentro de los 20\'s')
    elif 30 <= edad < 40:
        print('edad dentro de los 30\'s')
else:
    print(f"{edad} no esta en el rango")
