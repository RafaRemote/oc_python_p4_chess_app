from models.tournament import TournamentModel
from models.player import PlayerModel
from views.tournament import get_tournament_name
from utils.error import print_error

players = [
            PlayerModel('Fifi', 40),
            PlayerModel('Riri', 30),
            PlayerModel('Loulou', 90),
            PlayerModel('Donald', 10)
]

class TournamentController:
    def __init__(self):
        self.tournament = None

    def new_tournament(self):
        name = self.get_name()
        place = "Paris"
        self.tournament = TournamentModel(name, place)
        for i in range(8):
            name = self.get_player_name()
            elo = self.get_player_elo()
            player = PlayerModel(name, elo)
            self.tournament.add_player(player)
        self.tournament.players = players

    def get_name():
        name = get_tournament_name()
        while not name.isalpha():
            print_error('le nom contient des chiffres')
            name = get_tournament_name()
        return name

    

