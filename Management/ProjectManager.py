from ExtraFrames.EntryFrame import EntryFrame
from ExtraFrames.ResultFrame import ResultFrame
from ExtraFrames.TopFrame import TopFrame
from ExtraFrames.FooterFrame import FooterFrame
from ExtraFrames.KeyboardFrame import KeyboardFrame
from ExtraFrames.App import App
from utils.ExtraMethods import ExtraMethods as E
from utils.parser import extract_polynom, validate_entry
from utils.Calculator import performe_calculation
from config.assets import Assets
from utils.ButtonsCommands import *
from theme.font import *
from theme.style import Style
from theme.color import Color

class Controller:
    def __init__(self):

        #====================(window layers)===================
        self.__App = App()
        self.__EntryFrame = EntryFrame(self.__App)
        self.__ResultFrame = ResultFrame(self.__App)
        self.__TopFrame = TopFrame(self.__App)
        self.__FooterFrame= FooterFrame(self.__App)
        self.__KeyboardFrame = KeyboardFrame(self.__App)
        
        #====================(variables)=================
        self.__entry1, self.__str1=self.__EntryFrame.getentry(1)
        self.__entry2, self.__str2=self.__EntryFrame.getentry(2)
        self.widgets={
            "titles": [self.__TopFrame.get_title(), self.__ResultFrame.get_title()],
            "result_labels": [self.__ResultFrame.get_q_label(), self.__ResultFrame.get_r_label(), self.__ResultFrame.get_pgcd_label()],
            "entry_labels": [self.__EntryFrame.getentry(1)[0], self.__EntryFrame.getentry(2)[0]],
            "numeric_btns": self.__KeyboardFrame.getnumericbtns(),
            'non_numeric_keyboard_btns': self.__KeyboardFrame.get_non_numeric_btns(),
            'footer_btns': self.__FooterFrame.get_buttons(),
            'entry_btn': self.__EntryFrame.get_button()
        }

        #================(Methods Call)========================
        self.set_buttons_command()
        validate_entry(self.__entry1, self.__str1, "A(X)")
        validate_entry(self.__entry2, self.__str2, "B(X)")
        self.apply_images()
        self.load_fonts()
        self.configure_dimensions()
        self.load_colors()

        
    def __handle_result(self):
        p1 = extract_polynom(self.__entry1, self.__str1, "A(X)")
        p2 = extract_polynom(self.__entry2, self.__str2, "B(X)")

        if p1 and p2:
            Q, R, pgcd=performe_calculation(p1, p2)
            return Q, R, pgcd
        else:
            return None, None, None
        
        
    def display_result(self):
        Q, R, pgcd = self.__handle_result()
        validation = E.is_none(Q) and E.is_none(R) and E.is_none(pgcd)
        if validation:
            self.__EntryFrame.clear_entries()

        self.__ResultFrame.config_quotient(Q)
        self.__ResultFrame.config_rest(R)
        self.__ResultFrame.config_pgcd(pgcd)

        self.__ResultFrame.Show()


    def create(self):
        self.__TopFrame.Show()
        self.__EntryFrame.Show()
        self.__FooterFrame.Show(sticky=['sw', 's', 'se'])
        self.__App.mainloop()

    def set_buttons_command(self):
        #=============================(Entry btns)==========================================
        self.__EntryFrame.pgcd_command(self.display_result)

        #=============================(Footer btns)=========================================
        self.__FooterFrame.set_example_command(lambda: example_button_command(self, [self.__entry1, self.__str1], [self.__entry2, self.__str2]))
        self.__FooterFrame.set_tips_command(lambda: tips_button_command(self.__App))
        self.__FooterFrame.set_keyboard_command(lambda: keyboard_show_hide(self.__KeyboardFrame.getkeyboard_state(), self.__KeyboardFrame))
        
        #==============================(Keyboard btns)======================================
        btns=self.__KeyboardFrame.getbtns('general')
        for btn in btns:
            text=btn.cget('text')
            self.__KeyboardFrame.set_btns_command(btn, lambda t=text: keyboard_touche(t, self.__EntryFrame.getfocus()[0]))

        command1=lambda: clear_btns(self.__EntryFrame.getfocus(), 'clear all')
        command2=lambda: clear_btns(self.__EntryFrame.getfocus())
        self.__KeyboardFrame.set_clear_btns_command(command1, command2)

        #==============================(END)===========================================


    def apply_images(self):
        self.__EntryFrame.set_icon(Assets.convert("diviser", (100, 90)))
        self.__FooterFrame.set_icons(tipsicon=Assets.convert("request", (50, 50)), keyboardicon=Assets.convert('technology', (50, 50)), exampleicon=Assets.convert('book', (50, 50)))
        self.__TopFrame.set_icons(Assets.convert('math-book', (50, 50)), Assets.convert('calculating', (50, 50)))
        self.__KeyboardFrame.configure_btns(Assets.convert(("exposant(light)", "exposant"), (30, 30)))
        
    def load_fonts(self):
        #================(Fonts Vars)==================
        title_font=TitleCTkFont()
        result_font=ResultCTkFont()
        entry_font=EntryCTkFont()

        #================(Lables Vars)=================
        title_widgets=self.widgets['titles']
        result_widgets=self.widgets['result_labels']
        entry_widgets=self.widgets['entry_labels']

        for w in title_widgets:
            w.configure(font=title_font)
        for w in result_widgets:
            w.configure(font=result_font)
        for w in entry_widgets:
            w.configure(font=entry_font)
        
    def configure_dimensions(self):
        width, height=Style.EntryStyle.get_dimension()
        cr=Style.EntryStyle.corner_radius

        for w in self.widgets['entry_labels']:
            w.configure(width=width, height=height, corner_radius=cr)

    def load_colors(self):
        title_widgets=self.widgets['titles']
        result_widgets=self.widgets['result_labels']
        entry_widgets=self.widgets['entry_labels']
        numeric_btns=self.widgets['numeric_btns']
        non_numeric_btns=self.widgets['non_numeric_keyboard_btns']
        footer_btns=self.widgets['footer_btns']
        entry_btn=self.widgets['entry_btn']

        for t in title_widgets:
            t.configure(text_color=Color.TitleColor.PRIMARY)
        for r in result_widgets:
            r.configure(text_color=Color.ResultColor.PRIMARY)
        for e in entry_widgets:
            e.configure(fg_color=Color.EntryColor.PRIMARY, text_color=Color.EntryColor.TEXT, border_color=Color.EntryColor.BORDER)
        for n in numeric_btns:
            n.configure(hover_color=Color.Buttons.NumericButtons.HOVER, fg_color=Color.Buttons.NumericButtons.PRIMARY)
        for nnb in non_numeric_btns:
            nnb.configure(hover_color=Color.Buttons.NonNumericKeyboardButtons.Hover, fg_color=Color.Buttons.NonNumericKeyboardButtons.PRIMARY)
        for f in footer_btns:
            f.configure(hover_color=Color.Buttons.FooterButtons.HOVER, fg_color=Color.Buttons.FooterButtons.PRIMARY, text_color=Color.Buttons.FooterButtons.TEXT)

        entry_btn.configure(hover_color=Color.Buttons.EntryButton.HOVER, fg_color=Color.Buttons.EntryButton.PRIMARY)

        self.__ResultFrame.configure(border_color=Color.FrameColor.ResultFrameColor.BORDER, fg_color=Color.FrameColor.ResultFrameColor.PRIMARY)
        self.__KeyboardFrame.configure(border_color=Color.FrameColor.KeyboardFrameColor.BORDER)
        self.__EntryFrame.configure(fg_color=Color.FrameColor.EntryFrameColor.PRIMARY)
        self.__App.configure(fg_color=Color.FrameColor.AppColor.PRIMARY)

        
            


def main():
    C=Controller()
    C.create()