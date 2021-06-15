
class PlayerModel:
    def __init__(self, name, surname, year_birth, gender, elo, score):    
        self.name = name
        self.surname = surname
        self.year_birth = year_birth
        self.gender = gender
        self.opponents = list()
        self.elo = elo
        self.score = score

    def __call__(self):
        return self
    