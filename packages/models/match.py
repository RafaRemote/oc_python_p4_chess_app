""" Match model """


class MatchModel:
    """
    Class to represent a match
    ...

    Attributes
    ----------
    player1: tuple
        made of a player instance and a float number
    player2: tuple
        made of a player instance and a flaot number

    Methods
    -------
    none

    """

    def __init__(self, player1, player2, score1=0.0, score2=0.0):
        """
        Constructs attributes match object.

        Parameters
        ----------
        player1: instance
            player instance
        player2: instance
            player instance
        score1: float number
            score of player1
        score2: float number
            score of player2

        """

        self.player1 = (player1, score1)
        self.player2 = (player2, score2)
