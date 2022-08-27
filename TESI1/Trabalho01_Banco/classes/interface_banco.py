import tkinter as tk
from tkinter import ttk, messagebox, font
from tkinter.scrolledtext import ScrolledText

from Banco import Banco
from Cliente import Cliente
from Conta import Conta
from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupaca

class Display:
    def __init__(self, master):
        self.display = master
        # self.display.attributes("-fullscreen", True)
        self.display.title('GdB')
        self.container = self.display.winfo_screenwidth()
        self.alturaTotal = self.display.winfo_screenheight()
        self.display.geometry("{0}x{1}+0+0".format(self.container, self.alturaTotal))
        self.clientes = []
        self.banco = False

        def verify_bank():
            if self.banco == False:
                return False
            else:
                return True

        def atualizar_lista():
            tudo = self.tvw_principal.get_children()
            for i in tudo:
                self.tvw_principal.delete(i)
            for conta in self.banco.contas:
                if (conta.active):
                    status = "Conta Ativa"
                else:
                    status = "Conta Encerrada"
                if isinstance(conta, ContaCorrente):
                    self.tvw_principal.insert('',tk.END,values=(
                        conta.numero,"Conta Corrente",f"{conta.saldo:,.2f}",status
                    ))
                if isinstance(conta, ContaPoupaca):
                    self.tvw_principal.insert('',tk.END,values=(
                        conta.numero,"Conta Poupança",f"{conta.saldo:,.2f}",status
                    ))

        def criar_cliente():
            bank = verify_bank()
            if(bank):
                toplevel = tk.Toplevel(self.display)
                toplevel.geometry("500x200")
                toplevel.title("Cadastro de Cliente")
                toplevel.grab_set()

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

                    if nome and cpf and endereco:
                        confirmacao = messagebox.askyesno("Confirmação","Deseja criar?", parent=toplevel)
                        if confirmacao:
                            for cliente in self.clientes:
                                if cliente.cpf == cpf:
                                    messagebox.showerror("Error!",
                                    "Cliente com o mesmo CPF já cadastrado!",parent=toplevel)
                            classe = Cliente(nome, endereco, cpf)
                            self.clientes.append(classe)
                            toplevel.destroy()
                            atualizar_lista()
                        else:
                            messagebox.showinfo("Cancelado!","O Cadastro foi cancelado!")
                    else:
                        messagebox.showerror("Campos vazios!",
                        "Preencha todos os campos para cadastrar", parent=toplevel)

                self.cadastro_cliente = tk.Button(toplevel, text="Confimar", command=confirmar)
                self.cadastro_cliente.grid(row=3, column=0)
                self.cadastro_cliente = tk.Button(toplevel, text="Cancelar", command=toplevel.destroy)
                self.cadastro_cliente.grid(row=3, column=1)
            else:
                messagebox.showerror("ERROR!","DEFINA UM BANCO PARA PROSSEGUIR")

        def definir_banco():
            toplevel = tk.Toplevel(self.display)
            toplevel.geometry("500x200")
            toplevel.title("Definir banco")
            toplevel.grab_set()

            self.id_label_cadastro = tk.Label(toplevel, text='Código do Banco:')
            self.id_label_cadastro.grid(row=0, column=0)
            self.id_entry_cadastro = tk.Entry(toplevel, width=70)
            self.id_entry_cadastro.grid(row=0, column=1)

            self.nome_label_cadastro = tk.Label(toplevel, text="Digite o nome do banco:")
            self.nome_label_cadastro.grid(row=1, column=0)
            self.nome_entry_cadastro = tk.Entry(toplevel, width=70)
            self.nome_entry_cadastro.grid(row=1, column=1)

            def confirmar():
                idB = self.id_entry_cadastro.get()
                nome = self.nome_entry_cadastro.get()

                if idB and nome:
                    confirmacao = messagebox.askyesno("Confirmação"
                    ,"Deseja definir esse banco?", parent=toplevel)
                    if confirmacao:
                            self.banco = Banco(idB, nome)
                            toplevel.destroy()
                    else:
                        messagebox.showinfo("Cancelado!","O Cadastro foi cancelado!")
                else:
                    messagebox.showerror("Campos vazios!",
                    "Preencha todos os campos para definir", parent=toplevel)

            self.cadastro_cliente = tk.Button(toplevel, text="Confimar", command=confirmar)
            self.cadastro_cliente.grid(row=2, column=0)
            self.cadastro_cliente = tk.Button(toplevel, text="Cancelar", command=toplevel.destroy)
            self.cadastro_cliente.grid(row=2, column=1)

        def definir_juros():
            bank = verify_bank()
            if(bank):
                toplevel = tk.Toplevel(self.display)
                toplevel.title("Definir juros")
                toplevel.grab_set()

                self.lbl_saque = tk.Label(toplevel, text="Digite o valor:")
                self.lbl_saque.grid(row=0, column=0)
                self.entry_saque = tk.Entry(toplevel)
                self.entry_saque.grid(row=0, column=1)

                def confirmar():
                    valor = float(self.entry_saque.get())
                    confirm = messagebox.askyesno("Confirma?",f"Definir juros de {valor}%?")
                    if confirm:
                        self.banco.juros = valor
                        messagebox.showinfo("Sucesso","Novos juros definido!", parent=toplevel)
                        toplevel.destroy()
                    else: toplevel.destroy()
                    
                self.btn_confirmar = tk.Button(toplevel, text='Confirmar!', bg='gray', command=confirmar)
                self.btn_confirmar.grid(row=1, column=0)
            else:
                messagebox.showerror("ERROR!","DEFINA UM BANCO PARA PROSSEGUIR")

        def definir_desconto():
            bank = verify_bank()
            if(bank):
                toplevel = tk.Toplevel(self.display)
                toplevel.title("Definir desconto")
                toplevel.grab_set()

                self.lbl_desconto = tk.Label(toplevel, text="Digite o valor:")
                self.lbl_desconto.grid(row=0, column=0)
                self.entry_desconto = tk.Entry(toplevel)
                self.entry_desconto.grid(row=0, column=1)

                def confirmar():
                    valor = float(self.entry_desconto.get())
                    confirm = messagebox.askyesno("Confirma?",f"Definir desconto de {valor}?")
                    if confirm:
                        self.banco.desconto = valor
                        messagebox.showinfo("Sucesso","Novo desconto definido!", parent=toplevel)
                        toplevel.destroy()
                    else: toplevel.destroy()
                    
                self.btn_confirmar = tk.Button(toplevel, text='Confirmar!', bg='gray', command=confirmar)
                self.btn_confirmar.grid(row=1, column=0)
            else:
                messagebox.showerror("ERROR!","DEFINA UM BANCO PARA PROSSEGUIR")

        def treeview(toplevel):
            colunas = ['Cliente','Endereço' ,'CPF']
            self.tvw = ttk.Treeview(toplevel, columns=colunas, show="headings")
            self.tvw.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            self.tvw.heading(colunas[0], text="Cliente")
            self.tvw.heading(colunas[1], text="Endereço")
            self.tvw.heading(colunas[2], text="CPF")

            scrollbar = tk.Scrollbar(toplevel, command=self.tvw.yview)
            scrollbar.pack(side=tk.LEFT, fill=tk.BOTH,expand=True)
            self.tvw.configure(yscroll=scrollbar.set)

            for clientes in self.clientes:
                self.tvw.insert('',tk.END,values=(clientes.nome,clientes.endereco,clientes.cpf))

        def criar_corrente():
            bank = verify_bank()
            if(bank):
                toplevel = tk.Toplevel(self.display)
                toplevel.minsize(700,500)
                toplevel.title("Cadastro de Conta Corrente")
                toplevel.grab_set()

                self.clabel = tk.Label(toplevel, 
                text="Selecione o cliente para qual desejas criar uma conta corrente",
                font=("Arial","12"))
                self.clabel.pack(side=tk.TOP, fill=tk.X)

                treeview(toplevel)
                
                def select_cliente():
                    selecao = self.tvw.selection()
                    tamanho = len(selecao)
                    if tamanho > 1:
                        confirm = messagebox.askyesno("Confirmar"
                        ,f"Tem certeza que quer criar uma conta corrente para {tamanho} clientes?")
                        if(confirm):
                            for cliente in selecao:
                                cc = ContaCorrente(cliente, 0)
                                self.banco.contas.append(cc)
                                self.banco.fixar_desconto(self.banco.desconto)
                                atualizar_lista()
                                toplevel.destroy()
                        else:
                            messagebox.showinfo("Cancelado!","Operação cancelada!")
                    else:
                        if tamanho == 0:
                            messagebox.showerror("Error!"
                            ,"Nenhum cliente selecionado!", parent=toplevel)
                        else:
                            confirm = messagebox.askyesno("Confirmar"
                            ,f"Tem certeza que quer criar uma conta corrente para esse cliente?")
                            if(confirm):
                                cc = ContaCorrente(selecao[0], 0)
                                self.banco.contas.append(cc)

                self.frmBtns = tk.Frame(toplevel)
                self.frmBtns.pack(side=tk.LEFT, fill=tk.BOTH)
                self.btnS1 = tk.Button(self.frmBtns, text="Selecionar cliente(s)", command=select_cliente)
                self.btnS1.grid(row=0, column=0,ipady=10)
            else:
                messagebox.showerror("ERROR!","DEFINA UM BANCO PARA PROSSEGUIR")

        def criar_poupanca():
            bank = verify_bank()
            if(bank):
                toplevel = tk.Toplevel(self.display)
                toplevel.minsize(700,500)
                toplevel.title("Cadastro de Conta Poupança")
                toplevel.grab_set()

                self.clabel = tk.Label(toplevel, 
                text="Selecione o cliente para qual desejas criar uma conta poupança",
                font=("Arial","12"))
                self.clabel.pack(side=tk.TOP, fill=tk.X)

                treeview(toplevel)
                
                def select_cliente():
                    selecao = self.tvw.selection()
                    tamanho = len(selecao)
                    if tamanho > 1:
                        confirm = messagebox.askyesno("Confirmar"
                        ,f"Tem certeza que quer criar uma conta poupança para {tamanho} clientes?")
                        if(confirm):
                            for cliente in selecao:
                                cc = ContaPoupaca(cliente, 0)
                                self.banco.contas.append(cc)
                                self.banco.fixar_juros()
                                toplevel.destroy()
                        else:
                            messagebox.showinfo("Cancelado!","Operação cancelada!")
                    else:
                        if tamanho == 0:
                            messagebox.showerror("Error!"
                            ,"Nenhum cliente selecionado!", parent=toplevel)
                        else:
                            confirm = messagebox.askyesno("Confirmar"
                            ,f"Tem certeza que quer criar uma conta poupança para esse cliente?")
                            if(confirm):
                                cc = ContaPoupaca(selecao[0], 0)
                                self.banco.contas.append(cc)

                self.frmBtns = tk.Frame(toplevel)
                self.frmBtns.pack(side=tk.LEFT, fill=tk.BOTH)
                self.btnS1 = tk.Button(self.frmBtns, text="Selecionar cliente(s)", command=select_cliente)
                self.btnS1.grid(row=0, column=0,ipady=10)
            else:
                messagebox.showerror("ERROR!","DEFINA UM BANCO PARA PROSSEGUIR")

        #Tela principal >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

        self.logo = tk.Label(self.display, bg="yellow", text="Gerenciador de Bancos",
            height=3)
        self.logo.pack(side=tk.TOP, fill=tk.X, expand=True)

        self.menuBarra = tk.Menu(self.display)
        self.menu_cadastro = tk.Menu(self.menuBarra, tearoff=0)
        self.menu_cadastro.add_command(label="Criar Cliente", command=criar_cliente)
        self.menu_cadastro.add_command(label="Criar Conta Corrente", command=criar_corrente)
        self.menu_cadastro.add_command(label="Criar Conta Poupanca", command=criar_poupanca)
        self.menuBarra.add_cascade(label="Cadastros", menu=self.menu_cadastro)
        self.display.config(menu=self.menuBarra)

        self.menu_config = tk.Menu(self.menuBarra, tearoff=0)
        self.menuBarra.add_cascade(label="Configurações do banco", menu=self.menu_config)
        self.menu_config.add_command(label="Definir banco", command=definir_banco)
        self.menu_config.add_command(label="Definir juros", command=definir_juros)
        self.menu_config.add_command(label="Definir desconto", command=definir_desconto)

        self.tvw_principal = ttk.Treeview(self.display)
        colunas = ['Conta','Modalidade','Saldo', "Status"]
        self.tvw_principal = ttk.Treeview(self.display, columns=colunas, show="headings")
        self.tvw_principal.pack(side=tk.LEFT, fill=tk.BOTH)
        self.tvw_principal.heading(colunas[0], text="Conta")
        self.tvw_principal.heading(colunas[1], text="Modalidade")
        self.tvw_principal.heading(colunas[2], text="Saldo")
        self.tvw_principal.heading(colunas[3], text="Status")

        scrollbar = tk.Scrollbar(self.display, command=self.tvw_principal.yview)
        scrollbar.pack(side=tk.LEFT, fill=tk.BOTH)
        self.tvw_principal.configure(yscroll=scrollbar.set)

        def sacar():
            toplevel = tk.Toplevel(self.display)
            toplevel.title("Efetuar saque")
            toplevel.grab_set()

            self.lbl_saque = tk.Label(toplevel, text="Digite o valor:")
            self.lbl_saque.grid(row=0, column=0)
            self.entry_saque = tk.Entry(toplevel)
            self.entry_saque.grid(row=0, column=1)

            def confirmar():
                selecao = self.tvw_principal.selection()
                if len(selecao) != 1:
                    messagebox.showerror("Error","Selecione 1 conta somente!", parent=toplevel)
                else:
                    valor = float(self.entry_saque.get())
                    confirm = messagebox.askyesno("Confirmação!",
                    f"Deseja efetuar saque de R${valor:,.2f}?", parent=toplevel)

                    if (confirm):
                        item = self.tvw_principal.item(selecao, "values")
                        for conta in self.banco.contas:
                            if conta.numero == int(item[0]):
                                retorno = conta.sacar(valor)
                                if retorno == True:
                                    messagebox.showinfo("Secesso","Sucesso!", parent=toplevel)
                                    toplevel.destroy()
                                else:
                                    messagebox.showerror("Error",f"{retorno}", parent=toplevel)
                                    toplevel.destroy()
                                atualizar_lista()
                                break
                            
            self.btn_confirmar = tk.Button(toplevel, text='Confirmar!', bg='gray', command=confirmar)
            self.btn_confirmar.grid(row=1, column=0)

        def depositar():
            toplevel = tk.Toplevel(self.display)
            toplevel.title("Efetuar Depósito")
            toplevel.grab_set()

            self.lbl_deposito = tk.Label(toplevel, text="Digite o valor:")
            self.lbl_deposito.grid(row=0, column=0)
            self.entry_deposito = tk.Entry(toplevel)
            self.entry_deposito.grid(row=0, column=1)

            def confirmar():
                selecao = self.tvw_principal.selection()
                if len(selecao) != 1:
                    messagebox.showerror("Error","Selecione 1 conta somente!", parent=toplevel)
                else:
                    valor = float(self.entry_deposito.get())
                    confirm = messagebox.askyesno("Confirmação!",
                    f"Deseja efetuar depósito de R${valor:,.2f}?", parent=toplevel)

                    if (confirm):
                        item = self.tvw_principal.item(selecao, "values")
                        for conta in self.banco.contas:
                            if conta.numero == int(item[0]):
                                retorno = conta.depositar(valor)
                                if retorno == True:
                                    messagebox.showinfo("Secesso","Sucesso!", parent=toplevel)
                                    toplevel.destroy()
                                else:
                                    messagebox.showerror("Error",f"{retorno}", parent=toplevel)
                                    toplevel.destroy()
                                atualizar_lista()
                                break

            self.btn_confirm = tk.Button(toplevel, text="Confirmar", bg="gray", command=confirmar)
            self.btn_confirm.grid(row=1, column=0)

        def atualizacao_mensal():
            selecao = self.tvw_principal.selection()
            if len(selecao) != 1:
                messagebox.showerror("Error","Selecione 1 conta somente!", parent=self.display)
            else:
                item = self.tvw_principal.item(selecao, "values")
                for conta in self.banco.contas:
                    if conta.numero == int(item[0]):
                        if isinstance(conta, ContaPoupaca):
                            messagebox.showinfo("Sucesso","Conta Atualizada!")
                            conta.atualiza()
                            atualizar_lista()
                        else:
                            messagebox.showerror("Error", 
                            "Somente Conta Poupança pode usar 'atualizar'", parent= self.display)

        def extrato():
            selecao = self.tvw_principal.selection()
            item = self.tvw_principal.item(selecao, "values")
            if len(selecao) != 1:
                messagebox.showerror("Error","Selecione 1 conta somente!", parent=self.display)
            else:
                toplevel = tk.Toplevel(self.display)
                toplevel.minsize(700,500)
                toplevel.title("Cadastro de Conta Corrente")
                toplevel.grab_set()

                # self.sct = ScrolledText(toplevel)

                colunas = ['Operação','Valores' ,'Data']
                self.tvw = ttk.Treeview(toplevel, columns=colunas, show="headings")
                self.tvw.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
                self.tvw.heading(colunas[0], text="Operação")
                self.tvw.heading(colunas[1], text="Valores")
                self.tvw.heading(colunas[2], text="Data")

                self.tvw.column(column=[0], minwidth=0, width=300)
                self.tvw.column(column=[1], minwidth=0, width=300)
                self.tvw.column(column=[2], minwidth=0, width=150)

                scrollbar = tk.Scrollbar(toplevel, command=self.tvw.yview)
                scrollbar.pack(side=tk.LEFT, fill=tk.BOTH,expand=True)
                self.tvw.configure(yscroll=scrollbar.set)

                for conta in self.banco.contas:
                    if conta.numero == int(item[0]):
                        for mov in conta.extrato:
                            frag = [x for x in mov.split("|")]
                            self.tvw.insert('',tk.END,values=(frag[1],frag[2],frag[3]))
                        break
            
                def gerar_arquivo():
                    for conta in self.banco.contas:
                        if conta.numero == int(item[0]):
                            conta.imprimir_extrato()
                            messagebox.showinfo("Feito!","Arquivo do extrato gerado!")

                self.frmBtns = tk.Frame(toplevel)
                self.frmBtns.pack(side=tk.LEFT, fill=tk.BOTH)
                self.btnS1 = tk.Button(self.frmBtns, text="Gerar arquivo", command=gerar_arquivo)
                self.btnS1.grid(row=0, column=0,ipady=10)

        def encerrar_conta():
            selecao = self.tvw_principal.selection()
            item = self.tvw_principal.item(selecao, "values")
            if len(selecao) != 1:
                messagebox.showerror("Error","Selecione 1 conta somente!", parent=self.display)
            else:
                for conta in self.banco.contas:
                    if conta.numero == int(item[0]):
                        retorno = conta.change_active()
                        messagebox.showinfo("Info",retorno, parent=self.display)
                        atualizar_lista()

        self.frm_bp = tk.Frame(self.display)
        self.frm_bp.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.btn_atualizar = tk.Button(self.frm_bp, text="Atualizar lista!", command=atualizar_lista)
        self.btn_atualizar.grid(row=0, column=0, ipady=10, sticky=tk.EW, columnspan=2)
        self.btn_sacar = tk.Button(self.frm_bp, text="Efetuar Saque!", command=sacar)
        self.btn_sacar.grid(row=1, column=0, ipady=10, sticky=tk.EW)
        self.btn_depositar = tk.Button(self.frm_bp, text="Efetuar depósito!", command=depositar)
        self.btn_depositar.grid(row=1, column=1, ipady=10, sticky=tk.EW)
        self.btn_extrato = tk.Button(self.frm_bp, text="Extrato", command=extrato)
        self.btn_extrato.grid(row=2, column=0,ipady=10, sticky=tk.EW, columnspan=2)
        self.btn_atualizar = tk.Button(self.frm_bp, text="Atualização Mensal!", command=atualizacao_mensal)
        self.btn_atualizar.grid(row=3, column=0,ipady=10, sticky=tk.EW)
        self.btn_encerrar = tk.Button(self.frm_bp, text="Encerrar conta", command=encerrar_conta)
        self.btn_encerrar.grid(row=3, column=1,ipady=10, sticky=tk.EW)

        # Este frame está empurrando tudo para o topo da página >>>>>>>>>>>>>>>>>>>
        self.frm_empurra_cima = tk.Frame(self.display, height=self.alturaTotal)
        self.frm_empurra_cima.pack(side=tk.BOTTOM)
        # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


app = tk.Tk()
Display(app)
app.mainloop()