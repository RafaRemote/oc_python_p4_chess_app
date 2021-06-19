""" docstrings """

class PlayerModel:
    def __init__(self, name, surname, year_birth, gender, elo, score):    
        self.name = name
        self.surname = surname
        self.year_birth = year_birth
        self.gender = gender
        self.opponents = list()
        self.elo = elo
        self.score = float(score)

    def get_opponents(tour_info, round_number):
        list_players = tour_info.__dict__['players'][0]
        list_matches = tour_info.__dict__['rounds'][int(round_number)-1][3]
        for i in list_matches:
            i.player1[0].opponents.append(i.player2[0])
            i.player2[0].opponents.append(i.player1[0])
        return tour_info

    def __call__(self):
        return self
