""" controller returning a view for the menus """
import time

# from packages.controllers.player import PlayerController
# from packages.controllers.round import RoundController
from packages.models.menu import MenuModel
from packages.views.menu import MenuView
from packages.models.tournament import TournamentModel
from packages.views.tournament import TournamentView

# from packages.models.tournament import tournament_list
# from packages.models.tournament import players
# from packages.models.player import PlayerModel

from packages.views.player import PlayerView
# from packages.views.scoring import ScoringView
from packages.views.utils.display_error import Error
# from packages.views.utils.display_menu import display_menu
# from packages.views.utils.display_get_choice import get_choice


class MenuController:
    def __init__(self, name, choice):
        self.name = name
        self.choice = choice


    def manage_choice(self, user_choice):
        if user_choice == '1':
            # check in the DB if the tournament does already exist or not
            tournaments = TournamentView()
            tour_inputs = tournaments().__dict__
            name = tour_inputs['name']
            time_control = tour_inputs['time_control']
            description = tour_inputs['description']
            date = tour_inputs['date']
            tournament = TournamentModel(name, time_control, description, date)
            tournament()
            back_home = MenuController(name='HomeMenu', choice=None)
            back_home()
        elif user_choice == '2':

            # error = Error(['error', self.__class__.__name__, 'You have to enter tournament informations first'])
            # if 'y' in error():
            #     restart = MenuController('HomeMenu', choice=None)
            #     restart()
            # else:
            #     print('Bye, bye...')
            #     exit()
       
            player_inputs = PlayerView()
            res = player_inputs().__dict__.items()
            data_for_player_controller = PlayerController(res)
            data_for_player_controller()
            if res is not None:          
                rounds = RoundController()
                rounds()
                restart = MenuController('HomeMenu', choice=None)
                restart()








    def __call__(self):
        if self.name == 'HomeMenu':
            menu = MenuModel(self.name.lower(), self.choice)
            name = menu().__dict__.get('name')
            choice_list = menu().__dict__.get('choice_list')
            menuview = MenuView(name, choice_list, choice=None)
            user_input = menuview()
            self.manage_choice(user_input)
            exit()
            



            
        # menu = MenuModel(self.name, self.choice)
        # res = menu()
        # print(res.__dict__['name'])
        # name = res.__dict__.get('name')
        # options = res.__dict__.get('menu')
        # menuview = MenuView(name, options)
        # choice = menuview()
        # self.choice = choice.__dict__['choice']
        # if self.choice == '1':
        #     print('YES')
        #     check_tournament = TournamentModel()
        #     tournament_name = check_tournament()
            
        #     exit()
            
            
            # 


                # error = Error('error', self.__class__.__name__, 'Tournament infos already entered.')
                # if 'y' in error():
                #     restart = MenuController('HomeMenu', choice=None)
                #     restart()
                # else:
                #     print('Bye, bye...')
                #     exit()
            
            
            # res = tournament_model()
            # if isinstance(res, list) and 'error' in res:
            #     print('send', res)
            #     error = Error(res)
            #     if 'y' in error():
            #         restart = MenuController('HomeMenu', choice=None)
            #         restart()
                    
        #         else:
        #             print('Bye, bye...')
        #             exit()
        #     restart = MenuController('HomeMenu', choice=None)
        #     restart()

        # elif res.__dict__['choice'] == 2:
       
        
        # elif res.__dict__['choice'] == 3:
        #     score_view = ScoringView(tournament_list)
        #     res = score_view.round_one()
        #     update_tournament = TournamentModel(None, None)
        #     update = update_tournament.update_round(res)
        #     round2 = RoundController(tournament_list[0].__dict__.get('name'), players=None)
        #     round2.round2(update)
            


        #     restart = MenuController('HomeMenu', choice=None)
        #     restart()

        # else:
        #     display_menu(res.__dict__)
        #     answer = get_choice(self.name, self.choice)
        #     new_menu = MenuController(answer[0], answer[1])
        #     new_menu()

