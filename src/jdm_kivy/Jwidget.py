from kivy.app import App
from kivy.uix.widget import Widget

class JDMWidget(Widget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.root = App.get_running_app().root


