""" controller returning a view for the menus """
from packages.controllers.player import PlayerController
from packages.models.menu import MenuModel
from packages.models.tournament import TournamentModel
from packages.models.player import PlayerModel
from packages.views.tournament import TournamentView
from packages.views.player import PlayerView
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
                restart = MenuModel(answer_from_error[0], choice=None)
                display_menu(restart().__dict__)
                get_choice(answer_from_error[0], choice=None)

        elif res.__dict__['choice'] == 1:
            tournmanent_inputs = TournamentView()
            tournament_model = TournamentModel(tournmanent_inputs())
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

        elif res.__dict__['choice'] == 2:
            player_inputs = PlayerView()
            new_player = PlayerController(player_inputs())
            new_player()

        else:
            print(res.__dict__)
            display_menu(res.__dict__)
            answer = get_choice(self.name, self.choice)
            new_menu = MenuController(answer[0], answer[1])
            new_menu()

