import customtkinter as ctk

class ToolbarFrame(ctk.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self._settings_button=ctk.CTkButton(self, text='')

    def Show(self):
        for widget in self.winfo_children():
            widget.pack(side='left', anchor='w')
        self.pack(anchor='n', fill='x')
    
    def load_icons(self, settings_icon):
        self._settings_button.configure(image=settings_icon, compound=ctk.LEFT)

    def set_settings_command(self, command):
        self._settings_button.configure(command=command)
    
    def get_buttons(self):
        return self.winfo_children()