print("Proporcione los siguientes datos del libro:")
nombreLibro=input("Proporcione el nombre:")
idLibro=input("Proporcione el ID:")
precioLibro=float(input("Proporcione el precio:"))
envioLibro=input("Indica si el envio es gratio (True/False) :")
print(f"""
Nombre: {nombreLibro}
Id: {idLibro}
Precio: {precioLibro}
Envio Gratuito: {envioLibro}
""")
