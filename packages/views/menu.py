""" docstrings """

import os

from termcolor import colored


class MenuView:
    def __init__(self, name, choice_list, choice):
        self.name = name
        self.choice = choice
        self.choice_list = choice_list
        self.choice_string = None

    def check_choice(self):
        i=0
        while i < 1 :
            choice = input(' question ?')
            if choice.isnumeric() and int(choice) in range(1, len(self.choice_list)+1):
                i += 1
                return choice
            else:
                print(colored('you need to choose between 1 and', 'red'), len(self.choice_list))


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
        i = 0
        self.choice = self.check_choice()
        return self
