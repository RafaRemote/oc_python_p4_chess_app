""" docstrings """

import os

from termcolor import colored


class Error:
    """ expect a string

    returns the name of the class from where comes the error and y or n to continue or quit
    """

    def __init__(self, message):
        self.message = message
        self.option = None

    def __call__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print()
        print(colored('*** ' + self.message.upper() + ' ***', 'red'))
        print()
        option = input('do you want to try again ? y/n: ')
        self.option = option.lower()
        return self
