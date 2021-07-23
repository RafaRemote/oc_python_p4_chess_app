""" display a menu for players details and their rankings """

import os

from termcolor import colored
from rich.console import Console
from rich.table import Table
from rich import print


class RankingView:
    def __init__(self, scores):
        self.scores = scores
        self.player = None
        self.player_new_elo = None

    def choose(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        console = Console()
        table = Table(title='PLAYERS MENU', show_header=True, header_style='bold magenta')
        table.add_column("Choice Number")
        table.add_column("Option")
        table.add_row("1", "[orange1]"+"Alphabetical order")
        table.add_row("2", "[dark_violet]"+"Ranking by score")
        table.add_row("3", "[magenta2]"+"Change player's elo")
        table.add_row("4", "previous menu")
        console.print(table)
        print()
        choice = input('Your choice: ')
        if choice == '1' or choice == '2':
            self.print_ranking(choice)
        elif choice == '3':
            self.show_elos()
            return
        elif choice == '4':
            return
        else:
            print("[red]"+"you need to choose between 1, 2, 3 or 4")
            input(colored("press return to continue", "blue"))
            self.choose()

    def print_ranking(self, choice):
        if choice == '1':
            players = sorted(self.scores, key=lambda x: x[0].surname)
            color_surname = "[orange1]"
            color_score = "[white]"
        else:
            players = sorted(self.scores, key=lambda x: (x[2], x[0].elo), reverse=True)
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
        for player in players:
            table.add_row(str(player[0].name),
                          str(color_surname + player[0].surname),
                          str(player[0].year_birth),
                          str(player[0].gender),
                          str(player[0].elo),
                          str(color_score + str(player[2]))
                          )
        console.print(table)
        print()
        input(colored('press return to continue', 'blue'))
        self.choose()

    def show_elos(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        console = Console()
        table = Table(title="PLAYERS", show_header=True, header_style="bold magenta")
        table.add_column("Choice")
        table.add_column("Surname")
        table.add_column("Score", justify="center")
        counter = 0
        for player in self.scores:
            counter += 1
            table.add_row(str(counter),
                          player[0].surname,
                          str(player[0].elo)
                          )
        console.print(table)
        print()
        choice = input('which player\'s score do you want to modify?: ')
        if choice.isnumeric() and int(choice) in range(1, 9):
            self.modify_score(choice)
            return
        else:
            print('invalid choice. You need to choose a number between 1 and 8')
            input(colored('press return to continue', 'blue'))
            self.show_elos()

    def modify_score(self, choice):
        player = self.scores[int(choice) - 1][0]
        new_elo = input('what is the new elo of ' + colored(player.surname, 'yellow') + "? ")
        print('the new elo of', player.surname, 'is', new_elo)
        input('press return to continue')
        self.player = player
        self.player_new_elo = new_elo
        return self.player, self.player_new_elo

    def __call__(self):
        self.choose()
        return self.player, self.player_new_elo
