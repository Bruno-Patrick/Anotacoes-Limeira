import imp
from turtle import title
import bcrypt
import sqlite3
import tkinter as tk
from tkinter import BOTH, EW, LEFT, RIGHT, TOP, ttk, messagebox as msg

from Configurations import Configurations
from Login import Login
from Connection import Connection
from Professor import Professor
from Usuario import Usuario
from Treeview import Treeview
from Functions import Functions

class Display:

    def __init__(self, master):
        self.display = master
        self.larguraTotal = self.display.winfo_screenwidth()
        self.alturaTotal = self.display.winfo_screenheight()
        self.display.geometry("{0}x{1}+0+0".format(self.larguraTotal, self.alturaTotal))
        self.display.title("Controle de Notas Acadêmico")
        self.userSession = Login()
        self.bd = Connection()
        self.createtvw = Treeview()
        self.function = Functions()

        # if not self.userSession.isLogged:
        self.display.withdraw()

        def display_principal():
            #Contruindo Treeview para exibição dos alunos
            self.userConfigurations = self.bd.getConfigurationsByUser(self.userSession.getUserId)
            self.colunasTvwAlunos = self.createtvw.columnsgenerator(
                'id',
                'nome',
                f'N1={self.userConfigurations[0][1]}',
                'N1',f'N2={self.userConfigurations[0][2]}',
                'N2',
                'Prova Final')
            print(self.colunasTvwAlunos)
            self.tvwAlunos = self.createtvw.instancetvw(self.display,self.colunasTvwAlunos)
            self.tvwAlunos.pack(side=tk.TOP,fill=BOTH,expand=True)
            self.createtvw.heading(self.tvwAlunos,self.colunasTvwAlunos)
            self.createtvw.column(self.tvwAlunos,self.colunasTvwAlunos)

        def logar():
            if self.function.isFieldsEmpty(
                    self.toplevelLogin,
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
                        self.userLogin = Usuario(self.isUser[0][1],self.isUser[0][2],self.isUser[0][3])
                        self.userLogin.id = self.isUser[0][0]
                        self.userSession.set_user(self.userLogin)
                        self.toplevelLogin.destroy()

                        # A partir daqui inicia-se interface do usuário logado

                        # Verificando se o usuario já informou a quantidade de parciais
                        self.isConfiguration = self.bd.getConfigurationsByUser(self.userSession.getUserId)
                        if not self.isConfiguration:
                            # Tela para fazer a configuração inicial
                            self.toplevelConfigurations = tk.Toplevel(self.display)
                            self.toplevelConfigurations.title("Configurações iniciais")
                            self.toplevelConfigurations.geometry("500x100")

                            self.labelConfigurations1 = tk.Label(self.toplevelConfigurations,
                            text="Bem vindo!", font=10)
                            self.labelConfigurations1.pack(side=tk.TOP)

                            self.labelConfigurations2 = tk.Label(self.toplevelConfigurations,
                            text="Indique a quantidade de atividades que fará para N1 e para N2", font=10)
                            self.labelConfigurations2.pack(side=tk.TOP)

                            self.frameConfigurations = tk.Frame(self.toplevelConfigurations)
                            self.frameConfigurations.pack(side=tk.LEFT)

                            self.labelN1 = tk.Label(self.frameConfigurations, text="Quantidade de atividades para N1:")
                            self.labelN1.grid(row=0,column=0)

                            self.EntryN1 = tk.Entry(self.frameConfigurations, width=20)
                            self.EntryN1.grid(row=0,column=1)
                            self.EntryN1.insert(0, '0')

                            self.labelN2 = tk.Label(self.frameConfigurations, text="Quantidade de atividades para N2:")
                            self.labelN2.grid(row=1,column=0)

                            self.EntryN2 = tk.Entry(self.frameConfigurations, width=20)
                            self.EntryN2.grid(row=1,column=1)
                            self.EntryN2.insert(0, '0')

                            def saveConfiguration():
                                self.N1amount = self.EntryN1.get()
                                self.N2amount = self.EntryN2.get()
                                
                                if msg.askyesno('Confirme os dados',
                                f'Quantidade de atividades para N1: {self.N1amount} \nQuantidade de atividades para N2: {self.N2amount}'):
                                    
                                    self.configs = Configurations(str(self.N1amount), str(self.N2amount), str(self.userSession.getUserId))
                                    self.bd.inserir(self.configs)
                                    self.toplevelConfigurations.destroy()
                                    self.display.deiconify()
                                    display_principal()


                            self.buttonSaveConfiguration = tk.Button(self.frameConfigurations, text="Salvar!",command=saveConfiguration)
                            self.buttonSaveConfiguration.grid(row=0,column=2,rowspan=2)

                        else:
                            self.display.deiconify()
                            display_principal()                           

                    else:
                        msg.showerror("","Usuário ou senha incorretas!", parent=self.toplevelLogin)

        def cadastro():
            self.toplevelLogin.withdraw()
            self.toplevelCadastro = tk.Toplevel()
            self.toplevelCadastro.title("Cadastro")
            self.toplevelCadastro.minsize(100,300)

            self.frametoplevelCadastro = tk.Frame()
            self.frametoplevelCadastro.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

            self.fullnameLabel = tk.Label(self.toplevelCadastro, text="Nome completo:")
            self.fullnameEntry = tk.Entry(self.toplevelCadastro)
            self.fullnameLabel.grid(row=0,column=0)
            self.fullnameEntry.grid(row=0,column=1, sticky=EW)

            def verificar():
                self.toplevelCadastro.iconify()
                self.toplevelVerificar = tk.Toplevel(self.toplevelCadastro)
                self.toplevelVerificar.minsize(300,300)
                self.toplevelVerificar.title("Lista de professores")

                self.labelTexto = tk.Label(self.toplevelVerificar, text="Qual desses é você?",font=13)
                self.labelTexto.pack()

                #Instanciando dinamicamente Treeview dos professores
                self.colunasVerificar = self.createtvw.columnsgenerator("id","nome")
                self.tvwVerificar = self.createtvw.instancetvw(self.toplevelVerificar,self.colunasVerificar)
                self.tvwVerificar.pack(side=LEFT, fill=BOTH)
                self.createtvw.heading(self.tvwVerificar,self.colunasVerificar)
                self.createtvw.column(self.tvwVerificar,self.colunasVerificar)

                if not self.fullnameEntry.get():
                    self.tupla = self.bd.getAllProfessores()
                    self.createtvw.atualizar(self.tvwVerificar, self.tupla)
                else:
                    self.tupla = self.bd.getProfessorByName(self.fullnameEntry.get())
                    self.createtvw.atualizar(self.tvwVerificar, self.tupla)

                def callbackSelecionar():
                    self.retornoCallback = self.createtvw.selecionar(self.toplevelVerificar,self.tvwVerificar)
                    self.fullnameEntry.delete(0,tk.END)
                    self.fullnameEntry.insert(0,self.retornoCallback[1])
                    self.toplevelVerificar.destroy()
                    self.toplevelCadastro.deiconify()

                self.buttonConfirmarProfessor = tk.Button(self.toplevelVerificar, text="selecionar", command=callbackSelecionar)
                self.buttonConfirmarProfessor.pack(side=tk.TOP)

                def voltar():
                    self.toplevelCadastro.deiconify()
                    self.toplevelVerificar.destroy()

                self.buttonVoltar = tk.Button(self.toplevelVerificar, text="voltar", command=voltar)
                self.buttonVoltar.pack(side=tk.TOP)

                def cadastrarProfessor():
                    self.toplevelVerificar.iconify()
                    self.toplevelCadastroProfessor = tk.Toplevel(self.toplevelVerificar)
                    self.toplevelCadastroProfessor.title("Cadastro de professor")
                    self.toplevelCadastroProfessor.minsize(100,100)

                    self.labelNomeProfessor = tk.Label(self.toplevelCadastroProfessor, text="Nome:")
                    self.labelNomeProfessor.grid(row=0,column=0)

                    self.entryNomeProfessor = tk.Entry(self.toplevelCadastroProfessor)
                    self.entryNomeProfessor.grid(row=0,column=1)

                    def salvarProfessor():
                        self.nomeProfessor = self.entryNomeProfessor.get()
                        if self.nomeProfessor == '':
                            msg.showerror("Operação cancelada","Digite um nome válido para continuar",parent=self.toplevelCadastroProfessor)
                        else:
                            self.newProfessor =  Professor(self.nomeProfessor)
                            self.bd.inserir(self.newProfessor)
                            self.toplevelCadastroProfessor.destroy()
                            self.tupla = self.bd.getAllProfessores()
                            self.createtvw.atualizar(self.tvwVerificar, self.tupla)
                            self.toplevelVerificar.deiconify()


                    self.buttonSaveProfessor = tk.Button(self.toplevelCadastroProfessor, text="Salvar!",command=salvarProfessor)
                    self.buttonSaveProfessor.grid(row=0,column=2)

                    def cancelarCadastroProfessor():
                        self.toplevelCadastroProfessor.destroy()
                        self.toplevelVerificar.deiconify()
                        
                    self.cancelarCadastroProfessor = tk.Button(self.toplevelCadastroProfessor, text="Cancelar!",command=cancelarCadastroProfessor)
                    self.cancelarCadastroProfessor.grid(row=0,column=3)

                self.buttonCadastrarProfessor = tk.Button(self.toplevelVerificar, text="Cadastrar professor", command=cadastrarProfessor)
                self.buttonCadastrarProfessor.pack(side=tk.TOP)

            self.buttonVerificarfullname = tk.Button(self.toplevelCadastro,text="Verificar", command=verificar)
            self.buttonVerificarfullname.grid(row=0,column=2)

            self.usernameLabel = tk.Label(self.toplevelCadastro, text="username:")
            self.usernameEntry = tk.Entry(self.toplevelCadastro)
            self.usernameLabel.grid(row=1,column=0)
            self.usernameEntry.grid(row=1,column=1, sticky=EW)

            self.passwordLabel = tk.Label(self.toplevelCadastro, text="password:")
            self.passwordEntry = tk.Entry(self.toplevelCadastro)
            self.passwordLabel.grid(row=2,column=0)
            self.passwordEntry.grid(row=2,column=1)

            def confirmarCadastro():
                try:
                    professor = self.retornoCallback[0]
                except:
                    professor = ''
                username = self.usernameEntry.get()
                password = self.passwordEntry.get()
                self.isEmpty = self.function.isFieldsEmpty(
                    self.toplevelCadastro,
                    self.usernameEntry,
                    self.passwordEntry,
                    self.fullnameEntry)
                    
                if self.isEmpty:
                    msg.showerror('Operação não permitida','Preencha todos os campos para continuar!',parent=self.toplevelCadastro)
                elif not professor:
                    msg.showerror('Operação não permitida','Faça a verificação e selecione um professor válido',parent=self.toplevelCadastro)
                else:
                    try:
                        # self.hash = self.userSession.encript(password)
                        query = f'INSERT INTO usuario(hash,username,professor) VALUES("{password}","{username}","{professor}")'
                        self.bd.operation(query)
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