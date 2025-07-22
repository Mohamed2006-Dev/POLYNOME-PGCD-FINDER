import re as re
class ExtraMethods:
    @staticmethod
    def replace_exponents(text):
        '''Remplace X**n par Xⁿ en utilisant des caractères Unicode pour les exposants.'''
        def replace(match):
            base = match.group(1)
            exponent = match.group(2)
            superscript_map = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
            return base + exponent.translate(superscript_map)

        return re.sub(r'(X)\*\*([0-9]+)', replace, text)

    @staticmethod
    def sympy_format(text: str):
        exposants = "⁰¹²³⁴⁵⁶⁷⁸⁹"
        for exposant in exposants:
            if exposant in text:
                text=text.replace(exposant, f"**{exposants.index(exposant)}")
        return text
    
    @staticmethod
    def is_none(obj):
        return obj is None
    
    @staticmethod
    def show_example(entry):
        NotImplementedError()

    @staticmethod
    def iterate_over_btns(btns:dict, sticky, rowspan=1):
        for key in btns.keys():
            btn, row, col=btns[key]
            btn.configure(height = 50, font = ("Arial", 25))
            btn.grid(row=row, column=col, sticky=sticky, rowspan=rowspan)

if __name__=='__main__':
    print(ExtraMethods.replace_exponents("X**3"))
    print(ExtraMethods.sympy_format("X²"))