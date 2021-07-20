""" display a of opponents for each player """

import os

from termcolor import colored
from rich.console import Console
from rich.table import Table


class OpponentsView:
    def __init__(self, players):
        self.players = self.select_opponents(players)

    def select_opponents(self, players):
        selection = list()
        for count in range(1, 5):
            selection.append(players[-count])
        return selection

    def show_opponents(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        console = Console()
        table = Table(title='Opponents', show_header=True, header_style='bold magenta')
        table.add_column("Player")
        table.add_column("Opponent 1")
        table.add_column("Opponent 2")
        table.add_column("Opponent 3")
        table.add_column("Opponent 4")
        for player in self.players:
            if len(player.opponents) == 0:
                table.add_row(player.surname)
            elif len(player.opponents) == 1:
                table.add_row(player.suname,
                              player.opponents[0])
            elif len(player.opponents) == 2:
                table.add_row(player.surname,
                              player.opponents[0],
                              player.opponents[1])
            elif len(player.opponents) == 3:
                table.add_row(player.surname,
                              player.opponents[0],
                              player.opponents[1],
                              player.opponents[2])
            elif len(player.opponents) == 4:
                table.add_row(player.surname,
                              player.opponents[0],
                              player.opponents[1],
                              player.opponents[2],
                              player.opponents[3])
        console.print(table)
        input(colored("press return to continue", "blue"))
        return

    def __call__(self):
        self.show_opponents()
