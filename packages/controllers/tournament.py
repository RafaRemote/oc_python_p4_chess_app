""" docstrings """

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

    def add_tournament(self, tour):
        if tour.tour_title not in [title.tour_title for title in tournaments_list]:
            tournaments_list.append(tour)

    def add_first_round(self):
        if len(self.tour_info.rounds) == 0:
            players = self.tour_info.players
            players_elo_sorted = sorted(players, key=lambda x: x.elo, reverse=True)
            high_group = players_elo_sorted[:4]
            low_group = players_elo_sorted[4:]
            matches = []
            for i in range(0, len(high_group)):
                matches.append(MatchModel(high_group[i], low_group[i]))
            round = RoundModel(matches, 1)
            self.tour_info.rounds.append(round)

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
                while player2.elo in player1.opponents:
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
        tournament = TournamentModel(tour_place,
                                     tour_title,
                                     tour_time_control,
                                     tour_description,
                                     )
        new_tournament = tournament()
        self.add_tournament(new_tournament)
        self.tour_info = new_tournament
        self.add_first_round()
        return self
