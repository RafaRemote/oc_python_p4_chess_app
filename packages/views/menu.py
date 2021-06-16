import os

from termcolor import colored


class MenuView:
    def __init__(self, name, choice_list, choice):
        self.name = name
        self.choice = choice
        self.choice_list = choice_list

    def __call__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('      ', colored(self.name.upper(), 'magenta'))
        print()
        print()
        counter = 0
        for i in self.choice_list:
            print(counter + 1, ' -> ', i)
            counter += 1
        print()
        self.choice = input('your choice: ')
        return self.choice
