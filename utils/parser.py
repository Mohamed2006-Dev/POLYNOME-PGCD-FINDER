"""
parser.py

This module provides functions for validating and formatting polynomial input in the PGCD Finder application.
It ensures user input is cleaned, formatted, and compatible with sympy polynomial operations.
"""

import customtkinter as ctk
import re
from utils.ExtraMethods import ExtraMethods as E

def validate_entry(entry_tuple: list[ctk.CTkEntry | ctk.StringVar | str], user_input_ref: list[str], event=None) -> None:
    """
    Validate and format the entry field for polynomial input.
    Updates the user_input_ref list with the cleaned input.

    Args:
        entry_tuple (list): [entry widget, string variable, prefix string]
        user_input_ref (list): Reference to user input list to update.
        event: Optional event parameter (unused).
    """
    entry, string_var, prefix = entry_tuple
    current_value = string_var.get()

    # If the prefix is missing, validate the whole input
    if not current_value.startswith(f'{prefix} ='):
        if current_value.find(prefix.replace(')',''))==-1:
            cleaned_input = validate_user_input(current_value)
        else:
            cleaned_input=validate_user_input(current_value[len(prefix):])
    else:
        cleaned_input = validate_user_input(current_value[current_value.index('=') + 1:])

    match prefix:
        case 'A(X)':
            user_input_ref[0] = cleaned_input
        case 'B(X)':
            user_input_ref[1] = cleaned_input
    string_var.set(f'{prefix} ={cleaned_input}')

    # Restore cursor position
    entry.icursor(ctk.END)

def validate_user_input(user_input: str) -> str:
    """
    Clean and format the user input for a polynomial.

    - Replaces lowercase x with uppercase X.
    - Removes invalid characters.
    - Ensures proper multiplication and exponent formatting.

    Args:
        user_input (str): Raw user input string.

    Returns:
        str: Cleaned and formatted polynomial string.
    """
    # Replace lowercase x with uppercase X
    user_input = user_input.replace('x', "X")
    # Remove invalid characters
    user_input = re.sub(r'[^ X*0-9⁰¹²³⁴⁵⁶⁷⁸⁹+\-/]', '', user_input)
    # Remove repeated X
    user_input = re.sub(r'X{2,}', 'X', user_input)
    # Insert multiplication sign between coefficient and X
    def repl(match):
        coef = match.group(1)
        return f'{coef}*X'
    user_input = re.sub(r'(\d+)X', repl, user_input)
    # Remove misplaced operators and asterisks
    user_input = re.sub(r'(?<!\*)[+\-\/](?=\*)|\*(?=[+\-\/ ])', '', user_input)
    user_input = re.sub(r'[+\-\/]{2,}', '', user_input)
    user_input = re.sub(r'\*{3,}', '**', user_input)
    user_input = re.sub(r'(?<!X)[\*]{2}', 'X**', user_input)
    # Convert to Unicode superscript format
    user_input = E.replace_exponents(user_input)
    return user_input

