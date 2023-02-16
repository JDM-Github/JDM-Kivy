from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.core.window import Window

class JDMScreen(Screen):
    
    def __init__(self, **kw):
        super().__init__(**kw)
        self.root = App.get_running_app().root
        self.size = Window.size

    def handleBackButton(self) -> bool: return True
    def keyboard_down(self, window, scancode=None, key=None, keyAscii=None, *args): ...
    def keyboard_up(self, window, scancode=None, key=None, keyAscii=None, *args): ...
    def mouse_down(self, window, x, y, button, modifiers): ...
    def mouse_move(self, window, x, y, button): ...
    def mouse_up(self, window, x, y, button, modifiers): ...
