""" docstrings"""

import datetime

from packages.models.player import PlayerModel
from packages.models.round import RoundModel
from packages.models.tournament import TournamentModel
from packages.models.match import MatchModel


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
        round1 = RoundModel(self.tour_info, self.number, two_groups_players, next_matches=None)
        round = round1()
        tour_info = round.tour_info
        round1_number = round.number
        round1_start_date = round.start_date
        round1_end_date = round.end_date
        round1_matches = round1.matches
        update_tour = TournamentModel.update_tour(  tour_info, 
                                                    sorted_players_list_by_elo, 
                                                    round1_number, 
                                                    round1_start_date, 
                                                    round1_end_date, 
                                                    round1_matches)
        update = update_tour()
        update_opponents = PlayerModel.get_opponents(update, round1_number)
        return update_opponents

    def round_above_1(tour_info, round_number):
        list_players = []
        for i in tour_info.players[0]:
            list_players.append(i)
        list_matches = []
        for i in tour_info.rounds[0][3]:
            list_matches.append((i.player1[0], i.player1[0].surname, i.player2[0], i.player2[0].surname))
        matches_list = list()
        while len(list_players) != 0:
            i=0
            player1 = list_players[i]
            player2 = list_players[i+1]
            while player2.elo in player1.opponents:
                try:
                    i += 1
                    player2 = list_players[i+1]
                except IndexError:
                    player2 = list_players[1]
                    break
            matches_list.append(MatchModel(player1, player2))
            del list_players[0]
            del list_players[i]
        next_round = RoundModel(tour_info, round_number, tour_info.players, matches_list)
        round = next_round()
        update = TournamentModel.update_tour(    round.tour_info,
                                        round.players,
                                        round.number,
                                        round.start_date,
                                        round.end_date,
                                        round.matches
                                    )
        return update()

    def update_tour(tour_info, score_info):
        score = score_info.__dict__
        tour = tour_info.__dict__
        round_number = score['round_number']
        round_start_date = tour['rounds'][round_number-1][1]
        round_end_date = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        round_matches = score['matches']
        tour_informations = TournamentModel.update_tour_round(  tour_info, 
                                                                round_number, 
                                                                round_start_date, 
                                                                round_end_date, 
                                                                round_matches)
        tour_info = tour_informations()
        return tour_info
