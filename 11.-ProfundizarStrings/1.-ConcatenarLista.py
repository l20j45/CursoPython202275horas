tupla_str = ('Hola','Mundo','universidad','Python')
print(''.join(tupla_str))

lista_cursos = ['Java','JavaScript','Python','Angular','Spring']
mensaje = ''.join(lista_cursos)
print(mensaje)

cadena = 'holaMundo'
print('.'.join(cadena))

print(set(''.join(lista_cursos).lower()))

diccionario = {'nombre':'Juan', 'apellido':'perez', 'edad':'18'}
llaves = '-'.join(diccionario.keys())
values = '-'.join(diccionario.values())
print(llaves,values)