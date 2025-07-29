"""
EntryFrame module.

This module provides the EntryFrame class, a customtkinter frame for entering
polynomials A(X) and B(X). It includes two entry fields, a main button, and
methods for validation, focus management, clearing entries, and customizing
appearance and icon.
"""

import customtkinter as ctk
from utils.parser import validate_entry
from utils.ButtonsCommands import clear_btns

class EntryFrame(ctk.CTkFrame):
    """
    EntryFrame is a customtkinter frame for entering polynomials A(X) and B(X).

    It provides two entry fields, a main button, and methods for validation,
    focus management, clearing entries, and customizing appearance and icon.
    """
    def __init__(self, master):
        """
        Initialize the entry fields and main button.

        Args:
            master: The parent widget.
        """
        super().__init__(master)
        # StringVar and entry for polynomial A(X)
        self.__str_var_1 = ctk.StringVar(value='A(X) =')
        self.__entry1 = ctk.CTkEntry(self, textvariable=self.__str_var_1, font=("Arial", 20))

        # Main button for PGCD finder
        self.__pgcd_finder_button = ctk.CTkButton(self, text='Button', font=("Arial", 25), command=None)
        # Bind validation and focus events for entry 1
        self.__entry1.bind("<KeyRelease>", lambda x: validate_entry(self.getentrytuple(self.__entry1), self.user_input))
        self.__entry1.bind("<FocusIn>", lambda x: self.setfocus(self.__entry1))
        self.__entry1.bind('<BackSpace>', self.backspace_handler)

        # StringVar and entry for polynomial B(X)
        self.__str_var_2 = ctk.StringVar(value='B(X) =')
        self.__entry2 = ctk.CTkEntry(self, textvariable=self.__str_var_2, font=("Arial", 20))
        # Bind validation and focus events for entry 2
        self.__entry2.bind("<KeyRelease>", lambda x: validate_entry(self.getentrytuple(self.__entry2), self.user_input))
        self.__entry2.bind("<FocusIn>", lambda x: self.setfocus(self.__entry2))
        self.__entry2.bind("<BackSpace>", self.backspace_handler)

        # Track current focus and user input
        self.currentfocus = None
        self.user_input = ['', '']
        # Set initial focus to entry 1
        self.__entry1.focus_force()
        # Configure grid columns for layout
        self.__configure_column(3)
        
    def __configure_column(self, n: int) -> None:
        """
        Configure the column weights for layout.

        Args:
            n (int): Number of columns.
        Raises:
            TypeError: If n is not an integer.
        """
        if not isinstance(n, int):
            raise TypeError(f"Unexpected TypeError: the object must be 'int' not '{n.__class__}'")
        for i in range(n):
            self.columnconfigure(i, weight=1)

    def Show(self):
        """
        Display the widgets in the frame using grid layout.
        """
        for ind, widget in enumerate(self.winfo_children()):
            widget.grid(row=0, column=ind, pady=10)
        self.pack(fill='x', padx=10, pady=10)

    def getentry(self, n: int):
        """
        Return the entry widget by index.

        Args:
            n (int): 1 for A(X), 2 for B(X)
        Returns:
            CTkEntry: The entry widget for the specified polynomial.
        Raises:
            TypeError: If n is not an integer.
        """
        if not isinstance(n, int):
            raise TypeError(f"Unexpected TypeError: the object must be 'int' not '{n.__class__}'")
        match (n):
            case 1:
                return self.__entry1
            case 2:
                return self.__entry2
            
    def pgcd_command(self, command):
        """
        Set the command for the main button.

        Args:
            command (callable): Function to call when the button is pressed.
        """
        self.__pgcd_finder_button.configure(command=command)

    def clear_entries(self):
        """
        Clear both entry fields and reset validation.
        """
        self.__entry1.delete(0, ctk.END)
        self.__entry2.delete(0, ctk.END)
        validate_entry(self.getentrytuple(self.__entry1), self.user_input)
        validate_entry(self.getentrytuple(self.__entry2), self.user_input)

    def setfocus(self, entry, event=None):
        """
        Set the current focus to the given entry.

        Args:
            entry: The entry widget to focus.
            event: Optional event parameter (unused).
        """
        self.currentfocus = self.getentrytuple(entry)

    def getfocus(self):
        """
        Get the currently focused entry.

        Returns:
            tuple: (entry widget, string variable, prefix)
        """
        return self.currentfocus
    
    def getentrytuple(self, entry):
        """
        Return a tuple (entry, stringvar, prefix) for the given entry widget.

        Args:
            entry: The entry widget.
        Returns:
            tuple: (entry widget, string variable, prefix string)
        """
        match (entry):
            case self.__entry1:
                return (self.__entry1, self.__str_var_1, "A(X)")
            case self.__entry2:
                return (self.__entry2, self.__str_var_2, "B(X)")
            
    def set_icon(self, icon):
        """
        Set the icon for the main button.

        Args:
            icon: The image to display on the button.
        """
        self.__pgcd_finder_button.configure(image=icon, compound='top', text='')

    def get_button(self):
        """
        Get the main button widget.

        Returns:
            CTkButton: The main button widget.
        """
        return self.__pgcd_finder_button
    
    def backspace_handler(self, event):
        return clear_btns(self.currentfocus, self.user_input, event=event)