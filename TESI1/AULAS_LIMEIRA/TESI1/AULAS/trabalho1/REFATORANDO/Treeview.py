import tkinter as tk

class Treeview:
    __slots__ = ['columns','layouts']
    def __init__(self):
        self.__columns = []
        self.__layouts = ('place', 'grid', 'pack')

    @property
    def columns(self):
        return self.__columns

    def Insertcolumns(*args):
        for column in args:
            self.column.append(column)

    def layout(self, component, layout, configs):
        if layout == 'pack':
            component.pack(configs)
        elif layout == 'grid':
            component.grid(configs)

    def treeview(self, master):
        self.tvw = ttk.Treeview(master, columns=self.columns, show="headings")

        for column in self.columns:
            self.tvw.heading(self.columns[column], text=f"{column}")