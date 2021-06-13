class PlayerView:
    def __init__(self):
        self.name = None
        self.surname = None
        self.year_of_birth = None
        self.gender = None
        self.elo = None

    def __call__(self):
        name = input('Enter the name of the player: ')
        self.name = name
        surname = input('Enter the surname of the player: ')
        self.surname = surname
        year_of_birth = input('Enter year of birth: ')
        self.year_of_birth = year_of_birth
        gender = input('Enter the gender: m or w: ')
        self.gender = gender
        elo = input('Enter the Elo of the player: ')
        self.elo = elo
        return self
        
        





