"""  Tournaments view """

import os

from termcolor import colored
from rich.console import Console
from rich.table import Table


class TournamentsView:
    """
    Class to represent a tournaments view page
    ...

    Attributes
    ----------
    tournaments_list: list
        list of TournamentModel instances
    menu: list
        list of strings representing choices in a menu
    choice: int
        default set: none
        int representing user input as choice in a menu

    Methods
    -------
    print_tournaments_list(self):
        prints table
        returns nothing
    print_menu(self):
        prints table
        returns nothing
    check_choice(self):
        check user input
        assigns int to self.choice

    """

    def __init__(self, tournaments_list, menu):
        """
        Constructs attributes for TournamentsView object.

        Parameters
        ----------
        tournaments_list: list
            list of TournamentModel instances
        menu: list
            list of strings representing choices in a menu

        """

        self.tournaments_list = tournaments_list
        self.menu = menu
        self.choice = None

    def print_tournaments_list(self):
        """ prints table with self.tournaments_list, calls self.print(menu) """

        console = Console()
        table = Table(title=colored('CHOOSE THE TOURNAMENT YOU WANT TO MANAGE', 'magenta'),
                      show_header=True,
                      header_style="bold blue")
        table.add_column('Number', justify="center")
        table.add_column('Title')
        for i in self.tournaments_list:
            table.add_row(str(i.doc_id), i['title'])
        console.print(table)
        self.print_menu()

    def print_menu(self):
        """ prints table with self.tournaments_list, calls self.check_choice(), no return """

        console = Console()
        table = Table(title=colored('OPTIONS', 'blue'), show_header=True, header_style="bold blue")
        table.add_column('Choice', justify="center")
        table.add_column('Option')
        counter = len(self.tournaments_list)
        for i in self.menu:
            table.add_row(str(counter + 1), i)
            counter += 1
        console.print(table)
        self.check_choice()

    def check_choice(self):
        """ check user input, assign value (string) to self.choice, no return """

        correct_length = len(self.menu)+len(self.tournaments_list)
        i = 0
        while i < 1:
            print()
            choice = input('your choice ?: ')
            if choice.isnumeric() and int(choice) in range(0, correct_length+1):
                i += 1
                self.choice = choice
            else:
                print(colored("you need to choose between 0 and " + str(correct_length), "red"))

    def __call__(self):
        """ calls self.print_tournaments_list(), returns self.choice """

        os.system('cls' if os.name == 'nt' else 'clear')
        self.print_tournaments_list()
        return self.choice
