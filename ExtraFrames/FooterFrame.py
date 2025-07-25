import customtkinter as ctk
from config.assets import Assets

class FooterFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.__tipsbutton=ctk.CTkButton(self, text='TIPS', width = 50, height = 50, font = ("Arial", 35))

        self.__techbutton=ctk.CTkButton(self, text = 'keyboard', width = 50, height = 50, font = ("Arial", 35))
        
        self.__examplebutton=ctk.CTkButton(self, text= "EXAMPLE", width = 50, height = 50, font = ("Arial", 35))

        self.column_config()

        

    def Show(self, sticky:list[str]):
        for i, (widget, s) in zip(range(len(sticky)), zip(self.winfo_children(), sticky)):
            widget.grid(row=0, column=i, padx = 20, sticky=s)
        self.pack(fill = 'x', side = 'bottom', padx=10, pady=10, anchor = 'center')
        

    def column_config(self):
        for i in range(3):
            self.columnconfigure(i, weight=1)
        
    def set_example_command(self, command):
        self.__examplebutton.configure(command=command)

    def set_keyboard_command(self, command):
        self.__techbutton.configure(command=command)

    def set_tips_command(self, command):
        self.__tipsbutton.configure(command=command)

    def set_icons(self, tipsicon, keyboardicon, exampleicon):
        self.__tipsbutton.configure(image=tipsicon, compound='left')
        self.__techbutton.configure(image=keyboardicon, text='', compound='top')
        self.__examplebutton.configure(image=exampleicon, compound='right')

    def get_buttons(self):
        return [self.__techbutton, self.__examplebutton, self.__tipsbutton]
    
