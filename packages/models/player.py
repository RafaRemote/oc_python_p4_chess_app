
class PlayerModel:
    def __init__(self, lst):    
        self.name = lst[0]
        self.surname = lst[1]
        self.year_of_birth = lst[2]
        self.gender = lst[3]
        self.elo = lst[4]

    def __call__(self):
        return self
    