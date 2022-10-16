import tkinter as tk
from tkinter import ttk, messagebox as msg
from turtle import width

class Treeview:

    def columnsgenerator(self,*args):
        columns = []
        for i in args:
            if 'N1=' in i:
                i = i.split('N1=')
                i = i[1]
                for j in range(0,int(i)):
                    columns.append(f'atvN1.{j+1}')
            elif 'N2=' in i:
                i = i.split('N2=')
                i = i[1]
                for j in range(0,int(i)):
                    columns.append(f'atvN2.{j+1}')
            else:
                columns.append(i)
        print(columns)
        return columns

    def instancetvw(self, master, columns):
        tvw = ttk.Treeview(master, columns=columns, show='headings')
        return tvw

    def heading(self, tvw, columns):
        for num, column in enumerate(columns):
            tvw.heading(columns[num], text=f'{column}')

    def column(self, tvw, columns):
        for num in range(0, len(columns)):
            if columns[num] == 'id':
                tvw.column(column=[num], minwidth=0, width=30)  
            elif columns[num] == 'nome':
                tvw.column(column=[num], minwidth=0, width=250)
            elif 'atv' in columns[num]:
                tvw.column(column=[num], minwidth=0, width=30)
            else:
                tvw.column(column=[num], minwidth=0, width=80)

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