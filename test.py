# from jdm_kivy import *
from src.jdm_kivy import *

class MainScreen(JDMScreen): ...
class MainWidget(JDMWidget):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

if __name__ == "__main__":
    JDMApp(size=(700, 700)).run("main", MainScreen(), MainWidget())
