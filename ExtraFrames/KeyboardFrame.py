import customtkinter as ctk
from utils.ButtonsCommands import keyboard_touche
from utils.ExtraMethods import  ExtraMethods as E
from theme.color import Color

class KeyboardFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, border_width=4)
        self.btns={}
        self.clear_btns={}
        self.__is_shown=False

        self.inner_frame=ctk.CTkFrame(self, fg_color='transparent')
        self.inner_frame.pack(fill='both', padx=8, pady=8)

        self.__load_btns()
        self.column_config()
    
    def __load_btns(self):
        btns={}
        for i in list(range(10))+["+", "-", "*", "/", ".", "**"]:
            btn=ctk.CTkButton(self.inner_frame, text=f'{i}', font = ("Arial", 15))
            name=f"btn_{i}"
            btns[name]=btn
        
        position=[]
        for i, r in enumerate([[2, 1, 0], [2, 1, 0], [2, 1, 0]]):
            for c in r:
                position.append((i, c))
        
        for i in range(9, 0, -1):
            name=f'btn_{i}'
            row, col = position[9-i]
            self.btns[name] = (btns[name], row, col)

        for i in [("btn_+", 0, 3), ("btn_-", 1, 3), ("btn_*", 2, 3), ("btn_/", 3, 3), ("btn_.", 3, 1), ("btn_**", 3, 2)]:
            name, row, col=i
            self.btns[name] = (btns[name], row, col)
        self.btns['btn_0']=(btns["btn_0"], 3, 0)

        delete_btn=ctk.CTkButton(self.inner_frame, text = 'DELETE', compound='top')
        clear_btn=ctk.CTkButton(self.inner_frame, text = 'CLEAR', font = ("Arial", 40, 'bold'))\

        self.clear_btns["btn_delete"]=(delete_btn, 0, 4)
        self.clear_btns['btn_clear']=(clear_btn, 2, 4)

        del position, btns, delete_btn, clear_btn

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
        E.iterate_over_btns(self.clear_btns, 'nsew', 2)

        self.pack(padx= 10, pady = 10, side= 'bottom')
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
    
    def configure_btns(self, icon):
        self.btns['btn_**'][0].configure(image=icon, compound='top', text='')
        self.btns['btn_*'][0].configure(text='×')
        self.btns['btn_/'][0].configure(text='÷')

    def getallbtns(self):
        btns=[]
        for key in self.btns.keys():
            btns.append(self.btns[key][0])
        for key in self.clear_btns.keys():
            btns.append(self.clear_btns[key][0])
        return btns
    
    def getnumericbtns(self):
        btns=[]
        for i in range(10):
            btns.append(self.btns[f'btn_{i}'][0])
        return btns

    def get_non_numeric_btns(self):
        numeric_btns=self.getnumericbtns()
        btns=[]
        for btn in filter(lambda x: x not in numeric_btns, self.getallbtns()):
            btns.append(btn)
        return btns