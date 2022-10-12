import tkinter as tk
from turtle import left

class Tela:
    def __init__(self, master):
        self.display =  master
        self.display.minsize(400,100)
        self.display.title("Layout 01")

        self.display.top = tk.Label(
            self.display
            ,text="TOPO"
            ,bg="yellow"
            ,width=50
            ,height=5
        ).pack()

        self.display.mid = tk.Label(
            self.display
            ,text="ESQUERDA"
            ,bg="red"
            ,width=25
            ,justify="left"
        ).pack()

        self.display.midR = tk.Label(
            self.display
            ,text="ESQUERDA"
            ,bg="red"
            ,width=25
            ,justify="left"
        ).pack()


principalDisplay = tk.Tk()
Tela(principalDisplay)
principalDisplay.mainloop()