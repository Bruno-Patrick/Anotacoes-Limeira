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

    def column(self, tvw, columns):
        for num, column in enumerate(columns):
            tvw.heading(column[num], minwidth=150, width=150)           

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