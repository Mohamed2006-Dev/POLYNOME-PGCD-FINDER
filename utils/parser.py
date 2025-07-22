import customtkinter as ctk
from utils.ExtraMethods import ExtraMethods as E

def validate_entry(entry: ctk.CTkEntry, string_var: ctk.StringVar, prefix: str, event=None)->None:
    current_text = string_var.get()
    if 'x' in string_var.get():
        string_var.set(current_text.replace('x', 'X'))
    
    current_text=E.replace_exponents(string_var.get())
    string_var.set(current_text)

    if '=' in string_var.get():
        index = string_var.get().index('=')
        user_input = current_text[index + 1:]
    else:
        if prefix in string_var.get():
            user_input = string_var.get().replace(f'{prefix}', "")
        else:
            user_input = string_var.get()

    if not string_var.get().startswith(f"{prefix} ="):
        entry.delete(0, ctk.END)
        replace_with = f"{prefix} =" + user_input
        entry.insert(0, replace_with)

    if event:
        entry.icursor(event.widget.index(ctk.INSERT) + 1)

def extract_polynom(entry: ctk.CTkEntry, string_var: ctk.StringVar, prefix: str)->(str|None):
    validate_entry(entry, string_var, prefix)
    
    index: int=string_var.get().find('=')
    polynom: str = string_var.get()[index+1:]
    
    polynom=E.sympy_format(polynom)

    return polynom