"""
InstractionsFrame module.

This module provides the InstractionsFrame class, a customtkinter frame for
displaying usage instructions and tips to the user. It presents a user guide
with several tips for entering polynomials and using the application correctly,
and allows customization of appearance and colors.
"""

import customtkinter as ctk

class InstractionsFrame(ctk.CTkFrame):
    """
    InstractionsFrame is a customtkinter frame for displaying instructions and tips.

    It shows a title label and a set of instruction labels inside an inner frame,
    and provides methods to display the instructions, set an icon, change theme,
    and customize colors.
    """
    def __init__(self, master):
        """
        Initialize the instructions frame with all instruction labels.

        Args:
            master: The parent widget.
        """
        super().__init__(master)
        # Title label with optional icon
        self.instraction_label_title = ctk.CTkLabel(
            self, 
            text = "User Guide", 
            compound = 'left', 
            font = ("Arial", 50), 
            text_color= ('#3C1AB5','#2BDBEA')
        )
        # Inner frame to hold instruction labels
        self.inner_frame = ctk.CTkFrame(self, border_width=3)
        # Instruction tip labels
        self.tip_1_label = ctk.CTkLabel(
            self.inner_frame, 
            text = "✅ You can simply enter X3 and the app will automatically convert it to X³ (superscript).", 
            font = ("Arial", 30)
        )
        self.tip_2_label = ctk.CTkLabel(
            self.inner_frame, 
            text = "✅ You can write coefficients directly like 3X. The app will convert it to 3*X.", 
            font = ("Arial", 30)
        )
        self.tip_3_label = ctk.CTkLabel(
            self.inner_frame, 
            text = "✅ Use uppercase 'X'. If you use lowercase, it will be auto-corrected.", 
            font = ("Arial", 30)
        )
        self.tip_4_label = ctk.CTkLabel(
            self.inner_frame, 
            text = "✅ Start with simple polynomials and test your results progressively.", 
            font = ("Arial", 30)
        )
        self.tip_5_label = ctk.CTkLabel(
            self.inner_frame, 
            text = "⚠️ The exponent n should be a number from 0 to 9.", 
            font = ("Arial", 30)
        )
        self.tip_6_label = ctk.CTkLabel(
            self.inner_frame, 
            text = "⚠️ If something goes wrong, check your input structure and try again.", 
            font = ("Arial", 30)
        )
        self.tip_7_label = ctk.CTkLabel(
            self.inner_frame, 
            text = "⚠️ Don't use symbols other than numbers (0-9), operators (+, -, /, *), X, and exponents (**).", 
            font = ("Arial", 30)
        )
        self.tip_8_label = ctk.CTkLabel(
            self.inner_frame,
            text = "⚠️ If auto-correction is disabled, you must enter polynomials in the correct format",
            font = ("Arial", 30)
        )

    def Show(self):
        """
        Display all instruction labels in the frame.
        """
        self.instraction_label_title.pack(pady=10, padx=5, anchor='w')
        # Pack all instruction labels inside the inner frame
        for widget in self.inner_frame.winfo_children():
            widget.pack(pady=20, padx=20, anchor='w')
        self.inner_frame.pack(fill='both', pady=15, padx=5)
        self.pack(pady=30, padx=30, fill='both')
    
    def set_icon(self, icon):
        """
        Set the icon for the instruction title label.

        Args:
            icon: The image to display next to the title.
        """
        self.instraction_label_title.configure(image=icon)

    def load_color(self, text_color_tuple, title_color, frame_color, inner_color):
        """
        Set colors for the frame, inner frame, and instruction labels.

        Args:
            text_color: Color for instruction text.
            title_color: Color for the title label.
            frame_color: Background color for the main frame.
            inner_color: Tuple of (background, border) colors for the inner frame.
        """
        self.configure(fg_color=frame_color)
        self.inner_frame.configure(fg_color=inner_color[0], border_color=inner_color[1])
        text_color=None
        for i, instraction in enumerate(self.inner_frame.winfo_children()):
            if i<=3:
                text_color=text_color_tuple[0]
            else:
                text_color=text_color_tuple[1]
            instraction.configure(text_color=text_color)
        self.instraction_label_title.configure(text_color=title_color)
