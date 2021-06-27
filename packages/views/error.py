""" docstrings """

import os

from termcolor import colored


class Error:
    """ expect a string

    Attributes
    ----------

    message: string to be printed
    

    Methods
    -------

    __call__: displays a message and returns nothing when return key is pressed on input
    """

    def __init__(self, message):
        self.message = message

    def __call__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print()
        print(colored('*** ' + self.message.upper() + ' ***', 'red'))
        print()
        input(colored('press return to continue', 'blue'))
        return
