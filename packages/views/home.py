from packages.controllers.menu import MenuController
from packages.controllers.welcome import WelcomeController


class HomeMenu:
    def __init__(self):
        self.name = 'HomeMenu'

    def welcome(self):
        welcome = WelcomeController()
        welcome()

    def __call__(self):        
        menu = MenuController(self.name, choice=None)
        menu()    

