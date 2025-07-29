"""
ButtonsCommands module.

This module provides functions that implement the logic for button actions in the PGCD Finder application.
It includes handlers for example, tips, keyboard, clear, and settings buttons, and manages user input and
UI updates for these actions.
"""

import customtkinter as ctk
from theme.color import Color
from utils.parser import validate_entry
from ExtraFrames.Tips.TipsWindow import TipsWindow
from ExtraFrames.Settings.SettingsWindow import SettingsWindow

def example_button_command(controller, entry_tuple1: tuple[ctk.CTkEntry|ctk.StringVar|str], entry_tuple2: tuple[ctk.CTkEntry|ctk.StringVar|str], user_input: list[str]):
    """
    Fill the entry fields with example polynomials and update user input, then display the result.

    Args:
        controller: The main controller instance.
        entry_tuple1: Tuple for the first entry (A(X)).
        entry_tuple2: Tuple for the second entry (B(X)).
        user_input: List to store user input strings.
    """
    entry1= entry_tuple1[0]
    entry2= entry_tuple2[0]
    example_p1 = "X**2 + 2*X + 1"
    example_p2 = "X + 1"

    entry1.delete(0, ctk.END)
    entry2.delete(0, ctk.END)

    entry1.insert(0, f'A(X) ={example_p1}')
    entry2.insert(0, f'B(X) ={example_p2}')
    user_input[0] = example_p1
    user_input[1] = example_p2
    validate_entry(entry_tuple1, user_input)
    validate_entry(entry_tuple2, user_input)

    controller.show_result()

def tips_button_command(master):
    """
    Show the tips/help window.

    Args:
        master: The parent widget (main application window).
    """
    tip_window = TipsWindow(master)
    tip_window.load_image()
    tip_window.load_color(
        Color.FrameColor.AppColor.PRIMARY,
        (Color.FrameColor.TipsColor.ALLOWED, Color.FrameColor.TipsColor.WARNING),
        Color.FrameColor.TipsColor.TITLE,
        Color.FrameColor.TipsColor.PRIMARY,
        (Color.FrameColor.TipsColor.SECONDARY, Color.FrameColor.TipsColor.BORDER)
    )
    tip_window.Show()

def keyboard_touche(text, entry_tuple, user_input):
    """
    Insert text into the entry at the cursor position and validate.

    Args:
        text (str): Text to insert.
        entry_tuple: Tuple containing the entry widget.
        user_input: List to store user input strings.
    """
    entry = entry_tuple[0]
    entry.insert(entry.index('insert'), text)
    validate_entry(entry_tuple, user_input)

def clear_btns(entry_tuple, user_input, clear_type=None, event=None):
    """
    Handle clearing or deleting characters in the entry field. 
 
    Args: 
        entry_tuple: Tuple containing the entry widget, stringvar, and prefix. 
        user_input: List to store user input strings. 
        clear_type (str, optional): If 'clear all', clears the entire entry. 
        event (tk.Event, optional): The event object from a key binding (e.g., <Delete> or <BackSpace>). 
            Needed when the function is triggered from a key event to override default behavior. 
 
    Returns: 
        str: 'break' to override default behavior of delete keys when cursor is in the prefix zone 
             or after a custom clear action. 
             
    Notes:
        - This function prevents deleting a predefined prefix (e.g., "y = ") by returning 'break' 
          if the cursor is within the prefix zone.
        - If a text range is selected, it deletes the selection. Otherwise, it deletes the character 
          just before the cursor.
        - Always calls `validate_entry` after modifying the entry content to ensure proper formatting.
        - To intercept key events like BackSpace, bind this function to the specific Entry widget, 
          not to the master/root widget.
    """
    widget, _, prefix = entry_tuple

    cursor_index = widget.index('insert')
    # Prevent deleting the prefix
    if cursor_index <= len(prefix + ' ='):
        return 'break'
    
    if clear_type == 'clear all':
        widget.delete(0, ctk.END)
        validate_entry(entry_tuple, user_input)
        widget.icursor(ctk.END)
        return 'break'

    try:
        sel_start=widget.index('sel.first')
        sel_end=widget.index('sel.last')
        has_selection=(sel_start!=sel_end)
    except Exception:
        has_selection=False

    if has_selection:
        widget.delete('sel.first', 'sel.last')
    else:
        widget.delete(widget.index('insert') - 1, widget.index('insert'))
        widget.icursor(ctk.END)
    
    validate_entry(entry_tuple, user_input)
    print("Delete Buttons is pressed")
    return 'break'

def keyboard_show_hide(keyboard_state, keyboard_frame):
    """
    Show or hide the keyboard frame based on its current state.

    Args:
        keyboard_state (bool): Current state of the keyboard (shown/hidden).
        keyboard_frame: The KeyboardFrame instance.
    """
    if not keyboard_state:
        keyboard_frame.Show()
    else:
        keyboard_frame.Hide()

def settings_button_command(master, color, font):
    """
    Show the settings window and apply color/font to the theme title.

    Args:
        master: The parent widget (main application window).
        color: Color for the settings title.
        font: Font for the settings title.
    """
    settings_window = SettingsWindow(master)
    settings_window.Theme_Frame.set_title_color_font(color, font)
    settings_window.Show()
