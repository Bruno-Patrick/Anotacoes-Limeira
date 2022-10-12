from cgitb import text
import tkinter as tk

class Display:
    def __init__(self, master):
        self.display = master
        self.display.geometry("250x250")
        self.display.title('Calculadora')

        result = tk.Entry(self.display,bg="gray").grid(
            row=0, column=0, columnspan=4
        )

        button = tk.Button(self.display,text="7"
        ).grid(row=1, column=0)

        button = tk.Button(self.display,text="8"
        ).grid(row=1, column=1)

        button = tk.Button(self.display,text="9"
        ).grid(row=1, column=2)

        button = tk.Button(self.display,text="/"
        ).grid(row=1, column=3)

app = tk.Tk()
Display(app)
app.mainloop()