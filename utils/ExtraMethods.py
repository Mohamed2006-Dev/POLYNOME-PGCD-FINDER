"""
ExtraMethods module.

This module provides utility methods for polynomial string formatting, conversion between
Unicode superscript and sympy format, creation of sympy Poly objects, None checking,
and grid placement of customtkinter buttons.
"""

import re
import sympy as sp

class ExtraMethods:
    """
    Utility methods for polynomial string formatting, conversion, and button handling.
    """

    @staticmethod
    def replace_exponents(text: str) -> str:
        """
        Replace X**n with Xⁿ using Unicode superscript characters.

        Args:
            text (str): Polynomial string in sympy format.

        Returns:
            str: Polynomial string with Unicode superscript exponents.
        """
        def replace(match):
            base = match.group(1)
            exponent = match.group(2)
            superscript_map = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
            return base + exponent.translate(superscript_map)

        return re.sub(r'(X)\*\*([0-9]+)', replace, text)

    @staticmethod
    def sympy_format(text: str) -> str:
        """
        Convert Unicode superscript exponents back to sympy format (**n).

        Args:
            text (str): Polynomial string with Unicode superscripts.

        Returns:
            str: Polynomial string in sympy format.
        """
        superscripts = "⁰¹²³⁴⁵⁶⁷⁸⁹"
        for s in superscripts:
            if s in text:
                text = text.replace(s, f"**{superscripts.index(s)}")
        return text
    
    @staticmethod
    def convert_polynome(p: str) -> sp.Poly:
        """
        Convert a string polynomial to a sympy Poly object.

        Args:
            p (str): Polynomial string.

        Returns:
            sp.Poly: sympy Poly object.
        """
        p = ExtraMethods.sympy_format(p)
        X = sp.Symbol("X")
        return sp.Poly(p, X)

    @staticmethod
    def is_none(obj) -> bool:
        """
        Check if the given object is None.

        Args:
            obj: Any object.

        Returns:
            bool: True if obj is None, False otherwise.
        """
        return obj is None
    
    @staticmethod
    def iterate_over_btns(btns: dict, sticky, rowspan=1):
        """
        Place buttons in a grid with consistent style and layout.

        Args:
            btns (dict): Dictionary of buttons with (button, row, col) tuples.
            sticky: Sticky value for grid placement.
            rowspan (int): Rowspan for grid placement.
        """
        for key in btns.keys():
            btn, row, col = btns[key]
            btn.configure(height=50, font=("Arial", 25))
            btn.grid(row=row, column=col, sticky=sticky, rowspan=rowspan, padx=1, pady=1)
    
    @staticmethod
    def fix_float_format_in_string(poly_str):
        """
        Fix floating-point coefficients in a polynomial string for proper parsing.

        This method ensures that numbers like '2.500' become '2.5', trims the fractional part to at most
        two digits, and removes the decimal part if it is '00' (e.g., '3.00' becomes '3').

        Args:
            poly_str (str): The polynomial string to process.

        Returns:
            str: The polynomial string with properly formatted floating-point numbers.
        """
        def repl(match):
            integer_part = match.group(1)
            fractional_part = match.group(3)
            if len(fractional_part) > 2:
                fractional_part = fractional_part[:2]
            if fractional_part == '00':
                return integer_part
            return f'{integer_part}.{fractional_part.replace("0", "")}'
        # Replace occurrences like '2.500' with '2.5', '3.00' with '3', etc.
        poly_str = re.sub(r'(\d+)(\.)(\d+)', repl, poly_str)
        return poly_str

    @staticmethod
    def displayed_format(poly):
        poly=str(poly.as_expr())
        poly=ExtraMethods.replace_exponents(poly)
        poly=ExtraMethods.fix_float_format_in_string(poly)
        return poly

# Example usage for testing
if __name__ == '__main__':
    print(ExtraMethods.replace_exponents("X**3"))
    print(ExtraMethods.sympy_format("X²"))