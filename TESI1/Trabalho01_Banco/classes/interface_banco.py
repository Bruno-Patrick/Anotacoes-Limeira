import tkinter as tk
from tkinter import ttk

from Banco import Banco
from Cliente import Cliente
from Conta import Conta
from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupaca

class Display:
    def __init__(self, master):
        self.display = master
        # self.display.attributes("-fullscreen", True)
        self.display.title('Banco do Brasil')
        self.container = self.display.winfo_screenwidth()
        self.alturaTotal = self.display.winfo_screenheight()
        self.display.geometry("{0}x{1}+0+0".format(self.container, self.alturaTotal))

        def criar_cliente():
            toplevel = tk.Toplevel(self.display)
            toplevel.geometry("500x500")
            toplevel.title("Cadastro de Cliente")

            self.nome_label_cadastro = tk.Label(toplevel, text='Nome completo:')
            self.nome_label_cadastro.grid(row=0, column=0)
            self.nome_entry_cadastro = tk.Entry(toplevel, width=70)
            self.nome_entry_cadastro.grid(row=0, column=1)

            self.CPF_label_cadastro = tk.Label(toplevel, text="Digite seu CPF:")
            self.CPF_label_cadastro.grid(row=1, column=0)
            self.CPF_entry_cadastro = tk.Entry(toplevel, width=70)
            self.CPF_entry_cadastro.grid(row=1, column=1)

            self.endereco_label_cadastro = tk.Label(toplevel, text="Digite seu endereço:")
            self.endereco_label_cadastro.grid(row=2, column=0)
            self.endereco_entry_cadastro = tk.Entry(toplevel, width=70)
            self.endereco_entry_cadastro.grid(row=2, column=1)

            def confirmar():
                nome = self.nome_entry_cadastro.get()
                cpf = self.CPF_entry_cadastro.get()
                endereco = self.endereco_entry_cadastro.get()

                teste = Cliente(nome, cpf, endereco)
                print(teste.nome)

            self.cadastro_cliente = tk.Button(toplevel, text="Confimar", command=confirmar)
            self.cadastro_cliente.grid(row=3, column=0)


        self.logo = tk.Label(self.display, bg="yellow", text="Banco do Brasil",
            height=3)
        self.logo.pack(side=tk.TOP, fill=tk.X, expand=True)

        self.menuBarra = tk.Menu(self.display)
        self.menu_cadastro = tk.Menu(self.menuBarra, tearoff=0)
        self.menu_cadastro.add_command(label="Criar cliente", command=criar_cliente)
        self.menuBarra.add_cascade(label="Cadastrar-se", menu=self.menu_cadastro)
        self.display.config(menu=self.menuBarra)

        self.menu_config = tk.Menu(self.menuBarra, tearoff=0)
        self.menuBarra.add_cascade(label="Configurações", menu=self.menu_config)
        self.menu_config.add_command(label="Tamanho")

        # Este frame está empurrando tudo para o topo da página >>>>>>>>>>>>>>>>>>>
        self.frm_empurra_cima = tk.Frame(self.display, height=self.alturaTotal)
        self.frm_empurra_cima.pack()
        # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


app = tk.Tk()
Display(app)
app.mainloop()