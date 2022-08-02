class Productos():
    contador_productos = 0
    def __init__(self,nombre,precio):
        Productos.contador_productos+=1
        self._id_producto = Productos.contador_productos
        self._nombre = nombre
        self._precio = precio


    @property
    def id_producto(self):
        return self._id_producto

    @id_producto.setter
    def id_orden(self, id_producto):
        self._id_producto = id_producto    \

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        self._precio = precio

    def __str__(self):
        return f'producto [id_producto: {self._id_producto} nombre = {self._nombre} precio {self._precio}]'



if __name__ == '__main__':
    productos1=Productos(1,'colisionador de drones',99999)
    productos2=Productos(2,'colisionador de mentones',888888)

    print(productos1)
    print(productos1.contador_productos)
    print(productos2)
    print(productos2.contador_productos)