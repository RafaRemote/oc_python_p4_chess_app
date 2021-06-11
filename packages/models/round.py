class RoundModel:
    def __init__(self, number):
        self.number = number
        self.matchs = []

    def add_match(self, match):
        self.matchs.append(match)