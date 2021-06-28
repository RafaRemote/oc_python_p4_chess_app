""" display a welcome message """

import os

from pyfiglet import Figlet
from rich.console import Console
from rich.table import Table
from rich import print
from termcolor import colored


class WelcomeView:
    """
    A class used to display a message in a table
    ...
    Attributes
    ----------
    message: string
        message to be displayed as the title
    sub_title : string
        message to be displayed as the sub_title

    Methods
    -------
    clean_sentence(message, sub_title)
        prints the main message and the sub_title in a table


    """
    def __init__(self, message, sub_title):
        self.message = message
        self.sub_title = sub_title

    def clean_message(self, message):
        """ returns a table with the sentences specified """

        os.system('cls' if os.name == 'nt' else 'clear')
        console = Console()
        table = Table(show_header=True, header_style="bold orange1")
        f = Figlet(font='bubble')
        table.add_column(f.renderText(message.strip(' ').upper()),
                         justify="center")
        table.add_row(self.sub_title)
        console.print(table)
        print('')
        input(colored('press return to go to the main menu.', 'blue'))

    def __call__(self):
        self.clean_message(self.message)
