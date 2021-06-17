""" docstrings """

import datetime
import time
import os

from termcolor import colored

class TournamentView:
    def __init__(self):
        self.tour_title = self.get_name()
        self.tour_time_control = self.get_time_control()
        self.tour_description = self.get_description()
        self.tour_start_date = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

    def display_title(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored('      FIRST OF ALL: INPUT TOURNAMENT INFORMATIONS', 'magenta'))
        print()
        print()


    def get_name(self):
        self.display_title()
        name = input('Enter the name of the tournament[max: 20 characters]: ')
        print()
        if len(name) > 20:
            print(colored('You have enterd too many characters, the max is 20', 'red'))
            print('try again')
            print()
            self.get_name() 
        else: 
            return name

    def get_time_control(self):
        times = ['bullet', 'blitz', 'rapid']
        time_control = input('Enter time option: bullet, blitz or rapid: ')
        print()
        while time_control.lower() not in times:
            print(colored('the only options availabe are bullet, blitz or rapid.', 'red'))
            print('try again')
            print()
            self.get_time_control()
        else:
            return time_control

    def get_description(self):
        description = input('Enter a description for the tournament: ')
        if len(description)  > 500:
            print(colored('You have enterd too many characters, the max is 500', 'red'))
            print('try again')
            print()
            self.get_description()
        else:
            return description

    def __call__(self):
        print()
        print(colored('Saving informations...', 'green'))
        time.sleep(1)

        return self
