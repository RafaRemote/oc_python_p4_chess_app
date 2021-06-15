from packages.controllers.menu import MenuController
from packages.controllers.welcome import WelcomeController


class StartMenu:
    def __init__(self):
        self.name = 'StartMenu'

    def welcome(self):
        welcome = WelcomeController()
        welcome()

    def __call__(self):        
        menu = MenuController(name=self.name, choice=None)
        menu()    
