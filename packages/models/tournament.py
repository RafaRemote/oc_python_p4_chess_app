import datetime

TOTALROUNDS = 4
PLACE = 'Paris'

players = []
choice_of_times = ['bullet', 'blitz', 'rapid']

date = datetime.datetime.now().strftime("%a %d %B %Y")
class TournamentModel:
    def __init__(self, obj_from_controller, obj_player):
        if obj_from_controller is not None:
            self.name = obj_from_controller.__dict__['name']
            self.place = PLACE
            self.date = date
            self.total_rounds = TOTALROUNDS
            self.rounds = []
            self.players = []
            self.time_control = obj_from_controller.__dict__['time']
            self.description = obj_from_controller.__dict__['description']
        else:
            self.name = None
            self.place = None
            self.date = None
            self.total_rounds = None
            self.rounds = None
            self.players = None
            self.time_control = None
            self.description = None

        if obj_player is not None:
            self.players = obj_player

    def __call__(self):
        players.append(self.players)
        if self.time_control is not None and self.time_control not in choice_of_times:
            return ['error', self.__class__.__name__, f'{self.time_control} does not match with the propositions']
        else: 
            self.time_control = self.time_control
        return self


    def add_round(self, round):
        self.rounds.append(round)

