import time
import os
from termcolor import colored

class ScoringView:
    def __init__(self, tournament_list):
        self.tournament = tournament_list

    def __call__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored('ENTER THE RESULT FOR THE LAST ROUND PLAYED'))
        print('checking what tour you should enter the result')
        print(self.tournament[0].__dict__)
