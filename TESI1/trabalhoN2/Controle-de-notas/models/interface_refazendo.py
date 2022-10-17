import sqlite3
import tkinter as tk
from tkinter import BOTH, EW, LEFT, RIGHT, TOP, ttk, messagebox as msg


from Notas import Notas

from Configurations import Configurations
from Login import Login
from Aluno import Aluno
from Connection import Connection
from Professor import Professor
from Disciplinas import Disciplinas
from Usuario import Usuario
from Treeview import Treeview
from Functions import Functions

from datetime import date

class Display:

    def __init__(self, master):
        self.telaInicial = master

        # Variáveis para altura e largura da tela
        self.larguraTotal = self.display.winfo_screenwidth()
        self.alturaTotal = self.display.winfo_screenheight()


        # Cache de sessão do usuário
        self.userSession = Login()

        # Conexão com banco de dados
        self.bd = Connection()

        # Instância dinâmica do Treeview
        self.createtvw = Treeview()

        # Funções auxiliares
        self.function = Functions()

        # Ano atual
        self.currentTime = date.today()
        self.currentTime = self.currentTime.year

        self.telaInicial.minsize(100,100)
        self.telaInicial.title("Cadastros iniciais")

        def logar():
            if self.function.isFieldsEmpty(
                    self.userEntryLogin,
                    self.passwordEntryLogin):
                msg.showerror("Operação não permitida","Informe um usuario e senha",parent=self.passwordEntryLogin)
            else:
                self.usernameLogin = self.userEntryLogin.get()
                self.passwordLogin = self.passwordEntryLogin.get()
                self.isUser = self.bd.getUserByUserName(self.usernameLogin)
                if not self.isUser:
                    msg.showerror("","Usuário não encontrado!", parent=self.toplevelLogin)
                else:
                    # bytes = self.userSession.bytes(password)
                    self.hashRetornado = self.isUser[0][1]
                    # self.istrue = bcrypt.checkpw(b'12345', self.hashRetornado)
                    if self.passwordLogin == self.hashRetornado: 
                        self.userSession.login()

                        # Construção de um objeto usuário para ser inserido no cache de sessão do usuário
                        self.userLogin = Usuario(self.isUser[0][1],self.isUser[0][2],self.isUser[0][3])
                        self.userLogin.id = self.isUser[0][0]
                        self.userSession.set_user(self.userLogin)

                        # Assim que fizer login, será instânciado algumas variável globais
                        self.disciplinaAtual = self.bd.getDisciplinasbyProfessor(self.userSession.getUserId,ano=self.currentTime) #Primeira disciplina que o banco devolver, no ano atual

                        self.toplevelLogin.destroy()

                        print("LOGADO")

                        # Verificando se o usuario já informou a quantidade de parciais
                        # if not self.bd.getConfigurationsByUser(self.userSession.getUserId):
                        #     configurations()
                        # else:
                        #     display_principal()
                        #     self.display.deiconify()

                    else:
                        msg.showerror("","Usuário ou senha incorretas!", parent=self.toplevelLogin)
        
        def cadastro():
            self.toplevelLogin.withdraw()
            self.toplevelCadastro = tk.Toplevel(self.toplevelLogin)
            self.toplevelCadastro.title("Cadastro de usuário")
            self.toplevelCadastro.minsize(100,300)

            self.frametoplevelCadastro = tk.Frame()
            self.frametoplevelCadastro.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

            self.usernameLabel = tk.Label(self.toplevelCadastro, text="username:")
            self.usernameEntry = tk.Entry(self.toplevelCadastro)
            self.usernameLabel.grid(row=0,column=0)
            self.usernameEntry.grid(row=0,column=1, sticky=EW)

            self.passwordLabel = tk.Label(self.toplevelCadastro, text="password:")
            self.passwordEntry = tk.Entry(self.toplevelCadastro)
            self.passwordLabel.grid(row=1,column=0)
            self.passwordEntry.grid(row=1,column=1)

            def confirmarCadastro():
                username = self.usernameEntry.get()
                password = self.passwordEntry.get()

                self.isEmpty = self.function.isFieldsEmpty(
                    self.usernameEntry,
                    self.passwordEntry)
                    
                if self.isEmpty:
                    msg.showerror('Operação não permitida','Preencha todos os campos para continuar!',parent=self.toplevelCadastro)
                else:
                    try:
                        # query = f'INSERT INTO usuario(hash,username) VALUES("{password}","{username}")'
                        self.Newusuario = Usuario(password,username)
                        self.bd.inserir(self.newUsuario)

                        msg.showinfo("Sucesso!","Usuário cadastrado com sucesso!",parent=self.toplevelCadastro)
                        self.toplevelCadastro.destroy()
                        self.toplevelLogin.deiconify()
                    except sqlite3.IntegrityError:
                        msg.showerror('Operação não permitida','Já existe um usuário com esse username!',parent=self.toplevelCadastro)
                
            self.buttonCadastrar = tk.Button(self.toplevelCadastro, text="Cadastrar!", command=confirmarCadastro)
            self.buttonCadastrar.grid(row=3,column=0,sticky=EW)

            def cancel():
                self.toplevelCadastro.destroy()
                self.toplevelLogin.deiconify()

            self.buttonCancelar = tk.Button(self.toplevelCadastro, text="Cancelar!",command=cancel)
            self.buttonCancelar.grid(row=3,column=1,sticky=EW) 


        # self.toplevelLogin = tk.Toplevel(self.telaInicial)
        # self.toplevelLogin.title("Login")
        # self.toplevelLogin.geometry("300x200")

        self.frametoplevelLogin = tk.Frame(self.telaInicial)
        self.frametoplevelLogin.pack(side=tk.LEFT,fill=BOTH, expand=True)

        self.userLabelLogin = tk.Label(self.frametoplevelLogin, text="username:")
        self.userEntryLogin = tk.Entry(self.frametoplevelLogin)
        self.userLabelLogin.grid(row = 0, column = 0)
        self.userEntryLogin.grid(row = 0, column = 1, ipadx=30)

        self.passwordLabelLogin = tk.Label(self.frametoplevelLogin, text="password:")
        self.passwordEntryLogin = tk.Entry(self.frametoplevelLogin)
        self.passwordLabelLogin.grid(row = 1, column = 0)
        self.passwordEntryLogin.grid(row = 1, column = 1, ipadx=30)

        self.buttonLogin = tk.Button(self.frametoplevelLogin, text="Login",command=logar)
        self.buttonLogin.grid(row = 2, column = 0, sticky=EW)

        self.buttonCadastro = tk.Button(self.frametoplevelLogin, text="Criar cadastro", command=cadastro)
        self.buttonCadastro.grid(row = 2, column = 1, sticky=EW)