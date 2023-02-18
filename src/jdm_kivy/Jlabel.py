from kivy.app import App
from kivy.uix.label import Label

class JDMLabel(Label):
    
    def __init__(self, **kwargs):
        self.font_name = "consolas"
        self.bind(size=self.setter('text_size'))
        self.valign = 'center'
        self.halign = 'center'
        super().__init__(**kwargs)
        self.root = App.get_running_app().root
