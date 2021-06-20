""" docstrings """
import datetime
# import time

from packages.models.match import MatchModel


class RoundModel:
    def __init__(self, tour_info, number, players, next_matches=None):
        self.tour_info = tour_info
        self.number = number
        self.players = players
        self.start_date = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        self.end_date = None
        self.next_matches = next_matches
        self.matches = list()

    def __call__(self):
        if self.number != '1':
            for i in self.next_matches:
                self.matches.append(i)
        else:
            for i in range(0, len(self.players[0])):
                self.matches.append(MatchModel(self.players[0][i], self.players[1][i], score1=0.0, score2=0.0))
        return self
