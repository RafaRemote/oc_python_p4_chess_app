""" display a menu for players details and their rankings """

import os

from termcolor import colored
from rich.console import Console
from rich.table import Table
from rich import print


class RankingView:
    def __init__(self, players):
        self.players = players
        self.player = None

    def choose(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        console = Console()
        table = Table(title='PLAYERS MENU', show_header=True, header_style='bold magenta')
        table.add_column("Choice Number")
        table.add_column("Option")
        table.add_row("1", "[orange1]"+"Alphabetical order")
        table.add_row("2", "[dark_violet]"+"Ranking by score")
        table.add_row("3", "[magenta2]"+"Change player score")
        table.add_row("4", "previous menu")
        console.print(table)
        print()
        choice = input('Your choice: ')
        if choice == '1' or choice == '2':
            self.print_ranking(choice)
        elif choice == '3':
            self.show_scores()
        elif choice == '4':
            return 
        else:
            print("[red]"+"you need to choose between 1, 2 or 3")
            input(colored("press return to continue", "blue"))
            self.choose()

    def print_ranking(self, choice):
        if choice == '1':
            players = sorted(self.players, key=lambda x: x['surname'])
            color_surname = "[orange1]"
            color_score = "[white]"
        else:
            players = sorted(self.players, key=lambda x: (x['score'], x['elo']), reverse=True)
            color_surname = "[white]"
            color_score = "[dark_violet]"

        console = Console()
        table = Table(title="PLAYERS RANKING", show_header=True, header_style="bold magenta")
        table.add_column("Name", style="dim", width=12)
        table.add_column("Surname")
        table.add_column("Year of Birth", justify="center")
        table.add_column("Gender", justify="center")
        table.add_column("Elo", justify="center")
        table.add_column("Score", justify="center")
        for i in players:
            table.add_row(str(i['name']),
                          str(color_surname + i['surname']),
                          str(i['year_birth']),
                          str(i['gender']),
                          str(i['elo']),
                          str(color_score + str(i['score']))
                          )
        console.print(table)
        print()
        input(colored('press return to continue', 'blue'))
        self.choose()

    def show_scores(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        console = Console()
        table = Table(title="PLAYERS CURRENT SCORES", show_header=True, header_style="bold magenta")
        table.add_column("Choice")
        table.add_column("Surname")
        table.add_column("Score", justify="center")
        counter = 0
        for i in self.players:
            counter += 1
            table.add_row(str(counter),
                          i['surname'],
                          str(i['score'])
                          )
        console.print(table)
        print()
        choice = input('which player\'s score do you want to modify?: ')
        if choice.isnumeric() and int(choice) in range(1, 9):
            self.modify_score(choice)
        else:
            print('invalid choice. You need to choose a number between 1 and 8')
            input(colored('press return to continue', 'blue'))
            self.show_scores()

    def modify_score(self, choice):
        player = self.players[int(choice) - 1]
        score = input('what is the new score of ' + colored(player['surname'], 'yellow') + "? ")
        player['score'] += float(score)
        print('the new score of', player['surname'], 'is', player['score'])
        input('press return to continue')
        self.player = player
        self.player_new_score = float(score)
        self.choose()

    def __call__(self):
        self.choose()
        return self.player
