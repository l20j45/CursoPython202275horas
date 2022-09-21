import tkinter as tk
from tkinter import ttk, messagebox
import mariadb

class LoginVentana(tk.Tk):

    def __init__(self,conexionDatabase):
        super().__init__()
        self.geometry("300x130")
        self.title("Loggin")
        self.rowconfigure(0,weight=1)
        self.rowconfigure(1,weight=1)
        self.rowconfigure(2,weight=2)
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=2)
        self._crearComponentes()
        self.conexion=conexionDatabase

    def _mainLoggin(self):
        try:
            with self.conexion.cursor() as cursor:            
                sentencia = f'SELECT id,username,NAME,email FROM users WHERE username="{self.userTextbox.get()}" AND `password`="{self.passwordTextbox.get()} "limit 1;'
                print(sentencia)
                cursor.execute(sentencia)
                registros = cursor.fetchone()
                if registros!=None:
                    print(registros)
                    messagebox.showinfo('Datos Login', f'Entraste \nUsuario: {self.userTextbox.get()} , Password: {self.passwordTextbox.get()} ')
                    registros=None
                else:
                   messagebox.showerror('Datos Login', f'No entraste \nUsuario: {self.userTextbox.get()} , Password: {self.passwordTextbox.get()} ')        
        except Exception as e:
            print(f'Ocurrio un error {e} ')

 
    def _crearComponentes(self):
        userLabel=tk.Label(self,text="User:",justify=tk.RIGHT)
        passwordLabel=tk.Label(self,text="password:",justify=tk.RIGHT)
        self.userTextbox=ttk.Entry(self,width=35,justify=tk.LEFT)
        self.passwordTextbox=ttk.Entry(self,width=35,justify=tk.LEFT,show="*")
        sendButton = ttk.Button(self,text="Loggin",command=self._mainLoggin)
        
        userLabel.grid(row=0,column=0,sticky='NSE',padx=10)
        passwordLabel.grid(row=1,column=0,sticky='NSWE',padx=5)
        self.userTextbox.grid(row=0,column=1,padx=20)
        self.passwordTextbox.grid(row=1,column=1,padx=20)
        sendButton.grid(row=2,column=0,columnspan=2,sticky='N',pady=10)
        
if __name__=='__main__':
    conexionDatabase1 =  mariadb.connect(
        user="root",
        password="root",
        host="localhost",
        port=3319,
        database="test"
    )
    login_ventana=LoginVentana(conexionDatabase1)
    login_ventana.mainloop()
