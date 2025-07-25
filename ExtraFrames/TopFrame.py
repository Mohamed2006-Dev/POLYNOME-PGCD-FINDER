import customtkinter as ctk
from config.assets import Assets

class TopFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.__icon1_label=ctk.CTkLabel(self, compound="top", text = "")

        self.__Title=ctk.CTkLabel(self, text='PGCD FINDER', font=('Arial', 50))

        self.__icon2_label=ctk.CTkLabel(self, compound="top", text='')

        self.__configure_column(3)
    
    def Show(self):
        for (ind,widget), s in zip(enumerate(self.winfo_children()), ['nw', 'n', 'ne']):
            widget.grid(row=0, column=ind, pady=10, sticky=s, padx=10)
        self.pack(fill='x', padx=10, pady=10)

    def __configure_column(self, n:int)->None:
        if not isinstance(n, int):raise TypeError(f"Unexpected TypeError: the object must be 'int' not '{n.__class__}'")
        for i in range(n):
            self.columnconfigure(i, weight=1)

    def set_icons(self, icon1, icon2):
        self.__icon1_label.configure(image=icon1)
        self.__icon2_label.configure(image=icon2)

    def get_title(self):
        return self.__Title
