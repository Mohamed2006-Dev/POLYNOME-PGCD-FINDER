import customtkinter as ctk
from ExtraFrames.EntryFrame import EntryFrame 

class ResultFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.__Result=ctk.CTkLabel(self, text="Result", font=("Arial", 50), text_color=("#C31307","#EF8729"))
        self.__Q=ctk.CTkLabel(self, text='Quotient: ', font=("Arial", 30), text_color=("#248F0A","#5AF63F"))
        self.__R=ctk.CTkLabel(self, text='Rest: ', font=("Arial", 30), text_color= ("#248F0A", "#5AF63F"))
        self.__PGCD=ctk.CTkLabel(self, text="PGCD: ", font=("Arial", 30), text_color= ("#248F0A", "#5AF63F"))
    
    def Show(self):
        for widget in self.winfo_children():
            widget.pack(pady=10, anchor='center')
        self.pack(fill='x', pady=10, padx=10)
    
    def config_quotient(self,q:str)->None:
        self.__Q.configure(text=f"Quotient: {q.as_expr()}")

    def config_rest(self, r:str)->None:
        self.__R.configure(text=f"Rest: {r.as_expr()}")

    def config_pgcd(self, p:str)->None:
        self.__PGCD.configure(text=f"PGCD: {p.as_expr()}")
        