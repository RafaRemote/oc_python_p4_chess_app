''' utils when error encountered '''

from termcolor import colored


class Error:
    def __init__(self, message):
        self.name = message[1]
        self.message = message[2]
    

    def __call__(self):
        print()
        print(colored('*** ' + self.message.upper() + ' ***', 'magenta'))
        continue_or_quit = input('do you want to try again ? y/n: ')
        return [self.name, continue_or_quit]
