from packages.controllers.menu import MenuController
from packages.controllers.welcome import WelcomeController


class HomeMenu:
    def __init__(self):
        self.name = self.__class__.__name__

    def welcome(self):
        welcome = WelcomeController()
        welcome()

    def __call__(self):        
        menu = MenuController(self.name, choice=None)
        menu()    

   

