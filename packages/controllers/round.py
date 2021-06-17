""" docstrings"""

import datetime

from packages.models.player import PlayerModel
from packages.models.round import RoundModel
from packages.models.tournament import TournamentModel


class RoundController:
    def __init__(self, tour_info, round_number, players):
        self.tour_info = tour_info
        self.number = round_number
        self.players = players

    def round1(self):
        players_list = []
        for i in range(0, len(self.players['name'])):
            players_list.append(PlayerModel(
                                            self.players['name'][i], 
                                            self.players['surname'][i], 
                                            self.players['year_of_birth'][i], 
                                            self.players['gender'][i], 
                                            self.players['elo'][i], 
                                            score=float(0)
                                            )
                                        )
        sorted_players_list_by_elo = sorted(players_list, key=lambda x:x.elo, reverse=True)
        high_group = sorted_players_list_by_elo[:4]
        low_group = sorted_players_list_by_elo[4:]
        two_groups_players = [high_group, low_group]
        round1 = RoundModel(self.tour_info, self.number, two_groups_players)
        round1_tour = round1().__dict__['tour_info']
        round1_number = round1().__dict__['number']
        round1_start_date = round1().__dict__['start_date']
        round1_end_date = round1().__dict__['end_date']
        round1_matches = round1().__dict__['matches']
        update = TournamentModel.update_tour(round1_tour, round1_number, round1_start_date, round1_end_date, round1_matches)
        return update()

    def update_tour(tour_info, score_info):
        score = score_info.__dict__
        tour = tour_info.__dict__
        round_number = score['round_number']
        round_start_date = tour['rounds'][round_number-1][1]
        round_end_date = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        round_matches = score['matches']
        tour_info = TournamentModel.update_tour_round(tour_info, round_number, round_start_date, round_end_date, round_matches)
        return tour_info()
        