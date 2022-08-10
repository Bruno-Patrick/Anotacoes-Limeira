import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Frame:
    def __init__(self, master):
        self.display = master
        self.display.title("Exemplo com frames")
        self.display.minsize(300,300)


        self.colunas = ('Nome','Email','Telefone')
        self.tvw = ttk.Treeview(self.display, columns=self.colunas, show='headings', height=5)
        self.tvw.grid(row=0, column=0)

        self.tvw.heading('Nome',text='Nome')
        self.tvw.heading('Email',text='Email')
        self.tvw.heading('Telefone',text='Telefone')

        self.tvw.column('Nome', minwidth=0, width=300)
        self.tvw.column('Email', minwidth=0, width=250)
        self.tvw.column('Telefone', minwidth=0, width=200)

        self.scr = ttk.Scrollbar(self.display, command=self.tvw.yview)
        self.scr.grid(row=0, column=1, sticky=tk.NS)
        self.tvw.config(yscroll=self.scr.set)

        self.frame = tk.Frame(self.display)
        self.frame.grid(row=1, column=0)

        def inserir(texto):
            self.tvw.insert('', 'end', text=texto)

        def confirmar():
            nome = self.entryNome.get()
            email = self.entryEmail.get()
            telefone = self.entryTelefone.get()
            if nome == '' or email == '' or telefone == '':
                messagebox.showwarning("Error","Todos os campos devem estar preenchidos!")
            else:
                inserir(nome)
                inserir(email)
                inserir(telefone)

        def toplevel():
            self.topl = tk.Toplevel()
            self.topl.title("Cadastro")
            self.topl.minsize(400,400)

            self.lblNome = tk.Label(self.topl, text='Nome:')
            self.lblNome.grid(row=0, column=0)

            self.entryNome = tk.Entry(self.topl, width=60)
            self.entryNome.grid(row=0, column=1)

            self.lblEmail = tk.Label(self.topl, text='Email:')
            self.lblEmail.grid(row=1, column=0)

            self.entryEmail = tk.Entry(self.topl, width=60)
            self.entryEmail.grid(row=1, column=1)

            self.lblTelefone = tk.Label(self.topl, text='Telefone:')
            self.lblTelefone.grid(row=2, column=0)

            self.entryTelefone = tk.Entry(self.topl, width=60)
            self.entryTelefone.grid(row=2, column=1)

            self.frametopl = tk.Frame(self.topl)
            self.frametopl.grid(row=3, column=0)

            self.btnCadastroTopl = tk.Button(self.topl, text='Efetuar Cadastro', width=30, bg='yellow', command=confirmar)
            self.btnCadastroTopl.grid(row=3,column=0)

        self.btn_cadastro = tk.Button(self.frame, text='Fazer Cadastro', width=20, command=toplevel)
        self.btn_cadastro.pack()



app = tk.Tk()
Frame(app)
app.mainloop()