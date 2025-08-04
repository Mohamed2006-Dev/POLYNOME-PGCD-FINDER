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

    def show_empty(self):
        self.empty_window.pack(expand=True)
    
    def set_color(self, color):
        self.configure(fg_color=color)
    