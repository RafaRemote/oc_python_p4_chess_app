""" main controller managing the choices in the menus """


from packages.views.welcome import WelcomeView
from packages.models.player import PlayerModel
from packages.views.input_player import InputPlayerView
import time
import datetime

from packages.controllers.tournament import Tournament, TournamentController
from packages.views.ranking import RankingView
from packages.views.scoring import ScoringView
from packages.views.menu import MenuView
from packages.views.quit import QuitView
from packages.views.error import Error
from packages.views.round import RoundView
from packages.views.match import MatchView
from packages.views.info import InfoView
from packages.views.opponents import OpponentsView 
from packages.models.welcome import WelcomeModel
from packages.models.menu import MenuModel
from packages.models.match import MatchModel
from packages.models.tournament import TournamentModel, tournaments_list


class MenuController:
    def __init__(self, tour_info):
        self.tour_info = tour_info

    def welcome():
        welcome = WelcomeModel()
        welcomeview = WelcomeView(welcome.title, welcome.sub_title)
        welcomeview()
        menu = MenuController(tour_info=None)
        menu()


    def select_handler(self):
        menu_model = MenuModel()
        menu_model()
        start_menu = menu_model().start_menu
        menu = MenuView(start_menu)
        choice = menu().choice
        if choice == '0':
            tournament = TournamentController()
            self.tour_info = tournament().__dict__.get('tour_info').__dict__
            menu = MenuController(self.tour_info)
            menu()
        elif choice == '1':
            tour_list = TournamentModel.update_tour_list(self.tour_info)
            if len(tour_list) > 0 :
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
        elif choice in range(2, menu_length-1):
            self.tour_info = tournaments_list[(choice*-1)+1]
            # deserialized_players = list()
            # for i in self.tour_info['players']:
            #      deserialized_players.append(PlayerModel(name=i['name'],
            #                                              surname=i['surname'],
            #                                              year_birth=i['year_birth'],
            #                                              gender=i['gender'],
            #                                              elo=i['elo']))
            # self.tour_info['players'] = []
            # for i in deserialized_players:
            #     self.tour_info['players'].append(i)
            option = TournamentController.show_one(self.tour_info)
            self.manage_tour_details_choice(option)
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
            if self.tour_info['players'] is not None and len(self.tour_info['players']) == 8:
                error = Error('There is already a set of players for this tournament')
                error()
                choice = TournamentController.show_one(self.tour_info)
                self.manage_tour_details_choice(choice)  
            else:         
                input_players = InputPlayerView()
                players = input_players().__dict__
                serialized_players = list()
                i = 0
                while i < 8:
                    serialized_players.append({
                        'name': players['name'][i],
                        'surname' : players['surname'][i],
                        'year_birth': players['year_birth'][i],
                        'gender': players['gender'][i],
                        'elo': players['elo'][i],
                        'score': 0.0
                    })
                    i += 1
            tour_info = TournamentController.add_players(self.tour_info, serialized_players)
            choice = TournamentController.show_one(tour_info)
            self.manage_tour_details_choice(choice)
        elif choice == '2':
            if len(self.tour_info['players']) == 0:
                error = Error('No players added yet. First: add players, Second: start tournament')
                error()
                choice = TournamentController.show_one(self.tour_info)
                self.manage_tour_details_choice(choice)
            # et la si du coup len player plsu de 0 len round sup a 1 alors erreur deja commence
            else:
                TournamentModel.add_first_round_db(self.tour_info)
                tour = TournamentController.add_first_round(self.tour_info)
                self.tour_info = tour
                print(self.tour_info)
                exit()
                info = InfoView('First Round is starting now. You can check \'rounds details\' & \'matches details\'')
                info()
                choice = TournamentController.show_one(self.tour_info)
                self.manage_tour_details_choice(choice)  
        elif choice == '3':
            if len(self.tour_info['rounds']) == 0:
                error = Error('No round had been played yet.')
                error()
                choice = TournamentController.show_one(self.tour_info)
                self.manage_tour_details_choice(choice)
            elif len(self.tour_info['rounds']) == 4 and self.tour_info['rounds'][3].end_date is not None:
                error = Error("All rounds have been already played")
                error()
                choice = TournamentController.show_one(self.tour_info)
                self.manage_tour_details_choice(choice)
            # call score input (ScoringView) if the current round is max the 4th one
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
        elif choice == '4':
            if len(self.tour_info['rounds']) == 0:
                error = Error('No round started yet')
                error()
                choice = TournamentController.show_one(self.tour_info)
                self.manage_tour_details_choice(choice)
            round = RoundView(self.tour_info.rounds)
            round()
            #  instead of ...
            choice = TournamentController.show_one(self.tour_info)
            self.manage_tour_details_choice(choice)
        elif choice == '5':
            if len(self.tour_info['rounds']) == 0:
                error = Error('No round started yet -> no matches on the list')
                error()
                choice = TournamentController.show_one(self.tour_info)
                self.manage_tour_details_choice(choice)
            matches = MatchView(self.tour_info.rounds)
            matches()
            choice = TournamentController.show_one(self.tour_info)
            self.manage_tour_details_choice(choice)
        elif choice == '6':
            if len(self.tour_info['players']) == 0:
                error = Error('No players found in the database. Add players first.')
                error()
                choice = TournamentController.show_one(self.tour_info)
                self.manage_tour_details_choice(choice)
            else:
                players = TournamentModel.get_players()
                ranking = RankingView(players)
                res = ranking()
                PlayerModel.update_player_score(res)
                choice = TournamentController.show_one(self.tour_info)
                self.manage_tour_details_choice(choice)
        elif choice == '7':
            if len(self.tour_info['players']) == 0:
                error = Error('You need to add the players first.')
                error()
                choice = TournamentController.show_one(self.tour_info)
                self.manage_tour_details_choice(choice)
            opponents = OpponentsView(self.tour_info)
            opponents()
            choice = TournamentController.show_one(self.tour_info)
            self.manage_tour_details_choice(choice)
        elif choice == '8':
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
