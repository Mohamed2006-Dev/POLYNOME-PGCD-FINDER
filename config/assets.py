from PIL import Image
from customtkinter import CTkImage

class Assets:
    images = {}

    @classmethod
    def load_all(cls):
        cls.images['book']=Image.open(r"res\book.png")
        cls.images['calculating']=Image.open(r"res\calculating.png")
        cls.images['clear']=Image.open(r"res\clear.png")
        cls.images['clear(light)']=Image.open(r"res\clear(1).png")
        cls.images['diviser']=Image.open(r"res\diviser.png")
        cls.images['exposant']=Image.open(r"res\exposant_n(2).png")
        cls.images['exposant(light)']=Image.open(r"res\exposant_n(3).png")
        cls.images['math-book']=Image.open(r'res\math-book.png')
        cls.images['request']=Image.open(r'res\request.png')
        cls.images['technology']=Image.open(r'res\technology.png')
        cls.images['user-guide']=Image.open(r'res\user-guide.png')

    @classmethod
    def convert(cls, path:tuple[str]|str, size:tuple[int]):
        if isinstance(path, tuple):
            return CTkImage(light_image=cls.images[path[0]], dark_image=cls.images[path[1]], size=size)
        return CTkImage(light_image=cls.images[path], dark_image=cls.images[path], size=size)
    
Assets.load_all()