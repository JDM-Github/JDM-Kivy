import os
import json
from kivy.core.window import Window
from kivy.app import App, platform
from kivy.clock import Clock
from kivy.properties import StringProperty, BooleanProperty, NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.uix.screenmanager import ScreenManager, TransitionBase, SlideTransition

from .Jwidget import JDMWidget
from .Jscreen import JDMScreen

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
        with open(f"{os.path.split(__file__)[0]}/config.json") as f:
           self.config = json.load(f)
        if self.config.get("root_clock"):
            self._main_Clock = Clock.schedule_interval(self.update, 1/60)
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

    def change_screen(self, name: str, transition: TransitionBase = SlideTransition(direction='left')):
        self.prev_screen = self.current
        self.prev_screen_widget = self.current_screen
        self.transition = transition
        self.current = name

    def add_screen(self, screen_name: str, screen: JDMScreen = None, widget: JDMWidget = None):
        if not screen: screen = JDMScreen(name=screen_name)
        if not widget: widget = JDMWidget()
        setattr(self, screen_name, screen)
        screen = getattr(self, screen_name)
        screen.add_widget(widget)
        self.add_widget(screen)

class JDMApp(App):

    def __init__(self, title: str = None, size: list = (500, 500), manager: JDMRootManager=None, **kwargs):
        super().__init__(**kwargs)
        self.root: JDMRootManager = manager if manager else JDMRootManager()
        self.title = title
        if not platform == "android":
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

    def on_stop(self): super().on_stop()

    def run(self, screen_name: str, screen: JDMScreen = None, widget: JDMWidget = None):
        self.__first_screen = screen
        self.__first_screen_name = screen_name
        self.__first_widget = widget
        return super().run()

    def build(self):
        self.root.add_screen(
            self.__first_screen_name,
            self.__first_screen,
            self.__first_widget)
        return self.root
