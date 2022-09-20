import tkinter as tk
from tkinter import ttk


#widget events
def evento1():
    boton1.config(text='Boton 1 presionado')
def evento2():
    boton2.config(text='Boton 2 presionado')
def evento3():
    boton3.config(text='Boton 3 presionado')
def evento4():
    boton4.config(text='Boton 4 presionado', fg='blue',relief=tk.GROOVE) #elementos solo de TK

#main container
ventana = tk.Tk()
ventana.geometry("600x400")
ventana.title("Manejo de grid")
ventana.iconbitmap("./iconos/icono.ico")
#main container configurations
ventana.rowconfigure(0,weight=1)
ventana.rowconfigure(1,weight=5)
ventana.columnconfigure(0,weight=1)
ventana.columnconfigure(1,weight=10)
#widgets or elements
boton1 = ttk.Button(ventana, text="Boton 1",command=evento1)
boton2 = ttk.Button(ventana, text="Boton 2",command=evento2)
boton3 = ttk.Button(ventana, text="Boton 3",command=evento3)
boton4 = tk.Button(ventana, text="Boton 4",command=evento4)
#widget configuration
boton1.grid(row=0, column=0,sticky='NSWE', padx=40, pady=40, ipadx=20, ipady=20, columnspan=2)
boton2.grid(row=1, column=0,sticky='NSWE')
#boton3.grid(row=0, column=1,sticky='NSWE')
boton4.grid(row=1, column=1,sticky='NSWE')



ventana.mainloop()