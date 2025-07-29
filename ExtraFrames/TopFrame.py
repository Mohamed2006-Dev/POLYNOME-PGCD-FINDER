"""
TopFrame module.

This module provides the TopFrame class, a customtkinter frame for the top section
of the application, including two icon labels and the main title label. It allows
customization of icons and provides access to the title widget.
"""

import customtkinter as ctk

class TopFrame(ctk.CTkFrame):
    """
    TopFrame is a customtkinter frame for the top section, including icons and the main title.

    It provides methods to display the widgets, set icons, and retrieve the title label.
    """
    def __init__(self, master):
        """
        Initialize the top frame with two icon labels and a title label.

        Args:
            master: The parent widget.
        """
        super().__init__(master)
        # Left icon label
        self.__icon1_label = ctk.CTkLabel(self, compound="top", text="")

        # Title label
        self.__Title = ctk.CTkLabel(self, text='PGCD FINDER', font=('Arial', 50))

        # Right icon label
        self.__icon2_label = ctk.CTkLabel(self, compound="top", text='')

        # Configure grid columns for layout
        self.__configure_column(3)
    
    def Show(self):
        """
        Display the widgets in the top frame with sticky positioning.
        """
        for (ind, widget), s in zip(enumerate(self.winfo_children()), ['nw', 'n', 'ne']):
            widget.grid(row=0, column=ind, pady=10, sticky=s, padx=10)
        self.pack(fill='x', padx=10, pady=10)

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

    def set_icons(self, icon1, icon2):
        """
        Set the images for the two icon labels.

        Args:
            icon1: Image for the left icon label.
            icon2: Image for the right icon label.
        """
        self.__icon1_label.configure(image=icon1)
        self.__icon2_label.configure(image=icon2)

    def get_title(self):
        """
        Return the title label widget.

        Returns:
            CTkLabel: The title label widget.
        """
        return self.__Title
