from packages.models.player import PlayerModel
from packages.models.tournament import TournamentModel

class PlayerController:
    def __init__(self, obj_players):
        self.players = obj_players

    def __call__(self):
        player = []
        for k, l in self.players:
            for v in l:
                player.append(v)
        sequence = 8
        for i in range(0,int(len(player)/5)):
            name = player[i] 
            surname = player[i+ sequence] 
            year = player[i+ 2*sequence]
            gender = player[i+ 3*sequence]
            elo = player[i+ 4*sequence]
            added_player = PlayerModel([name, surname, year, gender, elo])
            update_tournament = TournamentModel(obj_from_controller=None, obj_player=added_player())
            update_tournament()
            i += 8




