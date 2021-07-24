""" display error """

import os

from termcolor import colored


class Error:
    """
    Class to represent an error page
    ...

    Attributes
    ----------
    message: str
        string displayed on error page

    Methods
    -------
    call(self):
        print
        returns nothing
    """

    def __init__(self, message):
        """
        Constructs attributes for Error object.

        Parameters
        ----------
        message: str
            string displayed on error page

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
        print(colored('*** ' + self.message.upper() + ' ***', 'red'))
        print()
        input(colored('press return to continue', 'blue'))
        return
