import customtkinter as ctk
from ExtraFrames.Settings.SettingsWindow import SettingsWindow

class ToolbarFrame(ctk.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self._settings_button=ctk.CTkButton(self, text='')

    def Show(self):
        for widget in self.winfo_children():
            widget.pack(side='left')
        self.pack(anchor='n', fill='x')
    
    def load_icon(self, settings_icon):
        self._settings_button.configure(image=settings_icon, compound=ctk.TOP)