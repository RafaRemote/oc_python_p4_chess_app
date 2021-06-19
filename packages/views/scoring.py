""" docstrings """

import time
import os
from termcolor import colored

class ScoringView:
    def __init__(self, round_number, matches):
        self.round_number = round_number
        self.matches = matches

    def check_score(self, player1_surname, player1_elo, player2_surname, player2_elo):
        print()
        print(colored('MATCH ','yellow'), colored(f' -- >> {player1_surname} (elo: {player1_elo}) VS {player2_surname} (elo: {player2_elo}) ', 'yellow'))
        print('--------')
        print()
        print(colored('[ >>> Type \'y\', \'n\' or \'d\' for draw match <<< ]','cyan'))
        print()
        score = input('score ?: ')
        print()
        if score == 'y':
            return 1.0
        elif score == 'n':
            return 0.0
        elif score == 'd':
            return 0.5
        else:
            print(colored(f'[[[  {score}  ]]] is not correct. You need to choose between: 0, 0.5 or 1', 'red'))
            self.check_score(player1_surname, player1_elo, player2_surname, player2_elo)

    def __call__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored(f'ENTER THE RESULT FOR ROUND {self.round_number}', 'magenta'))
        for i in self.matches:
            player1 = i.__dict__['player1'][0]
            player2 = i.__dict__['player2'][0]
            points = self.check_score(player1.surname, player1.elo, player2.surname, player2.elo)
            if points == 1.0:
                player1.score += 1.0
            elif points == 0.0:
                player2.score += 1.0
            elif points == 0.5:
                player1.score += 0.5
                player2.score += 0.5
            print()
            print('Player Score for this match')
            print(player1.surname, ':', player1.score)
            print(player2.surname, ':', player2.score)
            time.sleep(1)
        return self
