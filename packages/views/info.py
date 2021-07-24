""" display information """

import os

from termcolor import colored
from rich import print


class InfoView:
    """
    Class to represent an information page

    ...

    Attributes
    ----------
    message: str
        message displayed on information page

    Methods
    -------
    call(self):
        print
        returns nothing
    """

    def __init__(self, message):
        """
        Constructs attributes for InfoView object.

        Parameters
        ----------
        message: str
            string displayed on inforamtion page

        """
        self.message = message

    def __call__(self):
        """
        printing self.message

        Parameters
        ----------
        none

        Returns
        -------
        nothing

        """
        os.system('cls' if os.name == 'nt' else 'clear')
        print()
        print('[orange1]' + '*** ' + self.message.upper() + ' ***')
        print()
        input(colored('press return to continue', 'blue'))
        return
