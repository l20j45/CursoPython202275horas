class Pelicula:
    contadorPeliculas =0
    def __init__(self, nombre):
        Pelicula.contadorPeliculas += 1
        self._id=Pelicula.contadorPeliculas
        self._nombre = nombre
        
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, value):
        self._nombre = value
        
    def __str__(self) -> str:
        return f"Pelicula {self._id} (nombre {self._nombre})"
        
if __name__ == "__main__":
    pelicula1 =Pelicula("aladin")
    pelicula2 =Pelicula("boji")
    print(pelicula1)
    print(pelicula2)