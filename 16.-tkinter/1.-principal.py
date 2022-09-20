# GUI = Graphical User Interface
# Tkinter = Tk interface
# Importamos el modulo Tkinter

import tkinter as tk
import tkinter as ttk

# Creamos un objeto usando la clase Tk

ventana = tk.Tk()

# Modificamos el tamaño de la ventana (pixeles)
ventana.geometry('600x400')
# Cambiamos el nombre de la ventana
ventana.title('Nueva Ventana')
# configuramos el icono de la app
ventana.iconbitmap("./iconos/icono.ico")
# agregamos un boton a la app (widget)
def evento_click():
    boton1.config(text='Botón presionado')
    print('Ejecución del evento_click')
    # Creamos un nuevo botón y lo mostramos
    boton2 = ttk.Button(ventana, text='Nuevo botón')
    boton2.pack()

#otra cosa
boton1= ttk.Button(ventana,text='Dar Click',command=evento_click)
# Utilzamos el layout manager para mostrar el boton
boton1.pack()
# Iniciamos la ventana (esta linea la ejecutamos al final)
# si la ejecutamos antes, no se muestran los cambios anteriores
ventana.mainloop()