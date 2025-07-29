"""
SettingsWindow module.

This module provides the SettingsWindow class, a customtkinter Toplevel window
for managing application settings. It currently supports changing the appearance
mode (theme) using the ThemeFrame, and provides methods to display the settings
window and handle theme changes.
"""

import customtkinter as ctk
from ExtraFrames.Settings.ThemeFrame import ThemeFrame

class SettingsWindow(ctk.CTkToplevel):
    """
    SettingsWindow is a customtkinter Toplevel window for application settings.

    It displays a ThemeFrame for selecting the appearance mode and manages
    interactions with the parent window.
    """
    def __init__(self, master):
        """
        Initialize the SettingsWindow.

        Args:
            master: The parent widget (main application window).
        """
        super().__init__(master)
        # Create ThemeFrame for appearance mode selection
        self.Theme_Frame = ThemeFrame(self, ctk.get_appearance_mode())
        # Set command for theme change
        self.Theme_Frame.set_command(command=lambda: self.set_theme_command(self.Theme_Frame.get_theme()))

        # Set window geometry and properties
        self.geometry("800x85")
        self.resizable(True, False)
        self.title("Settings")
        self.lift()         # Bring window to front
        self.focus_set()    # Focus on this window
        self.grab_set()     # Make this window modal
        
        # Uncomment to disable window resizing
        # self.resizable(False, False) 
        
    def set_theme_command(self, theme):
        """
        Callback to set the application's theme.

        Args:
            theme (str): The selected appearance mode.
        """
        self.master.set_theme(theme)
    
    def Show(self):
        """
        Display the ThemeFrame in the settings window.
        """
        self.Theme_Frame.Show()
