""" Match view """

import os

from termcolor import colored
from rich.console import Console
from rich.table import Table
from rich import print


class MatchView:
    """
    Class to represent a view for match details
    ...

    Attributes
    ----------
    rounds: list
        list of MatchModel instances

    Methods
    -------
    print_matches(self):
        print matches details
        no return
    """

    def __init__(self, rounds):
        """
        Constructs attributes for Error object.

        Parameters
        ----------
        ronuds: list
            list of MatchModel instances

        """

        self.rounds = rounds

    def print_matches(self):
        """
        prints table with matches details

        Parameters
        ----------
        none

        Returns
        -------
        no return
        """

        os.system('cls' if os.name == 'nt' else 'clear')
        console = Console()
        table = Table(title=colored('MATCHES', 'magenta'), show_header=True, header_style="bold blue")
        table.add_column('Round')
        table.add_column('Player 1')
        table.add_column('Score Player 1')
        table.add_column('Score Player 2')
        table.add_column('Player 2')
        for round in self.rounds:
            for match in round.matches:
                if match.player1[1] == 0.0 and match.player2[1] == 0.0:
                    table.add_row("[orange1]"+str(round.number),
                                  "[orange1]"+match.player1[0].surname,
                                  "[orange1]"+str(match.player1[1]),
                                  "[orange1]"+str(match.player2[1]),
                                  "[orange1]"+match.player2[0].surname,
                                  )
                elif round.number == 2 or round.number == 4:
                    table.add_row("[yellow]"+str(round.number),
                                  "[yellow]"+match.player1[0].surname,
                                  "[yellow]"+str(match.player1[1]),
                                  "[yellow]"+str(match.player2[1]),
                                  "[yellow]"+match.player2[0].surname,
                                  )
                else:
                    table.add_row("[green]"+str(round.number),
                                  "[green]"+match.player1[0].surname,
                                  "[green]"+str(match.player1[1]),
                                  "[green]"+str(match.player2[1]),
                                  "[green]"+match.player2[0].surname,
                                  )
        console.print(table)
        self.print_color_meanings()

    def print_color_meanings(self):
        """ prints a table for the meaning of the colors """

        console = Console()
        table = Table(title='Meaning of Colors')
        table.add_column('Yellow', header_style='bold yellow', style='yellow')
        table.add_column('Green', header_style='bold green', style='green')
        table.add_column('Orange', header_style='bold orange1', style='orange1')
        table.add_row('round finished', 'round finished', 'round not finished')
        console.print(table)

    def __call__(self):
        """ calls self.print_matches(), prints input, returns nothing """

        self.print_matches()
        print()
        input(colored('press return to go back to the main menu', 'blue'))
