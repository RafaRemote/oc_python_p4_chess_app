import os

from termcolor import colored


class MenuView:
    def __init__(self, name, options):
        self.name = name
        self.options = options
        self.choice = None

    def __call__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('   ', colored(self.name.upper(), 'magenta'))
        print()
        print()
        counter = 0
        for i in self.options:
            print(counter + 1, ' -> ', i)
            counter += 1
        print()
        self.choice = input('your choice: ')
        return self
