""" Round view"""

import os

from termcolor import colored
from rich.console import Console
from rich.table import Table


class RoundView:
    """
    Class to represent a view for the rounds
    ...

    Attributes
    ----------
    rounds: list
        list of RoundModel instances

    Methods
    -------
    call(self):
        prints table
        no return
    """

    def __init__(self, tour):
        """
        Constructs attributes for RoundView object.

        Parameters
        ----------
        tour: instance
            instance of TournamentModel

        """

        self.rounds = tour.rounds

    def __call__(self):
        """ prints table with self.rounds , returns nothing """

        os.system('cls' if os.name == 'nt' else 'clear')
        console = Console()
        table = Table(title=colored('ROUNDS DETAILS', 'magenta'), show_header=True, header_style="bold magenta")
        table.add_column('Rounds', style="magenta")
        table.add_column('Start Date')
        table.add_column('End Date')
        for i in self.rounds:
            table.add_row("Round"+str(i.number), i.start_date, i.end_date)
        console.print(table)
        print()
        input(colored('press return to go back to the main menu', 'blue'))
