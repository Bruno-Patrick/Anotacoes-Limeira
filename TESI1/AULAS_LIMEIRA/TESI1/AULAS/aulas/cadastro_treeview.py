import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Display:

    def __init__(self, master):
        self.display = master
        self.display.title("Exemplo de Treeview")
        self.display.minsize(300,300)
 
        def deletar():
            selecao = self.tvw.selection()
            try:
                self.tvw.delete(selecao)
            except:
                messagebox.showinfo("Aviso!", "Selecione somente 1 campo!", parent=self.display)

        def del_all():
                answer = messagebox.askyesno('Aviso!','Isso deletará tudo, tens certeza?')
                if answer:
                    all = self.tvw.get_children()
                    for i in all:
                        self.tvw.delete(i)

        def del_select():
            selecao = self.tvw.selection()
            for i in selecao:
                self.tvw.delete(i)          

        def cadastrar():
            topl = tk.Toplevel(self.display)
            topl.title('Cadastro')
            topl.minsize(600,300)
            topl.grab_set()

            self.nome_label_cadastro = tk.Label(topl, text='Digite seu nome:')
            self.nome_label_cadastro.grid(row=0, column=0)
            self.nome_entry_cadastro = tk.Entry(topl, width=70)
            self.nome_entry_cadastro.grid(row=0, column=1)

            self.CPF_label_cadastro = tk.Label(topl, text="Digite seu CPF:")
            self.CPF_label_cadastro.grid(row=1, column=0)
            self.CPF_entry_cadastro = tk.Entry(topl, width=70)
            self.CPF_entry_cadastro.grid(row=1, column=1)

            self.telefone_label_cadastro = tk.Label(topl, text="Digite seu telefone:")
            self.telefone_label_cadastro.grid(row=2, column=0)
            self.telefone_entry_cadastro = tk.Entry(topl, width=30)
            self.telefone_entry_cadastro.grid(row=2, column=1, sticky=tk.EW)
        

            def verify():
                if self.nome_entry_cadastro.get() == '' or self.CPF_entry_cadastro.get() == '' or self.telefone_entry_cadastro.get() == '':
                    messagebox.showerror("Aviso!", "Todos os campos devem estar preenchidos!", parent=topl)
                else:
                    for i in range (15):
                        self.tvw.insert('', tk.END, values=(
                            self.nome_entry_cadastro.get(), self.CPF_entry_cadastro.get(), self.telefone_entry_cadastro.get()
                            ))
                    topl.destroy()

            frm_btns = tk.Frame(topl)
            frm_btns.grid(row=3,column=0)

            btn_confirmar = tk.Button(frm_btns, text='Confirmar cadastro',
             bg='grey', command=verify)
            btn_confirmar.pack(side=tk.LEFT)

            btn_cancelar = tk.Button(frm_btns, text='Cancelar cadastro', command=topl.destroy)
            btn_cancelar.pack(side=tk.LEFT)


        frm = tk.Frame(self.display)
        frm.pack(side=tk.BOTTOM)

        colunas = ['Nome', 'CPF', 'Telefone']

        self.tvw = ttk.Treeview(self.display, columns=colunas, show='headings')
        self.tvw.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.tvw.heading(colunas[0], text='Nome')
        self.tvw.heading(colunas[1], text='CPF')
        self.tvw.heading(colunas[2], text='Telefone')

        self.tvw.column(column=[0], minwidth=0, width=300)
        self.tvw.column(column=[1], minwidth=0, width=300)
        self.tvw.column(column=[2], minwidth=0, width=150)

        scrollbar = tk.Scrollbar(self.display, command=self.tvw.yview)
        scrollbar.pack(side=tk.LEFT, fill=tk.BOTH)
        self.tvw.configure(yscroll=scrollbar.set)


        #Cadastro
        btn_cadastro = tk.Button(frm, text='Cadastrar',
         bg='green', width=15, command=cadastrar)
        btn_cadastro.grid(row=0, column=0)

        #Delete
        btn_cadastro = tk.Button(frm, text='Deletar', bg='red', width=15, command=deletar)
        btn_cadastro.grid(row=0, column=1)

        #Delete select only
        btn_del_select = tk.Button(frm, text="Deletar selecionados", command=del_select)
        btn_del_select.grid(row=0, column=2)    

        #delete all
        btn_del_all = tk.Button(frm, text="Deletar todos!", command=del_all)
        btn_del_all.grid(row=0, column=3)

        def topl_atualizar():

            def atualizar_janela():
                topl_atualizar = tk.Toplevel(self.display)
                topl_atualizar.title('Atualizar dado')
                topl_atualizar.minsize(400,200)
                topl_atualizar.grab_set()

                self.nome_label_atualizar = tk.Label(topl_atualizar, text='Digite seu nome:')
                self.nome_label_atualizar.grid(row=0, column=0)
                self.nome_entry_atualizar = tk.Entry(topl_atualizar, width=50)
                self.nome_entry_atualizar.grid(row=0, column=1) 

                self.CPF_label_atualizar = tk.Label(topl_atualizar, text="Digite seu CPF:")
                self.CPF_label_atualizar.grid(row=1, column=0)
                self.CPF_entry_atualizar = tk.Entry(topl_atualizar, width=50)
                self.CPF_entry_atualizar.grid(row=1, column=1)

                self.telefone_label_atualizar = tk.Label(topl_atualizar, text="Digite seu telefone:")
                self.telefone_label_atualizar.grid(row=2, column=0)
                self.telefone_entry_atualizar = tk.Entry(topl_atualizar)
                self.telefone_entry_atualizar.grid(row=2, column=1, sticky=tk.EW)

                frm_btns_atualizar = tk.Frame(topl_atualizar)
                frm_btns_atualizar.grid(row=3,column=0)

                def confirmar():
                    nome = self.nome_entry_atualizar.get()
                    cpf = self.CPF_entry_atualizar.get()              
                    telefone = self.telefone_entry_atualizar.get()

                    if item[0] == nome and item[1] == cpf and item[2] == telefone:
                        messagebox.showwarning('Aviso!',
                        'Você deve alterar alguma coisa!', parent=topl_atualizar)
                    else:
                        confirmacao = messagebox.askyesno("Alterações feitas!",
                         "Deseja confirmar?", parent = topl_atualizar )
                        if confirmacao:
                            self.tvw.item(selecao, values=(nome, cpf, telefone))

                btn_confirmar = tk.Button(frm_btns_atualizar, text='Confirmar atualização',              
                bg='grey', command=confirmar)
                btn_confirmar.pack(side=tk.LEFT)

                btn_cancelar = tk.Button(frm_btns_atualizar, text='Cancelar atualização', command=topl_atualizar.destroy)
                btn_cancelar.pack(side=tk.LEFT)

            selecao = self.tvw.selection()
            if len(selecao) == 1:
                item = self.tvw.item(selecao, 'values')
                atualizar_janela()
                self.nome_entry_atualizar.insert(0, item[0])
                self.CPF_entry_atualizar.insert(0, item[1])
                self.telefone_entry_atualizar.insert(0, item[2])
            else:
                messagebox.showwarning("Alerta!", "Selecione somente 1 campo", parent=self.display)

        #atualizar
        btn_atualizar = tk.Button(frm, text="Atualizar!", command=topl_atualizar)
        btn_atualizar.grid(row=0, column=4)


app = tk.Tk()
Display(app)
app.mainloop()