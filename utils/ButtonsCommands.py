import customtkinter as ctk
from utils.ExtraMethods import ExtraMethods as E
from utils.parser import validate_entry 
from ExtraFrames.TipsWindow import TipsWindow

def example_button_command(controller, entry1: list[ctk.CTkEntry|ctk.StringVar], entry2: list[ctk.CTkEntry|ctk.StringVar]):
    p1="X² + 2*X + 1"
    p2="X + 1"

    entry1[0].delete(0, ctk.END)
    entry2[0].delete(0, ctk.END)

    entry1[0].insert(0, p1)
    entry2[0].insert(0, p2)

    validate_entry(entry1[0], entry1[1], "A(X)")
    validate_entry(entry2[0], entry2[1], "B(X)")

    controller.display_result()

def tips_button_command(master):
    tipwindow=TipsWindow(master)
    tipwindow.load_image()
    tipwindow.Show()

def keyboard_touche(text, entry):
    entry.insert(entry.index('insert'), text)

def clear_btns(entry,type=None):
    tk_entry, str_var, prefix=entry
    if type=='clear all':
        tk_entry.delete(0, ctk.END)
        validate_entry(tk_entry, str_var, prefix)
        return
    tk_entry.delete(tk_entry.index('insert')-1, tk_entry.index('insert'))
    validate_entry(tk_entry, str_var, prefix)

    
def keyboard_show_hide(keyboard_state, keyboardframe):
    if not keyboard_state:
        keyboardframe.Show()
    else:
        keyboardframe.Hide()