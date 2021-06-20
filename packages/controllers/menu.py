""" controller returning a view for the menus """
# import time

from packages.controllers.round import RoundController
from packages.controllers.scoring import ScoringController
from packages.controllers.ranking import RankingController
from packages.models.menu import MenuModel
from packages.views.menu import MenuView
from packages.views.error import Error
from packages.views.quit import QuitView

home_name = 'HomeMenu'


class MenuController:
    def __init__(self, tour_info, name, choice):
        self.tour_info = tour_info
        self.name = name
        self.choice = choice

    def manage_choice(self):
        round_number = '1'
        players = {
                'name': ['Simpsons', 'Simpsons', 'Simpsons', 'Simpsons', 'Simpsons', 'Szyslak', 'Burns', 'Flanders'],
                'surname': ['Homer', 'Marge', 'Bart', 'Lisa', 'Maggie', 'Moe', 'Montgomery', 'Ned'],
                'year_of_birth': ['1970', '1980', '2010', '2010', '2019', '1965', '1900', '1900'],
                'gender': ['m', 'w', 'm', 'w', 'w', 'm', 'm', 'm'],
                'elo': ['1100', '1900', '1300', '3000', '1050', '1500', '2000', '6000']
                }
        round1 = RoundController(self.tour_info, round_number, players)
        round = round1.round1()
        back_home = MenuController(tour_info=round, name=home_name, choice=None)
        back_home()

    def enter_1stround_score(self, round_number):
        round_number = round_number-1
        score = ScoringController(self.tour_info, round_number)
        tour_info = score()
        back_home = MenuController(tour_info=tour_info, name=home_name, choice=None)
        back_home()

    def enter_round_score(self, round_number):
        round_number = round_number-1
        score = RoundController.round_above_1(self.tour_info, round_number)
        updated_tour = score()
        scoring = ScoringController(updated_tour, round_number)
        scoring()
        tour_info = scoring.__dict__['tour_info']
        back_home = MenuController(tour_info, name=home_name, choice=None)
        back_home()

    def __call__(self):
        if self.name == home_name:
            menu = MenuModel(home_name.lower(), self.choice)
            name = self.tour_info().__dict__.get('tour_title') + ' Chess Tournament' + ' MENU '
            choice_list = menu().__dict__.get('choice_list')
            menuview = MenuView(name, choice_list, choice=None)
            user_input = menuview()
            user_choice = int(user_input.__dict__.get('choice'))
            len_rounds = len(self.tour_info.__dict__.get('rounds'))
            if user_choice == 1 and len_rounds == 0:
                self.manage_choice()
            elif user_choice == 1 and len_rounds > 0:
                error = Error('There is already a set of user.')
                if error().__dict__.get('option') == 'y':
                    menu = MenuController(tour_info=self.tour_info, name=home_name, choice=None)
                    menu()
                else:
                    quit = QuitView('See you soon!')
                    quit()
            elif int(user_choice) in range(2, 10) and len_rounds == 0:
                error = Error('You need to add players first. Please select \'1\'')
                if error().__dict__.get('option') == 'y':
                    menu = MenuController(tour_info=self.tour_info, name=home_name, choice=None)
                    menu()
                else:
                    quit = QuitView('See you soon!')
                    quit()
            elif user_choice == 2 and len_rounds == 1:
                self.enter_1stround_score(user_choice)
            elif user_choice == 3 and len_rounds == 1:
                self.enter_round_score(user_choice)
            elif user_choice == 4 and len_rounds == 2:
                self.enter_round_score(user_choice)
            elif user_choice == 5 and len_rounds == 3:
                self.enter_round_score(user_choice)
            elif user_choice == 6:
                player_info = RankingController(self.tour_info)
                res = player_info()
                if res is None:
                    back_home = MenuController(self.tour_info, name=home_name, choice=None)
                    back_home()
            else:
                error = Error('Attention please: you need to enter the scores round after round')
                if error().__dict__.get('option') == 'y':
                    menu = MenuController(tour_info=self.tour_info, name=home_name, choice=None)
                    menu()
                else:
                    quit = QuitView('See you soon!')
                    quit()
