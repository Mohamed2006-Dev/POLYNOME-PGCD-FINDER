"""
ProjectManager module.

This module contains the Controller class, which serves as the main controller for the PGCD Finder application.
It manages the initialization of UI frames, event binding, result display logic, and application configuration.
The Controller class coordinates all UI components, handles user input, and applies styles, fonts, and colors.
It also synchronizes settings such as auto-correction and theme between the settings window and entry frame.
"""

# ===================== Imports =====================
from ExtraFrames.EntryFrame import EntryFrame
from Exceptions.Expression import ExpressionError
from ExtraFrames.ResultFrame import ResultFrame
from ExtraFrames.TopFrame import TopFrame
from ExtraFrames.FooterFrame import FooterFrame
from ExtraFrames.KeyboardFrame import KeyboardFrame
from ExtraFrames.ToolbarFrame import ToolbarFrame
from ExtraFrames.App import App
from utils.ExtraMethods import ExtraMethods as E
from utils.parser import *
from utils.Calculator import *
from utils.ButtonsCommands import *
from config.assets import Assets
from theme.font import *
from theme.style import Style
from theme.color import Color

# ===================== Controller Class =====================
class Controller:
    """
    Main controller for the PGCD Finder application.

    Handles UI setup, event binding, result display logic, and applies styles, fonts, and colors.
    Coordinates all UI components, manages user input, and synchronizes settings such as auto-correction.
    """
    def __init__(self):
        # ---------- Window Layers ----------
        # Initialize all main frames and application window
        self.__App = App()
        self.__ToolbarFrame = ToolbarFrame(self.__App)
        self.__EntryFrame = EntryFrame(self.__App)
        self.__ResultFrame = ResultFrame(self.__App)
        self.__TopFrame = TopFrame(self.__App)
        self.__FooterFrame = FooterFrame(self.__App)
        self.__KeyboardFrame = KeyboardFrame(self.__App)
        
        # ---------- Widget References ----------
        # Store references to key widgets for easy configuration
        self.__entry1 = self.__EntryFrame.getentry(1)
        self.__entry2 = self.__EntryFrame.getentry(2)
        self.widgets = {
            "titles": [self.__TopFrame.get_title(), self.__ResultFrame.get_title()],
            "result_labels": [self.__ResultFrame.get_q_label(), self.__ResultFrame.get_r_label(), self.__ResultFrame.get_pgcd_label()],
            "entry_labels": [self.__EntryFrame.getentry(1), self.__EntryFrame.getentry(2)],
            "numeric_btns": self.__KeyboardFrame.getnumericbtns(),
            "non_numeric_keyboard_btns": self.__KeyboardFrame.get_non_numeric_btns(),
            "footer_btns": self.__FooterFrame.get_buttons(),
            "entry_btn": self.__EntryFrame.get_button(),
            "toolbar_btns": self.__ToolbarFrame.get_buttons()
        }

        # ---------- Initialization Calls ----------
        # Set up commands, images, fonts, dimensions, and colors
        self.set_buttons_command()
        self.apply_images()
        self.load_fonts()
        self.configure_dimensions()
        self.load_colors()
        # Link entry frame to the app for settings synchronization
        self.__App.set_entry_frame(self.__EntryFrame)

        # Bind Enter key to show result
        self.__App.bind('<Return>', self.show_result)
        # ---------- End Initialization ----------

    # ===================== Calculation & Result =====================
    def __compute_result(self):
        """
        Compute the calculation of quotient, remainder, and GCD.

        Returns:
            tuple: (Q, R, pgcd) or (None, None, None) on error.
        Raises:
            ExpressionError: If input is invalid or cannot be parsed.
        """
        try:
            p1 = E.convert_polynome(validate_user_input(self.__EntryFrame.user_input[0])) if self.__EntryFrame.user_input[0] != '' else ''
            p2 = E.convert_polynome(validate_user_input(self.__EntryFrame.user_input[1])) if self.__EntryFrame.user_input[1] != '' else ''

            if p1 and p2:
                Q, R, pgcd = perform_calculation(p1, p2)
                return Q, R, pgcd
            else:
                return None, None, None
        except Exception as e:
            self.__EntryFrame.clear_entries()
            self.__App.focus_force()
            self.__EntryFrame.currentfocus=None
            raise ExpressionError("Unexpected expression error: Polynomials are not in the correct format")

    def show_result(self, event=None):
        """
        Show the calculation result in the result frame.

        Raises:
            ExpressionError: If input is invalid.
        """
        Q, R, pgcd = self.__compute_result()
        validation = E.is_none(Q) and E.is_none(R) and E.is_none(pgcd)
        if validation:
            self.__EntryFrame.clear_entries()
            raise ExpressionError("Unexpected expression error: Polynomials are not in the correct format")

        self.__ResultFrame.config_quotient(Q)
        self.__ResultFrame.config_rest(R)
        self.__ResultFrame.config_pgcd(pgcd)
        self.__ResultFrame.Show()

    # ===================== UI Setup & Main Loop =====================
    def create(self):
        """
        Show all main frames and start the application main loop.
        """
        self.__ToolbarFrame.Show()
        self.__TopFrame.Show()
        self.__EntryFrame.Show()
        self.__FooterFrame.Show(sticky=['sw', 's', 'se'])
        self.__App.mainloop()

    # ===================== Button Commands =====================
    def set_buttons_command(self):
        """
        Bind all button commands for entry, footer, and keyboard.
        Sets up synchronization between settings and entry frame (e.g., auto-correction).
        """
        # Entry button
        self.__EntryFrame.pgcd_command(self.show_result)

        # Footer buttons
        self.__FooterFrame.set_example_command(
            lambda: example_button_command(
                self,
                self.__EntryFrame.getentrytuple(self.__entry1),
                self.__EntryFrame.getentrytuple(self.__entry2),
                self.get_user_input()
            )
        )
        self.__FooterFrame.set_tips_command(lambda: tips_button_command(self.__App))
        self.__FooterFrame.set_keyboard_command(lambda: keyboard_show_hide(self.__KeyboardFrame.getkeyboard_state(), self.__KeyboardFrame))
        
        # Keyboard buttons
        btns = self.__KeyboardFrame.getbtns('general')
        for btn in btns:
            text = btn.cget('text')
            self.__KeyboardFrame.set_btns_command(btn, lambda t=text: keyboard_touche(t, self.__EntryFrame.getfocus(), self.get_user_input(), self.__EntryFrame.get_auto_correction()))

        command1 = lambda: clear_btns(
                                    self.__EntryFrame.getfocus(), self.get_user_input(), 
                                    self.__EntryFrame.get_auto_correction(),'clear all'
                                    )
        command2 = lambda: clear_btns(
                                    self.__EntryFrame.getfocus(), self.get_user_input(), 
                                    self.__EntryFrame.get_auto_correction(), 'clear last'
                                    )
        self.__KeyboardFrame.set_clear_btns_command(command1, command2)
        
        #toolbar buttons
        self.__ToolbarFrame.set_settings_command(lambda: settings_button_command(self.__App, Color.FrameColor.SettingsColor.TITLE, SettingsTitleCTkFont()))
        self.__ToolbarFrame.set_history_command(lambda: history_button_command(self.__App))

    # ===================== Images & Icons =====================
    def apply_images(self):
        """
        Set icons/images for entry, footer, top, and keyboard frames.
        """
        self.__EntryFrame.set_icon(Assets.convert("diviser", (100, 90)))
        self.__FooterFrame.set_icons(
            tipsicon=Assets.convert("request", (50, 50)),
            keyboardicon=Assets.convert('technology', (50, 50)),
            exampleicon=Assets.convert('book', (50, 50))
        )
        self.__TopFrame.set_icons(
            Assets.convert('math-book', (50, 50)),
            Assets.convert('calculating', (50, 50))
        )
        self.__KeyboardFrame.configure_btns(Assets.convert(("exposant(light)", "exposant"), (30, 30)))

        self.__ToolbarFrame.load_icons(Assets.convert('settings', (20, 20)), Assets.convert('history', (20, 20)))

    # ===================== Fonts =====================
    def load_fonts(self):
        """
        Apply custom fonts to all relevant widgets.
        """
        title_font = TitleCTkFont()
        result_font = ResultCTkFont()
        entry_font = EntryCTkFont()

        title_widgets = self.widgets['titles']
        result_widgets = self.widgets['result_labels']
        entry_widgets = self.widgets['entry_labels']

        for w in title_widgets:
            w.configure(font=title_font)
        for w in result_widgets:
            w.configure(font=result_font)
        for w in entry_widgets:
            w.configure(font=entry_font)

    # ===================== Dimensions =====================
    def configure_dimensions(self):
        """
        Set dimensions and corner radius for entry widgets.
        """
        width, height = Style.EntryStyle.get_dimension()
        cr = Style.EntryStyle.corner_radius

        for w in self.widgets['entry_labels']:
            w.configure(width=width, height=height, corner_radius=cr)

    # ===================== Colors =====================
    def load_colors(self):
        """
        Apply color themes to all widgets and frames.
        """
        title_widgets = self.widgets['titles']
        result_widgets = self.widgets['result_labels']
        entry_widgets = self.widgets['entry_labels']
        numeric_btns = self.widgets['numeric_btns']
        non_numeric_btns = self.widgets['non_numeric_keyboard_btns']
        footer_btns = self.widgets['footer_btns']
        entry_btn = self.widgets['entry_btn']
        toolbar_btns=self.widgets['toolbar_btns']

        for t in title_widgets:
            t.configure(text_color=Color.TitleColor.PRIMARY)
        for r in result_widgets:
            r.configure(text_color=Color.ResultColor.PRIMARY)
        for e in entry_widgets:
            e.configure(fg_color=Color.EntryColor.PRIMARY, text_color=Color.EntryColor.TEXT, border_color=Color.EntryColor.BORDER)
        for n in numeric_btns:
            n.configure(hover_color=Color.Buttons.NumericButtons.HOVER, fg_color=Color.Buttons.NumericButtons.PRIMARY, text_color=Color.Buttons.NumericButtons.TEXT)
        for nnb in non_numeric_btns:
            nnb.configure(hover_color=Color.Buttons.NonNumericKeyboardButtons.HOVER, fg_color=Color.Buttons.NonNumericKeyboardButtons.PRIMARY, text_color=Color.Buttons.NonNumericKeyboardButtons.TEXT)
        for f in footer_btns:
            f.configure(hover_color=Color.Buttons.FooterButtons.HOVER, fg_color=Color.Buttons.FooterButtons.PRIMARY, text_color=Color.Buttons.FooterButtons.TEXT)
        for tool in toolbar_btns:
            tool.configure(hover_color=Color.FrameColor.AppColor.PRIMARY, fg_color=Color.Buttons.ToolbarButton.PRIMARY)

        entry_btn.configure(hover_color=Color.Buttons.EntryButton.HOVER, fg_color=Color.Buttons.EntryButton.PRIMARY)

        self.__ResultFrame.configure(border_color=Color.FrameColor.ResultFrameColor.BORDER, fg_color=Color.FrameColor.ResultFrameColor.PRIMARY)
        self.__KeyboardFrame.configure(border_color=Color.FrameColor.KeyboardFrameColor.BORDER)
        self.__EntryFrame.configure(fg_color=Color.FrameColor.EntryFrameColor.PRIMARY)
        self.__App.configure(fg_color=Color.FrameColor.AppColor.PRIMARY)
        self.__ToolbarFrame.configure(fg_color=Color.FrameColor.ToolbarColor.PRIMARY, border_color=Color.FrameColor.ToolbarColor.BORDER)
        self.__ToolbarFrame.get_inner_frame().configure(fg_color=Color.FrameColor.ToolbarColor.PRIMARY)

    # ===================== User Input =====================
    def get_user_input(self):
        """
        Return the current user input list from the entry frame.

        Returns:
            list: The user input list.
        """
        return self.__EntryFrame.user_input

# ===================== Main Entry Point =====================
def main():
    """
    Application entry point. Instantiates the controller and starts the UI.
    """
    C = Controller()
    C.create()