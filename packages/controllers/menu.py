""" controller returning a view for the menus """

from packages.models.menu import MenuModel, WelcomeModel

from packages.views.display_menu import display_menu


welcome_message = 'Welcome to your chess tournament manager!'

menus = {
        "HomeMenu" : [
            'create new tournament',
            'add players',
            'enter results',
            'show tournament ranking'
        ]
}

list_of_menus =  [
            'HomeMenu',
]

class WelcomeController:
    def __init__(self):
        pass
    
    def __call__(self):
        welcome = WelcomeModel(welcome_message)
        welcome()

class MenuController:
    def __init__(self, name, choice):
        self.name = name
        self.choice = choice
  
    def __call__(self):
        if self.name in menus:
            display_menu(MenuModel(menus[self.name], self.choice).get_menu())




        



