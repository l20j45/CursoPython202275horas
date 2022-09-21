import tkinter as tk
from tkinter import ttk, messagebox

class LoginVentana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x130")
        self.title("Loggin")
        self.rowconfigure(0,weight=1)
        self.rowconfigure(1,weight=1)
        self.rowconfigure(2,weight=2)
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=2)
        self._crearComponentes()

    def _mainLoggin(self):
        if self.userTextbox.get().lower()=="daniel" and self.passwordTextbox.get().lower()=="daniel":
            messagebox.showinfo('Datos Login', f'Entraste \nUsuario: {self.userTextbox.get()} , Password: {self.passwordTextbox.get()} ')
        else:
            messagebox.showerror('Datos Login', f'No entraste \nUsuario: {self.userTextbox.get()} , Password: {self.passwordTextbox.get()} ')

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
    login_ventana=LoginVentana()
    login_ventana.mainloop()
