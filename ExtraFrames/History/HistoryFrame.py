import customtkinter as ctk

class HistoryFrame(ctk.CTkFrame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, border_width=3,*args, **kwargs)
        self._inner_frame=ctk.CTkFrame(self)
        self._history_item_label = ctk.CTkLabel(self._inner_frame, text='')
        self._show_btn = ctk.CTkButton(self._inner_frame, text='', corner_radius=0, border_width=2)
        self._copy_clipboard_btn = ctk.CTkButton(self._inner_frame, text='', corner_radius=0, border_width=2)

        self._btns = [self._show_btn, self._copy_clipboard_btn]

    def Show(self):
        self._history_item_label.pack(side='left', anchor='w', padx=10)
        for btn in self._btns:
            btn.pack(side = 'right', anchor = 'e', fill = 'y')
        self._inner_frame.pack(fill='x', pady=10, padx=5)
        self.pack(fill = 'x', pady = 10, padx = 10)

    def set_icons(self, show_icon, copy_icon):
        self._show_btn.configure(image=show_icon, compound=ctk.TOP)
        self._copy_clipboard_btn.configure(image=copy_icon, compound=ctk.TOP)
    
    def set_history_label(self, text):
        self._history_item_label.configure(text=text)

    def set_show_command(self, command):
        self._show_btn.configure(command=command)

    def set_copy_clipboard_command(self, command):
        self._copy_clipboard_btn.configure(command=command)
    
    def set_colors(self, history_label_color, history_frame_border_color, buttons_fg_color):
        self._history_item_label.configure(text_color = history_label_color)
        self.configure(border_color = history_frame_border_color)
        for b in self._btns:
            b.configure(fg_color=buttons_fg_color, hover_color=buttons_fg_color)

    def set_font(self, history_label_font):
        self._history_item_label.configure(font = history_label_font)