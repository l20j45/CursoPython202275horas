def imprimirNumeros(numero):
    if numero > 0:
        print (numero)
        imprimirNumeros(numero-1)
    elif numero==0:
        return
    else:
        print("numero no valido pa")

imprimirNumeros(5)