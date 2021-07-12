""" controller for the tournament """

from tinydb import TinyDB, Query
db = TinyDB('db.json')
Tournament = Query()

from packages.views.input_tournament import InputTournamentView
from packages.views.tournaments import TournamentsView
from packages.views.tournament import TournamentView
from packages.models.menu import MenuModel
from packages.models.match import MatchModel
from packages.models.round import RoundModel
from packages.models.tournament import TournamentModel, tournaments_list


class TournamentController:
    def __init__(self):
        self.tour_info = None

    def add_players(tour_info, serialized_players):
        tour = TournamentModel.add_players(tour_info, serialized_players)
        return tour

    def add_first_round(tour_info):
        players = tour_info['players']
        players_elo_sorted = sorted(players, key=lambda x: x['elo'], reverse=True)
        high_group = players_elo_sorted[:4]
        low_group = players_elo_sorted[4:]
        matches = []
        for i in range(0, len(high_group)):
            matches.append(MatchModel(high_group[i],
                            low_group[i]
                            ))
        tour_info['rounds'].append([RoundModel(matches, 1)])
        return tour_info

    def add_round(tour_info):
        if len(tour_info.rounds) < 4:
            players_list = list()
            for i in tour_info.players:
                players_list.append(i)
            players = sorted(players_list, key=lambda x: (x.score, x.elo), reverse=True)
            matches = list()
            while len(players) != 0:
                i = 0
                player1 = players[i]
                player2 = players[i+1]
                while player2.unique_id in player1.opponents:
                    try:
                        i += 1
                        player2 = players[i+1]
                    except IndexError:
                        player2 = players[1]
                        break
                matches.append(MatchModel(player1, player2))
                del players[0]
                del players[i]
            next_round = RoundModel(matches, len(tour_info.rounds)+1)
            tour_info.rounds.append(next_round)
            return
        elif len(tour_info.rounds) == 4:
            return

    def show_one(tour_info):
        menu = MenuModel()
        tournament_menu = menu.tournament_menu
        tournament = TournamentView(tour_info, tournament_menu)
        return tournament()

    def show_all():
        menu = MenuModel()
        all_tournaments_menu = menu.all_tournaments_menu
        tournaments_list.reverse()
        show_tournaments = TournamentsView(tournaments_list, all_tournaments_menu)
        choice = show_tournaments()
        return choice

    def __call__(self):
        tournament = InputTournamentView()
        tour_inputs = tournament()
        tour_place = tour_inputs.tour_place
        tour_title = tour_inputs.tour_title
        tour_time_control = tour_inputs.tour_time_control
        tour_description = tour_inputs.tour_description
        tour_start_date = None
        rounds = []
        players = []
        tournament = TournamentModel(tour_place,
                                     tour_title,
                                     tour_time_control,
                                     tour_description,
                                     tour_start_date,
                                     rounds,
                                     players
                                     )
        new_tournament = tournament()
        self.tour_info = new_tournament
        return self