from pickle import TRUE
import tkinter as tk
from tkinter import ttk, messagebox
import Connection as bd

class Display:

    def __init__(self, master):
        self.display = master
        self.display.geometry("500x500")
        self.display.title("Cadastro de Clientes")
        

        self.frame = tk.Frame(self.display)
        self.frame.pack()


        self.name = tk.Label(self.frame, text="Nome:")
        self.name.grid(row=0, column=0)
        self.nameE = tk.Entry(self.frame, width=50)
        self.nameE.grid(row=0, column=1, columnspan=2)

        self.CPF = tk.Label(self.frame, text="CPF:")
        self.CPF.grid(row=1, column=0)
        self.CPFE = tk.Entry(self.frame, width=50)
        self.CPFE.grid(row=1, column=1, columnspan=2)

        def apagar_tvw():
            for i in self.tvw.get_children():
                self.tvw.delete(i)

        def inserir():
            name = self.nameE.get()
            cpf = self.CPFE.get()
            query = f"INSERT INTO cliente(nome, cpf) VALUES('{name}', '{cpf}');"
            bd.operation(query)
            messagebox.showinfo("Aviso", "Inserção feita com sucesso!", parent=self.display)
            apagar_tvw()
            atualizar_tvw()

            self.nameE.delete(0, 'end')
            self.CPFE.delete(0, 'end')

        def atualizar_tvw():
            query = 'SELECT * FROM cliente'
            dados = bd.consult(query)
            for x,y,z in dados:
                self.tvw.insert('',tk.END, values=(x,y,z))

        self.insertBtn = tk.Button(self.frame, text="Inserir", command=inserir)
        self.insertBtn.grid(row=2,column=2, sticky=tk.E)

        self.tvw = ttk.Treeview(self.frame, columns=('id','nome','cpf'), show='headings')
        self.tvw.grid(row=3, column=0, columnspan=3)

        self.tvw.heading('id',text='ID')
        self.tvw.heading('nome',text='NOME')
        self.tvw.heading('cpf',text='CPF')

        self.tvw.column('id', width=50)
        self.tvw.column('nome', width=225)
        self.tvw.column('cpf', width=225)
        atualizar_tvw()

        def deletar():
            for data in self.tvw.selection():
                item = self.tvw.item(data, 'values')
                query = f"DELETE FROM cliente WHERE id = {item[0]}"
                bd.operation(query)
            apagar_tvw()
            atualizar_tvw()
                
        def atualizar():
            for data in [x for x in self.tvw.selection() if len(self.tvw.selection()) == 1]:
                nome = self.tvw.item(data, 'values')[1]
                cpf = self.tvw.item(data, 'values')[2]

                self.nameE.insert(0, nome)
                self.CPFE.insert(0, cpf)

                self.confirmar['state'] = tk.NORMAL
                self.insertBtn['state'] = tk.DISABLED
                self.atualizar['state'] = tk.DISABLED
                self.deleteBtn['state'] = tk.DISABLED


        def confirmar():
            id = self.tvw.item(self.tvw.selection(), 'values')[0]
            nome = self.nameE.get()
            cpf = self.CPFE.get()

            query = f"UPDATE cliente SET nome='{nome}', cpf='{cpf}' WHERE id = {id}"

            bd.operation(query)
            apagar_tvw()
            atualizar_tvw()
            self.confirmar['state'] = tk.DISABLED
            self.atualizar['state'] = tk.NORMAL
            self.insertBtn['state'] = tk.NORMAL
            self.deleteBtn['state'] = tk.NORMAL

            self.nameE.delete(0, 'end')
            self.CPFE.delete(0, 'end')

        def cancelar():
            self.confirmar['state'] = tk.DISABLED
            self.cancelar['state'] = tk.DISABLED
            self.atualizar['state'] = tk.NORMAL
            self.insertBtn['state'] = tk.NORMAL
            self.deleteBtn['state'] = tk.NORMAL

            self.nameE.delete(0, 'end')
            self.CPFE.delete(0, 'end')

        self.framedelete = tk.Frame(self.display)
        self.framedelete.pack()

        self.deleteBtn = tk.Button(self.framedelete, text="Deletar", command=deletar)
        self.deleteBtn.grid(row=0,column=0)

        self.atualizar = tk.Button(self.framedelete, text="Atualizar", command=atualizar)
        self.atualizar.grid(row=0,column=1)

        self.confirmar = tk.Button(self.framedelete, text="Confirmar", command=confirmar)
        self.confirmar['state'] = tk.DISABLED
        self.confirmar.grid(row=0,column=2)

        self.cancelar = tk.Button(self.framedelete, text="Cancelar", command=cancelar)
        self.cancelar['state'] = tk.DISABLED
        self.cancelar.grid(row=0,column=3)

app = tk.Tk()
Display(app)
app.mainloop()