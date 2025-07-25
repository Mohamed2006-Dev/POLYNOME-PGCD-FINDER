class Style:
    class EntryStyle:
        
        width=300
        height=70

        corner_radius=30
        text_font="Helvetica Rounded"
        text_size=25
        
        @classmethod
        def get_dimension(cls):
            return cls.width, cls.height
        
        @classmethod
        def get_style(cls):
            return cls.text_font, cls.text_size
        
    class TitleStyle:
        font='Roboto'
        size=50
        
        @classmethod
        def get_style(cls):
            return cls.font, cls.size
        
    class ResultTextStyle:
        font='Segeo UI this'
        size=30
        weight='bold'

        @classmethod
        def get_style(cls):
            return cls.font, cls.size, cls.weight
        
    
        
