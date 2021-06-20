""" docstrings """

from packages.views.tournament import TournamentView
from packages.models.tournament import TournamentModel


class TournamentController:
    def __init__(self):
        self.tour_title = None
        self.tour_time_control = None
        self.tour_description = None
        self.tour_start_date = None

    def __call__(self):
        tournaments = TournamentView()
        tour_inputs = tournaments().__dict__
        self.tour_title = tour_inputs['tour_title']
        self.tour_time_control = tour_inputs['tour_time_control']
        self.tour_description = tour_inputs['tour_description']
        self.tour_start_date = tour_inputs['tour_start_date']
        tournament = TournamentModel(self.tour_title,
                                     self.tour_time_control,
                                     self.tour_description,
                                     self.tour_start_date
                                     )
        tour_info = tournament()
        return tour_info
