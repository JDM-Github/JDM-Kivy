import os
import math
import json
from PIL import Image
from .Jwidget import JDMWidget
from .Jlabel import JDMLabel
from .Jlogger import JDMLogger
from kivy.utils import get_color_from_hex as GetColor
from kivy.graphics import Rectangle, Color

def JDM_png_to_pdf(text: str, name: str):
    im = Image.open(text)
    im_ = im.convert('RGB')
    im_.save(f"{name}.pdf", save_all=True)
    im.close()

def JDM_getColor(string: str) -> str:
    with open(os.path.split(__file__)[0]+"/all_color.json", 'r') as f:
        main : dict = json.load(f)
        color : str = main.get(string.title())
    if not color:
        stri = '\n --> '.join(list(main.keys()))
        JDMLogger.warning(f"Color name {string.title()} is not found.\nAll color available:\n --> {stri}")
        return "#ffffff"
    return color

def JDM_png_to_pdf_list(text_list: list[str], name: str):
    im = Image.open(text)
    im_ = im.convert('RGB')
    all_list = list()
    for text in text_list[1:]:
        with Image.open(text) as f:
            all_list.append(f.convert('RGB'))
    im_.save(f"{name}.pdf", save_all=True, append_images=all_list)
    im.close()

def JDM_addTitle(widget: JDMWidget, text: str, height: float,
             background_color: str, foreground_color: str, font_size: int or str):
    widget._main_title = JDMLabel(text=text, font_size=font_size, color=GetColor(foreground_color),
                                  size=(widget.width, height), pos=(widget.x, widget.top-height))
    with widget.canvas:
        widget._main_title_color = Color(rgba=GetColor(background_color))
        widget._main_title_rect = Rectangle(size=(widget.width, height), pos=(widget.y, widget.top-height))
    widget.add_widget(widget._main_title)

class MathMMW:
    
    @staticmethod
    def get_mean(number_list: list) -> float:
        return sum(number_list) / len(number_list)

    @staticmethod
    def get_median(number_list: list) -> float:
        number_list.sort()
        length = len(number_list)
        if length % 2: return number_list[length // 2]
        else: return (number_list[length // 2 - 1] + number_list[length // 2]) / 2

    @staticmethod
    def get_mode(number_list: list) -> set:
        number_list.sort()
        new_list = list()
        for i in range(len(number_list)): new_list.append(number_list.count(number_list[i]))
        mode_dict = dict(zip(number_list, new_list))
        return set(k for (k, v) in mode_dict.items() if v == max(new_list) )

    @staticmethod
    def get_range(number_list: list) -> float:
        number_list.sort()
        return number_list[len(number_list)-1] - number_list[0]

    @staticmethod
    def get_deviation(number_list) -> list:
        mean = MathMMW.get_mean(number_list)
        return sum([((i - mean) * (i - mean)) for i in number_list])

    @staticmethod
    def get_variance(number_list) -> float:
        return MathMMW.get_deviation(number_list) / (len(number_list) - 1)

    @staticmethod
    def get_sdeviation(number_list) -> float:
        return math.sqrt(MathMMW.get_variance(number_list))