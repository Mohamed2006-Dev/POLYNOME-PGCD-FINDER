"""
color.py

This module defines the Color class, which contains color definitions for various UI elements and states
used throughout the PGCD Finder application. Colors are grouped by usage: entries, titles, results, frames,
and buttons, with support for light and dark modes.
"""

class Color:
    """
    Contains color definitions for various UI elements and states.
    """
    SECONDARY = 'transparent'

    class EntryColor:
        """
        Colors for entry fields.
        """
        PRIMARY = ('#91F5C5', '#084E2B')
        TEXT = ('#7A0A3F', "#3484DF")
        BORDER = ("#000000", "#FFFFFF")
    
    class TitleColor:
        """
        Colors for title labels.
        """
        PRIMARY = ('#824B40', '#DC745D')
    
    class ResultColor:
        """
        Colors for result labels.
        """
        PRIMARY = ("#838639", '#E5E619')

    class FrameColor:
        """
        Colors for different frames in the application.
        """
        class ResultFrameColor:
            """
            Colors for the result frame.
            """
            PRIMARY = ("#78E7E7", "#120E57")
            BORDER = ("#000000", "#FFFFFF") 

        class KeyboardFrameColor:
            """
            Colors for the keyboard frame.
            """
            BORDER = ("#7A7A7A", "#8D8B8B") 
        
        class EntryFrameColor:
            """
            Colors for the entry frame.
            """
            PRIMARY = 'transparent'

        class AppColor:
            """
            Colors for the main application window.
            """
            PRIMARY = ('#FFFFFF', '#000000')

        class SettingsColor:
            """
            Colors for the settings frame.
            """
            TITLE = ("#5D6B6E", "#8A7B7B")

        class TipsColor:
            """
            Colors for the tips and instructions frame.
            """
            TITLE = ("#23b0e2", '#2BDBEA')
            ALLOWED = ("#2BD82B", "#2BD82B")
            WARNING = ("#E4A00F", "#D5D82B")
            PRIMARY = 'transparent'
            SECONDARY = ("#F1F1F1", "#131212")
            BORDER = ("#000000", "#FFFFFF")
        
        class ToolbarColor:
            """
            Colors for toolbar frame
            """
            PRIMARY='transparent'
            BORDER=('#727070', "#727070")

    class Buttons:
        """
        Colors for various buttons.
        """
        HOVER = ("#7C7979", "#CEC6C6")

        class NumericButtons:
            """
            Colors for numeric keyboard buttons.
            """
            PRIMARY = ('#14EAEB', '#2b7bb9')
            TEXT = ("#000000", "#FFFFFF")
            HOVER = ('#2b7bb9', '#14EAEB')
        
        class NonNumericKeyboardButtons:
            """
            Colors for non-numeric keyboard buttons.
            """
            PRIMARY = ("#B8B1B1", "#8A8484")
            TEXT = ("#000000", "#FFFFFF")
            HOVER = ("#8A8484", "#B8B1B1")

        class FooterButtons:
            """
            Colors for footer buttons.
            """
            PRIMARY = 'transparent'
            HOVER = ("#B99941", "#D3C470")
            TEXT = ("#824B40", "#CC5500")

        class EntryButton:
            """
            Colors for the main entry button.
            """
            PRIMARY = 'transparent'
            HOVER = ("#7EF5BB", "#0D5C21")

        class ToolbarButton:
            """
            Colors for the toolbar buttons
            """
            PRIMARY='transparent'
            HOVER='transparent'