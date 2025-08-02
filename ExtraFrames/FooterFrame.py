"""
FooterFrame module.

This module provides the FooterFrame class, a customtkinter frame for displaying
footer buttons in the application. It includes buttons for TIPS, keyboard,
settings, and EXAMPLE, and provides methods to set commands, icons, and retrieve
the button widgets.
"""

import customtkinter as ctk

class FooterFrame(ctk.CTkFrame):
    """
    FooterFrame is a customtkinter frame for footer buttons (TIPS, keyboard, EXAMPLE).

    It provides methods to set commands, icons, and retrieve the button widgets.
    """
    def __init__(self, master):
        """
        Initialize the footer buttons.

        Args:
            master: The parent widget.
        """
        super().__init__(master)
        # Button for TIPS
        self.__tipsbutton = ctk.CTkButton(self, text='TIPS', width=50, height=50, font=("Arial", 35))
        # Button for keyboard
        self.__techbutton = ctk.CTkButton(self, text='keyboard', width=50, height=50, font=("Arial", 35))
        # Button for EXAMPLE
        self.__examplebutton = ctk.CTkButton(self, text="EXAMPLE", width=50, height=50, font=("Arial", 35))

        # Configure grid columns for layout
        self.column_config()

    def Show(self, sticky: list[str]):
        """
        Display the footer buttons with the given sticky configuration.

        Args:
            sticky (list[str]): List of sticky values for grid placement.
        """
        for i, (widget, s) in zip(range(len(sticky)), zip(self.winfo_children(), sticky)):
            widget.grid(row=0, column=i, padx=20, sticky=s)
        self.pack(fill='x', side='bottom', padx=10, pady=10, anchor='center')
        
    def column_config(self):
        """
        Configure the column weights for the footer layout.
        """
        for i in range(3):
            self.columnconfigure(i, weight=1)
        
    def set_example_command(self, command):
        """
        Set the command for the EXAMPLE button.

        Args:
            command (callable): Function to call when the EXAMPLE button is pressed.
        """
        self.__examplebutton.configure(command=command)

    def set_keyboard_command(self, command):
        """
        Set the command for the keyboard button.

        Args:
            command (callable): Function to call when the keyboard button is pressed.
        """
        self.__techbutton.configure(command=command)

    def set_tips_command(self, command):
        """
        Set the command for the TIPS button.

        Args:
            command (callable): Function to call when the TIPS button is pressed.
        """
        self.__tipsbutton.configure(command=command)

    def set_icons(self, tipsicon, keyboardicon, exampleicon):
        """
        Set the icons for the footer buttons.

        Args:
            tipsicon: Icon for the TIPS button.
            keyboardicon: Icon for the keyboard button.
            exampleicon: Icon for the EXAMPLE button.
        """
        self.__tipsbutton.configure(image=tipsicon, compound='left')
        self.__techbutton.configure(image=keyboardicon, text='', compound='top')
        self.__examplebutton.configure(image=exampleicon, compound='right')

    def get_buttons(self):
        """
        Return a list of all footer buttons.

        Returns:
            list: List of button widgets [keyboard, example, tips].
        """
        return [self.__techbutton, self.__examplebutton, self.__tipsbutton]

