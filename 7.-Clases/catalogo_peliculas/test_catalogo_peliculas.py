import sys
import os
from time import sleep
sys.path.insert(0, 'dominio')
sys.path.insert(0, 'servicio')

from CatalogoPeliculas import CatalogoPeliculas
from Pelicula import Pelicula



def menu():
    print("""Menu
    1) Agregar peliculas
    2) Listar Peliculas
    3) Eliminar archivos de peliculas
    4) Salir""")


opcion = 0

while opcion != 4:
    os.system("clear")
    menu()
    catalogo = CatalogoPeliculas('catalogo')
    opcion = int(input("Ingresa la opcion: "))
    if opcion == 1:
        nombrePelicula = input("Ingresa el nombre de la pelicula ")
        pelicula = Pelicula(nombrePelicula)
        catalogo.agregarPelicula(pelicula)
        sleep(2)
    elif opcion == 2:
        catalogo.listarPeliculas()
        sleep(10)
    elif opcion == 3:
        catalogo.eliminarDatos()
        sleep(2)
    elif opcion == 4:
        print("Saliendo del programa gracias".center(60, '#'))
        sleep(2)
    else:
        print("Opcion no reconocida")
        sleep(2)
