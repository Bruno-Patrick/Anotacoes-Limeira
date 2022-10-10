import tkinter as tk
from tkinter import ttk, messagebox as msg
from turtle import width

class Treeview:

    def columnsgenerator(self,*args):
        columns = []
        for i in args:
            columns.append(i)
        return columns

    def instancetvw(self, master, columns):
        tvw = ttk.Treeview(master, columns=columns, show='headings')
        return tvw

    def heading(self, tvw, columns):
        for num, column in enumerate(columns):
            tvw.heading(columns[num], text=f'{column}')

    def column(self, tvw, columns, *args):
        for num in range(0, len(columns)):
            for configurations in args:
                if num == configurations[0]:
                    tvw.column(column=[num], minwidth=configurations[1], width=configurations[2])           
                else:
                    tvw.column(column=[num], minwidth=0, width=150)           

    def atualizar(self, tvw, tupla):
        for i in tvw.get_children():
            tvw.delete(i)
        for dados in tupla:
            tvw.insert('', tk.END, values=dados)

    def selecionar(self, master, tvw):
        selecao = tvw.selection()
        if len(selecao) != 1:
            msg.showinfo("Operação não permitida!","Selecione apenas 1 professor!", parent=master)
        else:
            item = tvw.item(selecao, 'values')
            return item

tvw = Treeview
coluna = tvw.columnsgenerator('id','nome')
for num, column in enumerate(coluna):
    print(coluna[num])