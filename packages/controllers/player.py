from packages.views.player import get_player_name, get_player_elo
from packages.views.tournament import get_tournament_name
from packages.models.tournament import TournamentModel
from packages.models.player import PlayerModel
from .tournament import players



class PlayerController:
    def __init__(self):
        pass

    def __call__(self):
        print('i got', self.__dict__)
    
