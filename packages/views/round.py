""" display the details about the players """

import os

from termcolor import colored
from pyfiglet import Figlet
from rich.console import Console
from rich.table import Table


class RankingView:
    def __init__(self, players_info):
        self.info = players_info

    def __call__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        f = Figlet(font='digital')
        print(colored(f.renderText('RANKING'), 'magenta'))
        console = Console()
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Name", style="dim", width=12)
        table.add_column("Surname")
        table.add_column("Year of Birth", justify="center")
        table.add_column("Gender", justify="center")
        table.add_column("Elo", justify="center")
        table.add_column("Score", justify="center")
        for i in self.info:
            table.add_row(str(i.name),
                          str(i.surname),
                          str(i.year_birth),
                          str(i.gender),
                          str(i.elo),
                          str(i.score)
                          )
        console.print(table)
        print('\n' * 2)
        i = 0
        while i < 1:
            back_home = input('Type \'y\' to come back to the menu.')
            if back_home == 'y':
                return 'y'
            else:
                print(colored('You did not type the good key. Type \'y\' to go back to the menu',
                              'red'))
