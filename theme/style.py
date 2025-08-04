"""
style.py

This module defines the Style class, which contains style definitions for various UI elements
used throughout the PGCD Finder application. Styles are grouped by usage: entries, titles,
results, and settings, with support for font, size, and dimensions.
"""

class Style:
    """
    Contains style definitions for various UI elements.
    """

    class EntryStyle:
        """
        Style for entry fields.
        """
        width = 300
        height = 70
        corner_radius = 30
        text_font = "Helvetica Rounded"
        text_size = 25
        
        @classmethod
        def get_dimension(cls):
            """
            Return the width and height for entry fields.

            Returns:
                tuple: (width, height)
            """
            return cls.width, cls.height
        
        @classmethod
        def get_style(cls):
            """
            Return the font and size for entry fields.

            Returns:
                tuple: (font, size)
            """
            return cls.text_font, cls.text_size
        
    class TitleStyle:
        """
        Style for title labels.
        """
        font_name = 'Roboto'
        size = 50
        
        @classmethod
        def get_style(cls):
            """
            Return the font name and size for title labels.

            Returns:
                tuple: (font_name, size)
            """
            return cls.font_name, cls.size
        
    class ResultTextStyle:
        """
        Style for result text labels.
        """
        font_name = 'Segeo UI this'
        size = 30
        weight = 'bold'

        @classmethod
        def get_style(cls):
            """
            Return the font, size, and weight for result text.

            Returns:
                tuple: (font_name, size, weight)
            """
            return cls.font_name, cls.size, cls.weight

    class SettingsTitleStyle:
        """
        Style for settings title labels.
        """
        font_name = 'Noto Serif Vithkuqi'
        size = 25

        @classmethod
        def get_style(cls):
            """
            Return the font name and size for settings title labels.

            Returns:
                tuple: (font_name, size)
            """
            return cls.font_name, cls.size

    class HistoryStyle:
        """
        Style for history frame
        """
        font_name = "Quivira"
        size = 25

        @classmethod
        def get_style(cls):
            return cls.font_name, cls.size