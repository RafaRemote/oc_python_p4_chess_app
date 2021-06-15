import datetime
import time
import os

from termcolor import colored

class TournamentView:
    def __init__(self):
        self.name = self.get_name()
        self.time_control = self.get_time_control()
        self.description = self.get_description()
        self.date = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

    def get_name(self):
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
        if time_control.lower() not in times:
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
        return self



   


