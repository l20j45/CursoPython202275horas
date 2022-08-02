from ManejoArchivos import ManejoArchivos
import os

class CatalogoPeliculas:
    def __init__(self,ruta):
        self._ruta = ruta
        
    @property
    def ruta(self):
        return self._ruta
    @ruta.setter
    def ruta(self,value):
        self._ruta = value
        
    def agregarPelicula(self,pelicula):
        archivo = open(self._ruta+'.txt','a',encoding='utf-8')
        print("Registro guardado".center(50,'-'))
        archivo.write(pelicula.__str__() +'\n')
        
    def listarPeliculas(self):
        try:
            archivo = open(self._ruta+'.txt','r',encoding='utf-8')
            for linea in (archivo):
                print(f'{linea}')
        except Exception as e:
            print (F"Error: {e} ".center(50,'-'))
        
    def eliminarDatos(self):
        print("eliminando datos".center(50,'x'))
        os.remove(self._ruta+'.txt')
     