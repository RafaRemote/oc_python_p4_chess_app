""" Menu view """

import os

from termcolor import colored
from rich.console import Console
from rich.table import Table


class MenuView:
    """
    Class for a menu view
    ...

    Attributes
    ----------
    menu: list
        list of strings representing choices in a menu
    choice: int
        default set: none
        when int assigned: represent user input for choice in a menu

    Methods
    -------
    check_choice(self):
        check if the choice (int) is whith a correct range
    call(self):
        print table with list in self.menu

    """

    def __init__(self, menu):
        """
        Constructs attributes for MenuView object.

        Parameters
        ----------
        menu: list
            list of stings representing the choices in a menu

        """

        self.menu = menu
        self.choice = None

    def check_choice(self):
        """
        check if the user input (int for choice) is in a range
        assigns value to self.choice

        Parameters
        ----------
        none

        Returns
        -------
        str: the user input

        """

        i = 0
        while i < 1:
            print()
            choice = input('your choice ?: ')
            if choice.isnumeric() and int(choice) in range(0, len(self.menu)):
                i += 1
                return choice
            else:
                print(colored("you need to choose between 0 and " + str(len(self.menu)-1), "red"))

    def __call__(self):
        """
        prints table with the strings in the list of self.menu

        Parameters
        ----------
        none

        Returns
        -------
        instance of MenuView

        """

        os.system('cls' if os.name == 'nt' else 'clear')
        console = Console()
        table = Table(title=colored('MENU', 'magenta'), show_header=True, header_style="bold blue")
        table.add_column('choice', justify="center")
        table.add_column('option')
        counter = -1
        for i in self.menu:
            table.add_row(str(counter + 1), i)
            counter += 1
        console.print(table)
        self.choice = self.check_choice()
        return self
