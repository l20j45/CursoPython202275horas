texto = ""
calificacion = float(input("Ingresa tu calificacion: "))
if 9 <= calificacion <= 10:
    texto = "A"
elif 8 <= calificacion <= 9:
    texto = "B"
elif 7 <= calificacion <= 8:
    texto = "C"
elif 6 <= calificacion <= 7:
    texto = "D"
elif 0 <= calificacion <= 6:
    texto = "F"
else:
    print("Valor incorrecto")
print(texto)
