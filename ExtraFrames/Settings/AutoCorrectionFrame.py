"""
AutoCorrectionFrame module

This module provides the AutoCorrectionFrame class, a customtkinter Frame
for managing the auto-correction setting (ON/OFF) in the application.
It offers radio buttons for toggling the state, methods to retrieve and set
the state, and supports assigning a callback for state changes.
"""

import customtkinter as ctk

class AutoCorrectionFrame(ctk.CTkFrame):
    """
    A custom frame for toggling auto-correction ON or OFF.

    Attributes:
        _radio_var (ctk.BooleanVar): Variable tracking the ON/OFF state.
        _auto_correction_label (ctk.CTkLabel): Label for the frame.
        _on (ctk.CTkRadioButton): Radio button for ON state.
        _off (ctk.CTkRadioButton): Radio button for OFF state.
    """
    def __init__(self, master, value=True):
        """
        Initialize the AutoCorrectionFrame.

        Args:
            master: The parent widget.
            value (bool): Initial value for auto-correction (True for ON, False for OFF).
        """
        super().__init__(master)

        # Boolean variable to hold the state of auto-correction
        self._radio_var = ctk.BooleanVar(value=value)
        
        # Label for the auto-correction setting
        self._auto_correction_label = ctk.CTkLabel(self, text='Auto-Correction:', font=("Arial", 30))

        # Radio button for enabling auto-correction
        self._on = ctk.CTkRadioButton(self, text='ON', value=True, variable=self._radio_var)
        
        # Radio button for disabling auto-correction
        self._off = ctk.CTkRadioButton(self, text='OFF', value=False, variable=self._radio_var)

        # Configure column weights for layout
        self.col_configure()

    def get_state(self):
        """
        Get the current state of auto-correction.

        Returns:
            bool: True if ON, False if OFF.
        """
        return self._radio_var.get()
    
    def Show(self):
        """
        Display the frame and its widgets using grid and pack geometry managers.
        """
        # Place all child widgets in a single row
        for c, widget in enumerate(self.winfo_children()):
            widget.grid(row=0, column=c)
        # Adjust label position and padding
        self._auto_correction_label.grid_configure(sticky='sw', pady=10, padx=10)
        # Pack the frame to fill horizontally with padding
        self.pack(fill='x', padx=10, pady=10)

    def set_command(self, command):
        """
        Set a callback command to be called when either radio button is selected.

        Args:
            command (callable): The function to call on state change.
        """
        self._on.configure(command=command)
        self._off.configure(command=command)

    def col_configure(self):
        """
        Configure the column weights for the frame layout to ensure even distribution.
        """
        for i in range(3):
            self.columnconfigure(i, weight=1)

    def set_color_font(self, color, font):
        self._auto_correction_label.configure(text_color=color, font=font)