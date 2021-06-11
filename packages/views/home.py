from packages.controllers.menu import MenuController

class Home:
    def __init__(self):
        self.name = self.__class__.__name__

    def __call__(self):
        menu = MenuController(self.name)
        menu()
