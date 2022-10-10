import imp
import tkinter as tk
from tkinter import BOTH, EW, ttk, messagebox as msg
from Login import Login
from Connection import Connection
from Professor import Professor
from Usuario import Usuario

class Display:

    def __init__(self, master):
        self.display = master
        self.larguraTotal = self.display.winfo_screenwidth()
        self.alturaTotal = self.display.winfo_screenheight()
        self.display.geometry("{0}x{1}+0+0".format(self.larguraTotal, self.alturaTotal))
        self.display.title("Controle de Notas Acadêmico")
        self.userSession = Login()
        self.bd = Connection()

        if not self.userSession.isLogged:
            self.display.withdraw()

            def logar():
                username = self.userEntryLogin.get()
                password = self.passwordEntryLogin.get()

                ishash = self.bd.getHashByUserName(username)
                if not ishash:
                    msg.showerror("","Usuário não encontrado!", parent=self.toplevelLogin)
                else: 
                    istrue = self.userSession.isKeyTrue(password, ishash)
                    if istrue: self.userSession.login
                    # self.userSession.user = 
                    self.toplevelLogin.destroy()
                    self.display.deiconify()

            def cadastro():
                self.toplevelLogin.withdraw()
                self.toplevelCadastro = tk.Toplevel()
                self.toplevelCadastro.title("Cadastro")
                self.toplevelCadastro.geometry("300x200")

                self.frametoplevelCadastro = tk.Frame()
                self.frametoplevelCadastro.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

                self.fullnameLabel = tk.Label(self.toplevelCadastro, text="Nome completo:")
                self.fullnameEntry = tk.Entry(self.toplevelCadastro)
                self.fullnameLabel.grid(row=0,column=0)
                self.fullnameEntry.grid(row=0,column=1, sticky=EW)

                self.usernameLabel = tk.Label(self.toplevelCadastro, text="username:")
                self.usernameEntry = tk.Entry(self.toplevelCadastro)
                self.usernameLabel.grid(row=1,column=0)
                self.usernameEntry.grid(row=1,column=1, sticky=EW)

                self.passwordLabel = tk.Label(self.toplevelCadastro, text="password:")
                self.passwordEntry = tk.Entry(self.toplevelCadastro)
                self.passwordLabel.grid(row=2,column=0)
                self.passwordEntry.grid(row=2,column=1)

                def confirmar():
                    fullname = self.fullnameEntry.get()
                    username = self.usernameEntry.get()
                    password = self.passwordEntry.get()

                    professor = Professor(fullname)

                self.buttonCadastrar = tk.Button(self.toplevelCadastro, text="Cadastrar!", command=confirmar)
                self.buttonCadastrar.grid(row=2,column=0,sticky=EW)

                def cancel():
                    self.toplevelCadastro.destroy()
                    self.toplevelLogin.deiconify()

                self.buttonCancelar = tk.Button(self.toplevelCadastro, text="Cancelar!",command=cancel)
                self.buttonCancelar.grid(row=2,column=1,sticky=EW)  
            
            self.toplevelLogin = tk.Toplevel()
            self.toplevelLogin.title("Login")
            self.toplevelLogin.geometry("300x200")

            self.frametoplevelLogin = tk.Frame(self.toplevelLogin)
            self.frametoplevelLogin.pack(side=tk.LEFT,fill=BOTH, expand=True)

            self.userLabelLogin = tk.Label(self.frametoplevelLogin, text="username:")
            self.userEntryLogin = tk.Entry(self.frametoplevelLogin)
            self.userLabelLogin.grid(row = 0, column = 0)
            self.userEntryLogin.grid(row = 0, column = 1, ipadx=30)

            self.passwordLabelLogin = tk.Label(self.frametoplevelLogin, text="password:")
            self.passwordEntryLogin = tk.Entry(self.frametoplevelLogin)
            self.passwordLabelLogin.grid(row = 1, column = 0)
            self.passwordEntryLogin.grid(row = 1, column = 1, ipadx=30)

            self.buttonLogin = tk.Button(self.frametoplevelLogin, text="Login", command=logar)
            self.buttonLogin.grid(row = 2, column = 0, sticky=EW)

            self.buttonCadastro = tk.Button(self.frametoplevelLogin, text="Criar cadastro", command=cadastro)
            self.buttonCadastro.grid(row = 2, column = 1, sticky=EW)

            self.buttonCancelar = tk.Button(self.frametoplevelLogin, text="Cancelar!", command=self.display.destroy)
            self.buttonCancelar.grid(row=3,column=0,sticky=EW)


app = tk.Tk()
Display(app)
app.mainloop()