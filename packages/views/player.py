""" docstrings """

import os
import time

from termcolor import colored

class PlayerView:
    def __init__(self):
        self.name = []
        self.surname = []
        self.year_of_birth = []
        self.gender = []
        self.elo = []

    def __call__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('      ', colored('ENTER PLAYER INFORMATIONS', 'magenta'))

        counter = 0
        while counter < 8:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(colored('      Enter infos about the players'.upper(), 'magenta'))
            print()
            print(f'Yet, you entered {counter} on 8')
            print()
            print(f'Still {8 - counter} player info to enter')
            print()
            name = input('Enter the name of the player: ')
            self.name.append(name)
            surname = input('Enter the surname of the player: ')
            self.surname.append(surname)
            year_of_birth = input('Enter year of birth: ')
            self.year_of_birth.append(year_of_birth)
            gender = input('Enter the gender: m or w: ')
            self.gender.append(gender)
            elo = input('Enter the Elo of the player: ')
            self.elo.append(elo)
            counter += 1
            if counter == 8:
                print()
                print(colored(f'You have entered the {counter} players', 'green'))
                time.sleep(.5)
                print()
                print(colored('Saving informations...', 'green'))
                print()
                time.sleep(1.5)
                os.system('cls' if os.name == 'nt' else 'clear')
                break
        return self
