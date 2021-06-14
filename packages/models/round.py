import datetime
from time import strftime

from packages.models.match import MatchModel 


class RoundModel:
    def __init__(self, tournament_name, players):
        self.tournmanent_name = tournament_name
        self.name = None
        self.start_date = None
        self.end_date = None
        self.matches = []
        self.players = players

    def round1(self):
        self.name = 'Round1'
        self.start_date = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        list_of_players = self.players[:8]
        cleaned_list = []
        for i in list_of_players:
            cleaned_list.append(i.__dict__.get('elo'))
            cleaned_list.append(i)
        newlist = sorted(list_of_players, key=lambda x: x.elo, reverse=True)
        high_group = newlist[:4]
        low_group = newlist[4:]
        for i in range(0, 4):
            self.matches.append( MatchModel(high_group[i], low_group[i], score1=0, score2=0))
        return self

