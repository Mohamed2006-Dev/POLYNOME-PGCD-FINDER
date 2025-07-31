"""
parser.py

This module provides functions for validating and formatting polynomial input in the PGCD Finder application.
It ensures user input is cleaned, formatted, and compatible with sympy polynomial operations.
Supports both auto-correction and manual input modes.
"""

import customtkinter as ctk
import re
from utils.ExtraMethods import ExtraMethods as E
from Exceptions.Expression import ExpressionError

def validate_entry(entry_tuple: list[ctk.CTkEntry | ctk.StringVar | str], user_input_ref: list[str],
                    auto_correction_state:bool, event=None) -> None:
    """
    Validate and format the entry field for polynomial input.
    Updates the user_input_ref list with the cleaned input.

    Args:
        entry_tuple (list): [entry widget, string variable, prefix string]
        user_input_ref (list): Reference to user input list to update.
        auto_correction_state (bool): If True, auto-correct and format input; if False, accept as-is.
        event: Optional event parameter (unused).
    """
    entry, string_var, prefix = entry_tuple
    current_value = string_var.get()

    if not auto_correction_state:
        # In manual mode, just extract the raw input after the prefix and update user_input_ref
        try:
            match (prefix):
                case 'A(X)':
                    user_input_ref[0] = current_value[len(prefix):]
                case 'B(X)':
                    user_input_ref[1] = current_value[len(prefix):]
            return
        except Exception as e:
            raise ExpressionError("Unexpected polynome expression:")
    
    # In auto-correction mode, clean and format the input
    # If the prefix is missing, validate the whole input
    if not current_value.startswith(f'{prefix} ='):
        if current_value.find(prefix.replace(')','')) == -1:
            # Prefix not found, validate the entire input
            cleaned_input = validate_user_input(current_value)
        else:
            # Prefix found, validate input after prefix
            cleaned_input = validate_user_input(current_value[len(prefix):])
    else:
        # Prefix and '=' present, validate input after '='
        cleaned_input = validate_user_input(current_value[current_value.index('=') + 1:])

    # Update the user_input_ref list with the cleaned input
    match prefix:
        case 'A(X)':
            user_input_ref[0] = cleaned_input
        case 'B(X)':
            user_input_ref[1] = cleaned_input
    # Update the entry display with formatted input
    string_var.set(f'{prefix} ={cleaned_input}')

    # Restore cursor position to the end
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
    user_input = re.sub(r'[^ X*0-9⁰¹²³⁴⁵⁶⁷⁸⁹+\-/\.]', '', user_input)
    # Remove repeated X
    user_input = re.sub(r'X{2,}', 'X', user_input)
    # Insert multiplication sign between coefficient and X (Doesn't work if there is a space between X and n)
    def repl_coef(match):
        coef = match.group(1)
        return f'{coef}*X'
    user_input = re.sub(r'(\d+)X', repl_coef, user_input)
    # Convert 'Xn' to 'Xⁿ' (Doesn't work if there is a space between X and n)
    def repl_exponent(match):
        exponent=match.group(2)
        return f'X**{exponent}'
    user_input = re.sub(r'(X)(\d+)', repl_exponent, user_input)
    # Insert X if it doesn't exist behind exposant operator '**' 
    user_input = re.sub(r'(?<!X)[\*]{2}', 'X**', user_input)
    # Remove misplaced operators and asterisks
    user_input = re.sub(r'(?<!\*)[+\-\/](?=\*)|\*(?=[+\-\/ ])', '', user_input)
    # Remove multiple operators 
    user_input = re.sub(r'[+\-\/]{2,}', '', user_input)
    # Remove multiple exponants
    user_input = re.sub(r'\*{3,}', '**', user_input)
    # Convert to Unicode superscript format
    user_input = E.replace_exponents(user_input)
    return user_input

