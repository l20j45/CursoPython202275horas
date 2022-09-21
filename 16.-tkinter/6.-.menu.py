from logging.config import valid_ident
import sys
import tkinter as tk
from tkinter import Menu, ttk, messagebox


#widget events
def evento1():
    print(entrada1.get())
    etiqueta1.config(text=entrada1.get())
    if entrada1.get():
        messagebox.showinfo('Mensaje Informativo', entrada1.get() + ' Informativo')
        messagebox.showerror('Mensaje Error', entrada1.get() + ' Error')
        messagebox.showwarning('Mensaje Alerta', entrada1.get() + ' Alerta')
    entrada1.delete(0,tk.END)

def salir():
    ventana.quit()
    ventana.destroy()
    sys.exit(0)

def crearMenu():
    #configurar menu principal
    menu_principal=Menu(ventana)
    #tearoff = false, para evitar que se separe el menu de la interfaz
    submenu_archivo=Menu(menu_principal,tearoff=0)
    # Agregamos una nueva opcion al menu de archivo
    submenu_archivo.add_command(label="Nuevo")
    #agregamos un separador
    submenu_archivo.add_separator()
    submenu_archivo.add_command(label="Salir",command=salir)
    # Agregamos el submenu al menu principal
    submenu_archivo2=Menu(menu_principal,tearoff=0)
    # Agregamos una nueva opcion al menu de archivo
    submenu_archivo2.add_command(label="Acerca de")
    #agregamos un separador
    submenu_archivo2.add_separator()
    submenu_archivo2.add_command(label="Actualizaciones")
    
    menu_principal.add_cascade(menu=submenu_archivo,label="Archivo")
    menu_principal.add_cascade(menu=submenu_archivo2,label="Ayuda")
    ventana.config(menu=menu_principal,)
    
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

crearMenu()

ventana.mainloop()