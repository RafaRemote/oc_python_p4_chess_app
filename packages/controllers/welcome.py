from packages.models.welcome import WelcomeModel
from packages.views.utils.display_welcome import display_welcome_message


class WelcomeController:
    def __init__(self):
        pass

    def __call__(self):
        welcome = WelcomeModel()
        display_welcome_message(welcome())
