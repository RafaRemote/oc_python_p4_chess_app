""" controller for the tournament """

from packages.views.input_tournament import InputTournamentView
from packages.views.tournaments import TournamentsView
from packages.views.tournament import TournamentView
from packages.models.menu import MenuModel
from packages.models.match import MatchModel
from packages.models.tournament import TournamentModel
from packages.models.player import PlayerModel


from tinydb import TinyDB, Query
db = TinyDB('db.json')
Tournament = Query()


class TournamentController:
    def __init__(self):
        self.tour_info = None

    def add_players(tour_info, serialized_players):
        tour = TournamentModel.add_players(tour_info, serialized_players)
        return tour

    def add_round(tour_info):
        players_score = PlayerModel.get_players_score(tour_info.title)
        players_sorted = sorted(players_score, key=lambda x: (x[2], x[0].elo), reverse=True)
        players = list()
        [players.append(i[0]) for i in players_sorted]
        matches = list()
        while len(players) > 0:
            i = 0
            player1 = players[i]
            player2 = players[i+1]
            while TournamentController.check_opponents(tour_info.title, player1, player2):
                try:
                    i += 1
                    player2 = players[i+1]
                except IndexError:
                    i = 0
                    player2 = players[1]
                    break
            player1.opponents.append(player2.surname)
            player2.opponents.append(player1.surname)
            matches.append(MatchModel(player1, player2))
            del players[0]
            del players[i]
        TournamentModel.add_round(tour_info, matches)
        return

    def check_opponents(title, player1, player2):
        players_opponents = PlayerModel.get_opponents(title)
        for i in players_opponents:
            if i.surname == player1.surname:
                if player2.surname in i.opponents:
                    return True

    def show_one(tour_info):
        menu = MenuModel()
        tournament_menu = menu.tournament_menu
        choice = TournamentView(tour_info, tournament_menu)
        return choice()

    def show_all():
        menu = MenuModel()
        all_tournaments_menu = menu.all_tournaments_menu
        tournaments_list = TournamentModel.get_all_tournaments_db_doc()
        show_tournaments = TournamentsView(tournaments_list, all_tournaments_menu)
        choice = show_tournaments()
        return choice

    def __call__(self):
        tournament = InputTournamentView()
        tour_inputs = tournament()
        tournament = TournamentModel(place=tour_inputs.place,
                                     title=tour_inputs.title,
                                     time_control=tour_inputs.time_control,
                                     description=tour_inputs.description,
                                     start_date=None,
                                     rounds=[]
                                     )
        new_tour = tournament()
        return new_tour.title
