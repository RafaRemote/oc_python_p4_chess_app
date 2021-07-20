""" display menus """

import os

from termcolor import colored
from rich.console import Console
from rich.table import Table


class MenuView:
    def __init__(self, menu):
        self.menu = menu
        self.choice = None

    def check_choice(self):
        i = 0
        while i < 1:
            print()
            choice = input('your choice ?: ')
            if choice.isnumeric() and int(choice) in range(0, len(self.menu)):
                i += 1
                return choice
            else:
                print(colored("you need to choose between 0 and " + str(len(self.menu)-1), "red"))

    def __call__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        console = Console()
        table = Table(title=colored('MENU', 'magenta'), show_header=True, header_style="bold blue")
        table.add_column('choice', justify="center")
        table.add_column('option')
        counter = -1
        for i in self.menu:
            table.add_row(str(counter + 1), i)
            counter += 1
        console.print(table)
        self.choice = self.check_choice()
        return self
