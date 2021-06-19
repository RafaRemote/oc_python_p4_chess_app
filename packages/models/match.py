""" docstrings """

class MatchModel:
    def __init__(self, player1, player2, score1=None, score2=None):
        self.player1 = (player1, score1)
        self.player2 = (player2, score2)
