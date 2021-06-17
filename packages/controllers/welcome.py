""" docstrings """

from packages.models.welcome import WelcomeModel
from packages.views.welcome import WelcomeView


class WelcomeController:
    def __init__(self):
        pass

    def __call__(self):
        welcome = WelcomeModel()
        res = welcome().__dict__.get('message')
        welcomeview = WelcomeView(res)
        welcomeview()
