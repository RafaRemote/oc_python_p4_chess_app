""" controller returning a view for the menus """

import time
import datetime

from packages.controllers.tournament import TournamentController
from packages.views.ranking import RankingView
from packages.views.scoring import ScoringView
from packages.views.menu import MenuView
from packages.views.quit import QuitView
from packages.views.error import Error
from packages.views.round import RoundView
from packages.views.match import MatchView
from packages.models.menu import MenuModel
from packages.models.match import MatchModel
from packages.models.tournament import tournaments_list


class MenuController:
    def __init__(self, tour_info):
        self.tour_info = tour_info

    def select_handler(self):
        menu_model = MenuModel()
        start_menu = menu_model().start_menu
        menu = MenuView(start_menu)
        choice = menu().choice
        if choice == '0':
            tournament = TournamentController()
            tour_info = tournament()
            menu = MenuController(tour_info)
            menu()
        elif choice == '1' and self.tour_info is not None:
            chosen_option = TournamentController.show_all()
            self.manage_list_choice(int(chosen_option))
        else:
            error = Error('No tournament created yet')
            error()
            menu = MenuController(self.tour_info)
            menu()

    def manage_list_choice(self, choice):
        """ handle choice in list of tournaments
        """
        checker_menu = MenuModel()
        menu_length = len(checker_menu.all_tournaments_menu)
        if choice == 0:
            menu = MenuController(self.tour_info)
            menu()
        elif choice == 1:
            tournament = TournamentController()
            tournament()
            menu = MenuController(self.tour_info)
            menu()
        elif choice == menu_length - 1:
            quit = QuitView('The app is shutting down.')
            quit()
        elif choice in range(0, menu_length-1):
            self.tour_info = tournaments_list[int(choice)-2]
            choice = TournamentController.show_one(self.tour_info)
            self.manage_tour_details_choice(choice)
        else:
            error = Error('your choice is not in the list')
            error()

    def manage_tour_details_choice(self, choice):
        """ handle choice in list of options for each tournament
        """
        if choice == '0':
            TournamentController.show_all()
            choice = TournamentController.show_one(self.tour_info)
            self.manage_tour_details_choice(choice)
        elif choice == '1':
            print('this version contains a ready set of players')
            input('press return to continue')
            choice = TournamentController.show_one(self.tour_info)
            self.manage_tour_details_choice(choice)
        elif choice == '2':
            if len(self.tour_info.rounds) == 4 and self.tour_info.rounds[3].end_date is not None:
                error = Error("All rounds have been already played")
                error()
                choice = TournamentController.show_one(self.tour_info)
                self.manage_tour_details_choice(choice)

            elif len(self.tour_info.rounds) <= 4:
                round_number = len(self.tour_info.rounds)
                matches = self.tour_info.rounds[round_number-1].matches
                score_inputs = ScoringView(round_number, matches)
                score_inputs()
                self.tour_info.rounds[round_number-1].matches = []
                for i in score_inputs.new_matches:
                    self.tour_info.rounds[round_number-1].matches.append(MatchModel(i[0], i[1], i[2], i[3]))
                    i[0].opponents.append(i[1])
                    i[1].opponents.append(i[0])
                self.tour_info.rounds[round_number-1].end_date = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
                TournamentController.add_round(self.tour_info)
                back = TournamentController.show_one(self.tour_info)
                self.manage_tour_details_choice(back)
            else:
                error = Error('All rounds have been alread played. The tournament is finished.')
                error()
                back = TournamentController.show_one(self.tour_info)
                self.manage_tour_details_choice(back)
        elif choice == '3':
            round = RoundView(self.tour_info.rounds)
            round()
            #  instead of ...
            choice = TournamentController.show_one(self.tour_info)
            self.manage_tour_details_choice(choice)
        elif choice == '4':
            matches = MatchView(self.tour_info.rounds)
            matches()
            choice = TournamentController.show_one(self.tour_info)
            self.manage_tour_details_choice(choice)
        elif choice == '5':
            ranking = RankingView(self.tour_info.players)
            ranking()
            choice = TournamentController.show_one(self.tour_info)
            self.manage_tour_details_choice(choice)
        elif choice == '6':
            quit = QuitView('The app is shutting down')
            quit()
            time.sleep(2)
        else:
            error = Error('your choice is not in the list.')
            error()
            choice = TournamentController.show_one(self.tour_info)
            self.manage_tour_details_choice(choice)

    def __call__(self):
        self.select_handler()
