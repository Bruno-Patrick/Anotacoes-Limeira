import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Display:

    def __init__(self, master):
        self.display = master
        self.display.title("Exemplo de Treeview")
        self.display.minsize(300,300)
 
        def deletar():
            selecao = tvw.selection()
            try:
                tvw.delete(selecao)
            except:
                for i in range(0, len(selecao)):
                    tvw.delete(selecao[i])

        def cadastrar():
            topl = tk.Toplevel(self.display)
            topl.title('Cadastro')
            topl.geometry('600x200')

            nome_label = tk.Label(topl, text='Digite seu nome:')
            nome_label.grid(row=0, column=0)
            nome_entry = tk.Entry(topl, width=70)
            nome_entry.grid(row=0, column=1)

            email_label = tk.Label(topl, text="Digite seu email:")
            email_label.grid(row=1, column=0)
            email_entry = tk.Entry(topl, width=70)
            email_entry.grid(row=1, column=1)

            telefone_label = tk.Label(topl, text="Digite seu telefone:")
            telefone_label.grid(row=2, column=0)
            telefone_entry = tk.Entry(topl, width=30)
            telefone_entry.grid(row=2, column=1, sticky=tk.EW)
        

            def verify():
                if nome_entry.get() == '' or email_entry.get() == '' or telefone_entry.get() == '':
                    messagebox.showwarning("Preencha os campos!", "Todos os campos devem estar preenchidos!")
                else:
                    for i in range(15):
                        tvw.insert('', tk.END, values=(
                            nome_entry.get(), email_entry.get(), telefone_entry.get()
                            ))
                    topl.destroy()

            btn_confirmar = tk.Button(topl, text='Confirmar cadastro',
             bg='grey', command=verify)
            btn_confirmar.grid(row=3, column=0)

            btn_delete = tk.Button(topl, text='Cancelar cadastro', command=topl.destroy)
            btn_delete.grid(row=3, column=1)


        frm = tk.Frame(self.display)
        frm.pack(side=tk.BOTTOM)

        colunas = ['Nome', 'Email', 'Telefone']

        tvw = ttk.Treeview(self.display, columns=colunas, show='headings')
        tvw.pack(side=tk.LEFT, fill=tk.BOTH)

        tvw.heading(colunas[0], text='Nome')
        tvw.heading(colunas[1], text='Email')
        tvw.heading(colunas[2], text='Telefone')

        tvw.column(column=[0], minwidth=0, width=300)
        tvw.column(column=[1], minwidth=0, width=300)
        tvw.column(column=[2], minwidth=0, width=150)

        scrollbar = tk.Scrollbar(self.display, command=tvw.yview)
        scrollbar.pack(side=tk.LEFT, fill=tk.BOTH)
        tvw.configure(yscroll=scrollbar.set)


        #Cadastro
        btn_cadastro = tk.Button(frm, text='Cadastrar',
         bg='green', width=15, command=cadastrar)
        btn_cadastro.grid(row=0, column=0)

        #Delete
        btn_cadastro = tk.Button(frm, text='Deletar', bg='red', width=15, command=deletar)
        btn_cadastro.grid(row=0, column=1)


app = tk.Tk()
Display(app)
app.mainloop()