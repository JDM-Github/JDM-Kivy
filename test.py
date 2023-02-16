from jdm_kivy import *

class MainScreen(JDMScreen): ...
class MainWidget(JDMWidget): ...

if __name__ == "__main__":
    JDMApp(size=(500, 500)).run("main", MainScreen(), MainWidget())
