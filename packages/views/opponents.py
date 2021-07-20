""" display a of opponents for each player """

import os

from termcolor import colored
from rich.console import Console
from rich.table import Table

from packages.views.error import Error


class OpponentsView:
    def __init__(self, tour_info):
        self.tour_info = tour_info

    def show_opponents(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for played in self.tour_info.__dict__['players']:
            if len(played.opponents) < 4:
                error = Error('you can only check the opponents list at the end ot the tournmaent')
                error()
                input(colored("press return to continue", "blue"))
                return
            else:
                console = Console()
                table = Table(title='Opponents', show_header=True, header_style='bold magenta')
                table.add_column("Player")
                table.add_column("Opponent 1")
                table.add_column("Opponent 2")
                table.add_column("Opponent 3")
                table.add_column("Opponent 4")
                for player in self.tour_info.__dict__['players']:
                    table.add_row(player.surname,
                                  player.opponents[0].surname,
                                  player.opponents[1].surname,
                                  player.opponents[2].surname,
                                  player.opponents[3].surname
                                  )
                console.print(table)
                input(colored("press return to continue", "blue"))
                return

    def __call__(self):
        self.show_opponents()
