"""
ThemeFrame module.

This module provides the ThemeFrame class, a customtkinter frame for managing
the application's appearance mode settings. It allows users to select between
dark, light, and system appearance modes via radio buttons, and provides
methods to retrieve the selected mode, set commands for the radio buttons,
and customize the appearance of the title label.
"""

import customtkinter as ctk

class ThemeFrame(ctk.CTkFrame):
    """
    ThemeFrame is a customtkinter frame for appearance mode settings.

    It displays radio buttons for selecting dark, light, or system mode,
    and provides methods to interact with these settings.
    """
    def __init__(self, master, value='light'):
        """
        Initialize the ThemeFrame.

        Args:
            master: The parent widget.
            value (str): The initial appearance mode ('dark', 'light', or 'system').
        """
        super().__init__(master)
        # Variable to store the selected theme mode
        self.radio_var = ctk.StringVar(value=value.lower())
        # Label for the appearance mode section
        self.theme_settings_label = ctk.CTkLabel(self, text='Appearance mode:', font=("Arial", 30))
        # Radio button for dark mode
        self.dark_theme = ctk.CTkRadioButton(self, text='Dark mode', value='dark', variable=self.radio_var)
        # Radio button for light mode
        self.light_theme = ctk.CTkRadioButton(self, text='Light mode', value='light', variable=self.radio_var)
        # Radio button for system mode
        self.system_theme = ctk.CTkRadioButton(self, text='System mode', value='system', variable=self.radio_var)
        
        # Configure grid columns for layout
        self.configure_columns()
    
    def set_command(self, command):
        """
        Set a command callback for all radio buttons.

        Args:
            command (callable): Function to call when a radio button is selected.
        """
        for widget in self.winfo_children():
            if isinstance(widget, ctk.CTkRadioButton):
                widget.configure(command=command)

    def Show(self):
        """
        Display all widgets in the frame using grid layout and pack the frame.
        """
        for i, widget in enumerate(self.winfo_children()):
            widget.grid(row=0, column=i, pady=10, padx=10)
        self.theme_settings_label.grid_configure(sticky='w')
        self.pack(fill='x', padx=10, pady=10)

    def get_theme(self):
        """
        Get the currently selected appearance mode.

        Returns:
            str: The selected appearance mode ('dark', 'light', or 'system').
        """
        return self.radio_var.get()
    
    def configure_columns(self):
        """
        Configure grid columns to have equal weight for proper layout.
        """
        for i in range(4):
            self.columnconfigure(i, weight=1)

    def set_title_color_font(self, color, font):
        """
        Set the color and font of the title label.

        Args:
            color (str): The text color.
            font (tuple): The font specification.
        """
        self.theme_settings_label.configure(text_color=color, font=font)
