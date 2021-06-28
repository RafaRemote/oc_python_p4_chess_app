""" retrieve user inputs for the scores """

import os

from termcolor import colored
from rich.console import Console
from rich.table import Table


class ScoringView:
    def __init__(self, round_number, matches):
        self.round_number = round_number
        self.matches = matches
        self.player1 = tuple()
        self.player2 = tuple()
        self.new_matches = []

    def check_score(self, player1_surname, player1_elo, player2_surname, player2_elo, counter):
        console = Console()
        super_title = Table(title=colored('MATCH ', 'yellow')+str(counter),
                            show_header=True,
                            header_style="bold yellow")
        super_title.add_column(player1_surname, justify="center")
        super_title.add_column(player2_surname, justify="center")
        super_title.add_row(f'ELO {player1_elo}', f'ELO {player2_elo}')
        console.print(super_title)
        score = input(f'Did {player1_surname} won ? (\'y\' for yes, \'n\' for now, \'d\' for draw): ')
        print()
        if score == 'y':
            return 1.0
        elif score == 'n':
            return 0.0
        elif score == 'd':
            return 0.5
        else:
            print("[red]"+"invalid choice: you need to choose between: \'y\', \'n\' or \'d\'")
            self.check_score(player1_surname, player1_elo, player2_surname, player2_elo, counter)

    def __call__(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        counter = 0

        for i in self.matches:
            console = Console()
            welcome = Table(show_header=True, header_style="yellow")
            welcome.add_column('SCORES INPUTS', justify="center")
            welcome.add_row('ROUND ' + str(self.round_number))
            console.print(welcome)
            counter += 1
            player1 = i.__dict__['player1'][0]
            match_score1 = 0.0
            player2 = i.__dict__['player2'][0]
            match_score2 = 0.0
            points = self.check_score(player1.surname, player1.elo, player2.surname, player2.elo, counter)
            if points == 1.0:
                player1.score += 1.0
                match_score1 += 1.0
                self.player1 == (player1, match_score1)
            elif points == 0.0:
                player2.score += 1.0
                match_score2 += 1.0
                self.player2 == (player2, match_score2)
            elif points == 0.5:
                player1.score += 0.5
                match_score1 += 0.5
                self.player1 == (player1, match_score1)
                player2.score += 0.5
                match_score2 += 0.5
                self.player2 == (player2, match_score2)
            self.new_matches.append((player1, player2, match_score1, match_score2))
            print()
            table = Table(title=colored("SCORES MATCH "+str(counter)), show_header=True, header_style="bold blue")
            table.add_column("Name", style="dim")
            table.add_column("Surname")
            table.add_column("score", justify="center")
            table.add_row(str(player1.name), str(player1.surname), str(match_score1))
            table.add_row(str(player2.name), str(player2.surname), str(match_score2))
            console.print(table)
            print()
            input(colored('press return to continue', 'blue'))
            os.system('cls' if os.name == 'nt' else 'clear')
        return self
