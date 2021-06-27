""" docstrings """
import datetime
# import time

from packages.models.match import MatchModel


class RoundModel:
    def __init__(self, matches, number):
        self.number = number
        self.start_date = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        self.end_date = None
        self.matches = matches

    def __call__(self):
        return self
        

