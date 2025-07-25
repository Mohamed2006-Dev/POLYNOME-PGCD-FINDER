import customtkinter as ctk
from theme.style import Style

class TitleCTkFont(ctk.CTkFont):
    def __init__(self):
        font, size=Style.TitleStyle.get_style()
        super().__init__(font, size)

class ResultCTkFont(ctk.CTkFont):
    def __init__(self):
        font, size, weight=Style.ResultTextStyle.get_style()
        super().__init__(font, size, weight)

class EntryCTkFont(ctk.CTkFont):
    def __init__(self):
        font, size=Style.EntryStyle.get_style()
        super().__init__(font, size)
