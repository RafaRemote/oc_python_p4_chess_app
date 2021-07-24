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
    """
    A class to handle the tournament.

    ...

    Attributes
    ----------
    tour_info : instance
        instance of tournament

    Methods
    -------
    add_players(tour_info, serialized_players):
        calls TournamentModel.add_players(tour_info, serialized_players)
    add_round(tour_info):
        first round has specific rules
        next rounds have other rules
        this function calculates the composition of a round after the first one
    """
    def __init__(self):
        """
        Constructs all the necessary attributes for the menu object.

        Parameters
        ----------
        none
        """

        self.tour_info = None

    def add_players(tour_info, serialized_players):
        """
        Calls TournamentModel to add players to the database

        Parameters
        ----------
        tour_info:
            instance of the current tournament
        serialized_players:
            list of players to add to the database

        Returns
        -------
        tournament instance
        """

        tour = TournamentModel.add_players(tour_info, serialized_players)
        return tour

    def add_round(tour_info):
        """
        Constructs the composition of a round after the first one

        Parameters
        ----------
        tour_info: instance
            instance of tournament

        Returns
        -------
        none
        """

        players_score = PlayerModel.get_players_score(tour_info)
        players_sorted = sorted(players_score, key=lambda x: (x[2], x[0].elo), reverse=True)
        players = list()
        [players.append(i[0]) for i in players_sorted]
        matches = list()
        while len(players) > 0:
            i = 0
            player1 = players[i]
            player2 = players[i+1]
            while PlayerModel.check_opponents(tour_info, player1, player2):
                try:
                    i += 1
                    player2 = players[i+1]
                except IndexError:
                    i = 0
                    player2 = players[1]
                    break
            matches.append(MatchModel(player1, player2))
            del players[0]
            del players[i]
        TournamentModel.add_round(tour_info, matches)
        return

    def show_one(tour_info):
        """
        Calls a model of menu for one tournament then a view

        Parameters
        ----------
        tour_info: instance
            instance of tournament

        Returns
        -------
        choice of user in menu for one tourmaent
        """
        menu = MenuModel()
        tournament_menu = menu.tournament_menu
        choice = TournamentView(tour_info, tournament_menu)
        return choice()

    def show_all():
        """
        Calls a model of menu for list of tournaments then a view

        Parameters
        ----------
        none

        Returns
        -------
        choice of user in list of tournaments menu
        """
        menu = MenuModel()
        all_tournaments_menu = menu.all_tournaments_menu
        tournaments_list = TournamentModel.get_all_tournaments_db_doc()
        show_tournaments = TournamentsView(tournaments_list, all_tournaments_menu)
        choice = show_tournaments()
        return choice

    def __call__(self):
        """
        on call: calls a view for user inputs for a tournament

        Parameters
        ----------
        none

        Returns
        -------
        tournament instance
        """
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
