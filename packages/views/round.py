""" display the details about the rounds """

import os

from termcolor import colored
from rich.console import Console
from rich.table import Table


class RoundView:
    def __init__(self, rounds):
        self.rounds = rounds

    def __call__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        console = Console()
        table = Table(title=colored('ROUNDS DETAILS', 'magenta'), show_header=True, header_style="bold magenta")
        table.add_column('Rounds', style="magenta")
        table.add_column('Start Date')
        table.add_column('End Date')
        for i in self.rounds:
            if i.start_date is None:
                i.start_date = 'not yet'
            if i.end_date is None:
                i.end_date = 'not yet'
            table.add_row("Round"+str(i.number), i.start_date, i.end_date)
        console.print(table)
        print()
        input(colored('press return to go back to the main menu', 'blue'))
        return
