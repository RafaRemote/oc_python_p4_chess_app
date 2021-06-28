""" model tournament """

import datetime

from packages.models.player import PlayerModel

TOTALROUNDS = 4

players = [PlayerModel('Simpsons', 'Homer', 1970, 'm', 1100, 0.0),
           PlayerModel('Simpsons', 'Marge', 1980, 'w', 1900, 0.0),
           PlayerModel('Simpsons', 'Bart', 2008, 'm', 1100, 0.0),
           PlayerModel('Simpsons', 'Lisa', 2010, 'w', 1940, 0.0),
           PlayerModel('Simpsons', 'Maggie', 2018, 'w', 1050, 0.0),
           PlayerModel('Szyslak', 'Moe', 1960, 'm', 2200, 0.0),
           PlayerModel('Flanders', 'Ned', 1910, 'm', 2700, 0.0),
           PlayerModel('Burns', 'Montgomery', 1900, 'm', 1100, 0.0)
           ]

tournaments_list = list()


class TournamentModel:
    def __init__(self, place, tour_title, tour_time_control, tour_description):
        self.place = place
        self.tour_title = tour_title
        self.tour_time_control = tour_time_control
        self.tour_description = tour_description
        self.tour_start_date = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        self.total_rounds = TOTALROUNDS
        self.rounds = list()
        self.players = players

    def __call__(self):
        return self
