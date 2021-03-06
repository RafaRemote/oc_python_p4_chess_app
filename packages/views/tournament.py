"""  Tournament view """

import os

from termcolor import colored
from rich.console import Console
from rich.table import Table
from rich import print


class TournamentView:
    """
    Class to represent a view for a tournament
    ...

    Attributes
    ----------
    tour_info: instance
        TournamentModel instance
    menu: list
        list of strings representing choices in a menu
    choice: int
        default set: none
        represents user input as choice in a menu

    Methods
    -------
    print_tournament_details(self):
        prints table
        no return
    print_menu(self):
        prints table
        no return
    check_choice(self):
        prints input for choice
        assigns int to self.choice
    call(self):
        calls print_tournament_details(self)
        return self.choice

    """

    def __init__(self, tour_info, menu):
        """
        Constructs attributes for TournamentView object.

        Parameters
        ----------
        tour_info: instance
            TournamentModel instance
        menu: list
            list of strings representing choices in a menu

        """

        self.tour_info = tour_info
        self.menu = menu
        self.choice = None

    def print_tournament_details(self):
        """ prints table, calls self.print_menu(), no return"""

        os.system('cls' if os.name == 'nt' else 'clear')
        console = Console()
        table = Table(title=colored(self.tour_info.title + ' CHESS TOURNAMENT', 'magenta'),
                      show_header=True,
                      header_style="bold magenta"
                      )
        table.add_column('Denomination')
        table.add_column('Value', style="cyan")
        table.add_row("Name", self.tour_info.title)
        table.add_row("Place", self.tour_info.place)
        table.add_row("Start Date", self.tour_info.start_date[:10])
        table.add_row("Time-Control", self.tour_info.time_control)
        table.add_row("Description", self.tour_info.description)
        table.add_row("Total Rounds", str(self.tour_info.total_rounds))
        table.add_row("Players", '8')
        table.add_row("Matches per Round", '4')
        current_round = ''
        if self.tour_info.rounds and len(self.tour_info.rounds) > 0:
            current_round = self.tour_info.rounds[-1]
            if len(self.tour_info.rounds) == 4 and self.tour_info.rounds[3].end_date != "":
                table.add_row("Current round", "[red]"+"All rounds finished")
            elif self.tour_info.rounds[-1].end_date != "":
                table.add_row("[red]"+"Current Round", "[red]"+str(current_round.number), "[red]"+"finished")
            else:
                table.add_row("Current round", "[red]"+str(current_round.number))
        else:
            table.add_row("Current round", "[red]"+"No round started yet")
        console.print(table)
        self.print_menu()

    def print_menu(self):
        """ prints table with self.menu, calls self.check_choice(), no return """

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
        """ prints input, checks if input is in a range, assigns a value (string) to self.choice """

        i = 0
        while i < 1:
            print()
            choice = input('your choice ?: ')
            if choice.isnumeric() and int(choice) in range(0, len(self.menu)):
                i += 1
                self.choice = choice
            else:
                print("[red]""you need to choose between 0 and " + str(len(self.menu)-1))

    def __call__(self):
        """ calls self.print_tournament_details(), returns self.choice """

        self.print_tournament_details()
        return self.choice
