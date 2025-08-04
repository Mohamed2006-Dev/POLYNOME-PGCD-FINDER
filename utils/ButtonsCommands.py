"""
ButtonsCommands module.

This module provides functions that implement the logic for button actions in the PGCD Finder application.
It includes handlers for example, tips, keyboard, clear, and settings buttons, and manages user input and
UI updates for these actions. It also supports toggling auto-correction and synchronizing settings between
the settings window and the entry frame.
"""

import customtkinter as ctk
from theme.color import Color
from utils.parser import validate_entry
from utils.ExtraMethods import ExtraMethods as E
from ExtraFrames.Tips.TipsWindow import TipsWindow
from ExtraFrames.Settings.SettingsWindow import SettingsWindow
from ExtraFrames.History.HistoryWindow import HistoryWindow
from ExtraFrames.History.HistoryFrame import HistoryFrame
from utils.Calculator import perform_calculation
import pyperclip

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
    example_p1 = "X² + 2*X + 1"
    example_p2 = "X + 1"

    entry1.delete(0, ctk.END)
    entry2.delete(0, ctk.END)

    entry1.insert(0, f'A(X) ={example_p1}')
    entry2.insert(0, f'B(X) ={example_p2}')
    user_input[0] = example_p1
    user_input[1] = example_p2

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

def keyboard_touche(text, entry_tuple, user_input, auto_correction_state):
    """
    Insert text into the entry at the cursor position and validate.

    Args:
        text (str): Text to insert.
        entry_tuple: Tuple containing the entry widget.
        user_input: List to store user input strings.
    """
    if entry_tuple is None:
        return
    
    entry = entry_tuple[0]
    entry.insert(entry.index('insert'), text)
    validate_entry(entry_tuple, user_input, auto_correction_state=auto_correction_state)

def clear_btns(entry_tuple, user_input, auto_correction_state,clear_type=None, event=None):
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
    if entry_tuple is None:
        return 'break'
    
    widget, _, prefix = entry_tuple
    cursor_index = widget.index('insert')
    
    if clear_type == 'clear all':
        widget.delete(0, ctk.END)
        widget.insert(0, f'{prefix} =')
        widget.icursor(ctk.END)
        return 'break'
    
    # Prevent deleting the prefix
    if cursor_index <= len(prefix + ' ='):
        return 'break'
    

    try:
        sel_start=widget.index('sel.first')
        sel_end=widget.index('sel.last')
        has_selection=(sel_start!=sel_end)
    except Exception:
        has_selection=False

    if has_selection:
        if sel_start<=len(prefix):
            return 'break'
        widget.delete('sel.first', 'sel.last')

    else:
        widget.delete(widget.index('insert') - 1, widget.index('insert'))
        widget.icursor(ctk.END)
    
    validate_entry(entry_tuple, user_input, auto_correction_state, event)
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

def auto_correction_on_off(entry_frame, state):
    """
    Update the auto-correction state of the entry frame.

    Args:
        entry_frame: The EntryFrame instance whose auto-correction state will be updated.
        state (bool): The new auto-correction state (True for ON, False for OFF).
    """
    entry_frame.set_auto_correction(state)

def settings_button_command(master, color, font):
    """
    Show the settings window, apply color/font to the theme title, and synchronize auto-correction.

    Args:
        master: The parent widget (main application window).
        color: Color for the settings title.
        font: Font for the settings title.
    """
    settings_window = SettingsWindow(master)
    # Set the color and font for the theme and auto-correction frames title in the settings window
    settings_window.Theme_Frame.set_title_color_font(color, font)
    settings_window._Auto_Correction_Frame.set_color_font(color, font)
    # Set the command for auto-correction toggle to update the entry frame accordingly
    settings_window.set_auto_correction_command(
        lambda: auto_correction_on_off(master.get_entry_frame(), settings_window._Auto_Correction_Frame.get_state())
    )
    settings_window.Show()

def history_button_command(master, history, entries, result_frame):
    history_window=HistoryWindow(master)
    if not history: 
        history_window.show_empty()
    
    for d in history:
        history_frame=HistoryFrame(history_window)
        p1, p2, pgcd=d['poly1'], d['poly2'], d['pgcd']
        t=f'Pgcd({E.displayed_format(p1)}, {E.displayed_format(p2)}) = {E.displayed_format(pgcd)}'
        history_frame.set_history_label(text=t)
        history_frame.set_show_command(lambda history_data=d: show_history_command(history_window, entries, history_data, result_frame))
        history_frame.set_copy_clipboard_command(lambda text=t: copy_command(text))
        history_frame.Show()

def show_history_command(window, entries, history_dict, result_frame):
    window.destroy()
    entry1, entry2 = entries
    p1, p2 = history_dict['poly1'], history_dict['poly2']
    entry1.delete(0, ctk.END)
    entry1.insert(0, f'A(X) ={E.displayed_format(p1)}')
    entry2.delete(0, ctk.END)
    entry2.insert(0, f'B(X) ={E.displayed_format(p2)}')
    
    Q, R, PGCD = perform_calculation(p1, p2)
    result_frame.config_quotient(E.displayed_format(Q))
    result_frame.config_rest(E.displayed_format(R.as_expr))
    result_frame.config_pgcd(E.displayed_format(PGCD))
    result_frame.Show()

def copy_command(text):
    pyperclip.copy(text)