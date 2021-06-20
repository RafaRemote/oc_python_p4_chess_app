""" doctstrings"""
import os

from termcolor import colored


class OpponentsView:
    def __init__(self, tour_info):
        self.tour_info = tour_info

    def __call__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in self.tour_info.__dict__['players']:
            for k in i:
                for l in k.opponents:
                    print(k.surname, ':, opponents :', l.surname)
        i = 0
        while i < 1:
            back_home = input('Type \'y\' to come back to the menu.')
            if back_home == 'y':
                return 'y'
            else:
                print(colored('You did not type the good key. Type \'y\' to go back to the menu',
                              'red'))

