""" controller returning a view for the menus """
# import time

from packages.controllers.tournament import TournamentController
from packages.controllers.round import RoundController
from packages.controllers.scoring import ScoringController
from packages.controllers.ranking import RankingController
from packages.models.menu import MenuModel
from packages.views.menu import MenuView
from packages.views.round import RoundView
from packages.views.error import Error
from packages.views.quit import QuitView
from packages.views.opponents import OpponentsView

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
        round1 = RoundController(tour_info=self.tour_info,
                                 round_number=round_number,
                                 players=players
                                 )
        tour_info = round1.round1()     
        back_home = MenuController(tour_info=tour_info,
                                   name=home_name,
                                   choice=None
                                   )
        back_home()

    def add_round(self, round_number):
        score = ScoringController(tour_info=self.tour_info,
                                  round_number=round_number
                                  )
        tour_info = score()
        next_round = RoundController.round_above_1(tour_info, round_number)
        updated_tour_info = next_round()
        back_home = MenuController(tour_info=updated_tour_info,
                                   name=home_name,
                                   choice=None
                                   )
        back_home()

    def manage_error(self, error):
        if error.option == 'y':
            menu = MenuController(self.tour_info, name=home_name, choice=None)
            menu()
        else:
            quit = QuitView('Bye, bye')
            quit()

    def __call__(self):
        if self.name == home_name:
            menu = MenuModel(name=home_name.lower(),
                             choice=self.choice
                             )
            if self.tour_info is not None:
                name = self.tour_info().__dict__.get('tour_title') + ' Chess Tournament' + ' MENU '
            else:
                name = None
            choice_list = menu().__dict__.get('choice_list')
            menuview = MenuView(name=name,
                                choice_list=choice_list,
                                choice=None
                                )
            user_input = menuview()
            user_choice = int(user_input.__dict__.get('choice'))
            if user_choice == 0 and self.tour_info is None :
                tournament = TournamentController()
                self.tour_info = tournament()
                menu = MenuController(tour_info=self.tour_info, name=self.name, choice=None)
                menu()
            elif user_choice == 0 and self.tour_info is not None:
                error = Error('Details of the tournament are already entered')
                err = error()
                self.manage_error(self.tour_info, err)
                
            elif self.tour_info is not None:
                len_rounds = len(self.tour_info.__dict__.get('rounds'))
                if user_choice == 1 and len_rounds == 0:
                    self.manage_choice()
                elif user_choice == 1 and len_rounds >= 0:
                    error = Error('There is already a set of user.')
                    self.manage_error(self.tour_info, error())
                elif user_choice == 2 and len_rounds == 1:
                    round = 1
                    self.add_round(round)
                elif user_choice == 3 and len_rounds == 2:
                    round = 2
                    self.add_round(round)
                elif user_choice == 4 and len_rounds == 3:
                    round = 3
                    self.add_round(round)
                elif user_choice == 5 and len_rounds == 4:
                    round = 4 
                    self.add_round(round)
                elif user_choice == 6:
                    choice = "score"
                    player_info = RankingController(tour_info=self.tour_info,
                                                    choice=choice)
                    res = player_info()
                    if res is None:
                        back_home = MenuController(tour_info=self.tour_info,
                                                name=home_name,
                                                choice=None
                                                )
                        back_home()
                elif user_choice == 7:
                    choice = "alpha"
                    player_info = RankingController(tour_info=self.tour_info,
                                                    choice=choice)
                    res = player_info()
                    if res is None:
                        back_home = MenuController(tour_info=self.tour_info,
                                                name=home_name,
                                                choice=None
                                                )
                        back_home()

                elif user_choice == 8:
                    show_opponents = OpponentsView(self.tour_info)
                    res = show_opponents()
                    if res == 'y':
                        back_home = MenuController(tour_info=self.tour_info,
                                                name=home_name,
                                                choice=None
                                                )
                        back_home()
                elif user_choice == 9:
                    show_opponents = RoundView(self.tour_info)
                    res = show_opponents()
                    if res == 'y':
                        back_home = MenuController(tour_info=self.tour_info,
                                                name=home_name,
                                                choice=None
                                                )
                        back_home()

                else:
                    error = Error('Attention: you need to enter the scores round after round')
                    err = error()
                    self.manage_error(err)
            else:
                error = Error('no tournament existing yet')
                err = error()
                self.manage_error(err)
