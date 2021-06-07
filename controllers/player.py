from views.player import get_player_name, get_player_elo
from views.tournament import get_tournament_name
from models.tournament import TournamentModel
from models.player import PlayerModel
from .tournament import players
from utils.error import print_error


class PlayerController:
    def __init__(self):
        self.name = None
        self.elo = None

    def new_player(self):
        name = self.get_name()
        elo = self.get_elo()
        players.ppend.PlayerModel(name, elo)

    def get_name():
        name = get_player_name()
        while not name.isalpha():
            print_error('le nom contient des chiffres')
            name = get_tournament_name()
        return name

    def get_elo():
        elo = get_player_elo()
        while not elo.isnumeric():
            print_error('Veuillez indiquer un chiffre ')


    
