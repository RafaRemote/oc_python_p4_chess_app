""" retrieve user inputs for the scores """

import os

from termcolor import colored
from rich.console import Console
from rich.table import Table


class ScoringView:
    """
    Class to represent a scoring view page

    ...

    Attributes
    ----------
    round_number: int
        int representing length of rounds list in a TournamentModel instance
    matches: list
        list ot MatchModel instances
    player1: tuple
        empty tuple
    player2: tuple
        empty tuple
    new_matches: list
        empty list

    Methods
    -------
    checks_score(self, player1_surname, player1_elo, player2_surname, player2_elo, counter):
        print tables
        returns floats
    call(self):
        prints tables
        assigns values for self attributes
        return instance of ScoringView
    """

    def __init__(self, tour_info):
        """
        Constructs attributes for ScoringView object.

        Parameters
        ----------
        tour_info: instance
            TournamentModel instance
        """

        self.round_number = len(tour_info.rounds)
        self.matches = tour_info.rounds[-1].matches
        self.player1 = tuple()
        self.player2 = tuple()
        self.new_matches = []

    def check_score(self, player1_surname, player1_elo, player2_surname, player2_elo, counter):
        """
        prints tables, retrieves user inputs for scores

        Parameters
        ----------
        player1_surname: str
            player surname
        player1_elo: int
            player_elo
        player2_surname: str
            player surname
        player2_elo: int
            player elo
        counter: int
            represents number of the match

        Returns
        -------
        instance of ScoringView

        """

        console = Console()
        super_title = Table(title=colored('MATCH ', 'yellow')+str(counter),
                            show_header=True,
                            header_style="bold yellow")
        super_title.add_column(player1_surname, justify="center")
        super_title.add_column(player2_surname, justify="center")
        super_title.add_row(f'ELO {player1_elo}', f'ELO {player2_elo}')
        console.print(super_title)
        info_console = Console()
        info = Table(title=colored('INPUTS INFO', 'blue'),
                     show_header=True,
                     header_style="bold blue")
        info.add_column('INPUT')
        info.add_column('MEANING')
        info.add_row('y', 'WON')
        info.add_row('n', 'LOST')
        info.add_row('d', 'DRAW')
        info_console.print(info)
        print(f'Did {player1_surname} won ?')
        print()
        i = 0
        while i < 1:
            choices = ['y', 'n', 'd']
            score = input('===> ')
            if score not in choices:
                print(colored("invalid choice: you need to choose between: \'y\', \'n\' or \'d\'", "red"))
            elif score == 'y':
                i += 1
                return 1.0
            elif score == 'n':
                i += 1
                return 0.0
            elif score == 'd':
                i += 1
                return 0.5

    def __call__(self):
        """
        print table
        assign value for self.attributes

        Parameters
        ----------
        none

        Returns
        -------
        instance of ScoringView

        """
        os.system('cls' if os.name == 'nt' else 'clear')
        counter = 0
        for i in self.matches:
            console = Console()
            welcome = Table(show_header=True, header_style="yellow")
            welcome.add_column('SCORES INPUTS', justify="center")
            welcome.add_row('ROUND ' + str(self.round_number))
            console.print(welcome)
            counter += 1
            player1 = i.player1[0]
            score1 = 0.0
            player2 = i.player2[0]
            score2 = 0.0
            points = self.check_score(player1.surname,
                                      player1.elo,
                                      player2.surname,
                                      player2.elo,
                                      counter)
            if points == 1.0:
                score1 += 1.0
                self.player1 == (player1, score1)
            elif points == 0.0:
                score2 += 1.0
                self.player2 == (player2, score2)
            elif points == 0.5:
                score1 += 0.5
                self.player1 == (player1, score1)
                score2 += 0.5
                self.player2 == (player2, score2)
            self.new_matches.append((player1, player2, score1, score2))
            print()
            table = Table(title=colored("SCORES MATCH "+str(counter)), show_header=True, header_style="bold blue")
            table.add_column("Name", style="dim")
            table.add_column("Surname")
            table.add_column("score", justify="center")
            table.add_row(player1.name, player1.surname, str(score1))
            table.add_row(player2.name, player2.surname, str(score2))
            console.print(table)
            print()
            input(colored('press return to continue', 'blue'))
            os.system('cls' if os.name == 'nt' else 'clear')
        return self
