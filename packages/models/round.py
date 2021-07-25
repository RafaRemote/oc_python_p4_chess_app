""" Round model """


class RoundModel:
    """
    Class to represent a round
    ...

    Attributes
    ----------
    matches: list
        list of MatchModel instances
    number: int
        number of the round
    start_date: str, optional
        default set: none
        date and hour tournament starts
    end_date: str, optional
        default set: none
        date end hour tournament ends

    Methods
    -------
    call:
        returns RoundModel instance
    """

    def __init__(self, matches, number, start_date=None, end_date=None):
        """
        Constructs attributes for player object.

        Parameters
        ----------
        matches: list
            list of match instances
        number: int
            number of the round
        start_date: str, optional
            default set: none
            date and hour tournament starts
        end_date: str
            default set: none
            date end hour tournamanet ends
        """

        self.matches = matches
        self.number = number
        self.start_date = start_date
        self.end_date = end_date

    def __call__(self):
        """ returns RoundModel instance """

        return self
