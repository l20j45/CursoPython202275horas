from logging.config import valid_ident
import tkinter as tk
from tkinter import ttk, messagebox


#widget events
def evento1():
    print(entrada1.get())
    etiqueta1.config(text=entrada1.get())
    if entrada1.get():
        messagebox.showinfo('Mensaje Informativo', entrada1.get() + ' Informativo')
        messagebox.showerror('Mensaje Error', entrada1.get() + ' Error')
        messagebox.showwarning('Mensaje Alerta', entrada1.get() + ' Alerta')
    entrada1.delete(0,tk.END)


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
entrada1= ttk.Entry(ventana,width=30,justify=tk.CENTER)
etiqueta1 = tk.Label(ventana,text ="Aqui se mostrara el contenido de la caja de texto")
boton1 = ttk.Button(ventana, text="enviar",command=evento1)



#widget configuration
entrada1.grid(row=0,column=0,sticky='NSWE',padx=10,pady=10)
etiqueta1.grid(row=1,column=0,sticky='NSWE',padx=10,pady=10)
boton1.grid(row=2, column=0,sticky='NSWE')


ventana.mainloop()