""" docstrings """

from packages.views.scoring import ScoringView
from packages.controllers.round import RoundController
from packages.models.match import MatchModel


class ScoringController:
    def __init__(self, tour_info, round_number):
        self.tour_info = tour_info
        self.round_number = int(round_number)
        self.matches = self.get_matches()

    def get_matches(self):
        matches = self.tour_info.__dict__.get('rounds')[self.round_number-2][3]
        return matches

    def __call__(self):
        score_inputs = ScoringView(self.round_number, self.matches)
        inputs = score_inputs()
        list_matches = [] 
        for i in inputs.matches:
            player1 = i.player1[0]
            score1 = i.player1[0].score
            player2 = i.player2[0]
            score2 = i.player2[0].score
            list_matches.append(MatchModel(player1, player2, score1, score2))
        inputs.matches = []
        inputs.matches = list_matches
        tour_info = RoundController.update_tour(self.tour_info, inputs)
        return tour_info
