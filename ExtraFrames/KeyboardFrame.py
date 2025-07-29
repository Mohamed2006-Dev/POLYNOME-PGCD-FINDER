"""
KeyboardFrame module.

This module provides the KeyboardFrame class, a customtkinter frame for displaying
a numeric and operator keyboard. It creates buttons for digits, operators, clear,
and delete, and provides methods for showing/hiding the keyboard, setting commands,
customizing appearance, and retrieving button widgets.
"""

import customtkinter as ctk
from utils.ExtraMethods import ExtraMethods as E

class KeyboardFrame(ctk.CTkFrame):
    """
    KeyboardFrame is a customtkinter frame for a numeric and operator keyboard.

    It creates buttons for digits, operators, clear, and delete, and provides
    methods for showing/hiding the keyboard, setting commands, customizing
    appearance, and retrieving button widgets.
    """
    def __init__(self, master):
        """
        Initialize the keyboard and its buttons.

        Args:
            master: The parent widget.
        """
        super().__init__(master, border_width=4)
        self.btns = {}         # Dictionary for general buttons (digits/operators)
        self.clear_btns = {}   # Dictionary for clear/delete buttons
        self.__is_shown = False

        # Inner frame for keyboard layout
        self.inner_frame = ctk.CTkFrame(self, fg_color='transparent')
        self.inner_frame.pack(fill='both', padx=8, pady=8)

        self.__load_btns()
        self.column_config()
    
    def __load_btns(self):
        """
        Create and position all keyboard buttons.
        """
        btns = {}
        # Create digit and operator buttons
        for i in list(range(10)) + ["+", "-", "*", "/", ".", "**"]:
            btn = ctk.CTkButton(self.inner_frame, text=f'{i}', font=("Arial", 15))
            name = f"btn_{i}"
            btns[name] = btn
        
        # Positioning for digit buttons
        position = []
        for i, r in enumerate([[2, 1, 0], [2, 1, 0], [2, 1, 0]]):
            for c in r:
                position.append((i, c))
        
        # Assign positions for digit buttons 1-9
        for i in range(9, 0, -1):
            name = f'btn_{i}'
            row, col = position[9 - i]
            self.btns[name] = (btns[name], row, col)

        # Assign positions for operator and special buttons
        for i in [("btn_+", 0, 3), ("btn_-", 1, 3), ("btn_*", 2, 3), ("btn_/", 3, 3), ("btn_.", 3, 1), ("btn_**", 3, 2)]:
            name, row, col = i
            self.btns[name] = (btns[name], row, col)
        self.btns['btn_0'] = (btns["btn_0"], 3, 0)

        # Create clear and delete buttons
        delete_btn = ctk.CTkButton(self.inner_frame, text='DELETE', compound='top')
        clear_btn = ctk.CTkButton(self.inner_frame, text='CLEAR', font=("Arial", 40, 'bold'))

        self.clear_btns["btn_delete"] = (delete_btn, 0, 4)
        self.clear_btns['btn_clear'] = (clear_btn, 2, 4)

        # Clean up temporary variables
        del position, btns, delete_btn, clear_btn

    def getbtns(self, type):
        """
        Return the list of buttons by type.

        Args:
            type (str): 'general' for digit/operator buttons, 'clear' for clear/delete buttons.
        Returns:
            list: List of button widgets.
        """
        btns_type = None
        match (type):
            case "general":
                btns_type = self.btns
            case "clear":
                btns_type = self.clear_btns
        btns = []
        for btn in tuple(btns_type.values()):
            btns.append(btn[0])
        return btns
    
    def Show(self):
        """
        Show the keyboard on the screen.
        """
        E.iterate_over_btns(self.btns, 'ew')
        E.iterate_over_btns(self.clear_btns, 'nsew', 2)
        self.pack(padx=10, pady=10, side='bottom')
        self.__is_shown = not self.__is_shown

    def Hide(self):
        """
        Hide the keyboard.
        """
        self.pack_forget()
        self.__is_shown = not self.__is_shown
    
    def set_btns_command(self, btn, command):
        """
        Set the command for a general button.

        Args:
            btn: The button widget.
            command (callable): Function to call when the button is pressed.
        """
        btn.configure(command=command)

    def set_clear_btns_command(self, command1, command2):
        """
        Set the commands for the CLEAR and DELETE buttons.

        Args:
            command1 (callable): Function for CLEAR button.
            command2 (callable): Function for DELETE button.
        """
        self.clear_btns['btn_clear'][0].configure(command=command1)
        self.clear_btns['btn_delete'][0].configure(command=command2)
    
    def getkeyboard_state(self):
        """
        Return the current shown/hidden state of the keyboard.

        Returns:
            bool: True if shown, False if hidden.
        """
        return self.__is_shown
    
    def column_config(self):
        """
        Configure the column weights for the keyboard layout.
        """
        for i in range(4):
            self.columnconfigure(i, weight=1)
    
    def configure_btns(self, icon):
        """
        Configure icons and special text for operator buttons.

        Args:
            icon: Icon for the '**' button.
        """
        self.btns['btn_**'][0].configure(image=icon, compound='top', text='')
        self.btns['btn_*'][0].configure(text='×')
        self.btns['btn_/'][0].configure(text='÷')

    def getallbtns(self):
        """
        Return all keyboard buttons.

        Returns:
            list: List of all button widgets.
        """
        btns = []
        for key in self.btns.keys():
            btns.append(self.btns[key][0])
        for key in self.clear_btns.keys():
            btns.append(self.clear_btns[key][0])
        return btns
    
    def getnumericbtns(self):
        """
        Return only the numeric buttons.

        Returns:
            list: List of numeric button widgets.
        """
        btns = []
        for i in range(10):
            btns.append(self.btns[f'btn_{i}'][0])
        return btns

    def get_non_numeric_btns(self):
        """
        Return all non-numeric buttons.

        Returns:
            list: List of non-numeric button widgets.
        """
        numeric_btns = self.getnumericbtns()
        btns = []
        for btn in filter(lambda x: x not in numeric_btns, self.getallbtns()):
            btns.append(btn)
        return btns

