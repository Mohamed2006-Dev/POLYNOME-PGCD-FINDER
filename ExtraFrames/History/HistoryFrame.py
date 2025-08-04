import customtkinter as ctk

class HistoryFrame(ctk.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self._history_item_label = ctk.CTkLabel(self, text='')
        self._show_btn = ctk.CTkButton(self, text='')
        self._copy_clipboard_btn = ctk.CTkButton(self, text='')

        self._btns = [self._show_btn, self._copy_clipboard_btn]

    def Show(self):
        self._history_item_label.pack(side='left', anchor='w', padx=10)
        for btn in self._btns:
            btn.pack(side='right', anchor='e', fill='y')
        self.pack(fill='x', pady=10, padx=10)

    def set_icons(self, show_icon, copy_icon):
        self._show_btn.configure(image=show_icon)
        self._copy_clipboard_btn.configure(image=copy_icon)

    def set_font(self, font):
        self._history_item_label.configure(font=font)

    def set_color(self, color):
        self._history_item_label.configure(text_color=color)
    
    def set_history_label(self, text):
        self._history_item_label.configure(text=text)

    def set_show_command(self, command):
        self._show_btn.configure(command=command)

    def set_copy_clipboard_command(self, command):
        self._copy_clipboard_btn.configure(command=command)
    