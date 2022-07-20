import tkinter as tk

class Display:
    def __init__(self, master):
        self.display = master
        self.display.geometry("300x300")
        self.display.title("Layout 01")

        button1 = tk.Button(
            text='1'
        )
        button1.grid(row=0, column=1)

        button1 = tk.Button(
            text='2'
        )
        button1.grid(row=1, column=0,columnspan=2)

        button1 = tk.Button(
            text='3'
        )
        button1.grid(row=1, column=1,columnspan=2)

        button1 = tk.Button(
            text='4'
        )
        button1.grid(row=2, column=0)

        button1 = tk.Button(
            text='5'
        )
        button1.grid(row=2, column=1)

        button1 = tk.Button(
            text='6'
        )
        button1.grid(row=2, column=2)


app = tk.Tk()
Display(app)
app.mainloop()