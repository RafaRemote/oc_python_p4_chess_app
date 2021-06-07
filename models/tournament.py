class TournamentModel:
    def __init__(self, name, place):
        self.name = name
        self.place = place
        self.players = []
        self.rounds = []

    def add_player(self, player):
        self.players.append(player)

    def add_round(self, round):
        self.rounds.append(round)

