class Orden():
    contador_ordenes = 0
    def __init__(self ,productos):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._productos = list(productos)

    def agregarProductos(self,producto):
        self._productos.append(producto)

    def calcularTotal(self):
        total = 0
        for product in self._productos:
            total += product.precio
        return f'{total:,.2f}'

    @property
    def id_orden(self):
        return self._id_orden

    @id_orden.setter
    def id_orden(self, id_orden):
        self._id_orden = id_orden

    def __str__(self):
        productos_str = ''
        for product in self._productos:
            productos_str += '\n' + product.__str__() + '|'
        return f'Orden: [id orden:{self._id_orden},\nproductos: {productos_str}]'



if __name__ == '__main__':
    orden1=Orden(5,5,4,6,7,8,2,6)
    orden2=Orden(3,5,4,6,7,8,2,6)
    print(orden1)
    print(orden1.contador_ordenes)
    print(orden2)
    print(orden2.contador_ordenes)