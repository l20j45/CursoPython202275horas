texto=""
edad = int(input("proporciona tu edad: "))
if 0 <= edad <= 10:
    texto = "0-10 la infancia es increible"
elif 10 <= edad <= 20:
    texto = "10-20 Muchos cambios y mucho estudio"
elif 20 <= edad <= 30:
    texto = "20-30 Amor y comienza el trabajo"
else :
    print("Cualquier otro valor: Etapa de la vida no reconocida")
print(texto)
