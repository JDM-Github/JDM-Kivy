import os
import json
from kivy.core.window import Window
from kivy.app import App, platform
from kivy.clock import Clock
from kivy.properties import StringProperty, BooleanProperty, NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.uix.screenmanager import ScreenManager, TransitionBase, SlideTransition

from .Jwidget import JDMWidget
from .Jscreen import JDMScreen
from .Jlogger import JDMLogger

from kivy.core.text import LabelBase

path = f"{os.path.split(__file__)[0]}/assets/font"
LabelBase.register(
    name="consolas",
    fn_regular=f"{path}/consolas/consolas_regular.ttf",
    fn_bold=f"{path}/consolas/consolas_bold.ttf",
    fn_italic=f"{path}/consolas/consolas_italic.ttf",
    fn_bolditalic=f"{path}/consolas/consolas_italic_bold.ttf")

class JDMRootManager(ScreenManager):
    
    is_mouse_down = BooleanProperty(False)
    is_mouse_moving = BooleanProperty(False)

    mouse_button = StringProperty('')
    mouse_x = NumericProperty(0)
    mouse_y = NumericProperty(0)
    mouse_pos = ReferenceListProperty(mouse_x, mouse_y)
    
    prev_screen = StringProperty(None)
    prev_screen_widget = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.root = self
        self.size = Window.size
        self.elapseTime = None
        self.current_screen : JDMScreen
        self.__private_variable()
        with open(f"{os.path.split(__file__)[0]}/config.json") as f: self.__config = json.load(f)
        if self.__config.get("root_clock"): self._main_Clock = Clock.schedule_interval(self.update, 1/60)
        Window.bind(on_keyboard=self.hook_keyboard)

    def keyboard_down(self, window, scancode=None, key=None, keyAscii=None, *args):
        self.current_screen.keyboard_down(window, scancode, key, keyAscii, *args)

    def keyboard_up(self, window, scancode=None, key=None, keyAscii=None, *args):
        self.current_screen.keyboard_up(window, scancode, key, keyAscii, *args)

    def mouse_down(self, window, x, y, button, modifiers):
        self.is_mouse_down  = True
        self.current_screen.mouse_down(window, x, y, button, modifiers)

    def mouse_move(self, window, x, y, button):
        self.is_mouse_moving = True
        self.current_screen.mouse_move(window, x, y, button)

    def mouse_up(self, window, x, y, button, modifiers):
        self.is_mouse_down = False
        self.is_mouse_moving = False
        self.current_screen.mouse_up(window, x, y, button, modifiers)

    def _mouse_pos(self, window, pos):
        self.mouse_x, self.mouse_y = pos

    def hook_keyboard(self, _, key, *__):
        code = Window._keyboards.get("system").keycode_to_string(key)
        if code == 'escape':
            return self.current_screen.handleBackButton()
        return True

    def update(self, dt: float):
        self.elapseTime = dt

        if self.__config.get("display_fps"):
            if JDMApp.get_running_app(): JDMApp.get_running_app().title = (
                JDMApp.get_running_app()._main_title + f" -> FPS: {(1 / self.elapseTime):.2f}")
    
    def __private_variable(self):
        self.__adding_screen = False

    def add_widget(self, widget, *args, **kwargs):
        if self.__adding_screen: return super().add_widget(widget, *args, **kwargs)
        else: JDMLogger.warning("'function'(add_widget) could not be used to add a screen; instead, use 'function'(add_screen)")

    def change_screen(self, name: str, transition: TransitionBase = SlideTransition(direction='left')):
        if name not in self._get_screen_names(): self.add_screen(name)
        self.prev_screen = self.current
        self.prev_screen_widget = self.current_screen
        self.transition = transition
        self.current = name

    def add_screen(self, screen_name: str, screen: JDMScreen = None, widget: JDMWidget = None):
        if not screen: screen = JDMScreen(name=screen_name)
        if not widget: widget = JDMWidget()
        if not hasattr(self, screen_name):
            self.__adding_screen = True
            setattr(self, screen_name, screen)
            screen = getattr(self, screen_name)
            if not screen.name: screen.name = screen_name
            screen.add_widget(widget)
            self.add_widget(screen)
            self.__adding_screen = False
        else:  JDMLogger.warning("'class'(JDMScreen) cannot be added because the 'attributes'(screen_name) have already been defined.")

class JDMApp(App):

    def __init__(self, title: str = None, size: list = (500, 500), manager: JDMRootManager=None, **kwargs):
        super().__init__(**kwargs)
        self.root: JDMRootManager = manager if manager else JDMRootManager()
        self.title = title if title else __class__.__name__.removesuffix('App')
        self._main_title = self.title
        if not platform == 'android':
            Window.size = size
            Window.left = 1
            Window.top = 30

    def on_start(self):
        Window.bind(on_key_down=self.root.keyboard_down)
        Window.bind(on_key_up=self.root.keyboard_up)
        Window.bind(on_mouse_down=self.root.mouse_down)
        Window.bind(on_mouse_move=self.root.mouse_move)
        Window.bind(on_mouse_up=self.root.mouse_up)
        Window.bind(mouse_pos=self.root._mouse_pos)
        return super().on_start()

    def run(self, screen_name: str = "main", screen: JDMScreen = None, widget: JDMWidget = None):
        self.__first_screen = screen
        self.__first_screen_name = screen_name
        self.__first_widget = widget
        return super().run()

    def build(self):
        self.root.add_screen(
            self.__first_screen_name,
            self.__first_screen,
            self.__first_widget)
        JDMLogger.log_start_app(f"{self.title} is running")
        return self.root
