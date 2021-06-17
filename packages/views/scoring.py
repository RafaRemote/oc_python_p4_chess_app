""" docstrings """

import time
import os
from termcolor import colored

class ScoringView:
    def __init__(self, round_number, matches):
        self.round_number = round_number
        self.matches = matches

    def check_score(self, player_name):
        player_name = player_name
        while True:
            print(colored('Type \'y\' \'n\' or \'d\' for draw match ','blue'))
            score = input(f'{player_name} won?: ')
            if score.lower() == 'y':
                return 1.0
            elif score.lower() == 'n':
                return 0.0
            elif score.lower() == 'd':
                return 0.5
            else:
                print(colored(f'{score} is not correct. You need to choose y, n or d', 'red'))


    def get_round_score(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored(f'ENTER THE RESULT FOR ROUND {self.round_number}', 'magenta'))
        print()
        counter = 1
        for i in self.matches:
            player1 = i.__dict__['player1'][0]
            player2 = i.__dict__['player2'][0]
            print()
            print('MATCH ', counter)
            print('--------')
            counter += 1
            print(colored(f' -- >> {player1.surname} (elo: {player1.elo}) VS {player2.surname} (elo: {player2.elo}) ', 'yellow'))
            print()
            player1_score = self.check_score(player1.surname)
            player2_score = 0.0
            if player1_score == 1.0:
                player1.score += 1.0
            elif player1_score == 0.0:
                player2_score += 1.0
                player2.score += 1.0
            elif player1_score == 0.5:
                player1.score += 0.5
                player2.score += 0.5
                player2_score += 0.5
            print()
            print('Player Score for this match')
            print(player1.surname, ':', player1_score)
            print(player2.surname, ':', player2_score)
            time.sleep(1)

    def __call__(self):
        self.get_round_score()
        print('Coming back to main menu ...')
        time.sleep(1)
        return self
