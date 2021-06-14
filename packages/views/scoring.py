import time
import os
from termcolor import colored

class ScoringView:
    def __init__(self, tournament_list):
        self.tournament = tournament_list
        self.round = None

    def check_score(self):
        scores = [0, 0.5, 1]
        scores_string = ['0', '0.5', '1']
        while True:
            score = input('score ?: ')
            if score not in scores and score not in scores_string:
                print(colored(f'{score} is not correct. You need to choose between: 0, 0.5 or 1', 'red'))
                return input('score ?:' )
            else:
                return score

    def round_one(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.round = 'ONE'
        print(colored(f'ENTER THE RESULT FOR ROUND {self.round}', 'magenta'))
        print()
        
        player_one_object = self.tournament[0].__dict__.get('rounds')[0].__dict__.get('matches')[0].__dict__['player1']
        player_one_surname = self.tournament[0].__dict__.get('rounds')[0].__dict__.get('matches')[0].__dict__['player1'][0].__dict__.get('surname')
        player_one_name = self.tournament[0].__dict__.get('rounds')[0].__dict__.get('matches')[0].__dict__['player1'][0].__dict__.get('name')
        player_one_elo = self.tournament[0].__dict__.get('rounds')[0].__dict__.get('matches')[0].__dict__['player1'][0].__dict__.get('elo')
        # print(self.tournament[0].__dict__.get('rounds')[0].__dict__.get('matches')[0].__dict__['player1'][1])

        player_two_object = self.tournament[0].__dict__.get('rounds')[0].__dict__.get('matches')[0].__dict__['player2']
        player_two_surname = self.tournament[0].__dict__.get('rounds')[0].__dict__.get('matches')[0].__dict__['player2'][0].__dict__.get('surname')
        player_two_name = self.tournament[0].__dict__.get('rounds')[0].__dict__.get('matches')[0].__dict__['player2'][0].__dict__.get('name')
        player_two_elo = self.tournament[0].__dict__.get('rounds')[0].__dict__.get('matches')[0].__dict__['player2'][0].__dict__.get('elo')
        # print(self.tournament[0].__dict__.get('rounds')[0].__dict__.get('matches')[0].__dict__['player2'][1])

        print()
        print(f'{player_one_surname} {player_one_name} (Elo: {player_one_elo}) was playing against {player_two_surname} {player_two_name} (Elo: {player_two_elo})' )
        print()
        print(f'Enter the score for {player_one_surname}')
        score_player_one = self.check_score()
        print(f'Enter the score for {player_two_surname}')
        score_player_two = self.check_score()

        player_three_object = self.tournament[0].__dict__.get('rounds')[0].__dict__.get('matches')[1].__dict__['player1']
        player_three_surname = self.tournament[0].__dict__.get('rounds')[0].__dict__.get('matches')[1].__dict__['player1'][0].__dict__.get('surname')
        player_three_name = self.tournament[0].__dict__.get('rounds')[0].__dict__.get('matches')[1].__dict__['player1'][0].__dict__.get('name')
        player_three_elo = self.tournament[0].__dict__.get('rounds')[0].__dict__.get('matches')[1].__dict__['player1'][0].__dict__.get('elo')
        # print(self.tournament[0].__dict__.get('rounds')[0].__dict__.get('matches')[1].__dict__['player1'][1])

        player_four_object = self.tournament[0].__dict__.get('rounds')[0].__dict__.get('matches')[1].__dict__['player2']
        player_four_surname = self.tournament[0].__dict__.get('rounds')[0].__dict__.get('matches')[1].__dict__['player2'][0].__dict__.get('surname')
        player_four_name = self.tournament[0].__dict__.get('rounds')[0].__dict__.get('matches')[1].__dict__['player2'][0].__dict__.get('name')
        player_four_elo = self.tournament[0].__dict__.get('rounds')[0].__dict__.get('matches')[1].__dict__['player2'][0].__dict__.get('elo')
        # print(self.tournament[0].__dict__.get('rounds')[0].__dict__.get('matches')[1].__dict__['player2'][1])

        print()
        print(f'{player_three_surname} {player_three_name} (Elo: {player_three_elo}) was playing against {player_four_surname} {player_four_name} (Elo: {player_four_elo})' )
        print()
        print(f'Enter the score for {player_three_surname}')
        score_player_three = self.check_score()
        print(f'Enter the score for {player_four_surname}')
        score_player_four = self.check_score()

        player_five_object = self.tournament[0].__dict__.get('rounds')[0].__dict__.get('matches')[2].__dict__['player1']
        player_five_surname = self.tournament[0].__dict__.get('rounds')[0].__dict__.get('matches')[2].__dict__['player1'][0].__dict__.get('surname')
        player_five_name = self.tournament[0].__dict__.get('rounds')[0].__dict__.get('matches')[2].__dict__['player1'][0].__dict__.get('name')
        player_five_elo = self.tournament[0].__dict__.get('rounds')[0].__dict__.get('matches')[2].__dict__['player1'][0].__dict__.get('elo')
        # print(self.tournament[0].__dict__.get('rounds')[0].__dict__.get('matches')[2].__dict__['player1'][1])

        player_six_object = self.tournament[0].__dict__.get('rounds')[0].__dict__.get('matches')[2].__dict__['player2']
        player_six_surname = self.tournament[0].__dict__.get('rounds')[0].__dict__.get('matches')[2].__dict__['player2'][0].__dict__.get('surname')
        player_six_name = self.tournament[0].__dict__.get('rounds')[0].__dict__.get('matches')[2].__dict__['player2'][0].__dict__.get('name')
        player_six_elo = self.tournament[0].__dict__.get('rounds')[0].__dict__.get('matches')[2].__dict__['player2'][0].__dict__.get('elo')
        # print(self.tournament[0].__dict__.get('rounds')[0].__dict__.get('matches')[2].__dict__['player2'][1])

        print()
        print(f'{player_five_surname} {player_five_name} (Elo: {player_five_elo}) was playing against {player_six_surname} {player_six_name} (Elo: {player_six_elo})' )
        print()
        print(f'Enter the score for {player_five_surname}')
        score_player_five = self.check_score()
        print(f'Enter the score for {player_six_surname}')
        score_player_six = self.check_score()

        player_seven_object = self.tournament[0].__dict__.get('rounds')[0].__dict__.get('matches')[3].__dict__['player1']
        player_seven_surname = self.tournament[0].__dict__.get('rounds')[0].__dict__.get('matches')[3].__dict__['player1'][0].__dict__.get('surname')
        player_seven_name = self.tournament[0].__dict__.get('rounds')[0].__dict__.get('matches')[3].__dict__['player1'][0].__dict__.get('name')
        player_seven_elo = self.tournament[0].__dict__.get('rounds')[0].__dict__.get('matches')[3].__dict__['player1'][0].__dict__.get('elo')
        # print(self.tournament[0].__dict__.get('rounds')[0].__dict__.get('matches')[3].__dict__['player1'][1])

        player_eight_object = self.tournament[0].__dict__.get('rounds')[0].__dict__.get('matches')[3].__dict__['player2']
        player_eight_surname = self.tournament[0].__dict__.get('rounds')[0].__dict__.get('matches')[3].__dict__['player2'][0].__dict__.get('surname')
        player_eight_name = self.tournament[0].__dict__.get('rounds')[0].__dict__.get('matches')[3].__dict__['player2'][0].__dict__.get('name')
        player_eight_elo = self.tournament[0].__dict__.get('rounds')[0].__dict__.get('matches')[3].__dict__['player2'][0].__dict__.get('elo')
        # print(self.tournament[0].__dict__.get('rounds')[0].__dict__.get('matches')[3].__dict__['player2'][1])

        print()
        print(f'{player_seven_surname} {player_seven_name} (Elo: {player_seven_elo}) was playing against {player_eight_surname} {player_eight_name} (Elo: {player_eight_elo})' )
        print()
        print(f'Enter the score for {player_seven_surname}')
        score_player_seven = self.check_score()
        print(f'Enter the score for {player_eight_surname}')
        score_player_eight = self.check_score()

        print(colored('Saving informations...', 'green'))
        time.sleep(2)

        return([
                player_one_object, 
                int(score_player_one),
                player_two_object, 
                int(score_player_two),
                player_three_object, 
                int(score_player_three),
                player_four_object, 
                int(score_player_four),
                player_five_object, 
                int(score_player_five),
                player_six_object, 
                int(score_player_six),
                player_seven_object, 
                int(score_player_seven),
                player_eight_object, 
                int(score_player_eight)
        ])
