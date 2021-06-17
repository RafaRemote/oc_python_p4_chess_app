""" docstrings """

from packages.views.scoring import ScoringView
from packages.controllers.round import RoundController


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
        tour_info = RoundController.update_tour(self.tour_info, score_inputs())
        return tour_info



