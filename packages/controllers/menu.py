""" Menu controller """

from packages.controllers.tournament import TournamentController
from packages.models.welcome import WelcomeModel
from packages.models.menu import MenuModel
from packages.models.tournament import TournamentModel
from packages.models.player import PlayerModel
from packages.views.welcome import WelcomeView
from packages.views.input_player import InputPlayerView
from packages.views.ranking import RankingView
from packages.views.scoring import ScoringView
from packages.views.menu import MenuView
from packages.views.quit import QuitView
from packages.views.error import Error
from packages.views.round import RoundView
from packages.views.match import MatchView
from packages.views.info import InfoView
from packages.views.opponents import OpponentsView


class MenuController:
    """
    Class to handle the menu.
    ...

    Attributes
    ----------
    tour_info : instance
        instance of tournament

    Methods
    -------
    welcome():
        print a welcoming message when app starts.
    select_handler(self):
        handles the choice in the main menu
    manage_list_choice(self, choice):
        handles the choice in the menu for the list of tournaments
    manage_tour_details_choice(self, choice):
        handles the choice in the menu for one tournament

    """

    def __init__(self, tour_info):
        """
        Constructs all the necessary attributes for the menu object.

        Parameters
        ----------
            tour_info : instance
                instance of a tournament

        """

        self.tour_info = tour_info

    def welcome():
        """
        Calls WelcomeModel then calls WelcomeView with the return

        Parameters
        ----------
        None

        Returns
        -------
        calls the MenuController with no instance of tournament

        """

        welcome = WelcomeModel()
        welcomeview = WelcomeView(welcome.title, welcome.sub_title)
        welcomeview()
        menu = MenuController(tour_info=None)
        menu()

    def select_handler(self):
        """
        Handles the choice in the main menu.

        Parameters
        ----------
        None

        Returns
        -------
        depending on the choice:
            - calls: TournamentController():
                to construct a new tournament
            or
            - calls: TournamentModel.get_all_tournaments():
                to get the list of all the exising tournaments in the database

        """

        menu_model = MenuModel()
        menu_model()
        start_menu = menu_model().start_menu
        menu = MenuView(start_menu)
        choice = menu().choice
        if choice == '0':
            tournament = TournamentController()
            title = tournament()
            tour = TournamentModel.get_tournament(title)
            self.tour_info = tour
            menu = MenuController(self.tour_info)
            menu()
        elif choice == '1':
            tournaments_list = TournamentModel.get_all_tournaments()
            if len(tournaments_list) != 0:
                chosen_option = TournamentController.show_all()
                self.manage_list_choice(int(chosen_option))
            else:
                error = Error('No tournament created yet')
                error()
                menu = MenuController(self.tour_info)
                menu()
        else:
            error = Error('your choice is not in the list')
            error()

    def manage_list_choice(self, choice):
        """
        Handles the choice in the menu of the list of tournaments.

        Parameters
        ----------
        choice : int
            user input representing the choice in the menu, returned by TournamentController.show_all()

        Returns
        -------
        depending on the choice: calls models, controllers or views, no return.

        """

        checker_menu = MenuModel()
        menu_length = len(checker_menu.all_tournaments_menu) + len(TournamentModel.get_all_tournaments())
        if choice == menu_length - 2:
            menu = MenuController(self.tour_info)
            menu()
        elif choice == menu_length - 1:
            tournament = TournamentController()
            tournament()
            menu = MenuController(self.tour_info)
            menu()
        elif choice == menu_length:
            quit = QuitView('The app is shutting down.')
            quit()
        elif choice in range(1, menu_length-2):
            self.tour_info = TournamentModel.get_tournament_by_id(choice)
            option = TournamentController.show_one(self.tour_info)
            self.manage_tour_details_choice(option)
        else:
            error = Error('your choice is not in the list')
            error()
            menu = MenuController(self.tour_info)
            menu()

    def manage_tour_details_choice(self, choice):
        """
        Handles the choice in the menu for one tournament.

        Parameters
        ----------
        choice : str
            choice of the user in the menu, returned by TournamentController.show_one(self.tour_info)

        Returns
        -------
        depending on the choice: calls models, controllers or views, no return

        """

        if choice == '0':
            menu = MenuController(tour_info=None)
            menu()
        elif choice == '1':
            if len(PlayerModel.get_players(self.tour_info.title)) == 0:
                input_players = InputPlayerView()
                PlayerModel.add_players(input_players(), self.tour_info.title)
            elif len(PlayerModel.get_players(self.tour_info.title)) == 8:
                error = Error('There is already a set of players for this tournament')
                error()
            choice = TournamentController.show_one(self.tour_info)
            self.manage_tour_details_choice(choice)
        elif choice == '2':
            if len(PlayerModel.get_players(self.tour_info.title)) == 0:
                error = Error('No players added yet. First: add players, Second: start tournament')
                error()
                choice = TournamentController.show_one(self.tour_info)
                self.manage_tour_details_choice(choice)
            elif len(self.tour_info.rounds) > 0 and self.tour_info.rounds[-1].start_date is not None:
                error = Error('the current tournament did already start')
                error()
                choice = TournamentController.show_one(self.tour_info)
                self.manage_tour_details_choice(choice)
            else:
                TournamentModel.add_first_round_db(self.tour_info)
                self.tour_info = TournamentModel.get_tournament(self.tour_info.title)
                info = InfoView('First Round is starting now. You can check \'rounds details\' & \'matches details\'')
                info()
                choice = TournamentController.show_one(self.tour_info)
                self.manage_tour_details_choice(choice)
        elif choice == '3':
            self.tour_info = TournamentModel.get_tournament(self.tour_info.title)
            if len(PlayerModel.get_players(self.tour_info.title)) == 0:
                error = Error('No players added yet! You have to add players first.')
                error()
                choice = TournamentController.show_one(self.tour_info)
                self.manage_tour_details_choice(choice)
            elif len(self.tour_info.rounds) == 0:
                error = Error('You need to start the tournament first. Option 2.')
                error()
                choice = TournamentController.show_one(self.tour_info)
                self.manage_tour_details_choice(choice)
            elif len(self.tour_info.rounds) > 0 and self.tour_info.rounds[-1].end_date == '':
                error = Error('the current round is not finished.')
                error()
                choice = TournamentController.show_one(self.tour_info)
                self.manage_tour_details_choice(choice)
            elif len(self.tour_info.rounds) == 4 and self.tour_info.rounds[3].end_date != "":
                error = Error('All rounds have been played. This tournament is finished')
                error()
                choice = TournamentController.show_one(self.tour_info)
                self.manage_tour_details_choice(choice)
            else:
                round_number = str(TournamentModel.get_rounds_length(self.tour_info)+1)
                info = InfoView('matches for round ' + round_number + ' are getting prepared')
                info()
                TournamentController.add_round(self.tour_info)
                self.tour_info = TournamentModel.get_tournament(self.tour_info.title)
                choice = TournamentController.show_one(self.tour_info)
                self.manage_tour_details_choice(choice)
        elif choice == '4':
            if len(self.tour_info.rounds) == 0:
                error = Error('No round had been played yet.')
                error()
                choice = TournamentController.show_one(self.tour_info)
                self.manage_tour_details_choice(choice)
            elif len(self.tour_info.rounds) == 4 and self.tour_info.rounds[3].end_date != "":
                error = Error("All rounds have been already played")
                error()
                choice = TournamentController.show_one(self.tour_info)
                self.manage_tour_details_choice(choice)
            elif len(self.tour_info.rounds) <= 4:
                if self.tour_info.rounds[-1].end_date == "":
                    tournament = TournamentModel.get_tournament(self.tour_info.title)
                    score_inputs = ScoringView(tournament)
                    scores = score_inputs().new_matches
                    self.tour_info = TournamentModel.update_scores(self.tour_info, scores)
                    self.tour_info = TournamentModel.get_tournament(self.tour_info['title'])
                    choice = TournamentController.show_one(self.tour_info)
                    self.manage_tour_details_choice(choice)
                else:
                    error = Error('this round ended the: ' + self.tour_info.rounds[-1].end_date)
                    error()
                    choice = TournamentController.show_one(self.tour_info)
                    self.manage_tour_details_choice(choice)
                choice = TournamentController.show_one(self.tour_info)
                self.manage_tour_details_choice(choice)
            else:
                error = Error('All rounds have been alread played. The tournament is finished.')
                error()
                back = TournamentController.show_one(self.tour_info)
                self.manage_tour_details_choice(back)
        elif choice == '5':
            tournament = TournamentModel.get_tournament(self.tour_info.title)
            if len(tournament.rounds) == 0:
                error = Error('No round started yet')
                error()
                choice = TournamentController.show_one(self.tour_info)
                self.manage_tour_details_choice(choice)
            round = RoundView(tournament)
            round()
            choice = TournamentController.show_one(self.tour_info)
            self.manage_tour_details_choice(choice)
        elif choice == '6':
            if len(self.tour_info.rounds) == 0:
                error = Error('No round started yet -> no matches on the list')
                error()
                choice = TournamentController.show_one(self.tour_info)
                self.manage_tour_details_choice(choice)
            matches = MatchView(self.tour_info.rounds)
            matches()
            choice = TournamentController.show_one(self.tour_info)
            self.manage_tour_details_choice(choice)
        elif choice == '7':
            if len(PlayerModel.get_players(self.tour_info.title)) == 0:
                error = Error('No players found in the database. Add players first.')
                error()
                choice = TournamentController.show_one(self.tour_info)
                self.manage_tour_details_choice(choice)
            else:
                scores = PlayerModel.get_players_score(self.tour_info)
                ranking = RankingView(scores)
                new_elo = ranking()
                if new_elo[0] is None and new_elo[1] is None:
                    choice = TournamentController.show_one(self.tour_info)
                    self.manage_tour_details_choice(choice)
                else:
                    self.tour_info = PlayerModel.update_elo(self.tour_info, new_elo)
                    info = InfoView('Player\'s Elo has been updated')
                    info()
                    choice = TournamentController.show_one(self.tour_info)
                    self.manage_tour_details_choice(choice)
                choice = TournamentController.show_one(self.tour_info)
                self.manage_tour_details_choice(choice)
        elif choice == '8':
            if len(PlayerModel.get_players(self.tour_info.title)) == 0:
                error = Error('You need to add the players first.')
                error()
                choice = TournamentController.show_one(self.tour_info)
                self.manage_tour_details_choice(choice)
            opponents = PlayerModel.get_opponents(self.tour_info)
            opponents_view = OpponentsView(opponents)
            opponents_view()
            choice = TournamentController.show_one(self.tour_info)
            self.manage_tour_details_choice(choice)
        elif choice == '9':
            quit = QuitView('The app is shutting down')
            quit()
        else:
            error = Error('your choice is not in the list.')
            error()
            choice = TournamentController.show_one(self.tour_info)
            self.manage_tour_details_choice(choice)

    def __call__(self):
        """ calls self.select_handler(), no return """

        self.select_handler()
