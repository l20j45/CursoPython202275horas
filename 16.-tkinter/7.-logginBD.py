import tkinter as tk
from tkinter import ttk, messagebox
import mariadb

conexionDatabase1 =  mariadb.connect(
            user="root",
            password="root",
            host="localhost",
            port=3319,
            database="test"
        )
#widget events
def mainLoggin():
    try:
        with conexionDatabase1.cursor() as cursor:            
            sentencia = f'SELECT id,username,NAME,email FROM users WHERE username="{userTextbox.get()}" AND `password`="{passwordTextbox.get()} "limit 1;'
            print(sentencia)
            cursor.execute(sentencia)
            registros = cursor.fetchone()
            if registros!=0:
                messagebox.showinfo('Datos Login', f'Entraste \nUsuario: {userTextbox.get()} , Password: {passwordTextbox.get()} ')      
    except Exception as e:
        print(f'Ocurrio un error {e} ')
        messagebox.showerror('Datos Login', f'No entraste \nUsuario: {userTextbox.get()} , Password: {passwordTextbox.get()} ')   
 
#main container
mainWindow = tk.Tk()
mainWindow.geometry("300x130")
mainWindow.title("Loggin")
#main container configurations
mainWindow.rowconfigure(0,weight=1)
mainWindow.rowconfigure(1,weight=1)
mainWindow.rowconfigure(2,weight=2)
mainWindow.columnconfigure(0,weight=1)
mainWindow.columnconfigure(1,weight=2)
#widget or elements
userLabel=tk.Label(mainWindow,text="User:",justify=tk.RIGHT)
passwordLabel=tk.Label(mainWindow,text="password:",justify=tk.RIGHT)
userTextbox=ttk.Entry(mainWindow,width=35,justify=tk.LEFT)
passwordTextbox=ttk.Entry(mainWindow,width=35,justify=tk.LEFT,show="*")
sendButton = ttk.Button(mainWindow,text="Loggin",command=mainLoggin)
#widget condigurations
userLabel.grid(row=0,column=0,sticky='NSE',padx=10)
passwordLabel.grid(row=1,column=0,sticky='NSWE',padx=5)
userTextbox.grid(row=0,column=1,padx=20)
passwordTextbox.grid(row=1,column=1,padx=20)
sendButton.grid(row=2,column=0,columnspan=2,sticky='N',pady=10)
#launchers#
mainWindow.mainloop()