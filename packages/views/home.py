from packages.controllers.menu import MenuController, WelcomeController

class HomeMenu:
    def __init__(self):
        self.name = self.__class__.__name__

    def __call__(self):
        # welcome = WelcomeController()
        # welcome()
        menu = MenuController(self.name, choice=None)
        menu()
        choice = Choice()
        choice()

class Choice:
    def __init__(self):
        self.name = self.__class__.__name__
    
    def __call__(self):
        choice = input('your choice: ')
        chosen_option = MenuController(self.name, choice)
        chosen_option()


