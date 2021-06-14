''' utils when error encountered '''
import os

from termcolor import colored


class Error:
    """ expect a string 
    
    expected message: ['error', self.__class__.__name__, string]
    returns the name of the class from where comes the error and y or n to continue or quit
    """
    def __init__(self, message):
        self.name = message[1]
        self.message = message[2]
    

    def __call__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print()
        print(colored('*** ' + self.message.upper() + ' ***', 'red'))
        print()
        continue_or_quit = input('do you want to try again ? y/n: ')
        return [self.name, continue_or_quit]
