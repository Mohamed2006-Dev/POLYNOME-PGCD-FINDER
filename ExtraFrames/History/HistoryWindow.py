import customtkinter as ctk

class HistoryWindow(ctk.CTkToplevel):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.geometry("800x600")
        self.title("History")
        self.lift()         # Bring window to front
        self.focus_set()    # Focus on this window
        self.grab_set()     # Make this window modal

        self.empty_window = ctk.CTkLabel(
            self,
            text="No operations have been performed yet.\nYour operation history will appear here.",
            font=('Sergio UI', 35)
        )
        self._delete_btn = ctk.CTkButton(self, text='', height=50, width=50)

    def show_empty(self):
        self.empty_window.pack(expand=True)
    
    def set_color(self, color):
        self.configure(fg_color=color)

    def load_icon(self, icon):
        self._delete_btn.configure(image=icon, compound='top')
    
    def show_delete_btn(self):
        self._delete_btn.pack(side='right', anchor='se')
    
    def set_delete_btn_command(self, command):
        self._delete_btn.configure(command=command)