""" docstrings """

from packages.controllers.welcome import WelcomeController
from packages.controllers.menu import MenuController


class HomeMenu:
    def __init__(self):
        pass

    def welcome(self):
        welcome = WelcomeController()
        welcome()

    def __call__(self):
        menu = MenuController(tour_info=None)
        menu()
