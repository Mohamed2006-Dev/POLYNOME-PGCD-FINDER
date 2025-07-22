import customtkinter as ctk

class InstractionsFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.instraction_label_title = ctk.CTkLabel(self, text = "Guide d'utilisation", compound = 'left', font = ("Arial", 50), text_color= ('#3C1AB5','#2BDBEA'))
        self.tip_1_label = ctk.CTkLabel(self, text = "1-Pour définir correctement un polynôme, entrez les puissances sous la forme X**n.", font = ("Arial", 30))
        self.tip_2_label = ctk.CTkLabel(self, text = "2-La puissance n doit être un entier entre 0 et 9.", font = ("Arial", 30))
        self.tip_3_label = ctk.CTkLabel(self, text = "3-Les coefficients doivent être écrits sous la forme a*X.", font = ("Arial", 30))
        self.tip_4_label = ctk.CTkLabel(self, text = "4-Pour éviter les ambiguïtés dans les expressions complexes, utilisez des parenthèses.", font = ("Arial", 30))
        self.tip_5_label = ctk.CTkLabel(self, text = "5-Assurez-vous que chaque terme est bien formé.", font = ("Arial", 30))
        self.tip_6_label = ctk.CTkLabel(self, text = "6-Utilisez des polynômes simples pour commencer et vérifiez les résultats obtenus\nSi vous rencontrez une erreur, vérifiez la syntaxe de votre entrée.", font = ("Arial", 30))
    
    def Show(self):
        for widget in self.winfo_children():
            widget.pack(pady = 10, padx =10)
        self.pack(pady = 40, padx = 40, fill = 'both')
    
    def set_icon(self, icon):
        self.instraction_label_title.configure(image=icon)