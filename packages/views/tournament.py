import time
import os

from termcolor import colored

class TournamentView:
    def __init__(self):
        self.name = None
        self.time = None
        self.description = None

    def __call__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored('ENTER TOURNAMENT DETAILS', 'magenta'))
        print()
        name = input("Enter the name of the tournament: ")
        self.name = name
        time_control = input("Type the time control: bullet, blitz or rapid: ")
        self.time = time_control
        description = input("Enter a description of the tournament: ")
        self.description = description
        print()
        print(colored('Saving informations...', 'green'))
        print()
        time.sleep(2)
        return self

