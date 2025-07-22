from ExtraFrames.EntryFrame import EntryFrame
from ExtraFrames.ResultFrame import ResultFrame
from ExtraFrames.TopFrame import TopFrame
from ExtraFrames.FooterFrame import FooterFrame
from ExtraFrames.TipsWindow import TipsWindow
from ExtraFrames.KeyboardFrame import KeyboardFrame
from ExtraFrames.App import App
from Exceptions.Expression import ExpressionError
from utils.ExtraMethods import ExtraMethods as E
from utils.parser import extract_polynom, validate_entry
from utils.Calculator import performe_calculation
from config.assets import Assets
from utils.ButtonsCommands import *


class Controller:
    def __init__(self):
        self.__App = App()
        self.__EntryFrame = EntryFrame(self.__App)
        self.__ResultFrame = ResultFrame(self.__App)
        self.__TopFrame = TopFrame(self.__App)
        self.__FooterFrame= FooterFrame(self.__App)
        self.__KeyboardFrame = KeyboardFrame(self.__App)
        
        self.set_buttons_command()
        
        self.__entry1, self.__str1=self.__EntryFrame.getentry(1)
        self.__entry2, self.__str2=self.__EntryFrame.getentry(2)
        validate_entry(self.__entry1, self.__str1, "A(X)")
        validate_entry(self.__entry2, self.__str2, "B(X)")
        self.apply_images()
        
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
        self.__EntryFrame.pgcd_command(self.display_result)
        self.__FooterFrame.set_example_command(lambda: example_button_command(self, [self.__entry1, self.__str1], [self.__entry2, self.__str2]))
        self.__FooterFrame.set_tips_command(lambda: tips_button_command(self.__App))
        self.__FooterFrame.set_keyboard_command(lambda: keyboard_show_hide(self.__KeyboardFrame.getkeyboard_state(), self.__KeyboardFrame))
        
        btns=self.__KeyboardFrame.getbtns('general')
        for btn in btns:
            text=btn.cget('text')
            self.__KeyboardFrame.set_btns_command(btn, lambda t=text: keyboard_touche(t, self.__EntryFrame.getfocus()))

        command1=lambda: clear_btns(self.__EntryFrame.getfocus(), 'clear all')
        command2=lambda: clear_btns(self.__EntryFrame.getfocus())
        self.__KeyboardFrame.set_clear_btns_command(command1, command2)

        self.__FooterFrame.set_keyboard_command(lambda: keyboard_show_hide(self.__KeyboardFrame.getkeyboard_state(), self.__KeyboardFrame))

    def apply_images(self):
        self.__FooterFrame.set_icons(Assets.convert("request", (50, 50)), Assets.convert('technology', (50, 50)), Assets.convert('book', (50, 50)))
        self.__TopFrame.set_icons(Assets.convert('math-book', (50, 50)), Assets.convert('calculating', (50, 50)))
        
        

def main():
    C=Controller()
    C.create()