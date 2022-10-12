from struct import pack
import tkinter as tk

class Tela:

    def __init__(self, master):
        self.display = master
        self.display.title('Lula PT 13')
        self.display.minsize(200,200)

        self.v = tk.StringVar(self.display, '1')
        self.rbt_1 = tk.Radiobutton(self.display
        ,text='Opção 1'
        ,value='1'
        ,variable=self.v
        ).pack()

        self.rbt_2 = tk.Radiobutton(self.display
        ,text='Opção 2'
        ,value='2'
        ,variable=self.v
        ).pack()
        

app = tk.Tk()
Tela(app)
app.mainloop()