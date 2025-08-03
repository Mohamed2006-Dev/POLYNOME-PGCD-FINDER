import customtkinter as ctk

class ToolbarFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, border_width=1, corner_radius=0)
        self._inner_frame=ctk.CTkFrame(self, corner_radius=0)
        self._settings_button=ctk.CTkButton(self._inner_frame, text='', corner_radius=0, width=20, height=20)
        self._history_button=ctk.CTkButton(self._inner_frame, text='', corner_radius=0, width=20, height=20)

    def Show(self):
        for widget in self._inner_frame.winfo_children():
            widget.pack(side='left', anchor='w')
        self._inner_frame.pack(fill='x',pady=1)
        self.pack(anchor='n', fill='x')
    
    def load_icons(self, settings_icon, history_icon):
        self._settings_button.configure(image=settings_icon, compound=ctk.LEFT)
        self._history_button.configure(image=history_icon, compound=ctk.LEFT)

    def set_settings_command(self, command):
        self._settings_button.configure(command=command)

    def set_history_command(self, command):
        self._history_button.configure(command=command)
    
    def get_buttons(self):
        return self._inner_frame.winfo_children()
    
    def get_inner_frame(self):
        return self._inner_frame