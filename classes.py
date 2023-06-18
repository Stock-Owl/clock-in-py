from datetime import datetime as dt
from datetime import date as d
from datetime import time as t
from datetime import timedelta as tdelta

class EasyStyles:
    def Colorize(text: str, mode_: str = "f") -> str:
        ret_text = "{}".format(text)
        return ret_text
    
    # \u100b[
    styles: dict[str, str] = {
        "f_black": "\u100b[",
        "f_blue": "",
        "f_green": "",
        "f_aqua": "",
        "f_red": "",
        "f_purple": "",
        "f_yellow": "",
        "f_white": ""

    }

class TerminalMenu:
    pass    