""" retrieve user inputs about tournament details """

import time
import os

from termcolor import colored


class InputTournamentView:
    def __init__(self):
        self.place = self.get_place()
        self.title = self.get_title()
        self.time_control = self.get_time_control()
        self.description = self.get_description()

    def display_title(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored('      ENTER TOURNAMENT INFORMATIONS',
                      'magenta'
                      ))
        print()
        print()

    def check_len(self, name, max):
        if(len(name) == 0):
            print(colored('You entered nothing, you need to enter something.', 'red'))
            time.sleep(1)
            return False
        if len(name) > max:
            print(colored(f'You have entered too many characters, the max is {max}', 'red'))
            time.sleep(1)
            return False
        else:
            return True

    def get_place(self):
        self.display_title()
        print()
        place = input('Place the tournament is taking place [max: 20 characters]: ')
        if self.check_len(place, 20):
            print()
            return place
        else:
            self.get_place()

    def get_title(self):
        name = input('Name of the tournament [max: 20 characters]: ')
        if self.check_len(name, 20):
            print()
            return name
        else:
            self.get_name()

    def get_time_control(self):
        times = ['bullet', 'blitz', 'rapid']
        time_control = input('Enter time option: bullet, blitz or rapid: ')
        print()
        while time_control.lower() not in times:
            print(colored('the only options availabe are bullet, blitz or rapid.', 'red'))
            print('try again')
            print()
            return self.get_time_control()
        else:
            return time_control

    def get_description(self):
        description = input('Enter a description for the tournament [max 500 characters]: ')
        if self.check_len(description, 500):
            return description
        else:
            self.get_description()

    def __call__(self):
        print()
        input(colored('press return to go to the main menu', "blue"))
        return self
