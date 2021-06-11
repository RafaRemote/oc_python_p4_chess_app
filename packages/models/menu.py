""" model for the menus"""
from utils.display_welcome import display_welcome_message

class WelcomeModel:
    def __init__(self, message):
        self.title = message

    def __call__(self):
        display_welcome_message(self.title.lower())

class MenuModel:
    def __init__(self, one_list, choice):
        for i in one_list:
            self.__dict__[i] = i
        self.choice = choice

    def get_menu(self):
        return self.__dict__


            