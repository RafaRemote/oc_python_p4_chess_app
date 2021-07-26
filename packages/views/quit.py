""" Quit view """

import time
import os

from pyfiglet import Figlet
from termcolor import colored


class QuitView:
    """
    Class to represent an quit view page
    ...

    Attributes
    ----------
    message: str
        string displayed on quit page

    Methods
    -------
    clean_sentence(self, sentence):
        print a sentence

    """

    def __init__(self, message):
        """
        Constructs attributes for QuitView object.

        Parameters
        ----------
        message: str
            string displayed on quit page

        """

        self.message = message

    def clean_sentence(self, sentence):
        """
        prints string

        Parameters
        ----------
        sentence: str
            message to be displayed on the quit page

        Returns
        -------
        no return

        """

        os.system('cls' if os.name == 'nt' else 'clear')
        f = Figlet(font='term')
        print('      ', colored(f.renderText(sentence.strip(' ').upper()), 'magenta'))
        time.sleep(2)
        exit()

    def __call__(self):
        """ calls self.clean_sentence(self.message), no return """

        self.clean_sentence(self.message)
