from src.jdm_kivy import *

class MainWidget(JDMWidget): ...
class MainScreen(JDMScreen): ...

if __name__ == "__main__":
    JDMApp().run(screen_name="main", screen=MainScreen(), widget=MainWidget())
