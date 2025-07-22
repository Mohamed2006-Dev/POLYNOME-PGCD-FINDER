import customtkinter as ctk
from utils.ButtonsCommands import keyboard_touche
from utils.ExtraMethods import  ExtraMethods as E
class KeyboardFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.btns={}
        self.clear_btns={}
        self.__is_shown=False
        self.__load_btns()
        self.column_config()
    
    def __load_btns(self):
        btns={}
        for i in list(range(10))+["+", "-", "*", "/", ".", "**"]:
            btn=ctk.CTkButton(self, text=f'{i}', font = ("Arial", 15))
            name=f"btn_{i}"
            btns[name]=btn
        
        position=[]
        for i, r in enumerate([[0, 1, 2], [0, 1, 2], [0, 1, 2]]):
            for c in r:
                position.append((c, i))
        
        for i in range(9, 0, -1):
            name=f'btn_{i}'
            row, col = position[9-i]
            self.btns[name] = (btns[name], row, col)

        for i in [("btn_+", 0, 3), ("btn_-", 1, 3), ("btn_*", 2, 3), ("btn_/", 3, 3), ("btn_.", 3, 1), ("btn_**", 3, 2)]:
            name, row, col=i
            self.btns[name] = (btns[name], row, col)
            self.btns[name][0].configure(fg_color='#313131')
        self.btns['btn_0']=(btns["btn_0"], 3, 0)

        delete_btn=ctk.CTkButton(self, text = 'DELETE', fg_color='#313131', compound='top')
        clear_btn=ctk.CTkButton(self, text = 'CLS', fg_color='#313131', font = ("Arial", 40, 'bold'))\

        self.clear_btns["btn_delete"]=(delete_btn, 0, 4)
        self.clear_btns['btn_clear']=(clear_btn, 2, 4)

    def getbtns(self, type):
        btns_type=None
        match (type):
            case "general":
                btns_type=self.btns
            case "clear":
                btns_type=self.clear_btns
        btns=[]
        for btn in tuple(btns_type.values()):
            btns.append(btn[0])
        return btns
    
    def Show(self):
        E.iterate_over_btns(self.btns, 'ew')
        E.iterate_over_btns(self.clear_btns, 'nwes', 2)
        self.pack(padx= 10, pady = 10, fill = 'x', side= 'bottom')
        self.__is_shown=not self.__is_shown

    def Hide(self):
        self.pack_forget()
        self.__is_shown=not self.__is_shown
    
    def set_btns_command(self, btn, command):
        btn.configure(command=command)
    def set_clear_btns_command(self, command1, command2):
        self.clear_btns['btn_clear'][0].configure(command=command1)
        self.clear_btns['btn_delete'][0].configure(command=command2)
    
    def getkeyboard_state(self):
        return self.__is_shown
    
    def column_config(self):
        for i in range(4):
            self.columnconfigure(i, weight=1)