"""
ResultFrame module.

This module provides the ResultFrame class, a customtkinter frame for displaying
the result, quotient, remainder, and GCD of polynomial division. It includes
labels for each value and methods to update and retrieve these labels.
"""

import customtkinter as ctk
from utils.ExtraMethods import ExtraMethods as E

class ResultFrame(ctk.CTkFrame):
    """
    ResultFrame is a customtkinter frame for displaying the result, quotient, remainder, and GCD.

    It provides labels for each value and methods to update and retrieve these labels.
    """
    def __init__(self, master):
        """
        Initialize the result frame with labels for result, quotient, remainder, and GCD.

        Args:
            master: The parent widget.
        """
        super().__init__(master, corner_radius=20, border_width=5)
        # Main result label
        self.__Result = ctk.CTkLabel(self, text="Result", font=("Arial", 50), text_color=("#C31307", "#EF8729"))
        # Quotient label
        self.__Q = ctk.CTkLabel(self, text='Quotient: ', font=("Arial", 30), text_color=("#248F0A", "#5AF63F"))
        # Remainder label
        self.__R = ctk.CTkLabel(self, text='Rest: ', font=("Arial", 30), text_color=("#248F0A", "#5AF63F"))
        # GCD label
        self.__PGCD = ctk.CTkLabel(self, text="PGCD: ", font=("Arial", 30), text_color=("#248F0A", "#5AF63F"))
    
    def Show(self):
        """
        Display all result labels in the frame.
        """
        for widget in self.winfo_children():
            widget.pack(pady=10, padx=30, anchor='center')
        self.pack(pady=10, padx=10)
    
    def config_quotient(self, q) -> None:
        """
        Update the quotient label with the given value.

        Args:
            q: The quotient value (should have .as_expr() method).
        """
        result=E.fix_float_format_in_string(E.replace_exponents(str(q.as_expr())))
        self.__Q.configure(text=f"Quotient: {result}")
        del result

    def config_rest(self, r) -> None:
        """
        Update the remainder label with the given value.

        Args:
            r: The remainder value (should have .as_expr() method).
        """
        result=E.fix_float_format_in_string(E.replace_exponents(str(r.as_expr())))
        self.__R.configure(text=f"Rest: {result}")
        del result

    def config_pgcd(self, p) -> None:
        """
        Update the GCD label with the given value.

        Args:
            p: The GCD value (should have .as_expr() method).
        """
        result=E.fix_float_format_in_string(E.replace_exponents(str(p.as_expr())))
        self.__PGCD.configure(text=f"PGCD: {result}")
        del result
        
    def get_title(self):
        """
        Return the main result label widget.

        Returns:
            CTkLabel: The main result label.
        """
        return self.__Result

    def get_q_label(self):
        """
        Return the quotient label widget.

        Returns:
            CTkLabel: The quotient label.
        """
        return self.__Q
    
    def get_r_label(self):
        """
        Return the remainder label widget.

        Returns:
            CTkLabel: The remainder label.
        """
        return self.__R
    
    def get_pgcd_label(self):
        """
        Return the GCD label widget.

        Returns:
            CTkLabel: The GCD label.
        """
        return self.__PGCD