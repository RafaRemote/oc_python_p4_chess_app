from packages.models.round import RoundModel
from packages.models.tournament import TournamentModel
# from packages.controllers.scoring import ScoringController




class RoundController:
    def __init__(self, name, players):
        self.name = name
        self.players = players

    def round1(self):
        rounds = RoundModel(self.name, self.players)
        res = rounds.round1()
        update_tournament = TournamentModel(None, None)
        up_tournament = update_tournament.add_a_round(res)
        # update_scoring = ScoringModel(up_tournament)
        return(up_tournament) #tournament with round 1 matches
        
    def round2(self, update):
        update_round_model = RoundModel(self.name, players=None)
        update_round_model.round2(update)
        






