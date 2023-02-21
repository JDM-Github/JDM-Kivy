import os
import json

with open(f"{os.path.split(__file__)[0]}/config.json") as f:
    config = json.load(f)
    if not config.get('display_kivy_logs'):
        os.environ["KIVY_NO_CONSOLELOG"] = "1"
        os.system('cls')

from kivy import platform
from math import floor, ceil
from .Jwindow import JDMApp, Window, platform, Clock, JDMRootManager, BooleanProperty, ReferenceListProperty
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, ListProperty
from kivy.graphics import Line, Rectangle, RoundedRectangle, Color, Ellipse, Triangle
from kivy.utils import get_color_from_hex as GetColor, get_hex_from_color as GetHex, get_random_color as GetRandom
from kivy.metrics import sp, dp
from .Jwidget import JDMWidget
from .Jscreen import JDMScreen
from .Jconfig import JDMConfig
from .Jlabel import JDMLabel
from .Jimage import JDMImage
from .Jfunctions import JDM_png_to_pdf, JDM_png_to_pdf_list, JDM_addTitle, MathMMW, JDM_getColor
