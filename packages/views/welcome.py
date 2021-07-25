""" Welcome view """

import os

from pyfiglet import Figlet
from rich.console import Console
from rich.table import Table
from rich import print
from termcolor import colored


class WelcomeView:
    """
    Class to represent a Welcome view
    ...

    Attributes
    ----------
    message: string
        message to be displayed as the title
    sub_title : string
        message to be displayed as the sub_title

    Methods
    -------
    clean_message(message, title)
        modify strings
        prints the main message and the sub_title in a table
    """

    def __init__(self, title, sub_title):
        """
        Constructs attributes for WelcomeView object.

        Parameters
        ----------
        title: string
            message to be displayed as the title
        sub_title : string
            message to be displayed as the sub_title
        """

        self.title = title
        self.sub_title = sub_title

    def clean_message(self, title):
        """
        prints table

        Parameters
        ----------
        title: str
            string to be printed as the title

        Returns
        -------
        no return
        """

        os.system('cls' if os.name == 'nt' else 'clear')
        console = Console()
        table = Table(show_header=True, header_style="bold orange1")
        f = Figlet(font='bubble')
        table.add_column(f.renderText(title.strip(' ').upper()),
                         justify="center")
        table.add_row(self.sub_title)
        console.print(table)
        print('')
        input(colored('press return to go to the main menu.', 'blue'))

    def __call__(self):
        """
        calls self.clean_message(self.title)

        Parameters
        ----------
        none

        Returns
        -------
        no return
        """

        self.clean_message(self.title)
