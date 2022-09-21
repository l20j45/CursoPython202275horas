from logging.config import valid_ident
import tkinter as tk
from tkinter import ttk


#widget events
def evento1():
    print(entrada1.get())
    entrada2.config(state='normal')
    entrada2.delete(0,tk.END)
    entrada2.insert(0,entrada1_var1.get())
    entrada2.config(state='readonly')
    entrada1.delete(0,tk.END)
    entrada2.select_range(0,tk.END)
    entrada2.focus()

#main container
ventana = tk.Tk()
ventana.geometry("600x400")
ventana.title("Manejo de grid")
ventana.iconbitmap("./iconos/icono.ico")
#main container configurations
ventana.rowconfigure(0,weight=2)
ventana.rowconfigure(1,weight=5)
ventana.rowconfigure(2,weight=5)
ventana.columnconfigure(0,weight=1)

#widgets or elements
entrada1_var1=tk.StringVar(value="Ingresa la query")
entrada1= ttk.Entry(ventana,width=30,justify=tk.CENTER, textvariable=entrada1_var1)
entrada1.grid(row=0,column=0,sticky='NSWE',padx=10,pady=10)
entrada2= ttk.Entry(ventana,width=30,justify=tk.CENTER)
entrada2.grid(row=1,column=0,sticky='NSWE',padx=10,pady=10)
boton1 = ttk.Button(ventana, text="Boton 1",command=evento1)

#widget configuration
boton1.grid(row=2, column=0,sticky='NSWE')


ventana.mainloop()