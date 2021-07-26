""" Opponents view """

import os

from termcolor import colored
from rich.console import Console
from rich.table import Table


class OpponentsView:
    """
    Class to represent a view of player opponents
    ...

    Attributes
    ----------
    players: list
        list [<PlayerModel instance>, []]
        list[1] is a list of strings: surnames of the opponents

    Methods
    -------
    show_opponents(self):
        print a table
        returns nothing
    call(self):
        calls self.show_opponents()

    """

    def __init__(self, players):
        """
        Constructs attributes for OpponentsView instance.

        Parameters
        ----------
        players: list
            list [<PlayerModel instance>, []]
            list[1] is a list of strings: surnames of the opponents

        """

        self.players = players

    def show_opponents(self):
        """ prints table with self.players, no return """

        os.system('cls' if os.name == 'nt' else 'clear')
        console = Console()
        table = Table(title='Opponents', show_header=True, header_style='bold magenta')
        table.add_column("Player")
        table.add_column("Opponent 1")
        table.add_column("Opponent 2")
        table.add_column("Opponent 3")
        table.add_column("Opponent 4")
        for player in self.players:
            if len(player[1]) == 0:
                table.add_row("[green]"+player[0].surname)
            elif len(player[1]) == 1:
                table.add_row("[green]"+player[0].surname,
                              player[1][0])
            elif len(player[1]) == 2:
                table.add_row("[green]"+player[0].surname,
                              player[1][0],
                              player[1][1])
            elif len(player[1]) == 3:
                table.add_row("[green]"+player[0].surname,
                              player[1][0],
                              player[1][1],
                              player[1][2])
            elif len(player[1]) == 4:
                table.add_row("[green]"+player[0].surname,
                              player[1][0],
                              player[1][1],
                              player[1][2],
                              player[1][3])
        console.print(table)
        input(colored("press return to continue", "blue"))

    def __call__(self):
        """ calls self.show_opponents() """

        self.show_opponents()
