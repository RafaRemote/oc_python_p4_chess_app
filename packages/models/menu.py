""" model for the menus"""
import time
from pyfiglet 

welcome_message = 'WELCOME TO YOUR CHESS TOURNAMENT MANAGER'

# only lowercase characters
list_of_menus = [
                    'home',
]


home = [
            'create new tournament',
            'add players',
            'enter results',
            'show tournament ranking'
]

class Welcome:
    def __init__(self):
        self.title = welcome_message

    def __call__(self):
        print(list(welcome_message))

class MenuModel:
    def __init__(self, name):
        self.name = name


    def __call__(self):
        
        if self.name.lower() in list_of_menus:
            for i in home:
                print(i)


            