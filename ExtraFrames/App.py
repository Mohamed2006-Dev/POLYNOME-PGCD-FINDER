import customtkinter as ctk
import sympy as sp
from PIL import Image
from ExtraFrames.EntryFrame import EntryFrame
from ExtraFrames.TopFrame import TopFrame

class App(ctk.CTk):
    def __init__(self, title='PGCD FINDER'):
        super().__init__()
        self.title(title)
        self.after(100, lambda: self.state('zoomed'))
        self.maxsize(800, 900)
        self.minsize(600, 850)
        