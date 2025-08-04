"""
assets.py

This module provides the Assets class for loading and converting image assets for use in the PGCD Finder application.
It loads images from disk and converts them to CTkImage objects for use in customtkinter widgets.
"""

from PIL import Image
from customtkinter import CTkImage

class Assets:
    """
    Class for loading and converting image assets for the application.
    """
    images = {}

    @classmethod
    def load_all(cls):
        """
        Load all required images into the class dictionary.
        """
        cls.images['book'] = Image.open(r"res\book.png")
        cls.images['calculating'] = Image.open(r"res\calculating.png")
        cls.images['clear'] = Image.open(r"res\clear.png")
        cls.images['clear(light)'] = Image.open(r"res\clear(1).png")
        cls.images['diviser'] = Image.open(r"res\diviser.png")
        cls.images['exposant'] = Image.open(r"res\exposant_n(2).png")
        cls.images['exposant(light)'] = Image.open(r"res\exposant_n(3).png")
        cls.images['math-book'] = Image.open(r'res\math-book.png')
        cls.images['request'] = Image.open(r'res\request.png')
        cls.images['technology'] = Image.open(r'res\technology.png')
        cls.images['user-guide'] = Image.open(r'res\user-guide.png')
        cls.images['settings'] = Image.open(r'res\settings.png')
        cls.images['history'] = Image.open(r'res\history.png')
        cls.images['paste'] = Image.open(r'res\paste.png')
        cls.images['maximize'] = Image.open(r'res\maximize(dark).png')
        cls.images['maximize(light)'] = Image.open(r'res\maximize(light).png')
        cls.images['delete'] = Image.open(r'res\delete.png')

    @classmethod
    def convert(cls, key: tuple[str] | str, size: tuple[int]):
        """
        Convert loaded images to CTkImage for use in customtkinter widgets.

        Args:
            key (str or tuple): Key or tuple of keys for light/dark images.
            size (tuple): Size of the image.

        Returns:
            CTkImage: The converted image for use in customtkinter widgets.
        """
        if isinstance(key, tuple):
            return CTkImage(
                light_image=cls.images[key[0]],
                dark_image=cls.images[key[1]],
                size=size
            )
        return CTkImage(
            light_image=cls.images[key],
            dark_image=cls.images[key],
            size=size
        )

# Load all images at module import
Assets.load_all()