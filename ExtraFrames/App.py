"""
App module.

This module provides the App class, the main application window for the PGCD Finder.
It initializes the main window, sets its title, size, and appearance mode, and
provides a method to change the application's theme.
"""

import customtkinter as ctk
from ExtraFrames.KeyboardFrame import KeyboardFrame

class App(ctk.CTk):
    """
    Main application class for the PGCD Finder.

    Inherits from customtkinter.CTk and sets up the main window properties.
    """
    def __init__(self, title='PGCD FINDER'):
        """
        Initialize the main application window.

        Args:
            title (str): Window title.
        """
        super().__init__()
        self.title(title)
        # Maximize the window after 100ms
        self.after(100, lambda: self.state('zoomed'))
        # Set minimum window size
        self.minsize(800, 900)
        
    def set_theme(self, theme):
        """
        Set the application's appearance mode (theme).

        Args:
            theme (str): The appearance mode to apply.
        """
        ctk.set_appearance_mode(theme)
