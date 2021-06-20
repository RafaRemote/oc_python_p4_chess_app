""" docstrings """

from packages.models.welcome import WelcomeModel
from packages.views.welcome import WelcomeView


class WelcomeController:
    def __init__(self):
        pass

    def __call__(self):
        welcome = WelcomeModel()
        message = welcome.message
        sub_title = welcome.sub_title
        welcomeview = WelcomeView(message, sub_title)
        welcomeview()
