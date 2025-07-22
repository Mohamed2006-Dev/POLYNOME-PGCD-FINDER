import customtkinter as ctk
from PIL import Image
from ExtraFrames.InstractionsFrame import InstractionsFrame

class TipsWindow(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.geometry("1300x600")
        self.title("Instraction window")
        self.lift()
        self.focus_set()
        self.grab_set()
        self.resizable(False, False) 
        self.Instractionsframe=InstractionsFrame(self)
    
    def Show(self):
        self.Instractionsframe.Show()

    def load_image(self):
        self.Instractionsframe.set_icon(ctk.CTkImage(light_image=Image.open(r'res\user-guide.png'), dark_image=Image.open(r'res\user-guide.png'), size=(50, 50)))
