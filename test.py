from jdm_kivy import *

class NewScreen(JDMScreen):
    
    def __init__(self, **kw):
        super().__init__(**kw)

class MainWidget(JDMWidget):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

if __name__ == "__main__":
    JDMConfig.deactivate_root_clock()
    JDMApp(size=(700, 700)).run("first", widget=MainWidget(), screen=NewScreen())
