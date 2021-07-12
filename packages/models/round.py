""" round model """


import datetime


class RoundModel:
    def __init__(self, matches, number, start_date=None, end_date=None):
        self.number = number
        self.start_date = start_date
        self.end_date = end_date
        self.matches = matches

    def __call__(self):
        return self
