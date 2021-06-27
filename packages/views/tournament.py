"""  docstrings """

import os

from termcolor import colored
from rich.console import Console
from rich.table import Table
from rich import print


class TournamentView:
    def __init__(self, tour_info, menu):
        self.tour_info = tour_info
        self.menu = menu
        self.choice = None

    def print_tournament_details(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        console = Console()
        table = Table(title=colored(self.tour_info.tour_title + ' CHESS TOURNAMENT', 'magenta'),
                      show_header=True,
                      header_style="bold magenta"
                      )
        table.add_column('Denomination')
        table.add_column('Value', style="cyan")
        table.add_row("Name", self.tour_info.tour_title)
        table.add_row("Place", self.tour_info.place)
        table.add_row("Start Date", self.tour_info.tour_start_date[:10])
        table.add_row("Time-Control", self.tour_info.tour_time_control)
        table.add_row("Description", self.tour_info.tour_description)
        table.add_row("Total Rounds", str(self.tour_info.total_rounds))
        table.add_row("Players", str(len(self.tour_info.players)))
        table.add_row("Matches per Round", str(len(self.tour_info.rounds[0].matches)))
        current_round = self.tour_info.rounds[-1]
        if len(self.tour_info.rounds) == 4 and self.tour_info.rounds[3].end_date is not None:
            table.add_row("Current round", "[red]"+"All rounds finished")
        else:
            table.add_row("Current round", "[red]"+str(current_round.number))
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
                print(colored('you need to choose between 0 and', 'red'), len(self.menu)-1)

    def __call__(self):
        self.print_tournament_details()
        return self.choice
