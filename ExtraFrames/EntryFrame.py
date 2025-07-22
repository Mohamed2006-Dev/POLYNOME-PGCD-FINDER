import customtkinter as ctk
from PIL import Image
from utils.ExtraMethods import ExtraMethods as E
from utils.parser import validate_entry

class EntryFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.__str_var_1=ctk.StringVar()
        self.__entry1=ctk.CTkEntry(self, width=200, height=40, textvariable=self.__str_var_1, font=("Arial", 20), text_color=("#0303BD", '#30AEE5'))

        self.__image=Image.open("res\\diviser.png")
        self.__tk_image=ctk.CTkImage(self.__image, self.__image, (30, 30))
        self.__pgcd_finder_button = ctk.CTkButton(self, text='', font=("Arial", 25), image=self.__tk_image, command=None, compound='top', fg_color='transparent')
        self.__entry1.bind("<KeyRelease>", lambda x: validate_entry(self.__entry1, self.__str_var_1, "A(X)"))
        self.__entry1.bind("<FocusIn>", lambda x: self.setfocus(self.__entry1))

        self.__str_var_2=ctk.StringVar()
        self.__entry2=ctk.CTkEntry(self, width=200, height=40, textvariable=self.__str_var_2, font=("Arial", 20), text_color=("#0303BD", '#30AEE5'))
        self.__entry2.bind("<KeyRelease>", lambda x: validate_entry(self.__entry2, self.__str_var_2, "B(X)"))
        self.__entry2.bind("<FocusIn>", lambda x: self.setfocus(self.__entry2))
        self.currentfocus=self.__entry1
        self.__configure_column(3)
        

    def __configure_column(self, n:int)->None:
        if not isinstance(n, int):raise TypeError(f"Unexpected TypeError: the object must be 'int' not '{n.__class__}'")
        for i in range(n):
            self.columnconfigure(i, weight=1)

    def Show(self):
        for ind,widget in enumerate(self.winfo_children()):
            widget.grid(row=0, column=ind, pady=10)
        self.pack(fill='x', padx=10, pady=10)

    def getentry(self, n: int):
        if not isinstance(n, int):raise TypeError(f"Unexpected TypeError: the object must be 'int' not '{n.__class__}'")
        match (n):
            case 1:
                return self.__entry1, self.__str_var_1
            case 2:
                return self.__entry2, self.__str_var_2
            
    def pgcd_command(self, command):
        self.__pgcd_finder_button.configure(command=command)

    def clear_entries(self):
        self.__entry1.delete(0, ctk.END)
        self.__entry2.delete(0, ctk.END)
        validate_entry(self.__entry1, self.__str_var_1, "A(X)")
        validate_entry(self.__entry2, self.__str_var_2, "B(X)")

    def setfocus(self, entry, event=None):
        self.currentfocus=entry

    def getfocus(self):
        return self.currentfocus