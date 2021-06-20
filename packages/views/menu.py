""" docstrings """

import os

from termcolor import colored
from rich.console import Console
from rich.table import Table


class MenuView:
    def __init__(self, name, choice_list, choice):
        self.name = name
        self.choice = choice
        self.choice_list = choice_list
        self.choice_string = None

    def check_choice(self):
        i = 0
        while i < 1:
            print()
            choice = input('your choice ?: ')
            if choice.isnumeric() and int(choice) in range(0, len(self.choice_list)):
                i += 1
                return choice
            else:
                print(colored('you need to choose between 0 and', 'red'), len(self.choice_list)-1)

    def __call__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        console = Console()
        if self.name is not None:
            table = Table(title=colored(self.name.upper(), 'magenta'), show_header=True, header_style="bold blue")
        else:
            table = Table(show_header=True, header_style="bold blue")
        table.add_column('choice', justify="center")
        table.add_column('option')
        counter = -1
        for i in self.choice_list:
            table.add_row(str(counter + 1), i)
            counter += 1
        console.print(table)
        i = 0
        self.choice = self.check_choice()
        return self
