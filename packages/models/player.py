class PlayerModel:
    def __init__(self):
        self.name = None
        self.surname = None
        self.year_of_birth = None
        self.gender = None
        self.elo = None

    def __call__(self):
        for i, j in self.__dict__.items():
            print(i, j)
    