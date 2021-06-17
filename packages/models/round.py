""" docstrings """

import datetime

from packages.models.match import MatchModel 

class RoundModel:
    def __init__(self, tour_info, number, players):
        self.tour_info = tour_info  
        self.number = number
        self.players = players
        self.start_date = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        self.end_date = None
        self.matches = self.get_matches()

    def get_matches(self):
        matches = []
        if self.number == '1':
            for i in range(0, len(self.players[0])):
                matches.append(MatchModel(self.players[0][i], self.players[1][i], score1=0, score2=0))
            return matches

    def __call__(self):
            return self
