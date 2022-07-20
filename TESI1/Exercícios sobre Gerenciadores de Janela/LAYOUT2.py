from cmath import exp
import tkinter as tk

class Display:
    def __init__(self, master):
        self.display = master
        self.display.geometry("300x180")
        self.display.title("Layout 01")

        l1 = tk.Label(
            self.display, text="TOPO", bg="red"
        )
        l1.pack(fill=tk.BOTH,expand=True)

        l2 = tk.Label(
            self.display, text="TOPO", bg="green"
        )
        l2.pack(fill=tk.BOTH,expand=True)

        l3 = tk.Label(
            self.display, text="TOPO", bg="blue"
        )
        l3.pack(fill=tk.BOTH,expand=True)

        Left = tk.Label(
            self.display, bg="gray", text="ESQUERDA"
        )
        Left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        Right = tk.Label(
            self.display, bg="gray", text="DIREITA"
        )
        Right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        blackBLock = tk.Label(
            self.display, text="TOPO", bg="black"
        )
        blackBLock.pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)

        Left2 = tk.Label(
            self.display, bg="cyan", text="ESQUERDA"
        )
        Left2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        Right2 = tk.Label(
            self.display, bg="yellow", text="DIREITA"
        )
        Right2.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        Right2 = tk.Label(
            self.display, bg="magenta", text="DIREITA"
        )
        Right2.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)





app = tk.Tk()
Display(app)
app.mainloop()