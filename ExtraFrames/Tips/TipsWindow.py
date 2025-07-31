"""
TipsWindow module.

This module provides the TipsWindow class, a customtkinter Toplevel window
for displaying usage instructions and tips to the user. It embeds an
InstractionsFrame for presenting a user guide and allows customization
of colors, and icon image.
"""

import customtkinter as ctk
from PIL import Image
from ExtraFrames.Tips.InstractionsFrame import InstractionsFrame

class TipsWindow(ctk.CTkToplevel):
    """
    TipsWindow is a customtkinter Toplevel window for usage instructions and tips.

    It contains an InstractionsFrame for displaying a user guide, and provides
    methods to show the frame, set an icon image, and customize colors.
    """
    def __init__(self, master):
        """
        Initialize the tips window and embed the instructions frame.

        Args:
            master: The parent widget (main application window).
        """
        super().__init__(master)
        # Set window geometry and properties
        self.geometry("1300x800")
        self.title("Instractions")
        self.lift()         # Bring window to front
        self.focus_set()    # Focus on this window
        self.grab_set()     # Make this window modal
        self.resizable(False, False)
        # Add the instructions frame to this window
        self.Instractionsframe = InstractionsFrame(self)
    
    def Show(self):
        """
        Show the instructions frame inside the tips window.
        """
        self.Instractionsframe.Show()

    def load_image(self):
        """
        Load and set the icon image for the instructions frame.
        """
        self.Instractionsframe.set_icon(
            ctk.CTkImage(
                light_image=Image.open(r'res\user-guide.png'), 
                dark_image=Image.open(r'res\user-guide.png'), 
                size=(50, 50)
            )
        )

    def load_color(self, window_color, text_color_tuple, title_color, frame_color, inner_color):
        """
        Set colors for the tips window and the embedded instructions frame.

        Args:
            window_color: Background color for the window.
            text_color_tuple: Tuple of colors for Allowed and warning instractions.
            title_color: Color for the title label.
            frame_color: Background color for the main frame.
            inner_color: Tuple of (background, border) colors for the inner frame.
        """
        self.configure(fg_color=window_color)
        self.Instractionsframe.load_color(text_color_tuple, title_color, frame_color, inner_color)