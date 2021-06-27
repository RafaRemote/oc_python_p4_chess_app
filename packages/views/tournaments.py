"""  docstrings """

import os
import time

from termcolor import colored
from rich.console import Console
from rich.table import Table


class TournamentsView:
    def __init__(self, tournaments_list, menu):      
        self.tournaments_list = tournaments_list
        self.menu = menu
        self.choice = None

    def adjust_self_menu(self):
        counter = 0
        for i in self.tournaments_list:
            if 'Manage tournament: ' + i.tour_title not in self.menu:
                self.menu.insert(counter + 1, 'Manage tournament: ' + i.tour_title)
                counter += 1 


    def print_tournaments_list(self):
        console = Console()
        table = Table(title=colored('TOURNAMENTS', 'magenta'), show_header=True, header_style="bold blue")
        table.add_column('Number', justify="center")
        table.add_column('Title')
        counter = 0
        for i in self.tournaments_list:
            table.add_row(str(counter + 1), i.tour_title)
            counter += 1
        console.print(table)
        self.print_menu()

    def print_menu(self):
        console = Console()
        table = Table(title=colored('OPTIONS', 'blue'), show_header=True, header_style="bold blue")
        table.add_column('Choice', justify="center")
        table.add_column('Option')
        counter = -1
        for i in self.menu:
            table.add_row(str(counter + 1), i)
            counter += 1
        console.print(table)
        self.check_choice()

    def check_choice(self):
        i = 0
        while i < 1:
            print()
            choice = input('your choice ?: ')
            if choice.isnumeric() and int(choice) in range(0, len(self.menu)):
                i += 1
                self.choice = choice
            else:
                print("[red]"+"you need to choose between 0 and", len(self.menu)-1)

    def __call__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.adjust_self_menu()
        self.print_tournaments_list()
        return self.choice
