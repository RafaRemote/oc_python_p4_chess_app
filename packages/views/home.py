""" docstrings """

from packages.controllers.welcome import WelcomeController
from packages.controllers.menu import MenuController


class HomeMenu:
    def __init__(self):
        self.name = self.__class__.__name__

    def welcome(self):
        welcome = WelcomeController()
        welcome()

    def __call__(self):
        menu = MenuController(tour_info=None,
                              name=self.name,
                              choice=None)
        menu()
