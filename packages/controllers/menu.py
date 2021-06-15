""" controller returning a view for the menus """
import time

from packages.controllers.player import PlayerController
from packages.controllers.round import RoundController
from packages.models.menu import MenuModel
from packages.models.tournament import TournamentModel
from packages.models.tournament import tournament_list
from packages.models.tournament import players
from packages.models.player import PlayerModel
from packages.views.tournament import TournamentView
from packages.views.player import PlayerView
from packages.views.scoring import ScoringView
from packages.views.utils.display_error import Error
from packages.views.utils.display_menu import display_menu
from packages.views.utils.display_get_choice import get_choice


class MenuController:
    def __init__(self, name, choice):
        self.name = name
        self.choice = choice

    def __call__(self):
        menu = MenuModel(self.name, self.choice)
        res = menu()
        if isinstance(res, list) and 'error' in res:
            error = Error(res)
            answer_from_error = error()
            if 'y' in answer_from_error:               
                restart = MenuModel('HomeMenu', choice=None)
                restart()
                # display_menu(restart().__dict__)
                # get_choice(answer_from_error[0], choice=None)

        elif res.__dict__['choice'] == 1:
            if len(tournament_list) > 0:
                error = Error(['error', self.__class__.__name__, 'Tournament infos already entered.'])
                if 'y' in error():
                    restart = MenuController('HomeMenu', choice=None)
                    restart()
                else:
                    print('Bye, bye...')
                    exit()
            tournmanent_inputs = TournamentView()
            tournament_model = TournamentModel(tournmanent_inputs(), obj_player=None)
            res = tournament_model()
            if isinstance(res, list) and 'error' in res:
                print('send', res)
                error = Error(res)
                if 'y' in error():
                    restart = MenuController('HomeMenu', choice=None)
                    restart()
                    
                else:
                    print('Bye, bye...')
                    exit()
            restart = MenuController('HomeMenu', choice=None)
            restart()

        elif res.__dict__['choice'] == 2:
            if len(tournament_list) == 0:
                error = Error(['error', self.__class__.__name__, 'You have to enter tournament informations first'])
                if 'y' in error():
                    restart = MenuController('HomeMenu', choice=None)
                    restart()
                else:
                    print('Bye, bye...')
                    exit()
            if len(players) > 0 and len(tournament_list) > 0:
                error = Error(['error', self.__class__.__name__, 'There is already a set of players.'])
                if 'y' in error():
                    rounds = RoundController(tournament_list[0].__dict__.get('name'), players)
                    res = rounds.round1()
                    print('MenuController have recieved the tournament with the round one')
                    time.sleep(2)
                    restart = MenuController('HomeMenu', choice=None)
                    restart()
                else:
                    print('Bye, bye...')
                    exit()
            player_inputs = PlayerView()
            res = player_inputs().__dict__.items()
            data_for_player_controller = PlayerController(res)
            data_for_player_controller()
            if res is not None:          
                rounds = RoundController()
                rounds()
                restart = MenuController('HomeMenu', choice=None)
                restart()
        
        elif res.__dict__['choice'] == 3:
            score_view = ScoringView(tournament_list)
            res = score_view.round_one()
            update_tournament = TournamentModel(None, None)
            update = update_tournament.update_round(res)
            round2 = RoundController(tournament_list[0].__dict__.get('name'), players=None)
            round2.round2(update)
            


            restart = MenuController('HomeMenu', choice=None)
            restart()

        else:
            display_menu(res.__dict__)
            answer = get_choice(self.name, self.choice)
            new_menu = MenuController(answer[0], answer[1])
            new_menu()

