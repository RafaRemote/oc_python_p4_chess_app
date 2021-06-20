""" welcoming message display """

import time
import os

from pyfiglet import Figlet
from rich.console import Console
from rich.table import Table


class WelcomeView:
    def __init__(self, message, sub_title):
        self.message = message
        self.sub_title = sub_title

    def clean_sentence(self, sentence):
        os.system('cls' if os.name == 'nt' else 'clear')
        console = Console()
        table = Table(show_header=True, header_style="bold magenta")
        f = Figlet(font='bubble')
        table.add_column(f.renderText(sentence.strip(' ').upper()),
                         justify="center")
        table.add_row(self.sub_title)
        console.print(table)
        time.sleep(3)

    def __call__(self):
        self.clean_sentence(self.message)
