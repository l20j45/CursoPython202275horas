lista=["poliedro","policia","polifonia","polinizar","polaridad","politica"]
d = zip(*(lista))
prefijo=""
for count,letters in enumerate(d):
    if len(set(letters)) !=1:
        break
    else:
        prefijo+=letters[count]
if prefijo =="":
    mensaje ="No hay prefijos similares"
else:
    mensaje="Predijos similares: "
print(mensaje , prefijo)