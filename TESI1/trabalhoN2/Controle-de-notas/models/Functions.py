from operator import truediv
import tkinter as tk
from tkinter import ttk, messagebox as msg

class Functions:

    def isFieldsEmpty(self, *args):
        for field in args:
            if not field.get():
                return True
        return False