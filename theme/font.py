"""
font.py

This module defines custom font classes for use with customtkinter widgets in the PGCD Finder application.
Each class provides a specific font style for titles, results, entries, and settings titles, using style
definitions from the Style module.
"""

import customtkinter as ctk
from theme.style import Style

class TitleCTkFont(ctk.CTkFont):
    """
    Custom font for title labels.
    """
    def __init__(self):
        font_name, size = Style.TitleStyle.get_style()
        super().__init__(font_name, size)

class ResultCTkFont(ctk.CTkFont):
    """
    Custom font for result labels.
    """
    def __init__(self):
        font_name, size, weight = Style.ResultTextStyle.get_style()
        super().__init__(font_name, size, weight)

class EntryCTkFont(ctk.CTkFont):
    """
    Custom font for entry fields.
    """
    def __init__(self):
        font_name, size = Style.EntryStyle.get_style()
        super().__init__(font_name, size)

class SettingsTitleCTkFont(ctk.CTkFont):
    """
    Custom font for settings title labels.
    """
    def __init__(self):
        font_name, size = Style.SettingsTitleStyle.get_style()
        super().__init__(font_name, size)

class HistoryCTkFont(ctk.CTkFont):
    def __init__(self):
        font_name, size = Style.EntryStyle.get_style()
        super().__init__(font_name, size)