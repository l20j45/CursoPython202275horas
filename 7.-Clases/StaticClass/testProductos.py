from Orden import Orden
from Productos import Productos

productos1 = Productos('colisionador de drones', 1)
productos2 = Productos('colisionador de mentones', 2)
print(productos1)
print(productos2)
orden1 = Orden([productos1,productos2])
print(orden1)
print(f'total: {orden1.calcularTotal()}')

