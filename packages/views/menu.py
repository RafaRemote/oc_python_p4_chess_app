""" docstrings """

import os

from termcolor import colored


class MenuView:
    def __init__(self, name, choice_list, choice):
        self.name = name
        self.choice = choice
        self.choice_list = choice_list
        self.choice_string = None

    def __call__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('  ', colored(self.name.upper(), 'magenta'))
        print()
        print()
        counter = 0
        for i in self.choice_list:
            print(counter + 1, ' -> ', i)
            counter += 1
        print()
        self.choice = input('your choice: ')
        if int(self.choice)  in range(1, len(self.choice_list)+1):
            self.choice_string = self.choice_list[int(self.choice)-1]
        return self
