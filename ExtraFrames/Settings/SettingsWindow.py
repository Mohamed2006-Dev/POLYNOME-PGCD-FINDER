"""
SettingsWindow module.

This module provides the SettingsWindow class, a customtkinter Toplevel window
for managing application settings. It currently supports changing the appearance
mode (theme) using the ThemeFrame, managing the auto-correction setting using
the AutoCorrectionFrame, and provides methods to display the settings window
and handle changes for both theme and auto-correction.
"""

import customtkinter as ctk
from ExtraFrames.Settings.ThemeFrame import ThemeFrame
from ExtraFrames.Settings.AutoCorrectionFrame import AutoCorrectionFrame

class SettingsWindow(ctk.CTkToplevel):
    """
    SettingsWindow is a customtkinter Toplevel window for application settings.

    It displays a ThemeFrame for selecting the appearance mode and an
    AutoCorrectionFrame for toggling auto-correction, and manages
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
        # Create AutoCorrectionFrame for auto-correction ON/OFF selection
        self._Auto_Correction_Frame = AutoCorrectionFrame(self, self.get_auto_correction_state())
        # Set command for theme change
        self.Theme_Frame.set_command(command=lambda: self.set_theme_command(self.Theme_Frame.get_theme()))

        # Set window geometry and properties
        self.geometry("800x200")
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
    
    def set_auto_correction_command(self, command):
        """
        Set a callback command for the auto-correction radio buttons.

        Args:
            command (callable): The function to call when auto-correction state changes.
        """
        self._Auto_Correction_Frame.set_command(command)

    def get_auto_correction_state(self):
        """
        Retrieve the current auto-correction state from the parent window.

        Returns:
            bool: The current auto-correction state (True for ON, False for OFF).
        """
        state = self.master.get_entry_frame().get_auto_correction()
        return state
    
    

    def Show(self):
        """
        Display the ThemeFrame and AutoCorrectionFrame in the settings window.
        """
        self.Theme_Frame.Show()
        self._Auto_Correction_Frame.Show()

