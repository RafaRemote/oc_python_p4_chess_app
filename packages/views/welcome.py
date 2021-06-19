""" welcoming message display """

import time
import os

from pyfiglet import Figlet
from termcolor import colored

class WelcomeView:
    def __init__(self, message):
        self.message = message

    def clean_sentence(self, sentence):
        os.system('cls' if os.name == 'nt' else 'clear')
        f = Figlet(font='term')
        print('      ', colored(f.renderText(sentence.strip(' ').upper()), 'magenta'))
        time.sleep(.5)

    def __call__(self):
        self.clean_sentence(self.message)
