""" docstrings"""
import datetime
from packages.models import player

from packages.models.player import PlayerModel
from packages.models.round import RoundModel
from packages.models.tournament import TournamentModel
from packages.models.match import MatchModel


class RoundController:
    def __init__(self, tour_info, round_number):
        self.tour_info = tour_info
        self.round_number = round_number
