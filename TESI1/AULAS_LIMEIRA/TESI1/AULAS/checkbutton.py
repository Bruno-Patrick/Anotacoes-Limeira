from multiprocessing.sharedctypes import Value
from struct import pack
import tkinter as tk

class Tela:

    def __init__(self, master):
        self.display = master
        self.display.title('Lula PT 13')
        self.display.minsize(200,200)

        self.v = tk.StringVar(self.display, '1')
       
        self.v1 = tk.IntVar()
        self.v2 = tk.IntVar
        ckb_1 = tk.Checkbutton(self.display
            ,text='Op 1'
            ,variable=self.v1
        ).pack()
        ckb_2 = tk.Checkbutton(self.display
            ,text='Op 2'
            ,variable=self.v2
        ).pack()
        

app = tk.Tk()
Tela(app)
app.mainloop()