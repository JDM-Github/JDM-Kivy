from kivy.uix.image import Image
from kivy.app import App

class JDMImage(Image):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.root = App.get_running_app().root
